# Prompt d'installation — à coller dans Claude Code sur le VPS d'Ozi

Tu installes la tâche hebdomadaire « Otizi décrypte — carrousels hebdo » sur ce serveur. Elle génère chaque lundi trois carrousels Instagram (gîtes et chambres d'hôtes), pousse les images sur GitHub et crée des brouillons dans Metricool. Rien ne doit être publié automatiquement : toujours `draft: true`. Travaille sous l'utilisateur courant, sans sudo sauf si c'est indispensable pour installer un paquet (demande-moi avant).

ÉTAPE 1 — Dépôt
Clone `git@github.com:geoffroybag/otizi-social-assets.git` dans `~/otizi-social-assets` (ou `git pull` s'il existe). Vérifie que `git push` est possible (`git push --dry-run`). Lis `CLAUDE.md`, `tools/README.md`, `tools/tache-hebdo.md` et `tools/ozi-tache-hebdo.md` : ils décrivent la charte, la procédure hebdo et la mise en place.

ÉTAPE 2 — Prérequis de rendu
- Python 3 et Pillow (`pip install --user pillow` si absent).
- Un navigateur headless : `google-chrome` ou `chromium` (`which google-chrome chromium chromium-browser`). S'il n'y en a pas, propose-moi l'installation du paquet de la distribution (ou `playwright install chromium` dans un venv) et attends mon accord.
- Police Figtree : `git clone --depth 1 https://github.com/erikdkennedy/figtree.git ~/otizi-social-assets/tools/fonts/figtree`.
- Dans `tools/carrousel_lib.py`, remplace les chemins absolus `/tmp/claude-0/.../scratchpad/...` par des chemins relatifs au dépôt : la police dans `tools/fonts/figtree/fonts/ttf`, les sorties (`carrousel-<slug>/`, `png-<slug>/`) dans `~/otizi-social-assets/work/` (dossier à ajouter au `.gitignore`), et la commande Chrome par celle trouvée au point précédent. Fais la même correction de chemins dans les scripts d'exemple `tools/post_*.py` (variable `S`, `PROJ`, `sys.path`).
- Test : exécute `python3 tools/post_5etoiles.py` et vérifie que `work/png-5etoiles/slide-01.png` fait 1080×1350 et ressemble à la planche de `tools/README.md` (fond bleu clair, titres violets). Montre-moi l'image.

ÉTAPE 3 — Metricool (serveur MCP, fonctionne sur le plan Free)
`claude mcp add --transport http metricool https://ai.metricool.com/mcp` puis `claude mcp list`. Si Metricool n'est pas « connected », dis-moi de lancer `/mcp` dans une session interactive pour m'authentifier (compte Metricool otizi.app@gmail.com) ; attends que je confirme. Ensuite, teste `getBrandSettings` : on doit voir la marque Otizi, `blogId` 7842510, Instagram `otizi_app`. Ne crée aucun post pendant ce test.

ÉTAPE 4 — Répétition à blanc
Lance une fois la procédure de `tools/tache-hebdo.md` en mode test : sujets de la semaine du 10 novembre (cotisations des chambres d'hôtes, basse saison, petit-déjeuner), mais avec ces garde-fous : commit et push autorisés, posts Metricool créés en brouillon avec `draft: true`, et dates de publication lundi 10, mercredi 12, vendredi 14 novembre à 12h15 Europe/Paris. Montre-moi les trois planches de contrôle et les `plannerUrl`. Mets `tools/calendrier-editorial.md` à jour (état « préparé »). Si quelque chose échoue (rendu, push, Metricool), corrige l'outillage, commit, et relance ; n'écris jamais de chiffre non sourcé pour « faire passer » un carrousel.

ÉTAPE 5 — Planification
Crée le lancement récurrent, chaque lundi à 07:00 Europe/Paris, de préférence comme tâche Ozi (route Todo / tâche interne) si Ozi sait exécuter une commande ; sinon un cron sous cet utilisateur. La commande exécute Claude Code en mode non interactif depuis `~/otizi-social-assets` avec le prompt de `tools/tache-hebdo.md`, les outils Bash, Read, Write, Edit, Glob, Grep, WebSearch, WebFetch et `mcp__metricool__*` autorisés, un journal dans `~/otizi-social-assets/work/logs/AAAA-MM-JJ.log`, et un timeout de 40 minutes. À la fin de chaque exécution, le compte rendu (dates, titres, sources, liens Metricool, points à vérifier) doit m'être envoyé par la notification push d'Ozi ; si Ozi n'a pas de canal depuis un script, écris-le dans `work/compte-rendu.md` et dis-moi comment tu l'as branché.
Ajoute dans `tools/ozi-tache-hebdo.md` une section « Installé le <date> » qui documente exactement ce que tu as mis en place (commande, chemin du script, emplacement des logs, comment lancer à la main, comment désactiver). Commit et push.

RÈGLES
- Jamais de publication automatique : `draft: true` sur tous les posts, et pas de `updateScheduledPost` sur un post existant sans mon accord.
- Pas de statistique inventée ; source en pied de slide ; vouvoiement ; pas de pub Otizi/Bookhome dans le corps des slides.
- Avant toute installation de paquet système, toute modification hors du dépôt et du dossier `work/`, ou toute commande qui touche à Ozi lui-même, explique ce que tu vas faire et attends mon accord.
- Termine par un résumé : ce qui est installé, ce qui reste à faire de mon côté, et la commande pour lancer la tâche à la main.
