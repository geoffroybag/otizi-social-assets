#!/usr/bin/env python3
"""Carrousel « Conseil » : fixer ses prix pour Noël et le Nouvel An sans se brader."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from carrousel_lib import *

PROJ = work_dir("prix-noel", "project")
N = 9
SRC_CAL = "Source : education.gouv.fr, calendrier scolaire 2026-2027 (arrêté du 22 oct. 2025)"
SRC_KAYAK = "Source : Kayak, « Où partir à Noël 2026 », 13 oct. 2026 (recherches du 1er avr. au 1er sept. 2026, pourcentages approximatifs)"
SRC_AIR = "Source : Airbnb, newsroom France, 8 déc. 2022 (mesures du Nouvel An, en place depuis 2020)"
SRC_ACPT = "Source : décret n° 2026-121 du 20 fév. 2026 (JO du 22 fév.), réservations depuis le 1er mars 2026"
NOSRC = "Conseil · gîtes et chambres d'hôtes"
slides = {}

slides["Main.dc.html"] = page("Couverture", category_pill("Conseil", "conseil"),
    f"""
    {title_boxes([("Noël et Nouvel An :", "white", 62), ("vos prix", "mint", 104), ("sans vous brader", "white", 66)])}
    <div>{para("Deux semaines de vacances, deux réveillons un jeudi soir, deux clientèles qui n'ont rien à voir. Minimum de nuits, suppléments, acompte, dates à ne pas solder : la méthode pour fixer votre grille des fêtes.", 36, BODY, maxw=860)}
      <div style="width: 260px; height: 10px; border-radius: 5px; background: {ACCENT}; margin-top: 18px"></div></div>
    """,
    "Conseils pour les gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {INK}; font-weight: 900">Glisser {icon("arrow")}</span>',
    body_gap=44, cover=True)

slides["S1.dc.html"] = page("Le calendrier", f"2 / {N}",
    f"""
    {title_plain(["Le calendrier", "2026-2027"])}
    <div style="display: flex; flex-direction: column; gap: 14px">
      {card("du samedi 19 décembre 2026 au lundi 4 janvier 2027, les mêmes dates pour les zones A, B et C.", "Vacances scolaires :")}
      {card("Noël tombe un vendredi, le 1er janvier aussi : deux week-ends de trois jours, et deux réveillons un jeudi soir.", "Deux ponts naturels :", light=True)}
      {card("du 19 au 26 décembre, puis du 26 décembre au 2 janvier. Et une dernière fenêtre, souvent oubliée, du 2 au 4 janvier.", "Deux semaines pleines :")}
    </div>
    {para("Posez ces dates dans votre calendrier avant de toucher aux prix : c'est elles qui dictent les durées de séjour que vous pouvez demander.", 29, MUTED)}
    """,
    SRC_CAL, body_gap=30)

slides["S2.dc.html"] = page("Ce que cherchent les voyageurs", f"3 / {N}",
    f"""
    {title_plain(["Ce que disent", "les recherches"])}
    {stat("+20&nbsp;%", "de recherches d'hébergements en France pour les fêtes 2026, par rapport à l'an dernier", 120)}
    {numbered([
        ("Les prix des locations de vacances reculent de 10 %", "sur un an, selon les mêmes données : la demande monte, mais l'offre aussi. Suivre le marché à la baisse n'est pas une obligation."),
        ("Le Nouvel An se paie plus cher que Noël :", "une arrivée le 21 décembre coûte en moyenne 23 % de moins qu'une arrivée le 31 décembre."),
        ("Les baisses de dernière minute existent :", "l'an dernier, une semaine avant Noël, les tarifs étaient environ 18 % plus bas qu'en octobre. Ceux qui ont vendu tôt n'ont pas eu à solder."),
    ])}
    """,
    SRC_KAYAK, body_gap=28)

slides["S3.dc.html"] = page("Deux clientèles", f"4 / {N}",
    f"""
    {title_plain(["Deux semaines,", "deux clientèles"])}
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px">
      <div style="background: #FFFFFF; border: 2px solid {LINE}; border-radius: 18px; padding: 28px; display: flex; flex-direction: column; gap: 12px">
        <div style="font-size: 40px; line-height: 1; font-weight: 900; letter-spacing: -0.02em; color: {VIOLET}">Noël</div>
        <div style="font-size: 27px; line-height: 1.3; color: {BODY}">Des familles, souvent trois générations, qui cherchent une maison entière, une grande table, une cheminée et du calme. Elles réservent tôt, restent longtemps, et reviennent.</div>
      </div>
      <div style="background: {VIOLET}; color: #FFFFFF; border-radius: 18px; padding: 28px; display: flex; flex-direction: column; gap: 12px">
        <div style="font-size: 40px; line-height: 1; font-weight: 900; letter-spacing: -0.02em; color: {ACCENT}">Nouvel An</div>
        <div style="font-size: 27px; line-height: 1.3">Des groupes d'amis, des couples, des gens qui veulent faire la fête ou fuir la ville. Séjours plus courts, décision plus tardive, plus de bruit, plus de risque.</div>
      </div>
    </div>
    {para("Une seule grille pour les deux, c'est soit brader Noël, soit rater le Nouvel An. Traitez-les comme deux saisons distinctes dans votre calendrier.", 30)}
    """,
    NOSRC, body_gap=32)

slides["S4.dc.html"] = page("Le minimum de nuits", f"5 / {N}",
    f"""
    {title_plain(["Le minimum de nuits,", "votre premier levier"], 70)}
    {numbered([
        ("Noël : trois nuits au moins,", "du jeudi 24 au dimanche 27, ou la semaine entière. Une famille ne vient pas réveillonner pour une nuit, et vous ne voulez pas d'un ménage le 25 au matin."),
        ("Nouvel An : jamais une seule nuit.", "Trois nuits minimum autour du 31 écarte la plupart des fêtes improvisées. Airbnb lui-même bloque depuis 2020 les réservations d'une seule nuit du 31 décembre pour un logement entier aux voyageurs sans historique."),
        ("Entre les deux :", "acceptez les séjours qui enchaînent, du 26 au 2 par exemple. Un trou de deux nuits entre Noël et le Nouvel An ne se revend presque jamais."),
    ])}
    """,
    SRC_AIR, body_gap=32)

slides["S5.dc.html"] = page("Suppléments et inclus", f"6 / {N}",
    f"""
    {title_plain(["Facturez ce qui coûte,", "incluez ce qui marque"], 68)}
    <div style="display: flex; flex-direction: column; gap: 12px">
      {item("Le bois de chauffage, le linge, le ménage de fin de séjour : des lignes à part, annoncées avant la réservation", "yes")}
      {item("La taxe de séjour, sur une ligne distincte de votre facture", "yes")}
      {item("Le sapin, les décorations, le panier de bienvenue : inclus, c'est eux qu'on photographie", "yes")}
      {item("Un « supplément fêtes » sans contrepartie : c'est votre prix de base qui doit monter, pas une ligne obscure", "no")}
    </div>
    {para("En chambres d'hôtes, le réveillon se vend à part : une table d'hôtes à prix fixe par personne, menu annoncé, réservée à l'avance. Le prix de la chambre, lui, reste celui de la saison.", 28, MUTED)}
    """,
    NOSRC, body_gap=28)

slides["S6.dc.html"] = page("Acompte et conditions", f"7 / {N}",
    f"""
    {title_plain(["L'acompte et", "les conditions"])}
    {para("Les fêtes sont la période où une annulation fait le plus mal : la date ne se revend pas. C'est le moment de relire vos conditions, en direct comme sur les plateformes.", 31)}
    {numbered([
        ("Pour un meublé de tourisme, l'acompte est plafonné à 25 %", "du loyer total, et le solde ne peut être exigé qu'un mois au plus tôt avant l'entrée dans les lieux."),
        ("Depuis le 1er mars 2026,", "cet acompte peut être versé jusqu'à douze mois avant la remise des clés, contre six auparavant : vous pouvez l'encaisser dès la réservation d'un Noël lointain."),
        ("Écrivez vos conditions d'annulation", "noir sur blanc, avec les dates, et la caution. Sur les plateformes, choisissez une politique stricte pour ces deux semaines."),
    ])}
    """,
    SRC_ACPT, body_gap=28)

slides["S7.dc.html"] = page("Les dates à ne pas brader", f"8 / {N}",
    f"""
    {title_plain(["Les dates", "à ne pas brader"])}
    {numbered([
        ("Les nuits du 24, du 25 et du 31 décembre", "ne se soldent pas. Si la maison est encore libre à dix jours, ajoutez un avantage (bois offert, départ tardif, panier) plutôt que de baisser le prix affiché : le prix, lui, vous suit l'an prochain."),
        ("Les semaines qui suivent, oui.", "Du 4 janvier au début des vacances d'hiver, la demande retombe : c'est là que votre tarif de basse saison reprend, franchement."),
        ("Et si vous fêtez Noël en famille,", "fermez. Une maison louée sans accueil ni réponse coûte plus cher en avis qu'elle ne rapporte."),
    ])}
    """,
    NOSRC, body_gap=34)

slides["S8.dc.html"] = page("À retenir", f"9 / {N}",
    f"""
    {title_plain(["La check-list", "de la semaine"])}
    {numbered([
        ("Posez le calendrier :", "19 décembre au 4 janvier, deux ponts du vendredi, deux semaines pleines."),
        ("Réglez les durées :", "trois nuits minimum à Noël comme au Nouvel An, pas de trou entre les deux."),
        ("Fixez deux grilles,", "Noël et Nouvel An, avec les suppléments annoncés et l'acompte encaissé à la réservation."),
        ("Décidez des nuits que vous ne solderez pas,", "et de celles, en janvier, où vous reprendrez votre tarif de basse saison."),
    ])}
    {para("Sources : education.gouv.fr, calendrier scolaire 2026-2027 · Kayak, « Où partir à Noël 2026 », 13 oct. 2026 · Airbnb, newsroom France, 8 déc. 2022 · décret n° 2026-121 du 20 fév. 2026. Chiffres indicatifs, à adapter à votre maison.", 21, MUTED)}
    """,
    "Chaque semaine, ce qui change pour les gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {VIOLET}; font-weight: 900">Suivez-nous {icon("arrow")}</span>',
    body_gap=28)

order = list(slides.keys())
titles = ["1 · Couverture", "2 · Le calendrier", "3 · Les recherches", "4 · Deux clientèles", "5 · Minimum de nuits", "6 · Suppléments et inclus", "7 · Acompte et conditions", "8 · Dates à ne pas brader", "9 · Check-list"]
write_all(slides, PROJ)
json.dump(canvas_json("Carrousel prix de Noël et du Nouvel An", order, titles), open(PROJ + "/canvas.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
render_all(PROJ, order, work_dir("prix-noel", "png"))
print("ok", len(order))
