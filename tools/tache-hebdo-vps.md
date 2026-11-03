# Contexte d'exécution sur le VPS (préambule ajouté par `tools/bin/run-hebdo.sh`)

Tu es lancé en mode non interactif (`claude -p`) par un cron, sous l'utilisateur `otizi`, depuis le dépôt `otizi-social-assets` déjà cloné : le répertoire courant. Le prompt de la tâche suit ce préambule ; là où ils diffèrent, c'est ce préambule qui s'applique.

## Ce qui est déjà en place (ne pas refaire)

- Le dépôt est à jour (`git pull` fait par le script). Pas d'outil `add_repo`, pas de clone, pas de `/home/claude`.
- La police Figtree est dans `tools/fonts/figtree/fonts/ttf` et `tools/carrousel_lib.py` la trouve seul (`FONT_DIR`).
- Le navigateur headless est configuré par la variable `OTIZI_CHROME` ; `carrousel_lib.render_all` l'utilise. Rien à adapter dans la bibliothèque.
- Les sorties vont dans `work/` (ignoré par git) : `work_dir("<slug>", "project")` pour le canevas, `work_dir("<slug>", "png")` pour les PNG. Les scripts `tools/post_*.py` montrent l'usage.
- Planche de contrôle : `python3 tools/bin/planche.py <slug>` écrit `work/planches/<slug>.png`. Regarde-la (outil Read) avant de continuer.
- Push : `git push origin main` fonctionne tel quel (aide d'identification configurée). Commits en français, courts.
- Metricool : serveur MCP `metricool` (outils `mcp__metricool__getBrandSettings`, `mcp__metricool__createScheduledPost`, `mcp__metricool__getScheduledPosts`, …). Marque Otizi, `blogId` 7842510, fuseau `Europe/Paris`, toujours `draft: true`. Jamais `updateScheduledPost` sur un post existant.

## Compte rendu (remplace l'étape 6 : pas de SendUserFile ni SendUserMessage ici)

Écris le compte rendu dans `work/compte-rendu.md`, en français, en Markdown, court. Le script l'envoie ensuite à Geoffroy par Ozi (notification push). Contenu :

1. Pour chaque carrousel : date prévue, titre, source principale, lien Metricool du brouillon (`plannerUrl`), chemin de la planche (`work/planches/<slug>.png`), commit.
2. Ce que Geoffroy doit faire : ouvrir Metricool et retirer « brouillon » sur les posts validés, ou répondre avec des corrections.
3. Points à vérifier : chiffres non confirmés, sujets remplacés, événement daté à finaliser, erreurs rencontrées.

Si une étape échoue (rendu, push, Metricool), écris quand même le compte rendu avec l'erreur exacte et ce qui a été fait, puis termine. N'invente jamais un chiffre pour « faire passer » un carrousel : sans source, écris sans chiffre.
