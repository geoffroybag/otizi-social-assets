# Outillage « Otizi décrypte »

Génération des carrousels Instagram (1080×1350) dans la charte Otizi, à partir de scripts Python.

## Fichiers

- `carrousel_lib.py` : briques de mise en page (couverture à blocs inclinés, pages intérieures sobres, listes numérotées, barres, stats, pastille de catégorie) et rendu PNG via Chrome headless.
- `post_*.py` : un script par carrousel, qui décrit le contenu slide par slide et écrit :
  - `carrousel-<slug>/project/*.dc.html` + `canvas.json` (format du canevas Design de Claude),
  - `png-<slug>/slide-NN.png` (images prêtes pour Instagram).
- `calendrier-editorial.md` : sujets validés, planning, état (à faire / préparé / publié).
- La police Figtree vient de `https://github.com/erikdkennedy/figtree` (dossier `fonts/ttf`), à cloner à côté avant le rendu.

## Charte

- Fond `#EDF4FE`, violet `#472ed8` (titres, wordmark, cartes d'accent), menthe `#00e2ae` (pastille « décrypte », coches, traits, courbe de la couverture), texte `#2B2F45`.
- Couverture : wordmark « Otizi décrypte », pastille de catégorie en haut à droite (Actu = violet, Conseil = blanc, Vie d'hôte = menthe), titre en 2-3 blocs inclinés, éclats menthe, sous-titre, trait menthe, courbe menthe en bas à droite.
- Pages intérieures : titre droit en violet avec trait menthe, cartes blanches liserées ou violettes, pas d'éclats ni de courbe, compteur « n / N » en haut à droite, source en pied.
- Règles de contenu : une idée par slide, chiffres toujours sourcés (source en pied de slide), jamais de statistique inventée, pas de pub Otizi dans le corps (signature en pied seulement), 5 hashtags max dans la légende.

## Procédure hebdomadaire

1. Lire `calendrier-editorial.md`, prendre les trois sujets de la semaine.
2. Pour chaque sujet : vérifier l'actualité et les chiffres (recherche web), écrire `post_<slug>.py`, générer, contrôler la planche, pousser les PNG dans `<slug>-AAAA-MM/`.
3. Créer les posts dans Metricool (marque Otizi, `blogId` 7842510, fuseau Europe/Paris) : lundi, mercredi, vendredi à 12h15, images par URL `raw.githubusercontent.com/geoffroybag/otizi-social-assets/<commit>/<dossier>/slide-NN.png`, légende + alt-texts, **en brouillon** (`draft: true`) tant que Geoffroy n'a pas validé.
4. Mettre à jour le calendrier (état, liens) et envoyer la planche de contrôle à Geoffroy.
