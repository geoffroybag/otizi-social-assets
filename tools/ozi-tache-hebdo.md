# Tâche Ozi « Otizi décrypte — carrousels hebdo »

Spécification pour une tâche automatique sur le VPS d'Ozi. Rythme : chaque vendredi à 15h (Europe/Paris), pour la semaine suivante ; posts programmés, relus par Geoffroy avant le lundi.

## Prérequis sur le VPS

- Python 3 + Pillow (`pip install pillow`).
- Chrome ou Chromium headless (`google-chrome --headless=new` ou `chromium --headless=new`), utilisé par `carrousel_lib.render_all` ; à défaut, Playwright + Chromium.
- Police Figtree : `git clone --depth 1 https://github.com/erikdkennedy/figtree.git` (chemin à renseigner dans `fontdir`).
- Clone de ce dépôt avec droit de push (clé SSH ou token GitHub de Geoffroy).
- Un accès web pour vérifier l'actualité et les chiffres (Ozi).

## Ce que la tâche fait

1. `git pull`. Lire `tools/calendrier-editorial.md` : piocher trois sujets dans « Stock » pour le lundi, mercredi et vendredi de la semaine suivante (sujets datés d'abord, puis l'ordre de la table, trois familles). Laisser dans le stock tout sujet qui dépend d'une information que seul Geoffroy a. Si le stock tombe sous six sujets, en chercher de nouveaux sur le web (jusqu'à huit), marqués « proposé le JJ/MM », listés dans le compte rendu.
2. Pour chaque sujet : vérifier l'actualité et chaque chiffre sur le web, noter la source. Règles de `README.md` : rien d'inventé, source en pied de slide, une idée par slide, vouvoiement, pas de pub dans le corps, 8-9 slides.
3. Écrire `tools/post_<slug>.py` sur le modèle de `post_5etoiles.py` / `post_attentes.py` (catégorie : actu / conseil / vie), l'exécuter : il écrit le canevas (`carrousel-<slug>/project/`) et les PNG (`png-<slug>/`). Assembler une planche de contrôle (voir le bloc Pillow en bas des exemples) et corriger les débordements.
4. Copier les PNG dans `<slug>-AAAA-MM/`, déplacer les sujets du Stock vers « Programmés » (date, état `programmé`, slug), commit + push. Les images deviennent publiques à `https://raw.githubusercontent.com/geoffroybag/otizi-social-assets/<sha>/<slug>-AAAA-MM/slide-NN.png`.
5. Pour chaque carrousel, un article de blog (700 à 1 000 mots) dans `~/vr-admin-website` (`content/articles/<slug>.md`, image `static/blog/images/<slug>.webp` par `tools/bin/cover.py`, contrôle `tools/bin/article-check.py`), commités sur `master` : la GitHub Action du dépôt régénère otizi.fr en quelques minutes ; `master` est ensuite fusionné dans `develop` (staging). Publication avant relecture, décision de Geoffroy du 3 novembre 2026. Repli : branche et PR vers `master`. Les légendes Instagram renvoient à `otizi.fr/blog/<slug>`.
6. Envoyer à Geoffroy (push Ozi) les planches et un récapitulatif : dates, titres, sources, lien de la PR du blog, points à vérifier.

## Metricool depuis Claude Code (fonctionne sur le plan Free)

L'API REST Metricool est réservée aux plans Advanced/Custom, mais le **serveur MCP Metricool** (celui qu'utilise Claude) fonctionne sur le plan Free. Comme Ozi passe par Claude Code, il suffit de l'ajouter une fois, sous l'utilisateur qui exécute Ozi :

```
claude mcp add --transport http metricool https://ai.metricool.com/mcp
```

Puis, dans une session Claude Code interactive, `/mcp` → Metricool → s'authentifier (OAuth : l'URL s'ouvre ou se copie dans un navigateur, connexion avec le compte Metricool otizi.app@gmail.com). Le jeton est ensuite rafraîchi automatiquement. À vérifier avec `claude mcp list` (Metricool « connected »).

Outils disponibles ensuite : `getBrandSettings` (marque Otizi, `blogId` 7842510), `createScheduledPost`, `getScheduledPosts`, `updateScheduledPost`, `getBestTimeToPostByNetwork`. Structure du post : voir `tache-hebdo.md`, étape 5 (`draft: false`, `autoPublish: true`, lundi/mercredi/vendredi suivants à 12h15 ; médias = URL publiques raw.githubusercontent.com ; alt-texts ; légende 3 paragraphes, 5 hashtags max).

Prérequis Claude Code côté VPS : `WebSearch` activé (vérification des chiffres), Chrome/Chromium headless pour le rendu, Pillow, accès push au dépôt. Lancer la tâche en mode non interactif, par exemple :

```
claude -p "$(cat tools/tache-hebdo.md)" --allowedTools "Bash,Read,Write,Edit,WebSearch,WebFetch,mcp__metricool__*"
```

(adapter le nom du serveur MCP et la politique d'autorisations à la configuration d'Ozi ; le compte rendu final est renvoyé par Ozi en push.)

## Installé le 3 novembre 2026 (VPS, utilisateur `otizi`)

Mise en place faite par Claude Code sur le VPS ; répétition à blanc réussie le jour même (semaine du 9 novembre, trois brouillons Metricool, 11 minutes). Le même jour, Geoffroy a fixé le rythme définitif : lancement le **vendredi à 15h** (Paris) pour la semaine suivante, posts **programmés** et non plus en brouillon (il relit dans Metricool avant le lundi).

**Dépôt et push.** `~/otizi-social-assets`, remote HTTPS `https://github.com/geoffroybag/otizi-social-assets.git`. Le push s'authentifie par `tools/bin/git-credential-ozi.sh` (aide d'identification git, configurée dans `.git/config` du clone, pas dans le dépôt) : elle lit `GITHUB_TOKEN` dans le fichier d'environnement d'Ozi (`/home/otizi/ozi/deploy/.env`) au moment du push, sans jamais le stocker ni l'afficher.

**Rendu.** Chromium de Playwright, déjà présent : `~/.cache/ms-playwright/chromium-1194/chrome-linux/chrome` (variable `OTIZI_CHROME`, posée par le script de lancement), avec les bibliothèques apt `libatk1.0-0t64 libatk-bridge2.0-0t64 libatspi2.0-0t64 libxdamage1 libasound2t64 libcairo2 libcups2t64 libpango-1.0-0`. Pillow par le paquet `python3-pil`. Police : `tools/fonts/figtree/` (clone de erikdkennedy/figtree, ignoré par git ; à recloner si le dossier manque). `tools/carrousel_lib.py` calcule tout seul la racine du dépôt, la police et le dossier `work/` ; les PNG sont rendus dans une fenêtre 1080×1500 puis recadrés à 1080×1350 (ce Chromium perd ~90 px en bas sinon). Planche de contrôle : `python3 tools/bin/planche.py <slug>` → `work/planches/<slug>.png`.

**Metricool.** Serveur MCP `metricool` ajouté à Claude Code en portée utilisateur (`claude mcp add --scope user --transport http metricool https://ai.metricool.com/mcp`), authentifié par Geoffroy (`/mcp`, compte otizi.app@gmail.com). Vérifié : marque Otizi, `blogId` 7842510, Instagram `otizi_app`, fuseau Europe/Paris. `claude mcp list` doit dire « Connected » ; sinon, refaire `/mcp` dans une session interactive sous `otizi`.

**Script de lancement.** `tools/bin/run-hebdo.sh` : `git pull`, prompt = `tools/tache-hebdo-vps.md` (préambule VPS, prioritaire) + `tools/tache-hebdo.md`, puis `claude -p` avec `--allowedTools "Bash,Read,Write,Edit,Glob,Grep,WebSearch,WebFetch,mcp__metricool"`, délai de 40 minutes (`timeout`), verrou `work/.run-hebdo.lock`. Journal : `work/logs/AAAA-MM-JJ.log` (plus `work/logs/cron.log` pour les passages du cron). Compte rendu écrit par la tâche dans `work/compte-rendu.md`, puis déposé dans Ozi.

- `run-hebdo.sh` (sans option) : lancement à la main, mode « manual ».
- `run-hebdo.sh --cron` : ne tourne que s'il est 15 h à Paris, et si la routine est cochée sur la page État d'Ozi.
- `run-hebdo.sh --poll` : toutes les deux minutes ; lance si « Lancer maintenant » a été cliqué sur la page État d'Ozi, sinon sort sans rien faire.
- `run-hebdo.sh --test` : répétition, ajoute `work/consigne-test.md` au prompt (sujets, dates, garde-fous).
- `run-hebdo.sh --dry` : affiche le prompt assemblé.

**Cron** (`crontab -e` sous `otizi` ; le système est en UTC, le script ne garde que l'appel qui tombe à 15 h de Paris) :

```
0 13,14 * * 5 /home/otizi/otizi-social-assets/tools/bin/run-hebdo.sh --cron >> /home/otizi/otizi-social-assets/work/logs/cron.log 2>&1
*/2 * * * * /home/otizi/otizi-social-assets/tools/bin/run-hebdo.sh --poll >> /home/otizi/otizi-social-assets/work/logs/cron.log 2>&1
```

**Compte rendu et tableau de bord dans Ozi.** Le script dialogue avec `http://127.0.0.1:3001/api/internal/carousels` (secret `OZI_DEPLOY_SECRET`, lu dans le fichier d'environnement d'Ozi à l'appel) : `GET` (routine active ? lancement demandé ?), `POST { event: "start" }` au début, `POST { event: "end", status, summary }` à la fin. Ozi en fait une conversation « 📸 Carrousels hebdo — <date> », prévient le téléphone, et la page État (bloc « Carrousels Instagram ») montre le dernier et le prochain passage, une case pour couper la routine, et « Lancer maintenant ». Tant que cette version d'Ozi n'est pas déployée, le script se replie sur la route Todo (`POST /api/internal/todo/conversations`, secret `OZI_TODO_SECRET`) : la conversation est alors ouverte avec le compte rendu en consigne et Ozi le relaie.

**Blog otizi.fr.** Clone `~/vr-admin-website` (dépôt `geoffroybag/vr-admin-website`), même aide d'identification que le dépôt social (jeton d'Ozi lu au push). Le dépôt a deux GitHub Actions : un push sur `master` régénère le site de production (SSH sur le serveur d'Otizi, `make generate`), un push sur `develop` régénère le staging. La tâche écrit les articles et les couvertures, les commite sur `master` (uniquement `content/articles/` et `static/blog/images/`), pousse, puis fusionne `master` dans `develop` et pousse : rien à faire côté Geoffroy, les releases de code du site (`yarn deploy`, git-flow) continuent comme avant. Repli si le push est refusé : branche `blog/semaine-<date>` et PR vers `master` avec `tools/bin/gh-ozi.sh` (gh avec le jeton d'Ozi en `GH_TOKEN`, jamais affiché).

**Lancer à la main** : `cd ~/otizi-social-assets && tools/bin/run-hebdo.sh` (ou `--test` après avoir écrit `work/consigne-test.md`). **Désactiver** : décocher « Préparer les carrousels Instagram chaque vendredi » sur la page État d'Ozi (le cron appelle, le script sort aussitôt), ou commenter les deux lignes du cron. **Vérifier** : `crontab -l`, `tail work/logs/cron.log`, `claude mcp list`.
