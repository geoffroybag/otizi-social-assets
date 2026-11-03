#!/bin/bash
# Lancement de la tâche « Otizi décrypte — carrousels hebdo » sur le VPS.
#
#   tools/bin/run-hebdo.sh            # lancement normal (cron du lundi 7h Paris)
#   tools/bin/run-hebdo.sh --test     # répétition : lit work/consigne-test.md en plus
#   tools/bin/run-hebdo.sh --dry      # affiche le prompt et sort
#
# Journal : work/logs/AAAA-MM-JJ.log. Compte rendu : work/compte-rendu.md, envoyé
# à Geoffroy par Ozi (route Todo, notification push). Voir tools/ozi-tache-hebdo.md.
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
DAY="$(date +%F)"
LOG="work/logs/$DAY.log"
MODE="${1:-}"

log() { printf '%s %s\n' "$(date '+%F %T')" "$*" | tee -a "$LOG"; }

# --- prompt : préambule VPS + prompt de la tâche (+ consigne de test)
PROMPT="$(cat tools/tache-hebdo-vps.md; printf '\n\n---\n\n'; cat tools/tache-hebdo.md)"
if [ "$MODE" = "--test" ] && [ -f work/consigne-test.md ]; then
  PROMPT="$PROMPT$(printf '\n\n---\n\n# Consigne de test (prioritaire sur tout ce qui précède)\n\n'; cat work/consigne-test.md)"
fi
if [ "$MODE" = "--dry" ]; then printf '%s\n' "$PROMPT"; exit 0; fi

# --- verrou : jamais deux exécutions en même temps
exec 9>work/.run-hebdo.lock
if ! flock -n 9; then log "Une exécution est déjà en cours, abandon."; exit 0; fi

log "Début ($MODE) dans $REPO"
rm -f work/compte-rendu.md
if ! git pull --ff-only origin main >>"$LOG" 2>&1; then log "git pull a échoué (voir le journal)"; fi

# --- Claude Code non interactif, 40 minutes au plus
STATUS=0
timeout --signal=TERM --kill-after=60 "${TIMEOUT_MINUTES}m" \
  claude -p "$PROMPT" --allowedTools "$ALLOWED_TOOLS" --output-format text >>"$LOG" 2>&1 || STATUS=$?
if [ "$STATUS" -eq 124 ]; then log "Arrêt : délai de $TIMEOUT_MINUTES minutes dépassé."
elif [ "$STATUS" -ne 0 ]; then log "claude -p a fini en erreur (code $STATUS)."
else log "claude -p terminé."; fi

# --- compte rendu → Ozi (conversation + notification push)
if [ -s work/compte-rendu.md ]; then
  REPORT="$(cat work/compte-rendu.md)"
else
  REPORT="$(printf 'Aucun compte rendu écrit par la tâche (code de sortie %s).\n\nDernières lignes du journal %s :\n\n```\n%s\n```\n' "$STATUS" "$LOG" "$(tail -n 40 "$LOG" | cut -c1-300)")"
fi
TITLE="Carrousels hebdo : compte rendu du $(date '+%d/%m/%Y')"
if [ "$MODE" = "--test" ]; then TITLE="$TITLE (test)"; fi
CONTENT="$(printf 'Compte rendu automatique de la tâche « Otizi décrypte — carrousels hebdo » (script tools/bin/run-hebdo.sh, journal %s). Transmets-le à Geoffroy tel quel, sans rien ajouter ni vérifier : reprends-le en Markdown, puis une ligne « Points à vérifier » s'"'"'il y en a.\n\n%s' "$REPO/$LOG" "$REPORT")"
SECRET="$(grep -E '^OZI_TODO_SECRET=' "$OZI_ENV_FILE" | head -1 | cut -d= -f2- | tr -d '"' | tr -d "'")"
if [ -z "$SECRET" ]; then
  log "OZI_TODO_SECRET introuvable : compte rendu non envoyé, voir work/compte-rendu.md"
else
  BODY="$(python3 -c 'import json,sys; print(json.dumps({"title": sys.argv[1], "content": sys.argv[2][:19000]}, ensure_ascii=False))' "$TITLE" "$CONTENT")"
  HTTP="$(curl -s -o work/.ozi-reponse.json -w '%{http_code}' -X POST "$OZI_URL/api/internal/todo/conversations" \
    -H "Authorization: Bearer $SECRET" -H 'Content-Type: application/json' --data-binary "$BODY")"
  if [ "$HTTP" = "201" ]; then
    log "Compte rendu envoyé à Ozi : $(python3 -c 'import json; print(json.load(open("work/.ozi-reponse.json"))["conversation"]["url"])' 2>/dev/null)"
  else
    log "Envoi à Ozi refusé (HTTP $HTTP) : compte rendu dans work/compte-rendu.md"
  fi
fi
unset SECRET
log "Fin."
