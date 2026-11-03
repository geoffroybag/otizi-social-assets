# otizi-social-assets

Visuels et outillage du compte Instagram « Otizi décrypte » (gîtes et chambres d'hôtes).

- Charte, règles de contenu et procédure : `tools/README.md`.
- Sujets et planning : `tools/calendrier-editorial.md` (source de vérité, à mettre à jour à chaque passage) : table « Programmés » (datés) et table « Stock » (à piocher le vendredi, réapprovisionné par recherche web sous six sujets).
- Tâche hebdomadaire (vendredi 15h, pour la semaine suivante) : `tools/tache-hebdo.md` (prompt commun) + `tools/tache-hebdo-vps.md` (préambule quand elle tourne sur le VPS) ; lancement `tools/bin/run-hebdo.sh` ; mise en place et exploitation : `tools/ozi-tache-hebdo.md`, section « Installé ».
- Génération : `tools/carrousel_lib.py` + un `tools/post_<slug>.py` par carrousel ; images finales dans `<slug>-AAAA-MM/` à la racine (URL publiques via raw.githubusercontent.com).
- Blog : chaque carrousel donne un article sur otizi.fr/blog (dépôt `geoffroybag/vr-admin-website`, `content/articles/<slug>.md`, clone `~/vr-admin-website`, PR vers `develop`, jamais de push direct ni de merge).
- Metricool : marque Otizi, `blogId` 7842510, fuseau Europe/Paris ; les posts sont programmés (`draft: false`) pour lundi, mercredi, vendredi 12h15 ; Geoffroy relit dans Metricool avant le lundi. Jamais `updateScheduledPost` sans son accord.
