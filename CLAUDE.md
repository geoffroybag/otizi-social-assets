# otizi-social-assets

Visuels et outillage du compte Instagram « Otizi décrypte » (gîtes et chambres d'hôtes).

- Charte, règles de contenu et procédure : `tools/README.md`.
- Sujets et planning : `tools/calendrier-editorial.md` (source de vérité, à mettre à jour à chaque passage).
- Tâche hebdomadaire (lundi 7h) : `tools/tache-hebdo.md` ; mise en place côté Ozi / Claude Code : `tools/ozi-tache-hebdo.md`.
- Génération : `tools/carrousel_lib.py` + un `tools/post_<slug>.py` par carrousel ; images finales dans `<slug>-AAAA-MM/` à la racine (URL publiques via raw.githubusercontent.com).
- Metricool : marque Otizi, `blogId` 7842510, fuseau Europe/Paris ; les posts sont créés en brouillon (`draft: true`), jamais publiés sans validation de Geoffroy.
