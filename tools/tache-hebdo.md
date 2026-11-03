# Tâche planifiée « Otizi décrypte — carrousels hebdo »

Fréquence conseillée : chaque lundi à 7h (Europe/Paris). Approbation automatique nécessaire (push GitHub + création de brouillons Metricool).
Connecteurs requis dans la tâche : Metricool, Claude Code Remote (GitHub). Les brouillons Metricool ne sont jamais publiés sans validation de Geoffroy.

## Prompt à coller dans la tâche

Tâche automatique « Otizi décrypte — carrousels hebdo ». Objectif : préparer les trois carrousels Instagram de la semaine pour le compte @otizi_app (média « Otizi décrypte », actu et conseils pour les gîtes et chambres d'hôtes en France), les déposer en BROUILLON dans Metricool, et envoyer à Geoffroy une planche de contrôle. Rien ne doit être publié ni programmé en publication automatique sans sa validation : les posts Metricool sont créés avec `draft: true`.

ÉTAPE 1 — Récupérer l'outillage
Attache le dépôt GitHub `geoffroybag/otizi-social-assets` avec l'outil add_repo (accès push), clone-le dans /home/claude/otizi-social-assets, puis lis `tools/README.md` et `tools/calendrier-editorial.md`. Le README décrit la charte et la procédure ; `tools/carrousel_lib.py` contient les briques de mise en page et le rendu PNG ; `tools/post_5etoiles.py`, `tools/post_attentes.py` et `tools/post_airbnb_corvees.py` sont des exemples complets à imiter (structure, ton, longueur des textes, nombre de slides : 8 à 9).
Clone aussi la police : `git clone --depth 1 https://github.com/erikdkennedy/figtree.git` dans le scratchpad, et adapte le chemin des polices dans `carrousel_lib.py` (variable `fontdir` de `render_all`) ainsi que les chemins de sortie, qui pointent vers un ancien scratchpad. Le rendu utilise `google-chrome --headless=new` ; vérifie qu'il est présent (`which google-chrome`), sinon signale-le et arrête-toi.

ÉTAPE 2 — Choisir les sujets
Dans `tools/calendrier-editorial.md`, prends les trois sujets de la semaine qui commence (lundi, mercredi, vendredi) à l'état « à faire ». S'il en manque, complète avec la section « Réserve » en respectant l'alternance Actu / Conseil / Vie d'hôte. Un sujet marqué « besoin d'un volontaire » ou dépendant d'une information que seul Geoffroy a : remplace-le par un sujet de réserve et signale-le.

ÉTAPE 3 — Vérifier et rédiger
Pour chaque sujet, fais une recherche web pour vérifier l'actualité et chaque chiffre (dates, montants, pourcentages) et note la source. Règles strictes de contenu : jamais de statistique inventée (si tu n'as pas de chiffre sourcé, écris sans chiffre) ; source affichée en pied des slides qui citent un chiffre ; une idée par slide ; ton média, factuel, pédagogique, à la HugoDécrypte ; aucune publicité pour Otizi ou Bookhome dans le corps (la signature en pied de dernière slide suffit) ; pas de photos de presse ni de marques tierces dans les visuels ; textes en français, vouvoiement. Pour un sujet « Actu » daté (vote, entrée en vigueur), si l'événement n'a pas encore eu lieu au moment de l'exécution, rédige la version « ce qui est prévu » et signale dans le récapitulatif qu'une version « ce qui a été décidé » devra être faite le jour J.
Écris un script `tools/post_<slug>.py` par carrousel sur le modèle des exemples (catégorie de la couverture : « Actu » = actu, « Conseil » = conseil, « Vie d'hôte » = vie), génère les slides et les PNG, et construis une planche de contrôle (toutes les slides réduites sur une image) pour chaque carrousel. Regarde chaque planche et corrige les débordements de texte (titres trop longs, cartes qui dépassent) avant de continuer.

ÉTAPE 4 — Publier les images
Copie les PNG dans un dossier `<slug>-AAAA-MM/` à la racine du dépôt, ajoute les scripts dans `tools/`, mets à jour `tools/calendrier-editorial.md` (état « préparé », slug du dossier), commit et push sur `main`. Note le SHA court du commit : les URL d'images sont `https://raw.githubusercontent.com/geoffroybag/otizi-social-assets/<sha>/<dossier>/slide-NN.png`. Vérifie avec curl que chaque URL répond 200 avant l'étape suivante.

ÉTAPE 5 — Créer les brouillons dans Metricool
Avec le connecteur Metricool (outil createScheduledPost), marque Otizi `blogId` 7842510, fuseau `Europe/Paris`, réseau `instagram`, `instagramData.type` POST, `draft: true`, `autoPublish: true`, dates : lundi, mercredi et vendredi de la semaine à 12h15 (si le lundi est déjà passé au moment de l'exécution, décale ce post au samedi 12h15 et signale-le). Chaque post : les 8-9 URL d'images dans l'ordre, un alt-text par slide, et une légende de 3 courts paragraphes (accroche avec le fait principal, question pour faire réagir, 5 hashtags maximum parmi #gite #chambredhotes #locationsaisonniere #hebergeur #airbnb #booking #lmnp). Note le `plannerUrl` renvoyé pour chaque post.
Si le connecteur Metricool n'est pas disponible ou renvoie une erreur, ne crée rien et signale-le : les images et les scripts restent dans le dépôt.

ÉTAPE 6 — Compte rendu à Geoffroy
Envoie-lui les trois planches de contrôle (SendUserFile) et un message court (SendUserMessage) en français : pour chaque carrousel, la date prévue, le titre, la source principale, le lien Metricool du brouillon ; puis ce qu'il doit faire : ouvrir Metricool et retirer la case « brouillon » sur les posts validés, ou répondre dans la conversation avec les corrections. Termine par la liste des points à vérifier de son côté (chiffres non confirmés, sujets remplacés, événement daté à finaliser).
