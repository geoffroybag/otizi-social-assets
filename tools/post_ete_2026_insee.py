#!/usr/bin/env python3
"""Carrousel « Vie d'hôte » : été 2026, record de fréquentation depuis quinze ans, porté entièrement par les voyageurs résidant en France (Insee Focus n° 387)."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from carrousel_lib import *

PROJ = work_dir("ete-2026-insee", "project")
N = 9
SRC_INSEE = "Source : Insee Focus n° 387, « Saison touristique d'été 2026 », 29 sept. 2026 (mai à août, données provisoires)"
SRC_T3 = "Source : Insee, Informations rapides n° 275, 19 nov. 2026 (juillet à septembre 2026)"
SRC_EURO = "Sources : Insee Focus n° 387 (29 sept. 2026) · Eurostat via Rental Scale-Up, 9 oct. 2026 (nuitées plateformes 2025)"
slides = {}

slides["Main.dc.html"] = page("Couverture", category_pill("Vie d'hôte", "vie"),
    f"""
    {title_boxes([("Été 2026 :", "white", 96), ("un record", "mint", 104), ("sans les étrangers", "white", 66)])}
    <div>{para("260,5 millions de nuitées dans les hôtels, campings et résidences de mai à août, le plus haut niveau depuis quinze ans. Et toute la hausse vient des voyageurs qui vivent en France. Ce que ça dit pour votre maison.", 36, BODY, maxw=860)}
      <div style="width: 260px; height: 10px; border-radius: 5px; background: {ACCENT}; margin-top: 18px"></div></div>
    """,
    "La vie des gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {INK}; font-weight: 900">Glisser {icon("arrow")}</span>',
    body_gap=44, cover=True)

slides["S1.dc.html"] = page("Le chiffre", f"2 / {N}",
    f"""
    {title_plain(["Le chiffre", "de l'été"])}
    {stat("260,5&nbsp;M", "de nuitées dans les hébergements collectifs de tourisme en France, de mai à août 2026", 110)}
    {para("C'est 2,8 millions de plus que l'été 2025 (+1,1 %), et le plus haut niveau depuis quinze ans, malgré une saison marquée par les épisodes caniculaires et les incendies de juillet.", 31)}
    <div style="display: flex; flex-direction: column; gap: 12px">
      {card("92,0 millions de nuitées, +1,7&nbsp;%", "Hôtels :")}
      {card("126,5 millions, +1,1&nbsp;%", "Campings :")}
      {card("42,0 millions, −0,4&nbsp;%", "Résidences de tourisme, villages de vacances :")}
    </div>
    """,
    SRC_INSEE, body_gap=30)

slides["S2.dc.html"] = page("Qui a fait la hausse", f"3 / {N}",
    f"""
    {title_plain(["Qui a fait", "la hausse ?"])}
    {stat("100&nbsp;%", "de la hausse vient des résidents : les voyageurs dont le domicile est en France", 120)}
    {para("Leurs nuitées progressent de 1,6 % et représentent plus de deux nuitées estivales sur trois. Celles des non-résidents stagnent sur la saison, et reculent même en août. L'Insee l'écrit : « la clientèle non résidente ne contribue globalement pas à la hausse de la fréquentation touristique estivale en 2026 ».", 30)}
    {card("l'Insee compte les résidents par domicile, pas par nationalité. Un Allemand qui vit à Lyon est un résident ; un Français de Londres ne l'est pas.", "Précision :", light=True)}
    """,
    SRC_INSEE, body_gap=28)

slides["S3.dc.html"] = page("Pays par pays", f"4 / {N}",
    f"""
    {title_plain(["Les voisins viennent,", "les lointains hésitent"], 68)}
    {para("Nuitées des clientèles étrangères dans les hôtels, été 2026 par rapport à l'été 2025 :", 30)}
    <div style="display: flex; flex-direction: column; gap: 12px">
      {card("Allemagne +3,9&nbsp;%, Belgique +3,1&nbsp;%, Pays-Bas +3,0&nbsp;%, Royaume-Uni +1,2&nbsp;%", "En hausse :")}
      {card("Chine −9,0&nbsp;%, Japon −10,8&nbsp;%, Espagne −8,5&nbsp;%, Italie −3,0&nbsp;%", "En baisse :", light=True)}
    </div>
    {para("Les Américains, première clientèle étrangère des hôtels avec 5,4 millions de nuitées, ne progressent plus que de 0,8 %. Dans les campings, les Néerlandais, de loin les plus nombreux, reculent de 3,1 %.", 29)}
    """,
    SRC_INSEE, body_gap=26)

slides["S4.dc.html"] = page("Où ça a marché", f"5 / {N}",
    f"""
    {title_plain(["Le nord et l'ouest", "gagnent, le sud perd"], 70)}
    {numbered([
        ("Manche Est – Mer du Nord : +5,6 %.", "Nord Atlantique – Manche Ouest : +5,0 %. Les côtes fraîches ont été les grandes gagnantes de l'été."),
        ("Les communes rurales : +3,2 %,", "soit 3,7 millions de nuitées de plus. La montagne progresse de 1,3 %."),
        ("Le littoral Sud Atlantique : −2,3 %,", "pénalisé par les incendies de juillet, mais la baisse était déjà sensible en juin. Les zones urbaines denses : −3,9 %, probablement à cause des canicules."),
    ])}
    """,
    SRC_INSEE, body_gap=34)

slides["S5.dc.html"] = page("Et vous dans tout ça", f"6 / {N}",
    f"""
    {title_plain(["Et les gîtes", "dans tout ça ?"])}
    {para("L'Insee ne compte ici que les hôtels, les campings et les hébergements collectifs. Les meublés, les chambres d'hôtes et « la fréquentation réalisée par les plateformes de réservation entre particuliers » ne sont pas mesurés dans cette enquête.", 31)}
    <div style="display: flex; flex-direction: column; gap: 14px">
      {card("Eurostat, qui compte les nuitées réservées via Airbnb, Booking et Expedia, donnait déjà 60 % de nuitées françaises réservées par des résidents en 2025, contre 38 % dans l'UE.", "Même direction côté plateformes :", light=True)}
      {card("les données de juillet et août 2026 sont provisoires ; le bilan du troisième trimestre, publié le 19 novembre, confirme la tendance : +1,8 % pour les résidents, −0,4 % pour les non-résidents.", "À lire avec prudence :")}
    </div>
    """,
    SRC_EURO, body_gap=28)

slides["S6.dc.html"] = page("Ce que ça change", f"7 / {N}",
    f"""
    {title_plain(["Ce que ça change", "pour votre maison"])}
    {numbered([
        ("Votre client est à trois heures de route.", "Il vit en France, cherche en français, revient quand il a aimé. Pages, photos, réponses : tout doit lui parler d'abord."),
        ("La clientèle étrangère n'est pas un relais garanti.", "Les voisins européens viennent toujours ; les lointains, moins. Un gîte qui ne vise que l'export se fragilise."),
        ("La fraîcheur devient un argument.", "Volets, ventilateurs, pièces traversantes, ombre, rivière à côté : ce que vous avez, dites-le dans l'annonce."),
    ])}
    """,
    SRC_INSEE, body_gap=34)

slides["S7.dc.html"] = page("Trois actions", f"8 / {N}",
    f"""
    {title_plain(["Trois actions", "avant le printemps"])}
    {numbered([
        ("Réécrivez à vos voyageurs de cet été.", "Ils habitent en France, ils vous connaissent, ils peuvent revenir en direct, sans commission, pour un week-end de printemps."),
        ("Parlez aux régions voisines.", "Les deux tiers des nuitées sont résidentes : dans votre description, citez les villes à deux ou trois heures de chez vous, et ce qu'on y gagne à venir."),
        ("Préparez l'été chaud.", "Si l'été 2027 ressemble à 2026, une maison fraîche, loin des villes denses, aura un avantage. Vérifiez vos équipements maintenant."),
    ])}
    """,
    SRC_INSEE, body_gap=34)

slides["S8.dc.html"] = page("À retenir", f"9 / {N}",
    f"""
    {title_plain(["À retenir"])}
    {numbered([
        ("260,5 millions de nuitées", "dans les hébergements collectifs de mai à août 2026 : +1,1 %, le plus haut niveau depuis quinze ans."),
        ("Toute la hausse vient des résidents", "(+1,6 %) ; les non-résidents stagnent, et reculent en août."),
        ("Le nord, l'ouest, le rural et la montagne progressent ;", "le Sud Atlantique et les villes denses reculent."),
    ])}
    {para("Sources : Insee Focus n° 387, « Saison touristique d'été 2026 », Gilles Valaison, 29 sept. 2026 (hôtels, campings et autres hébergements collectifs de tourisme ; données de juillet et août provisoires) · Insee, Informations rapides n° 275, 19 nov. 2026 (troisième trimestre) · Eurostat via Rental Scale-Up, 9 oct. 2026.", 21, MUTED)}
    """,
    "Chaque semaine, ce qui change pour les gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {VIOLET}; font-weight: 900">Suivez-nous {icon("arrow")}</span>',
    body_gap=30)

order = list(slides.keys())
titles = ["1 · Couverture", "2 · Le chiffre", "3 · Qui a fait la hausse", "4 · Pays par pays", "5 · Où ça a marché", "6 · Et les gîtes", "7 · Ce que ça change", "8 · Trois actions", "9 · À retenir"]
write_all(slides, PROJ)
json.dump(canvas_json("Carrousel été 2026 Insee", order, titles), open(PROJ + "/canvas.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
render_all(PROJ, order, work_dir("ete-2026-insee", "png"))
print("ok", len(order))
