#!/usr/bin/env python3
"""Carrousel « Vie d'hôte » : le petit-déjeuner qui fait parler (chambres d'hôtes)."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from carrousel_lib import *

PROJ = work_dir("petit-dejeuner", "project")
N = 8
SRC_CT = "Source : Code du tourisme, art. D. 324-13"
SRC_AL = "Sources : règlement (UE) 1169/2011 (INCO) · décret 2015-447 du 17 avril 2015"
slides = {}

slides["Main.dc.html"] = page("Couverture", category_pill("Vie d'hôte", "vie"),
    f"""
    {title_boxes([("Chambres d'hôtes :", "white", 70), ("le petit-déjeuner", "mint", 74), ("qui fait parler", "white", 86)])}
    <div>{para("C'est la moitié de ce que le voyageur achète, et souvent la moitié de l'avis qu'il laisse. Produits locaux, mise en scène, allergies, coût réel : ce qui se joue sur la table du matin.", 36, BODY, maxw=860)}
      <div style="width: 260px; height: 10px; border-radius: 5px; background: {ACCENT}; margin-top: 18px"></div></div>
    """,
    "L'actu des gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {INK}; font-weight: 900">Glisser {icon("arrow")}</span>',
    body_gap=44, cover=True)

slides["S1.dc.html"] = page("Pas une option", f"2 / {N}",
    f"""
    {title_plain(["Ce n'est pas", "une option"])}
    {para("En chambre d'hôtes, la nuitée et le petit-déjeuner sont vendus ensemble : c'est la définition légale. Cinq chambres au plus, quinze personnes au plus, et l'accueil assuré par l'habitant.", 34)}
    <div style="display: flex; flex-direction: column; gap: 14px">
      {card("le petit-déjeuner n'est pas un extra à facturer. Il est compris dans le prix de la chambre.", "Conséquence n° 1 :")}
      {card("c'est le seul moment où tous vos voyageurs vous voient travailler. C'est là que se fabrique l'avis.", "Conséquence n° 2 :", light=True)}
    </div>
    """,
    SRC_CT, body_gap=32)

slides["S2.dc.html"] = page("Local d'abord", f"3 / {N}",
    f"""
    {title_plain(["Local d'abord,", "maison si possible"])}
    {para("Le pain du boulanger du village, la confiture de la voisine, les œufs de la ferme, le miel du coin : chaque produit raconte où l'on est. C'est ce que le voyageur ne trouve pas à l'hôtel.", 32)}
    {numbered([
        ("Nommez les producteurs", "sur une petite carte posée sur la table. Les voyageurs photographient la carte."),
        ("Une seule chose faite maison suffit,", "si elle est bonne : un gâteau, une brioche, une compote."),
        ("Évitez les portions individuelles sous plastique :", "c'est exactement ce que le voyageur fuit en choisissant une chambre d'hôtes."),
    ])}
    """,
    "Vie d'hôte · chambres d'hôtes", body_gap=30)

slides["S3.dc.html"] = page("La mise en scène", f"4 / {N}",
    f"""
    {title_plain(["La table se photographie.", "Dressez-la pour ça."], 70)}
    {numbered([
        ("La lumière :", "près d'une fenêtre, dehors dès que la saison le permet. Une table dressée avant que les voyageurs descendent."),
        ("Le service :", "à table quand vous avez deux ou trois chambres, le buffet rassure quand il y en a cinq. De la vaisselle qui va ensemble, des fleurs du jardin."),
        ("L'heure :", "une plage claire, annoncée la veille, et de la souplesse pour les départs tôt. Un plateau préparé vaut mieux qu'un voyageur parti à jeun."),
    ])}
    {para("Un petit-déjeuner qui finit sur Instagram, avec le nom de votre maison, vaut toutes les publicités.", 28, MUTED)}
    """,
    "Vie d'hôte · chambres d'hôtes", body_gap=32)

slides["S4.dc.html"] = page("Allergies et régimes", f"5 / {N}",
    f"""
    {title_plain(["Allergies et régimes :", "une question, la veille"], 70)}
    {numbered([
        ("Demandez à la réservation ou la veille :", "allergies, intolérances, végétarien, sans gluten, sans lactose. Une question, et vous évitez l'assiette qui reste pleine."),
        ("Sachez dire ce qu'il y a dedans :", "pour les aliments non préemballés, l'information écrite sur les 14 allergènes est la règle (gluten, lait, œufs, fruits à coque, arachide, soja, sésame, moutarde, céleri, sulfites, lupin, poisson, crustacés, mollusques)."),
        ("Prévoyez une alternative simple :", "du pain sans gluten au congélateur, un lait végétal, des fruits frais. Ça ne coûte presque rien et ça se raconte."),
    ])}
    """,
    SRC_AL, body_gap=36)

slides["S5.dc.html"] = page("Le coût réel", f"6 / {N}",
    f"""
    {title_plain(["Le coût réel :", "faites le calcul une fois"], 70)}
    {numbered([
        ("Comptez tout :", "les produits, mais aussi votre temps (préparation, service, vaisselle), l'énergie, le linge de table, la casse."),
        ("Tenez un carnet pendant une semaine :", "le coût d'un petit-déjeuner par personne surprend presque toujours."),
        ("Le gaspillage est le premier poste :", "un buffet pour deux personnes en jette la moitié. Servez à l'assiette et proposez de resservir."),
        ("Répercutez-le dans le prix de la chambre,", "jamais en supplément : il est compris par définition."),
    ])}
    """,
    "Vous avez votre chiffre ? Dites-le en commentaire", body_gap=36)

slides["S6.dc.html"] = page("Ce qui fait parler", f"7 / {N}",
    f"""
    {title_plain(["Ce qui fait parler,", "en bien et en mal"], 72)}
    <div style="display: flex; flex-direction: column; gap: 12px">
      {item("Un produit qu'on ne trouve nulle part ailleurs", "yes")}
      {item("L'hôte qui s'assied cinq minutes à la table", "yes")}
      {item("Une attention pour les enfants", "yes")}
      {item("Le café en dosette, tiède", "no")}
      {item("La confiture industrielle en mini-pots", "no")}
      {item("L'hôte invisible et la table en libre-service", "no")}
    </div>
    """,
    "Vie d'hôte · chambres d'hôtes", body_gap=30)

slides["S7.dc.html"] = page("À retenir", f"8 / {N}",
    f"""
    {title_plain(["Le test", "de cette semaine"])}
    {numbered([
        ("Mangez le petit-déjeuner que vous servez,", "à l'heure où vous le servez, assis à la place du voyageur."),
        ("Remplacez un produit industriel", "par un produit du coin, et écrivez d'où il vient."),
        ("Ajoutez la question « allergies ou régime ? »", "à votre message de la veille de l'arrivée."),
    ])}
    {para("Sources : Code du tourisme, art. D. 324-13 (définition de la chambre d'hôtes) · règlement (UE) 1169/2011 et décret 2015-447 (information sur les allergènes).", 22, MUTED)}
    """,
    "Chaque semaine, ce qui change pour les gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {VIOLET}; font-weight: 900">Suivez-nous {icon("arrow")}</span>',
    body_gap=30)

order = list(slides.keys())
titles = ["1 · Couverture", "2 · Pas une option", "3 · Local", "4 · Mise en scène", "5 · Allergies", "6 · Coût réel", "7 · Ce qui fait parler", "8 · À retenir"]
write_all(slides, PROJ)
json.dump(canvas_json("Carrousel petit-déjeuner", order, titles), open(PROJ + "/canvas.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
render_all(PROJ, order, work_dir("petit-dejeuner", "png"))
print("ok", len(order))
