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

## Metricool : attention au plan

L'API Metricool (`POST https://app.metricool.com/api/v2/scheduler/posts?blogId=7842510&userId=…`, en-tête `X-Mc-Auth`, body : `publicationDate{dateTime,timezone}`, `text`, `providers[{network:"instagram"}]`, `instagramData{type:"POST"}`, `draft`, médias normalisés via `GET /api/actions/normalize/image/url?url=…` puis `media:{mediaId}`) n'est ouverte qu'aux plans **Advanced et Custom**. Sur le plan Free, Ozi ne peut pas programmer les posts lui-même.

Deux options tant que le compte est en Free :
- **Manuel** : Geoffroy crée les posts dans Metricool à partir des PNG du dépôt et des légendes que la tâche écrit dans `<slug>-AAAA-MM/legende.txt`.
- **Via Claude** : le connecteur Metricool de Claude fonctionne sur le plan Free ; un réveil hebdomadaire dans la conversation Claude lit le dépôt (sujets à l'état « préparé »), crée les brouillons Metricool et passe l'état à « programmé » une fois validé.

Si le compte passe en Advanced : ajouter le token dans les secrets d'Ozi et faire l'étape Metricool directement depuis la tâche (toujours en `draft: true`).
