# otizi-social-assets

Visuels et outillage du compte Instagram « Otizi décrypte » (gîtes et chambres d'hôtes).

- Charte, règles de contenu et procédure : `tools/README.md`.
- Sujets et planning : `tools/calendrier-editorial.md` (source de vérité, à mettre à jour à chaque passage) : table « Programmés » (datés) et table « Stock » (à piocher le vendredi, réapprovisionné par recherche web sous six sujets).
- Tâche hebdomadaire (vendredi 15h, pour la semaine suivante) : `tools/tache-hebdo.md` (prompt commun) + `tools/tache-hebdo-vps.md` (préambule quand elle tourne sur le VPS) ; lancement `tools/bin/run-hebdo.sh` ; mise en place et exploitation : `tools/ozi-tache-hebdo.md`, section « Installé ».
- Génération : `tools/carrousel_lib.py` + un `tools/post_<slug>.py` par carrousel ; images finales dans `<slug>-AAAA-MM/` à la racine (URL publiques via raw.githubusercontent.com).
- Photo : chaque carrousel a une photo libre de droits de banque d'images, Unsplash par défaut (`tools/bin/photo.py`, `work/photos/<slug>.jpg`), en plein écran sur la slide 1 (`photo_cover`, texte blanc sur dégradé sombre) et en couverture de l'article ; crédit du photographe en dernière ligne de la légende Instagram et en fin d'article, jamais sur la slide. Jamais de photo de presse, de capture d'écran ni de marque.
- Blog : chaque carrousel donne un article sur otizi.fr/blog (dépôt `geoffroybag/vr-admin-website`, `content/articles/<slug>.md`, clone `~/vr-admin-website`) : commit sur `master` (déploiement automatique), puis `master` fusionné dans `develop` ; seulement les articles et leurs images, jamais `--force`.
- Metricool : marque Otizi, `blogId` 7842510, fuseau Europe/Paris ; les posts sont programmés (`draft: false`) pour lundi, mercredi, vendredi 12h15 ; Geoffroy relit dans Metricool avant le lundi. Jamais `updateScheduledPost` sans son accord.
