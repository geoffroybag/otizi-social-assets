#!/usr/bin/env python3
"""Carrousel « Conseil » : livret d'accueil, ce qu'il doit contenir en 2026."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from carrousel_lib import *

PROJ = work_dir("livret-accueil", "project")
N = 9
SRC_TRI = "Source : service-public.gouv.fr, tri des biodéchets (1er janvier 2024)"
SRC_URG = "Sources : service-public.gouv.fr, numéros d'urgence · fiche F19950 (détecteur de fumée)"
SRC_AIR = "Source : Airbnb, politique « Règles de la maison et demandes raisonnables » (réservations dès le 20 nov. 2026)"
SRC_LOI = "Sources : service-public.gouv.fr, fiches F743 (taxe de séjour) et F2043 (meublé de tourisme)"
slides = {}

slides["Main.dc.html"] = page("Couverture", category_pill("Conseil", "conseil"),
    f"""
    {title_boxes([("Livret d'accueil :", "white", 70), ("ce qu'il doit", "mint", 92), ("contenir en 2026", "white", 68)])}
    <div>{para("Arrivée autonome, Wi-Fi, tri, numéros utiles, règles écrites comme des demandes : la liste à jour, et les trois choses qui ont changé cette année.", 36, BODY, maxw=860)}
      <div style="width: 260px; height: 10px; border-radius: 5px; background: {ACCENT}; margin-top: 18px"></div></div>
    """,
    "Conseils pour les gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {INK}; font-weight: 900">Glisser {icon("arrow")}</span>',
    body_gap=44, cover=True)

slides["S1.dc.html"] = page("Pourquoi le relire", f"2 / {N}",
    f"""
    {title_plain(["Pourquoi le relire", "cette année"])}
    {para("Un livret d'accueil vieillit vite : un code qui change, un restaurant fermé, une règle qui n'a plus le droit d'exister. Trois nouveautés méritent une relecture complète.", 32)}
    {numbered([
        ("Le tri des biodéchets", "est généralisé depuis le 1er janvier 2024 : votre collectivité a mis en place une solution, votre livret doit l'expliquer."),
        ("L'enregistrement national", "des meublés de tourisme s'applique depuis le 20 mai 2026 : un numéro à 13 caractères sur chaque annonce."),
        ("Les règles de départ d'Airbnb", "changent le 20 novembre 2026 : ce qui était « obligatoire » devient une « demande »."),
    ])}
    """,
    "Sources : service-public.gouv.fr · Airbnb (20 oct. 2026)", body_gap=30)

slides["S2.dc.html"] = page("L'arrivée autonome", f"3 / {N}",
    f"""
    {title_plain(["L'arrivée autonome,", "lue depuis la voiture"], 70)}
    {para("Le voyageur ouvre votre livret sur son téléphone, à la nuit tombée, devant un portail. Tout ce qui précède l'entrée doit tenir en une page.", 31)}
    {numbered([
        ("L'adresse exacte et une photo de l'entrée,", "avec le nom du portail ou de la porte, et où se garer."),
        ("La boîte à clés ou le code,", "avec une photo de l'endroit, et ce qu'il faut faire si ça ne s'ouvre pas : votre numéro, puis celui d'une personne relais."),
        ("Les heures d'arrivée et de départ,", "et la marche à suivre si le voyageur arrive plus tôt ou plus tard."),
    ])}
    """,
    "Conseil · gîtes et chambres d'hôtes", body_gap=30)

slides["S3.dc.html"] = page("Wi-Fi et équipements", f"4 / {N}",
    f"""
    {title_plain(["Le Wi-Fi et", "les équipements"])}
    {numbered([
        ("Le nom du réseau et le mot de passe,", "écrits en clair et copiables, pas sur une photo. Ajoutez le débit mesuré dans la pièce où l'on travaille."),
        ("Une fiche par appareil compliqué :", "poêle, chaudière, plaque à induction, lave-linge, volets. Une photo et trois phrases suffisent."),
        ("Piscine, spa, cheminée :", "les consignes de sécurité, écrites noir sur blanc, et l'endroit où se trouvent la barrière, l'alarme ou l'extincteur."),
        ("Ce qui ne marche pas :", "dites-le avant qu'ils le découvrent. Une prise capricieuse signalée n'est plus un défaut dans l'avis."),
    ])}
    """,
    "Conseil · gîtes et chambres d'hôtes", body_gap=34)

slides["S4.dc.html"] = page("Le tri", f"5 / {N}",
    f"""
    {title_plain(["Le tri des déchets,", "version 2024"], 72)}
    {para("Depuis le 1er janvier 2024, le tri à la source des biodéchets concerne tout le monde : votre collectivité doit proposer une solution (bac dédié, composteur, point d'apport). Mais chaque commune fait différemment, et vos voyageurs viennent d'ailleurs.", 31)}
    {numbered([
        ("Où sont les bacs,", "avec une photo, et le jour de collecte si le voyageur doit les sortir pendant son séjour."),
        ("Quoi va où :", "trois lignes, pas un tableau : emballages, verre, déchets alimentaires, reste."),
        ("Écrivez-le comme une demande,", "pas comme une règle : « merci de trier dans les bacs de la cuisine » suffit, et reste conforme aux règles d'Airbnb."),
    ])}
    """,
    SRC_TRI, body_gap=30)

slides["S5.dc.html"] = page("Les numéros utiles", f"6 / {N}",
    f"""
    {title_plain(["Les numéros", "qui rassurent"])}
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px">
      {card("numéro d'urgence européen, joignable partout", "112 :")}
      {card("Samu (urgence médicale)", "15 :")}
      {card("police ou gendarmerie", "17 :")}
      {card("sapeurs-pompiers", "18 :")}
      {card("par SMS ou application, pour les personnes sourdes ou malentendantes", "114 :")}
      {card("médecin de garde, pharmacie, vétérinaire, et vous.", "Les vôtres :", light=True)}
    </div>
    {para("En location saisonnière, c'est au propriétaire d'installer, d'entretenir et de remplacer le détecteur de fumée (norme NF EN 14604). Indiquez où il est, et vérifiez la pile à chaque changement de saison.", 27, MUTED)}
    """,
    SRC_URG, body_gap=28)

slides["S6.dc.html"] = page("Des demandes, pas des règles", f"7 / {N}",
    f"""
    {title_plain(["Des demandes,", "pas des règles"])}
    {para("Pour les réservations Airbnb faites à partir du 20 novembre 2026, un hôte ne peut plus exiger de laver la vaisselle, retirer les draps, lancer une machine ou sortir les poubelles hors du logement. Ni facturer une pénalité si ce n'est pas fait.", 31)}
    <div style="display: flex; flex-direction: column; gap: 12px">
      {item("« Merci de déposer la vaisselle sale dans l'évier »", "yes")}
      {item("« Merci de regrouper les serviettes utilisées »", "yes")}
      {item("« Vaisselle faite et rangée obligatoire »", "no")}
      {item("« 50 € de supplément si les draps ne sont pas retirés »", "no")}
    </div>
    {para("En direct ou sur Booking, vos conditions s'appliquent. Mais un livret qui demande poliment vaut mieux qu'un règlement qui menace, quel que soit le canal.", 27, MUTED)}
    """,
    SRC_AIR, body_gap=26)

slides["S7.dc.html"] = page("Ce que la loi demande", f"8 / {N}",
    f"""
    {title_plain(["Ce que la loi", "vous demande"])}
    {numbered([
        ("La taxe de séjour :", "le tarif doit être affiché chez le logeur, et la taxe apparaît sur une ligne distincte de la facture. Une ligne dans le livret, et le voyageur ne la découvre pas au départ."),
        ("Le numéro d'enregistrement :", "13 caractères, sur chaque annonce du meublé, y compris votre site. Dans le livret, il rassure : votre maison est déclarée."),
        ("Les voyageurs étrangers :", "une fiche individuelle de police à faire remplir à l'arrivée et à conserver six mois. Prévenez-les dans le livret, ils ne seront pas surpris."),
    ])}
    """,
    SRC_LOI, body_gap=34)

slides["S8.dc.html"] = page("À retenir", f"9 / {N}",
    f"""
    {title_plain(["Le test", "de cette semaine"])}
    {numbered([
        ("Ouvrez votre livret sur votre téléphone,", "dehors, la nuit : trouvez-vous le code d'entrée en moins de dix secondes ?"),
        ("Cherchez les mots « obligatoire » et « interdit »,", "et réécrivez chaque phrase en demande."),
        ("Ajoutez trois lignes :", "le tri de votre commune, les numéros d'urgence, l'emplacement du détecteur de fumée."),
    ])}
    {para("Sources : service-public.gouv.fr (tri des biodéchets ; numéros d'urgence ; fiche F19950 détecteur de fumée ; fiche F743 taxe de séjour ; fiche F2043 meublé de tourisme) · Airbnb, politique « Règles de la maison et demandes raisonnables », 20 oct. 2026.", 21, MUTED)}
    """,
    "Chaque semaine, ce qui change pour les gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {VIOLET}; font-weight: 900">Suivez-nous {icon("arrow")}</span>',
    body_gap=30)

order = list(slides.keys())
titles = ["1 · Couverture", "2 · Pourquoi le relire", "3 · Arrivée autonome", "4 · Wi-Fi et équipements", "5 · Le tri", "6 · Numéros utiles", "7 · Demandes, pas règles", "8 · Ce que la loi demande", "9 · À retenir"]
write_all(slides, PROJ)
json.dump(canvas_json("Carrousel livret d'accueil 2026", order, titles), open(PROJ + "/canvas.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
render_all(PROJ, order, work_dir("livret-accueil", "png"))
print("ok", len(order))
