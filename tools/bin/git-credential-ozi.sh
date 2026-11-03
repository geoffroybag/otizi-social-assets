#!/bin/sh
# Aide d'identification git : fournit à git le jeton GitHub d'Ozi, lu dans
# le fichier d'environnement d'Ozi au moment du push. Jamais stocké dans la
# config git, jamais affiché. Utilisé par le remote HTTPS de ce dépôt (voir
# tools/ozi-tache-hebdo.md, section « Installé »).
ENV_FILE="${OZI_ENV_FILE:-/home/otizi/ozi/deploy/.env}"
case "$1" in
  get)
    token=$(grep -E '^GITHUB_TOKEN=' "$ENV_FILE" | head -1 | cut -d= -f2- | tr -d '"' | tr -d "'")
    [ -n "$token" ] || exit 1
    printf 'username=x-access-token\npassword=%s\n' "$token"
    ;;
  *) ;;  # store / erase : rien à faire
esac
