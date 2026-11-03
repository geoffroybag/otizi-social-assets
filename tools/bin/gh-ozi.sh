#!/bin/sh
# `gh` avec le jeton GitHub d'Ozi : lu dans le fichier d'environnement d'Ozi au moment
# de l'appel, donné à gh par GH_TOKEN, jamais affiché (la sortie est masquée).
# Usage : tools/bin/gh-ozi.sh pr create --repo geoffroybag/vr-admin-website …
ENV_FILE="${OZI_ENV_FILE:-/home/otizi/ozi/deploy/.env}"
GH_TOKEN="$(grep -E '^GITHUB_TOKEN=' "$ENV_FILE" | head -1 | cut -d= -f2- | tr -d '"' | tr -d "'")"
[ -n "$GH_TOKEN" ] || { echo "jeton GitHub introuvable" >&2; exit 1; }
export GH_TOKEN
gh "$@" 2>&1 | sed -e "s#$GH_TOKEN#<masqué>#g"
