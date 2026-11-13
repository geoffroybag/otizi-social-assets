# Calendrier éditorial — Otizi décrypte

Rythme : 3 carrousels par semaine (lundi, mercredi, vendredi à 12h15, Europe/Paris), préparés et programmés le vendredi précédent à 15h par la tâche automatique ; Geoffroy relit dans Metricool avant le lundi.
Familles : **Actu** (réglementation, plateformes), **Conseil** (métier, applicable tout de suite), **Vie d'hôte** (tendances, retours d'expérience, côté voyageur).

Deux listes, à tenir à jour à chaque passage :

- **Programmés** : les carrousels datés, état `programmé` (dans Metricool, à relire avant publication) ou `publié`.
- **Stock** : les sujets à venir, sans date, dans l'ordre d'intérêt. Le vendredi, la tâche en pioche trois pour la semaine suivante (un sujet daté se place sur la bonne semaine, voir la colonne « Quand »), puis réapprovisionne le stock par une recherche web s'il tombe sous six sujets (entrées marquées « proposé le JJ/MM » dans Notes, à valider ou retirer par Geoffroy).

Ce fichier se lit aussi sur la page État d'Ozi (bloc « Carrousels Instagram ») et se modifie sur GitHub.

Avant de réapprovisionner le Stock par une recherche web, piocher d'abord dans la banque d'idées `tools/idees-contenu.md` (sujets validés par Geoffroy le 5 nov. 2026, classés par public : hébergeurs installés, nouveaux hébergeurs, études open data, outils).

## Programmés

| Date | Famille | Sujet | État | Notes |
|---|---|---|---|---|
| mar 3 nov 2026 | Actu | Airbnb interdit les corvées de départ (règles du 20 nov.) | publié | https://www.instagram.com/p/DfRvIiSG77Q/ |
| jeu 5 nov 2026 | Conseil | Les 5 détails qui font une note 5 étoiles | publié | `5-etoiles-2026-11/`, `tools/post_5etoiles.py` ; source : OnePoll pour Booking.com (nov. 2025) ; https://www.instagram.com/p/DfW5zcOFT3C/ |
| ven 6 nov 2026 | Vie d'hôte | Ce que les voyageurs regardent avant de réserver (OnePoll/Booking) | publié | `attentes-voyageurs-2026-11/`, `tools/post_attentes.py` ; source : OnePoll pour Booking.com (nov. 2025) ; publié le 6 nov. à 13h45 ; https://www.instagram.com/p/DfZo5ZJlRFB/ |
| lun 9 nov 2026 | Actu | Chambres d'hôtes : 21,2 % de cotisations, le choc 2026 | publié | `cotisations-2026-11/`, `tools/post_cotisations.py` ; sources : Compta Online (taux 2026), The Connexion (23 déc. 2025), QE n° 6664, Assemblée nationale (2e séance du 30 oct. 2026), LCP (3 nov. 2026) ; **publié avec l'ancienne version des slides 7 et 9 (amendement I-540 « adopté », avant le rejet du 4 nov.) ; le dépôt et l'article sont à jour, pas le post Instagram** ; article otizi.fr/blog/cotisations-chambres-hotes-2026 ; https://www.instagram.com/p/DfhM_Ghm48o/ |
| mer 11 nov 2026 | Conseil | Basse saison : 6 façons de remplir novembre | publié | `basse-saison-2026-11/`, `tools/post_basse_saison.py` ; sans chiffre (aucune donnée sourcée) ; https://www.instagram.com/p/DfmWl8dm2-d/ |
| ven 13 nov 2026 | Vie d'hôte | Le petit-déjeuner qui fait parler (chambres d'hôtes) | publié | `petit-dejeuner-2026-11/`, `tools/post_petit_dejeuner.py` ; sources : Code du tourisme art. D. 324-13, règlement (UE) 1169/2011, décret 2015-447 ; https://www.instagram.com/p/DfrgKYjlQS1/ |
| lun 16 nov 2026 | Actu | Combien vous coûtent vraiment les plateformes ? (lancement du simulateur de commissions) | programmé | `simulateur-commissions-2026-11/`, `tools/post_simulateur_commissions.py` ; exemple 30 000 € de CA → 4 428 € de commissions par an TTC (formule réelle du simulateur : taux × 1,2 de TVA ; la note du stock disait 3 900 €, c'était sans la TVA et sans les bons taux), 22 140 € sur 5 ans, +1 302 €/an à 40 % de direct ; sources : Toutsurmesfinances (28 oct. 2026, Airbnb 15,5 % au 13 oct.), Rental Scale-Up (16 oct. 2026, Abritel 12 % au 29 oct. ; 8 juil. 2026, TVA), Smoobu (Booking 15 % en moyenne), service-public F2043 ; **le simulateur utilise encore 8 % pour Abritel, à passer à 12 %** ; article otizi.fr/blog/commissions-plateformes-2026 ; https://app.metricool.com/planner/calendar?blogId=7842510&openWithPostUuid=-4755118019022729804 |
| mer 18 nov 2026 | Conseil | Livret d'accueil : ce qu'il doit contenir en 2026 | programmé | `livret-accueil-2026-11/`, `tools/post_livret_accueil.py` ; sans statistique ; sources : service-public.gouv.fr (tri des biodéchets A15940, numéros d'urgence A17758, détecteur de fumée F19950, taxe de séjour F743, meublé de tourisme F2043), Airbnb (politique du 20 oct. 2026 via Rental Scale-Up) ; article otizi.fr/blog/livret-accueil-2026 ; https://app.metricool.com/planner/calendar?blogId=7842510&openWithPostUuid=-691827644620977393 |
| ven 20 nov 2026 | Actu | Airbnb : les nouvelles règles de la maison s'appliquent (réservations dès le 20 nov.) | programmé | `airbnb-regles-2026-11/`, `tools/post_airbnb_regles.py` ; boucle avec le post du 3 nov. ; rassemblement d'hôtes annoncé le 20 nov. à 16 h devant le siège d'Airbnb France (TourMaG, 28 oct. 2026 : pétition > 21 000 signatures) ; sources : Rental Scale-Up (21 et 23 oct. 2026), Euronews (21 oct. 2026), TourMaG et Mediaterranee (28 oct. 2026), Toutsurmesfinances (28 oct. 2026) ; article otizi.fr/blog/airbnb-regles-maison-20-novembre ; https://app.metricool.com/planner/calendar?blogId=7842510&openWithPostUuid=3315648246279588631 |

## Stock

| Famille | Sujet | Quand | Notes |
|---|---|---|---|
| Actu | Le plateau des plateformes : pourquoi le direct redevient stratégique | dès la semaine du 23 nov. (le post simulateur passe le 16 nov.) | Eurostat : nuitées via plateformes +6,9 % jan.–juin 2026 contre +13,4 % en 2025 ; France n° 1 en Europe (213 M de nuitées en 2025) ; renvoie au simulateur |
| Actu | Enregistrement national obligatoire : le guide pas à pas | | service-public.gouv.fr ; concerne aussi ceux qui ont déjà un numéro ; les chambres d'hôtes restent en déclaration mairie |
| Conseil | Les 5 réglages de calendrier qui font perdre des réservations | | durée minimum, délai de préparation, fenêtre de réservation, jours d'arrivée ; sans chiffre |
| Conseil | Le message post-séjour qui fait revenir les clients en direct | | modèle de message ; pas de chiffre inventé ; renvoie au simulateur |
| Actu | Taxe d'habitation : votre commune peut vous exonérer | avant les budgets communaux (déc.–janv.) | loi de finances 2026 : exonération possible partout sur vote local, gîtes ruraux exclus de plein droit ; modèle de courrier à la mairie en téléchargement (capture email) |
| Actu | Chambres d'hôtes : fin de l'exonération 760 € au 31 déc. 2026 | mi-décembre | que faire au 1er janvier ; à lier au post cotisations du 9 nov. |
| Vie d'hôte | Été 2026 : record depuis 15 ans, mais sans les étrangers | | Insee Focus n° 387 : plus de deux nuitées sur trois sont françaises ; conséquence : viser familles françaises et proximité |
| Actu | Budget 2027 : ce qui a été voté pour les meublés | à dater (examen au Sénat) | amortissement 1,5 %/5 000 € par foyer ; **à revoir (6 nov.) : l'Assemblée a rejeté la première partie le 4 nov. (scrutin n° 9759), il n'y a pas eu de vote le 17 ; le Sénat repart du texte initial du gouvernement ; angle et date à confirmer par Geoffroy ; laissé dans le stock le 13 nov.** |
| Conseil | Fixer ses prix pour Noël et le Nouvel An | fin novembre | minimum de nuits, suppléments, dates à ne pas brader |
| Vie d'hôte | Déco de Noël dans un gîte : jusqu'où aller ? | fin novembre | attentes, agacements, budget |
| Actu | Taxe de séjour 2027 : nouveaux tarifs, qui collecte quoi | début décembre | communes ont voté avant le 1er oct. ; application 1er janv. |
| Vie d'hôte | Portrait d'hôte : un client raconte son premier hiver | | besoin d'un volontaire (Geoffroy) : ne pas piocher sans son accord |
| Conseil | Rédiger une annonce qui convertit | | |
| Conseil | Les micro-doutes qui font basculer vos clients vers une OTA | | idée de Geoffroy (4 nov.) : les voyageurs ne quittent pas le site d'un hébergeur pour un gros problème technique mais pour de petites hésitations, des moments subtils mais décisifs ; lister ces micro-doutes et comment les lever |
| Conseil | Et si le secret des réservations directes résidait dans l'anticipation ? | | idée de Geoffroy (4 nov.) : anticiper les questions, les besoins et les objections du voyageur avant qu'il ne les formule ; angle hôte, pas de pub Otizi dans les slides |
| Conseil | Des photos sans photographe | | |
| Conseil | Gérer un avis injuste | | |
| Conseil | Arrivée autonome sans stress | | |
| Conseil | Le ménage entre deux séjours | | |
| Conseil | Accueillir des animaux, ou pas | | |
| Vie d'hôte | Les demandes de voyageurs les plus absurdes | | |
| Vie d'hôte | Gîte vs chambre d'hôtes : deux métiers | | |
| Conseil | Ouvrir un gîte en 2026 : les 10 démarches dans l'ordre | | déclaration mairie, enregistrement national, SIRET, assurance, taxe de séjour ; cible nouveaux hébergeurs ; check-list téléchargeable par email (outil à faire) |
| Conseil | Faut-il être sur Airbnb ET Booking au début ? | | cible nouveaux hébergeurs |
| Conseil | Première saison : fixer ses prix sans se brader | | cible nouveaux hébergeurs ; renvoie au futur calculateur de prix plancher |
| Vie d'hôte | Tendances de voyage 2027 | | début 2027 |
| Actu | Loi Le Meur, deux ans après (19 nov. 2024) | autour du 19 nov. | |
| Actu | DPE et meublés de tourisme | | |
| Actu | Acomptes plafonnés à 25 % (décret 2026-121) | | |
| Actu | Nouveautés Airbnb de l'hiver | | |
| Actu | Faut-il faire classer son gîte ? (micro-BIC 77 700 € / 50 % vs 15 000 € / 30 %) | | fusionne « Meublé non classé » ; renvoie au futur simulateur micro-BIC |
