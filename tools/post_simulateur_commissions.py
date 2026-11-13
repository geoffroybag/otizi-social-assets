#!/usr/bin/env python3
"""Carrousel « Actu » : combien vous coûtent vraiment les plateformes ? (commissions 2026 et simulateur)."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from carrousel_lib import *

PROJ = work_dir("simulateur-commissions", "project")
N = 9
SRC_AIR = "Sources : Toutsurmesfinances (28 oct. 2026) · Rental Scale-Up (16 oct. 2026) · Smoobu, guide des commissions"
SRC_TVA = "Sources : Rental Scale-Up (8 juil. 2026) · Mediaterranee (28 oct. 2026)"
SRC_SIM = "Calcul : simulateur de commissions otizi.fr/outils, taux ci-dessus, TVA 20 %"
SRC_FISC = "Sources : Toutsurmesfinances (28 oct. 2026) · service-public.gouv.fr (micro-BIC 2026)"
slides = {}

slides["Main.dc.html"] = page("Couverture", category_pill("Actu", "actu"),
    f"""
    {title_boxes([("Combien vous coûtent", "white", 62), ("vraiment", "mint", 104), ("les plateformes ?", "white", 70)])}
    <div>{para("Airbnb, Booking, Abritel : les commissions ont changé cet automne. Un exemple chiffré sur une année, ce que la TVA ajoute, et un outil gratuit pour faire votre propre calcul.", 36, BODY, maxw=860)}
      <div style="width: 260px; height: 10px; border-radius: 5px; background: {ACCENT}; margin-top: 18px"></div></div>
    """,
    "L'actu des gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {INK}; font-weight: 900">Glisser {icon("arrow")}</span>',
    body_gap=44, cover=True)

slides["S1.dc.html"] = page("Ce qui a changé", f"2 / {N}",
    f"""
    {title_plain(["Ce qui a changé", "cet automne"])}
    {numbered([
        ("Airbnb : 15,5 % payés par l'hôte", "depuis le 13 octobre 2026 en Europe. Avant, l'hôte payait environ 3 % et le voyageur le reste. Le voyageur ne paie plus de frais : c'est vous qui payez tout."),
        ("Abritel : 12 % depuis le 29 octobre 2026", "dans les nouvelles conditions de la formule à la commission, contre 8 % auparavant (5 % de commission et 3 % de frais de paiement)."),
        ("Booking.com : 15 % en moyenne,", "selon votre contrat, votre région et les programmes de visibilité auxquels vous participez. Inchangé."),
    ])}
    """,
    SRC_AIR, body_gap=34)

slides["S2.dc.html"] = page("La TVA", f"3 / {N}",
    f"""
    {title_plain(["Le chiffre que l'on", "oublie : la TVA"], 72)}
    {stat("18,6 %", "du prix payé par le voyageur partent chez Airbnb, TVA comprise, pour un hôte non assujetti : 15,5 % × 1,2", 120)}
    {para("Les plateformes facturent leur commission avec 20 % de TVA. Si vous n'êtes pas assujetti à la TVA (c'est le cas de la plupart des gîtes et chambres d'hôtes en micro-entreprise), vous ne la récupérez pas. Elle s'ajoute au taux affiché.", 31)}
    {card("12 % d'Abritel deviennent 14,4 %, 15 % de Booking deviennent 18 %.", "Même logique partout :", light=True)}
    """,
    SRC_TVA, body_gap=30)

slides["S3.dc.html"] = page("Un exemple", f"4 / {N}",
    f"""
    {title_plain(["Un exemple :", "30 000 € de recettes"], 72)}
    {para("Un gîte qui encaisse 30 000 € par an, avec la répartition par défaut du simulateur : 50 % par Airbnb, 25 % par Booking, 10 % par Abritel, 15 % en direct.", 30)}
    {stat("4&nbsp;428&nbsp;€", "de commissions par an, TVA comprise, soit 369 € par mois et près de 15 % de vos recettes", 110)}
    {para("Taux retenus : Airbnb 15,5 %, Booking 15 %, Abritel 8 % (ancienne formule, encore dans le simulateur), TVA 20 %.", 25, MUTED)}
    """,
    SRC_SIM, body_gap=30)

slides["S4.dc.html"] = page("Sur cinq ans", f"5 / {N}",
    f"""
    {title_plain(["Sur cinq ans,", "à activité constante"], 74)}
    {stat("22&nbsp;140&nbsp;€", "sur cinq ans, pour le même gîte, sans compter les hausses de taux à venir", 110)}
    {para("Ce n'est pas un coût caché : c'est le prix de la visibilité et des réservations que les plateformes vous apportent. La question n'est pas de les quitter, mais de savoir ce que vous payez, et quelle part de vos séjours pourrait venir en direct.", 31)}
    """,
    SRC_SIM, body_gap=36)

slides["S5.dc.html"] = page("Ce que le direct change", f"6 / {N}",
    f"""
    {title_plain(["Ce que change", "le passage au direct"], 72)}
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px">
      <div style="background: #FFFFFF; border: 2px solid {LINE}; border-radius: 18px; padding: 28px; display: flex; flex-direction: column; gap: 10px">
        <div style="font-size: 100px; line-height: 0.9; font-weight: 900; letter-spacing: -0.04em; color: {VIOLET}">15 %</div>
        <div style="font-size: 27px; line-height: 1.3; color: {BODY}">de réservations en direct aujourd'hui, dans l'exemple : 4 428 € de commissions.</div>
      </div>
      <div style="background: {VIOLET}; color: #FFFFFF; border-radius: 18px; padding: 28px; display: flex; flex-direction: column; gap: 10px">
        <div style="font-size: 100px; line-height: 0.9; font-weight: 900; letter-spacing: -0.04em; color: {ACCENT}">40 %</div>
        <div style="font-size: 27px; line-height: 1.3">en direct demain : 1 302 € de plus chaque année, à chiffre d'affaires égal.</div>
      </div>
    </div>
    {card("un site qui prend les réservations, un moyen de paiement, et du temps pour répondre. Mais il n'est pas proportionnel à vos recettes.", "Le direct a un coût aussi :")}
    """,
    SRC_SIM, body_gap=30)

slides["S6.dc.html"] = page("Trois réflexes", f"7 / {N}",
    f"""
    {title_plain(["Trois réflexes", "à prendre maintenant"])}
    {numbered([
        ("Répercutez la commission dans vos prix plateforme :", "pour retrouver 97 € net sur une nuit affichée 100 € avant le 13 octobre, le tarif Airbnb doit passer à 115 €."),
        ("Donnez une raison de réserver en direct :", "un prix un peu plus bas, un départ tardif, un petit-déjeuner offert. L'avantage doit être visible sur votre site et dans votre message post-séjour."),
        ("Mesurez chaque mois la part de chaque canal :", "ce que vous ne mesurez pas ne bouge pas. Le chiffre à suivre, c'est le pourcentage de nuits en direct."),
    ])}
    """,
    "Source : Toutsurmesfinances, 28 oct. 2026 (calcul des 115 €)", body_gap=34)

slides["S7.dc.html"] = page("Et la fiscalité", f"8 / {N}",
    f"""
    {title_plain(["Attention à l'effet", "sur vos impôts"], 74)}
    <div style="display: flex; flex-direction: column; gap: 14px">
      {card("relever vos prix pour absorber la commission gonfle le chiffre d'affaires déclaré, sans gain réel pour vous. Et le plafond du micro-BIC d'un meublé non classé est de 15 000 € de recettes en 2026.", "En micro-entreprise (micro-BIC),")}
      {card("la commission est une charge déductible : vous êtes imposé sur ce qu'il vous reste, pas sur ce que le voyageur a payé.", "Au régime réel,", light=True)}
    </div>
    {para("Si vous êtes proche d'un seuil, c'est le moment de refaire le calcul avec votre comptable.", 28, MUTED)}
    """,
    SRC_FISC, body_gap=32)

slides["S8.dc.html"] = page("Faites votre calcul", f"9 / {N}",
    f"""
    {title_plain(["Faites le calcul", "pour votre maison"], 76)}
    {numbered([
        ("Votre chiffre d'affaires annuel,", "toutes plateformes confondues, hors taxe de séjour."),
        ("La part de chaque canal :", "Airbnb, Booking, Abritel, autres, direct."),
        ("Le résultat :", "vos commissions par an et par mois, et ce que vous gagneriez à 40 % de direct. Simulateur gratuit, 30 secondes, lien en bio."),
    ])}
    {para("Sources : Toutsurmesfinances, 28 oct. 2026 (Airbnb 15,5 % au 13 oct.) · Rental Scale-Up, 16 oct. 2026 (Abritel 12 % au 29 oct.) et 8 juil. 2026 (TVA) · Smoobu, guide des commissions (Booking 15 % en moyenne) · service-public.gouv.fr (micro-BIC). Résultats indicatifs, non contractuels.", 21, MUTED)}
    """,
    "Chaque semaine, ce qui change pour les gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {VIOLET}; font-weight: 900">Suivez-nous {icon("arrow")}</span>',
    body_gap=30)

order = list(slides.keys())
titles = ["1 · Couverture", "2 · Ce qui a changé", "3 · La TVA", "4 · Exemple 30 000 €", "5 · Sur cinq ans", "6 · Le direct", "7 · Trois réflexes", "8 · Fiscalité", "9 · Faites le calcul"]
write_all(slides, PROJ)
json.dump(canvas_json("Carrousel simulateur de commissions", order, titles), open(PROJ + "/canvas.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
render_all(PROJ, order, work_dir("simulateur-commissions", "png"))
print("ok", len(order))
