#!/usr/bin/env python3
"""Carrousel « Conseil » : les 5 détails qui font une note 5 étoiles."""
import sys, json
sys.path.insert(0, "/tmp/claude-0/-home-claude/fc645d01-7205-5ab5-8091-97d967632241/scratchpad")
from carrousel_lib import *

S = "/tmp/claude-0/-home-claude/fc645d01-7205-5ab5-8091-97d967632241/scratchpad"
PROJ = S + "/carrousel-5etoiles/project"
N = 8
slides = {}
F = "Conseil · gîtes et chambres d'hôtes"

slides["Main.dc.html"] = page("Couverture", category_pill("Conseil", "conseil"),
    f"""
    {title_boxes([("Les 5 détails", "white", 96), ("qui font", "mint", 104), ("une note 5 étoiles", "white", 76)])}
    <div>{para("Et les 3 qui vous en coûtent une à coup sûr. Check-list à faire avant la prochaine arrivée.", 38, BODY, maxw=860)}
      <div style="width: 260px; height: 10px; border-radius: 5px; background: {ACCENT}; margin-top: 18px"></div></div>
    """,
    "L'actu des gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {INK}; font-weight: 900">Glisser {icon("arrow")}</span>',
    body_gap=44, cover=True)

slides["S1.dc.html"] = page("Pourquoi ça compte", f"2 / {N}",
    f"""
    {title_plain(["La note se joue", "sur des détails"])}
    {para("Un voyageur ne note pas votre maison : il note l'écart entre ce qu'il attendait et ce qu'il a trouvé. Les cinq points qui suivent sont ceux qui reviennent le plus souvent dans les avis, en bien comme en mal.", 34)}
    {stat("52 %", "des voyageurs français regardent d'abord les avis et les notes avant de réserver (OnePoll pour Booking, nov. 2025)", 130)}
    """,
    "Source : OnePoll pour Booking.com, 2 000 Français, nov. 2025")

slides["S2.dc.html"] = page("1 · La literie", f"3 / {N}",
    f"""
    {title_plain(["1. Une literie", "irréprochable"])}
    {numbered([
        ("Matelas de moins de 8 ans,", "ferme et sans creux : un matelas fatigué se lit dans l'avis dès la première nuit."),
        ("Draps en coton, repassés ou au moins lisses,", "et un deuxième oreiller par personne."),
        ("Couette adaptée à la saison :", "une couette d'hiver en août ou un plaid en janvier, c'est une étoile en moins."),
    ])}
    {para("49 % des voyageurs citent le confort du lit comme attente n° 1 dans la chambre.", 28, MUTED)}
    """,
    "Source : OnePoll pour Booking.com, nov. 2025")

slides["S3.dc.html"] = page("2 · La propreté", f"4 / {N}",
    f"""
    {title_plain(["2. Propre, et", "visiblement propre"])}
    {numbered([
        ("Les 4 endroits que tout le monde vérifie :", "joints de douche, intérieur du micro-ondes, dessous des toilettes, filtre de la hotte."),
        ("Zéro odeur :", "ni humidité ni parfum d'ambiance trop fort. Aérer 20 minutes avant l'arrivée vaut mieux qu'un diffuseur."),
        ("Une cuisine rangée :", "47 % des voyageurs sont rebutés par du désordre dans la cuisine, avant même la propreté."),
    ])}
    """,
    "Source : OnePoll pour Booking.com, nov. 2025")

slides["S4.dc.html"] = page("3 · Le Wi-Fi", f"5 / {N}",
    f"""
    {title_plain(["3. Un Wi-Fi", "qui marche partout"])}
    {numbered([
        ("Testez-le dans chaque pièce", "avec votre téléphone, pas seulement à côté de la box."),
        ("Affichez le mot de passe", "à l'entrée et dans le livret d'accueil, avec un QR code si possible."),
        ("Annoncez le débit réel :", "« fibre, 300 Mb/s » ou « ADSL, suffisant pour les mails ». Un télétravailleur déçu laisse un avis à 2 étoiles."),
    ])}
    {para("Les équipements essentiels (Wi-Fi, TV) pèsent pour 51 % des voyageurs dans le choix d'un logement.", 28, MUTED)}
    """,
    "Source : OnePoll pour Booking.com, nov. 2025")

slides["S5.dc.html"] = page("4 · L'arrivée", f"6 / {N}",
    f"""
    {title_plain(["4. Une arrivée", "sans friction"])}
    {numbered([
        ("Les infos d'accès la veille,", "pas le matin même : adresse exacte, parking, code, où sont les clés."),
        ("Lumière allumée et chauffage réglé", "quand le voyageur arrive de nuit ou en hiver. C'est le détail qui marque."),
        ("Un message dans l'heure qui suit l'arrivée :", "« Tout va bien ? ». Ça règle la plupart des petits soucis avant qu'ils finissent dans l'avis."),
    ])}
    """,
    "Astuce : un livret d'accueil numérique évite la plupart des questions")

slides["S6.dc.html"] = page("5 · L'attention", f"7 / {N}",
    f"""
    {title_plain(["5. Une attention", "qui ne coûte rien"])}
    {numbered([
        ("Un produit local sur la table :", "une bouteille, un pot de miel, des biscuits. Le prix importe peu, le geste oui."),
        ("Un mot manuscrit", "avec le prénom du voyageur et deux adresses du coin que vous aimez vraiment."),
        ("Le petit rangement impeccable :", "51 % des voyageurs attendent un rangement irréprochable dans la chambre. Des cintres vides, ça compte."),
    ])}
    """,
    "Source : OnePoll pour Booking.com, nov. 2025")

slides["S7.dc.html"] = page("Les 3 qui coûtent une étoile", f"8 / {N}",
    f"""
    {title_plain(["Et les 3 qui vous", "coûtent une étoile"])}
    <div style="display: flex; flex-direction: column; gap: 14px">
      {item("Une douche qui coule mal ou tiède", "no")}
      {item("Un ménage de départ exigé (et depuis le 20 nov., interdit sur Airbnb)", "no")}
      {item("Des photos plus belles que la réalité : 27 % refusent un logement peu photogénique, mais tous sanctionnent la déception", "no")}
    </div>
    {para("À faire avant la prochaine arrivée : passez cette liste en revue, et demandez à un proche de dormir une nuit chez vous en jouant le voyageur.", 28, MUTED)}
    """,
    "Chaque semaine, ce qui change pour les gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {VIOLET}; font-weight: 900">Suivez-nous {icon("arrow")}</span>',
    body_gap=30)

order = list(slides.keys())
titles = ["1 · Couverture", "2 · Pourquoi", "3 · Literie", "4 · Propreté", "5 · Wi-Fi", "6 · Arrivée", "7 · Attention", "8 · À éviter"]
write_all(slides, PROJ)
json.dump(canvas_json("Carrousel 5 étoiles", order, titles), open(PROJ + "/canvas.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
render_all(PROJ, order, S + "/png-5etoiles")
print("ok", len(order))
