#!/usr/bin/env python3
"""Carrousel « Vie d'hôte » : ce que les voyageurs regardent vraiment avant de réserver (OnePoll pour Booking, nov. 2025)."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from carrousel_lib import *

PROJ = work_dir("attentes", "project")
N = 8
SRC = "Source : OnePoll pour Booking.com, 2 000 Français, nov. 2025"
slides = {}

slides["Main.dc.html"] = page("Couverture", category_pill("Vie d'hôte", "vie"),
    f"""
    {title_boxes([("Ce que les", "white", 84), ("voyageurs regardent", "mint", 66), ("avant de réserver", "white", 76)])}
    <div>{para("Une enquête auprès de 2 000 Français partant en vacances. Les chiffres bousculent quelques idées reçues sur ce qui fait réserver.", 38, BODY, maxw=860)}
      <div style="width: 260px; height: 10px; border-radius: 5px; background: {ACCENT}; margin-top: 18px"></div></div>
    """,
    "L'actu des gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {INK}; font-weight: 900">Glisser {icon("arrow")}</span>',
    body_gap=44, cover=True)

slides["S1.dc.html"] = page("Les 5 critères", f"2 / {N}",
    f"""
    {title_plain(["Les 5 critères", "qui font réserver"])}
    <div style="display: flex; flex-direction: column; gap: 22px">
      {bar("L'emplacement", 64)}
      {bar("Les avis et les notes", 52)}
      {bar("Les équipements essentiels (Wi-Fi, TV)", 51)}
      {bar("Les photos", 48)}
      {bar("Un extérieur : jardin, terrasse, balcon", 31)}
    </div>
    {para("Part des voyageurs citant chaque critère comme déterminant.", 26, MUTED)}
    """,
    SRC, body_gap=36)

slides["S2.dc.html"] = page("L'emplacement", f"3 / {N}",
    f"""
    {title_plain(["L'emplacement d'abord,", "mais vous pouvez le raconter"])}
    {stat("64 %", "en font le critère n° 1. Vous ne déplacerez pas votre gîte, mais vous pouvez changer ce que le voyageur en comprend.", 150)}
    {numbered([
        ("Dites la distance en minutes,", "pas en kilomètres : « 12 min à pied de la plage », « 25 min de Carcassonne »."),
        ("Nommez ce qu'il y a autour :", "le marché du samedi, la cave, le sentier qui part du portail."),
        ("Une carte dans l'annonce", "vaut mieux qu'un paragraphe."),
    ])}
    """,
    SRC, body_gap=30)

slides["S3.dc.html"] = page("Les photos", f"4 / {N}",
    f"""
    {title_plain(["Les photos :", "on regarde tout"])}
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px">
      <div style="background: #FFFFFF; border: 2px solid {LINE}; border-radius: 18px; padding: 28px; display: flex; flex-direction: column; gap: 10px">
        <div style="font-size: 96px; line-height: 0.9; font-weight: 900; letter-spacing: -0.04em; color: {VIOLET}">48 %</div>
        <div style="font-size: 27px; line-height: 1.3; color: {BODY}">regardent toutes les photos disponibles avant de réserver.</div>
      </div>
      <div style="background: {VIOLET}; color: #FFFFFF; border-radius: 18px; padding: 28px; display: flex; flex-direction: column; gap: 10px">
        <div style="font-size: 96px; line-height: 0.9; font-weight: 900; letter-spacing: -0.04em; color: {ACCENT}">27 %</div>
        <div style="font-size: 27px; line-height: 1.3">refusent un logement qu'ils jugent peu photogénique.</div>
      </div>
    </div>
    {numbered([
        ("L'extérieur passe avant la chambre :", "31 % citent le jardin ou la terrasse, contre 22 % pour la chambre et 14 % pour le salon."),
        ("Une photo par pièce, à la lumière du jour,", "et la première sur ce que vous avez de plus singulier."),
    ])}
    """,
    SRC, body_gap=28)

slides["S4.dc.html"] = page("Pièce par pièce", f"5 / {N}",
    f"""
    {title_plain(["Pièce par pièce,", "ce qu'ils attendent"])}
    {numbered([
        ("Salon :", "sobre et confortable (59 %), avec vue sur le jardin (58 %) et une TV connectée (43 %)."),
        ("Chambre :", "rangement impeccable (51 %), lit confortable (49 %), lumière naturelle (45 %)."),
        ("Cuisine :", "le désordre rebute 47 % des voyageurs. L'équipement moderne compte plus que la taille."),
        ("Salle de bain :", "lumière, douche séparée et fenêtre reviennent en tête, sans chiffre détaillé."),
    ])}
    """,
    SRC, body_gap=36)

slides["S5.dc.html"] = page("Le jardin", f"6 / {N}",
    f"""
    {title_plain(["Le jardin,", "l'angle mort des annonces"])}
    {para("Les voyageurs ont des avis tranchés sur l'extérieur, et ils ne les écrivent pas toujours dans l'avis.", 32)}
    <div style="display: flex; flex-direction: column; gap: 14px">
      {item("45 % sont rebutés par un jardin négligé", "no")}
      {item("44 % par un jardin trop minéral", "no")}
      {item("35 % par des plantes artificielles", "no")}
      {item("45 % apprécient une intimité préservée : haie, claustra, brise-vue", "yes")}
    </div>
    """,
    SRC, body_gap=30)

slides["S6.dc.html"] = page("La déco", f"7 / {N}",
    f"""
    {title_plain(["Côté déco,", "pas de piège"])}
    <div style="display: flex; flex-direction: column; gap: 22px">
      {bar("Scandinave", 43, 50)}
      {bar("Luxe contemporain", 28, 50)}
      {bar("Cottage", 25, 50)}
      {bar("Rustique", 25, 50)}
    </div>
    {para("Styles préférés des voyageurs interrogés. Une seule règle : un style assumé et cohérent se vend mieux qu'un mélange.", 28, MUTED)}
    """,
    SRC, body_gap=36)

slides["S7.dc.html"] = page("À retenir", f"8 / {N}",
    f"""
    {title_plain(["Ce que vous pouvez", "changer ce week-end"])}
    {numbered([
        ("Réécrivez la première ligne de votre annonce", "autour de l'emplacement, en minutes et en lieux concrets."),
        ("Refaites 3 photos :", "l'extérieur, la chambre rangée, la cuisine dégagée."),
        ("Passez une heure dans le jardin :", "c'est le critère le plus sous-estimé, et le moins cher à améliorer."),
    ])}
    {para("Enquête OnePoll pour Booking.com, 2 000 adultes français partant en vacances, 4-10 novembre 2025. Relayée par Le Routard, janvier 2026.", 24, MUTED)}
    """,
    "Chaque semaine, ce qui change pour les gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {VIOLET}; font-weight: 900">Suivez-nous {icon("arrow")}</span>',
    body_gap=30)

order = list(slides.keys())
titles = ["1 · Couverture", "2 · 5 critères", "3 · Emplacement", "4 · Photos", "5 · Pièce par pièce", "6 · Jardin", "7 · Déco", "8 · À retenir"]
write_all(slides, PROJ)
json.dump(canvas_json("Carrousel attentes voyageurs", order, titles), open(PROJ + "/canvas.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
render_all(PROJ, order, work_dir("attentes", "png"))
print("ok", len(order))
