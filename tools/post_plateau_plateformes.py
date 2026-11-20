#!/usr/bin/env python3
"""Carrousel « Actu » : la croissance des plateformes ralentit de moitié (Eurostat, premier semestre 2026), le direct redevient stratégique."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from carrousel_lib import *

PROJ = work_dir("plateau-plateformes", "project")
N = 9
SRC_RSU = "Source : Rental Scale-Up, 9 oct. 2026, d'après Eurostat (Airbnb, Booking.com, Expedia)"
SRC_EURO = "Sources : Eurostat, communiqués du 2 juil. 2026 (T1) et du 2 oct. 2026 (T2) · Rental Scale-Up, 9 oct. 2026"
SRC_COM = "Sources : Rental Scale-Up, 9 oct. 2026 · Toutsurmesfinances, 28 oct. 2026 (commissions)"
slides = {}

slides["Main.dc.html"] = page("Couverture", category_pill("Actu", "actu"),
    f"""
    {title_boxes([("Plateformes :", "white", 72), ("la croissance", "mint", 86), ("ralentit de moitié", "white", 64)])}
    <div>{para("Airbnb, Booking et Expedia : +6,9 % de nuitées en Europe au premier semestre 2026, contre +13,4 % un an plus tôt. La France reste le premier marché. Ce que ce coup de frein change pour votre maison.", 36, BODY, maxw=860)}
      <div style="width: 260px; height: 10px; border-radius: 5px; background: {ACCENT}; margin-top: 18px"></div></div>
    """,
    "L'actu des gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {INK}; font-weight: 900">Glisser {icon("arrow")}</span>',
    body_gap=44, cover=True)

slides["S1.dc.html"] = page("Le chiffre", f"2 / {N}",
    f"""
    {title_plain(["Le chiffre", "de l'automne"])}
    {stat("+6,9&nbsp;%", "de nuitées réservées via Airbnb, Booking.com et Expedia dans l'Union européenne, de janvier à juin 2026", 120)}
    {para("Sur les mêmes mois de 2025, la hausse était de 13,4 %. Le marché continue de grandir, mais deux fois moins vite. Eurostat publie ces données à partir des chiffres transmis par les trois plateformes elles-mêmes.", 31)}
    {card("ont progressé de 10 % ou plus au premier semestre, contre 11 un an plus tôt.", "Seuls 3 des 13 plus grands marchés européens", light=True)}
    """,
    SRC_RSU, body_gap=32)

slides["S2.dc.html"] = page("Trimestre par trimestre", f"3 / {N}",
    f"""
    {title_plain(["Un ralentissement", "qui s'accentue"])}
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px">
      <div style="background: #FFFFFF; border: 2px solid {LINE}; border-radius: 18px; padding: 28px; display: flex; flex-direction: column; gap: 10px">
        <div style="font-size: 92px; line-height: 0.9; font-weight: 900; letter-spacing: -0.04em; color: {VIOLET}">+9,7 %</div>
        <div style="font-size: 27px; line-height: 1.3; color: {BODY}"><b>Janvier à mars 2026 :</b> 144,3 millions de nuitées dans l'UE.</div>
      </div>
      <div style="background: {VIOLET}; color: #FFFFFF; border-radius: 18px; padding: 28px; display: flex; flex-direction: column; gap: 10px">
        <div style="font-size: 92px; line-height: 0.9; font-weight: 900; letter-spacing: -0.04em; color: {ACCENT}">+5,3 %</div>
        <div style="font-size: 27px; line-height: 1.3"><b>Avril à juin 2026 :</b> 258,8 millions de nuitées, soit 13,1 millions de plus qu'au printemps 2025.</div>
      </div>
    </div>
    {para("Mois par mois, la courbe est en dents de scie : +11,4 % en mars, +1,4 % en avril, +14,2 % en mai, +1,2 % en juin. Le printemps 2026 n'a pas tenu le rythme de 2025.", 30)}
    """,
    SRC_EURO, body_gap=30)

slides["S3.dc.html"] = page("La France première", f"4 / {N}",
    f"""
    {title_plain(["La France,", "premier marché d'Europe"], 72)}
    {stat("213 M", "de nuitées réservées en France via les trois plateformes en 2025, devant l'Espagne (189 M) et l'Italie (139 M)", 140)}
    {para("Au premier semestre 2026, la France a progressé de 6,9 %, exactement la moyenne européenne, après +13,3 % un an plus tôt. Six régions françaises figurent dans les vingt plus demandées d'Europe : Provence-Alpes-Côte d'Azur, Île-de-France, Rhône-Alpes, Languedoc-Roussillon, Aquitaine et Bretagne.", 30)}
    """,
    SRC_RSU, body_gap=34)

slides["S4.dc.html"] = page("Qui dort chez vous", f"5 / {N}",
    f"""
    {title_plain(["Qui dort", "chez vous ?"])}
    {stat("60 %", "des nuitées plateformes en France sont réservées par des personnes qui résident en France, contre 38 % en moyenne dans l'UE", 150)}
    {para("Un voyageur français est un voyageur que vous pouvez atteindre sans plateforme : il cherche en français, il revient, il recommande votre maison à ses proches.", 31)}
    {card("tombent en juillet et août. Les deux tiers de l'année se jouent hors de l'été.", "35 % des nuitées françaises seulement", light=True)}
    """,
    SRC_RSU, body_gap=30)

slides["S5.dc.html"] = page("Ce que ça change", f"6 / {N}",
    f"""
    {title_plain(["Ce que ce coup de frein", "change pour vous"], 70)}
    {numbered([
        ("La vague porteuse faiblit.", "Quand le marché croît de 13 % par an, presque toutes les annonces se remplissent. À 7 %, elles se disputent les mêmes voyageurs : les notes, les photos et le prix pèsent davantage."),
        ("Les plateformes cherchent leur marge ailleurs.", "Airbnb fait payer 15,5 % à l'hôte depuis le 13 octobre, Abritel est passé à 12 % le 29 octobre. Moins de croissance en volume, plus de commission par nuit."),
        ("Le direct n'est plus un bonus.", "C'est le seul canal dont la croissance ne dépend que de vous : votre site, vos anciens voyageurs, votre territoire."),
    ])}
    """,
    SRC_COM, body_gap=32)

slides["S6.dc.html"] = page("Ce qu'on ne sait pas", f"7 / {N}",
    f"""
    {title_plain(["Plateau, ou", "simple pause ?"])}
    {para("Personne ne sait encore pourquoi la croissance ralentit. Rental Scale-Up évoque des budgets plus serrés, le prix des carburants et une offre de logements en baisse dans certaines villes, sans trancher.", 31)}
    <div style="display: flex; flex-direction: column; gap: 14px">
      {card("951,6 millions de nuitées dans l'UE, +11,4 % en un an. Le ralentissement part de très haut.", "2025 reste une année record :")}
      {card("Eurostat compte des nuitées, pas des réservations ni des logements, et qualifie ces statistiques d'expérimentales.", "À lire avec prudence :", light=True)}
    </div>
    """,
    "Sources : Eurostat, communiqué du 1er avr. 2026 (année 2025) · Rental Scale-Up, 9 oct. 2026", body_gap=30)

slides["S7.dc.html"] = page("Trois décisions", f"8 / {N}",
    f"""
    {title_plain(["Trois décisions", "à prendre cet hiver"])}
    {numbered([
        ("Mesurez votre part de direct.", "Le pourcentage de nuits réservées sans plateforme est le chiffre à suivre chaque mois. Notre simulateur gratuit vous dit ce que la différence vous coûte, lien en bio."),
        ("Écrivez à vos voyageurs français.", "Six nuitées sur dix sont réservées par des résidents : ceux de cet été vous connaissent déjà et peuvent revenir en direct, sans commission."),
        ("Travaillez l'hors-saison.", "Deux tiers des nuitées se font hors de juillet-août. Une maison ouverte, visible et bien tarifée en janvier capte une demande qui existe."),
    ])}
    """,
    SRC_RSU, body_gap=32)

slides["S8.dc.html"] = page("À retenir", f"9 / {N}",
    f"""
    {title_plain(["À retenir"])}
    {numbered([
        ("+6,9 % au premier semestre 2026", "contre +13,4 % en 2025 : la croissance des plateformes a été divisée par deux en Europe."),
        ("La France reste n° 1 :", "213 millions de nuitées en 2025, 60 % réservées par des résidents français."),
        ("Le direct devient stratégique :", "moins de croissance pour tous, plus de commission par nuit, et un canal que vous contrôlez."),
    ])}
    {para("Sources : Rental Scale-Up, « Europe's short-term rental growth halved in 2026 », 9 oct. 2026, d'après Eurostat · Eurostat, communiqués du 1er avr., du 2 juil. et du 2 oct. 2026 (nuitées réservées via Airbnb, Booking.com et Expedia, statistiques expérimentales) · Toutsurmesfinances, 28 oct. 2026 (commissions).", 21, MUTED)}
    """,
    "Chaque semaine, ce qui change pour les gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {VIOLET}; font-weight: 900">Suivez-nous {icon("arrow")}</span>',
    body_gap=30)

order = list(slides.keys())
titles = ["1 · Couverture", "2 · Le chiffre", "3 · Trimestre par trimestre", "4 · La France première", "5 · Qui dort chez vous", "6 · Ce que ça change", "7 · Plateau ou pause", "8 · Trois décisions", "9 · À retenir"]
write_all(slides, PROJ)
json.dump(canvas_json("Carrousel plateau des plateformes", order, titles), open(PROJ + "/canvas.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
render_all(PROJ, order, work_dir("plateau-plateformes", "png"))
print("ok", len(order))
