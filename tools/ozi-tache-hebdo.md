# Tâche Ozi « Otizi décrypte — carrousels hebdo »

Spécification pour une tâche automatique sur le VPS d'Ozi. Rythme : chaque lundi à 7h (Europe/Paris).

## Prérequis sur le VPS

- Python 3 + Pillow (`pip install pillow`).
- Chrome ou Chromium headless (`google-chrome --headless=new` ou `chromium --headless=new`), utilisé par `carrousel_lib.render_all` ; à défaut, Playwright + Chromium.
- Police Figtree : `git clone --depth 1 https://github.com/erikdkennedy/figtree.git` (chemin à renseigner dans `fontdir`).
- Clone de ce dépôt avec droit de push (clé SSH ou token GitHub de Geoffroy).
- Un accès web pour vérifier l'actualité et les chiffres (Ozi).

## Ce que la tâche fait

1. `git pull`. Lire `tools/calendrier-editorial.md` : prendre les trois sujets « à faire » de la semaine (lundi, mercredi, vendredi). Remplacer par un sujet de la réserve tout sujet qui dépend d'une information que seul Geoffroy a.
2. Pour chaque sujet : vérifier l'actualité et chaque chiffre sur le web, noter la source. Règles de `README.md` : rien d'inventé, source en pied de slide, une idée par slide, vouvoiement, pas de pub dans le corps, 8-9 slides.
3. Écrire `tools/post_<slug>.py` sur le modèle de `post_5etoiles.py` / `post_attentes.py` (catégorie : actu / conseil / vie), l'exécuter : il écrit le canevas (`carrousel-<slug>/project/`) et les PNG (`png-<slug>/`). Assembler une planche de contrôle (voir le bloc Pillow en bas des exemples) et corriger les débordements.
4. Copier les PNG dans `<slug>-AAAA-MM/`, mettre le calendrier à l'état « préparé » avec le slug, commit + push. Les images deviennent publiques à `https://raw.githubusercontent.com/geoffroybag/otizi-social-assets/<sha>/<slug>-AAAA-MM/slide-NN.png`.
5. Envoyer à Geoffroy (push Ozi) les planches et un récapitulatif : dates, titres, sources, points à vérifier.

## Metricool depuis Claude Code (fonctionne sur le plan Free)

L'API REST Metricool est réservée aux plans Advanced/Custom, mais le **serveur MCP Metricool** (celui qu'utilise Claude) fonctionne sur le plan Free. Comme Ozi passe par Claude Code, il suffit de l'ajouter une fois, sous l'utilisateur qui exécute Ozi :

```
claude mcp add --transport http metricool https://ai.metricool.com/mcp
```

Puis, dans une session Claude Code interactive, `/mcp` → Metricool → s'authentifier (OAuth : l'URL s'ouvre ou se copie dans un navigateur, connexion avec le compte Metricool otizi.app@gmail.com). Le jeton est ensuite rafraîchi automatiquement. À vérifier avec `claude mcp list` (Metricool « connected »).

Outils disponibles ensuite : `getBrandSettings` (marque Otizi, `blogId` 7842510), `createScheduledPost`, `getScheduledPosts`, `updateScheduledPost`, `getBestTimeToPostByNetwork`. Structure du post : voir `tache-hebdo.md`, étape 5 (toujours `draft: true` ; médias = URL publiques raw.githubusercontent.com ; alt-texts ; légende 3 paragraphes, 5 hashtags max).

Prérequis Claude Code côté VPS : `WebSearch` activé (vérification des chiffres), Chrome/Chromium headless pour le rendu, Pillow, accès push au dépôt. Lancer la tâche en mode non interactif, par exemple :

```
claude -p "$(cat tools/tache-hebdo.md)" --allowedTools "Bash,Read,Write,Edit,WebSearch,WebFetch,mcp__metricool__*"
```

(adapter le nom du serveur MCP et la politique d'autorisations à la configuration d'Ozi ; le compte rendu final est renvoyé par Ozi en push.)
