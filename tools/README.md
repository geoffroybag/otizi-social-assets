# Outillage « Otizi décrypte »

Génération des carrousels Instagram (1080×1350) dans la charte Otizi, à partir de scripts Python.

## Fichiers

- `carrousel_lib.py` : briques de mise en page (couverture à blocs inclinés, photo de couverture `photo()`, `photo_cover()` plein écran, `photo_block()` encadrée, pages intérieures sobres, listes numérotées, barres, stats, pastille de catégorie) et rendu PNG via Chrome headless.
- `post_*.py` : un script par carrousel, qui décrit le contenu slide par slide et écrit :
  - `carrousel-<slug>/project/*.dc.html` + `canvas.json` (format du canevas Design de Claude),
  - `png-<slug>/slide-NN.png` (images prêtes pour Instagram).
- `calendrier-editorial.md` : table « Programmés » (carrousels datés, `programmé` / `publié`) et table « Stock » (sujets à venir, sans date, réapprovisionné par la tâche quand il passe sous six). Lisible sur la page État d'Ozi, modifiable sur GitHub.
- La police Figtree vient de `https://github.com/erikdkennedy/figtree` : `git clone --depth 1 https://github.com/erikdkennedy/figtree.git tools/fonts/figtree` (ignoré par git), trouvée automatiquement par `carrousel_lib.py`.
- `carrousel_lib.py` rend dans `work/` (ignoré par git) : `work_dir("<slug>", "project")` et `work_dir("<slug>", "png")` ; navigateur headless : `OTIZI_CHROME` ou `google-chrome`/`chromium` dans le PATH.
- `bin/planche.py <slug>` : planche de contrôle (toutes les slides) dans `work/planches/<slug>.png`. `bin/photo.py search "<requête>"` / `bin/photo.py get <slug> <id>` : photo libre de droits (Unsplash, Pexels ou Pixabay) pour la slide 1 et l'article (`work/photos/`). `bin/cover.py <slug> <sortie.webp>` : couverture d'article de blog 1600×900 (la photo recadrée, sinon une bande de la slide 1). `bin/article-check.py <article.md>` : contrôle d'un article avant la PR. `bin/gh-ozi.sh` : `gh` avec le jeton d'Ozi. `bin/run-hebdo.sh` : lancement de la tâche hebdo sur le VPS (voir `ozi-tache-hebdo.md`).

## Charte

- Fond `#EDF4FE`, violet `#472ed8` (titres, wordmark, cartes d'accent), menthe `#00e2ae` (pastille « décrypte », coches, traits, courbe de la couverture), texte `#2B2F45`.
- Couverture (`photo_cover`) : photo de banque d'images plein écran, dégradé sombre en bas, wordmark « Otizi décrypte » en haut à gauche (blanc + pastille menthe), compteur « 1/N » en haut à droite, pastille de catégorie blanche (Actu, Conseil, Vie d'hôte), texte blanc en gras en une ou deux phrases avec le chiffre clé en menthe, flèche blanche en bas à droite. Sans crédit sur la slide (il va dans la légende). Variante encadrée (`page(…, cover=True)` + `photo_block`) : photo à coins arrondis au-dessus du titre en 2-3 blocs inclinés, éclats menthe, sous-titre court, courbe menthe.
- Pages intérieures : titre droit en violet avec trait menthe, cartes blanches liserées ou violettes, pas d'éclats ni de courbe, compteur « n / N » en haut à droite, source en pied.
- Règles de contenu : une idée par slide, chiffres toujours sourcés (source en pied de slide), jamais de statistique inventée, pas de pub Otizi dans le corps (signature en pied seulement), 5 hashtags max dans la légende.

## Procédure hebdomadaire

1. Le vendredi à 15h : lire `calendrier-editorial.md`, piocher trois sujets du Stock pour la semaine suivante ; réapprovisionner le stock par une recherche web s'il tombe sous six.
2. Pour chaque sujet : vérifier l'actualité et les chiffres (recherche web), écrire `post_<slug>.py`, générer, contrôler la planche, pousser les PNG dans `<slug>-AAAA-MM/`.
3. Programmer les posts dans Metricool (marque Otizi, `blogId` 7842510, fuseau Europe/Paris) : lundi, mercredi, vendredi de la semaine suivante à 12h15, images par URL `raw.githubusercontent.com/geoffroybag/otizi-social-assets/<commit>/<dossier>/slide-NN.png`, légende + alt-texts, programmés (`draft: false`) : Geoffroy relit dans Metricool avant le lundi.
4. Un article de blog par carrousel sur otizi.fr (dépôt `vr-admin-website`, commit sur `master`, déploiement automatique par GitHub Action, puis `master` fusionné dans `develop`), la légende Instagram y renvoie.
5. Mettre à jour le calendrier (état, liens) et envoyer la planche de contrôle à Geoffroy.
