#!/bin/bash
# Lancement de la tâche « Otizi décrypte — carrousels hebdo » sur le VPS.
#
#   tools/bin/run-hebdo.sh            # lancement à la main (mode « manual »)
#   tools/bin/run-hebdo.sh --cron     # cron du lundi : ne tourne que s'il est 7h à Paris
#                                     # et si la routine est active dans Ozi (page État)
#   tools/bin/run-hebdo.sh --poll     # cron toutes les 2 min : lance si « Lancer maintenant »
#                                     # a été demandé sur la page État d'Ozi, sinon sort
#   tools/bin/run-hebdo.sh --test     # répétition : lit work/consigne-test.md en plus
#   tools/bin/run-hebdo.sh --dry      # affiche le prompt et sort
#
# Journal : work/logs/AAAA-MM-JJ.log. Compte rendu : work/compte-rendu.md, déposé
# dans Ozi (route /api/internal/carousels, conversation + notification push).
# Si Ozi n'a pas encore cette route (ancienne version), repli sur la route Todo.
# Voir tools/ozi-tache-hebdo.md.
set -u
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$REPO" || exit 1

export PATH="/home/otizi/.local/bin:/usr/local/bin:/usr/bin:/bin"
export HOME="${HOME:-/home/otizi}"
export OTIZI_CHROME="${OTIZI_CHROME:-/home/otizi/.cache/ms-playwright/chromium-1194/chrome-linux/chrome}"
export TZ="Europe/Paris"
OZI_URL="${OZI_URL:-http://127.0.0.1:3001}"
OZI_ENV_FILE="${OZI_ENV_FILE:-/home/otizi/ozi/deploy/.env}"
TIMEOUT_MINUTES="${TIMEOUT_MINUTES:-40}"
ALLOWED_TOOLS="Bash,Read,Write,Edit,Glob,Grep,WebSearch,WebFetch,mcp__metricool"

mkdir -p work/logs work/planches
MODE_FLAG="${1:-}"
case "$MODE_FLAG" in
  --cron) MODE="cron" ;;
  --poll) MODE="page" ;;
  --test) MODE="test" ;;
  *) MODE="manual" ;;
esac

# Secrets lus dans le fichier d'environnement d'Ozi au moment de l'appel, jamais affichés.
env_value() { grep -E "^$1=" "$OZI_ENV_FILE" 2>/dev/null | head -1 | cut -d= -f2- | tr -d '"' | tr -d "'"; }
AGENT_SECRET="$(env_value OZI_DEPLOY_SECRET)"

json() { python3 -c 'import json,sys; print(json.dumps(dict(zip(sys.argv[1::2], sys.argv[2::2])), ensure_ascii=False))' "$@"; }
# Appel de la route des carrousels d'Ozi ; écrit la réponse dans work/.ozi-reponse.json, rend le code HTTP.
ozi_get() { curl -s -o work/.ozi-reponse.json -w '%{http_code}' --max-time 10 -H "Authorization: Bearer $AGENT_SECRET" "$OZI_URL/api/internal/carousels"; }
ozi_post() { curl -s -o work/.ozi-reponse.json -w '%{http_code}' --max-time 20 -X POST -H "Authorization: Bearer $AGENT_SECRET" -H 'Content-Type: application/json' --data-binary "$1" "$OZI_URL/api/internal/carousels"; }
field() { python3 -c 'import json,sys; v=json.load(open("work/.ozi-reponse.json")).get(sys.argv[1]); print("true" if v is True else "false" if v is False else "" if v is None else v)' "$1" 2>/dev/null; }

# --- prompt : préambule VPS + prompt de la tâche (+ consigne de test)
PROMPT="$(cat tools/tache-hebdo-vps.md; printf '\n\n---\n\n'; cat tools/tache-hebdo.md)"
if [ "$MODE" = "test" ] && [ -f work/consigne-test.md ]; then
  PROMPT="$PROMPT$(printf '\n\n---\n\n# Consigne de test (prioritaire sur tout ce qui précède)\n\n'; cat work/consigne-test.md)"
fi
if [ "$MODE_FLAG" = "--dry" ]; then printf '%s\n' "$PROMPT"; exit 0; fi

# --- cron du lundi : seulement à 7h Paris (le cron est en UTC : appels à 5h et 6h UTC), et si Ozi dit que la routine est active
if [ "$MODE" = "cron" ]; then
  [ "$(TZ=Europe/Paris date +%H)" = "07" ] || exit 0
  if [ -n "$AGENT_SECRET" ] && [ "$(ozi_get)" = "200" ] && [ "$(field enabled)" = "false" ]; then
    printf '%s routine désactivée sur la page État : pas de lancement.\n' "$(date '+%F %T')" >> work/logs/cron.log
    exit 0
  fi
fi
# --- passage toutes les 2 min : Ozi a-t-il une demande « Lancer maintenant » ?
if [ "$MODE" = "page" ]; then
  [ -n "$AGENT_SECRET" ] || exit 0
  [ "$(ozi_get)" = "200" ] || exit 0
  [ "$(field requested)" = "true" ] || exit 0
fi

# --- verrou : jamais deux exécutions en même temps
exec 9>work/.run-hebdo.lock
if ! flock -n 9; then printf '%s une exécution est déjà en cours, abandon (%s).\n' "$(date '+%F %T')" "$MODE" >> work/logs/cron.log; exit 0; fi

DAY="$(date +%F)"
LOG="work/logs/$DAY.log"
log() { printf '%s %s\n' "$(date '+%F %T')" "$*" | tee -a "$LOG"; }
STARTED_AT="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
log "Début ($MODE) dans $REPO"
if [ -n "$AGENT_SECRET" ]; then
  HTTP="$(ozi_post "$(json event start mode "$MODE" startedAt "$STARTED_AT" log "$REPO/$LOG")")"
  [ "$HTTP" = "200" ] || log "Ozi n'a pas enregistré le début (HTTP $HTTP)."
fi
rm -f work/compte-rendu.md
if ! git pull --ff-only origin main >>"$LOG" 2>&1; then log "git pull a échoué (voir le journal)"; fi

# --- Claude Code non interactif, 40 minutes au plus
STATUS=0
timeout --signal=TERM --kill-after=60 "${TIMEOUT_MINUTES}m" \
  claude -p "$PROMPT" --allowedTools "$ALLOWED_TOOLS" --output-format text >>"$LOG" 2>&1 || STATUS=$?
if [ "$STATUS" -eq 124 ]; then RESULT="timeout"; log "Arrêt : délai de $TIMEOUT_MINUTES minutes dépassé."
elif [ "$STATUS" -ne 0 ]; then RESULT="failure"; log "claude -p a fini en erreur (code $STATUS)."
elif [ ! -s work/compte-rendu.md ]; then RESULT="failure"; log "claude -p terminé mais sans compte rendu."
else RESULT="success"; log "claude -p terminé."; fi
FINISHED_AT="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

# --- compte rendu → Ozi (conversation + notification push)
if [ -s work/compte-rendu.md ]; then
  REPORT="$(cat work/compte-rendu.md)"
else
  REPORT="$(printf 'Aucun compte rendu écrit par la tâche (code de sortie %s).\n\nDernières lignes du journal :\n\n```\n%s\n```\n' "$STATUS" "$(tail -n 40 "$LOG" | cut -c1-300)")"
fi
REPORT="$(printf '%s' "$REPORT" | head -c 18000)"
SENT=""
if [ -n "$AGENT_SECRET" ]; then
  HTTP="$(ozi_post "$(json event end mode "$MODE" startedAt "$STARTED_AT" finishedAt "$FINISHED_AT" status "$RESULT" summary "$REPORT" log "$REPO/$LOG")")"
  if [ "$HTTP" = "200" ]; then SENT="carousels"; log "Compte rendu déposé dans Ozi (conversation $(field conversationId))."
  else log "Route des carrousels d'Ozi indisponible (HTTP $HTTP) : repli sur la route Todo."; fi
fi
if [ -z "$SENT" ]; then
  TODO_SECRET="$(env_value OZI_TODO_SECRET)"
  if [ -z "$TODO_SECRET" ]; then
    log "Aucun secret Ozi : compte rendu non envoyé, voir work/compte-rendu.md"
  else
    TITLE="Carrousels hebdo : compte rendu du $(date '+%d/%m/%Y')"
    [ "$MODE" = "test" ] && TITLE="$TITLE (test)"
    CONTENT="$(printf 'Compte rendu automatique de la tâche « Otizi décrypte — carrousels hebdo » (script tools/bin/run-hebdo.sh, journal %s, résultat : %s). Transmets-le à Geoffroy tel quel, sans rien ajouter ni vérifier : reprends-le en Markdown, puis une ligne « Points à vérifier » s'"'"'il y en a.\n\n%s' "$REPO/$LOG" "$RESULT" "$REPORT")"
    HTTP="$(curl -s -o work/.ozi-reponse.json -w '%{http_code}' -X POST "$OZI_URL/api/internal/todo/conversations" \
      -H "Authorization: Bearer $TODO_SECRET" -H 'Content-Type: application/json' --data-binary "$(json title "$TITLE" content "$CONTENT")")"
    if [ "$HTTP" = "201" ]; then log "Compte rendu envoyé à Ozi (route Todo)."; else log "Envoi à Ozi refusé (HTTP $HTTP) : compte rendu dans work/compte-rendu.md"; fi
    unset TODO_SECRET
  fi
fi
unset AGENT_SECRET
log "Fin ($RESULT)."
