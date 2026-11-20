#!/usr/bin/env python3
"""Carrousel « Vie d'hôte » : la déco de Noël dans un gîte ou des chambres d'hôtes, jusqu'où aller ?"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from carrousel_lib import *

PROJ = work_dir("deco-noel", "project")
N = 9
SRC_SANTE = "Source : sante.fr, « Profiter du sapin de Noël en toute sécurité », 24 juil. 2025"
SRC_FEU = "Sources : sante.fr (24 juil. 2025) · Groupama, prévention du feu de sapin (conseils des pompiers)"
NOSRC = "Vie d'hôte · gîtes et chambres d'hôtes"
slides = {}

slides["Main.dc.html"] = page("Couverture", category_pill("Vie d'hôte", "vie"),
    f"""
    {title_boxes([("Déco de Noël", "white", 76), ("dans un gîte :", "mint", 84), ("jusqu'où aller ?", "white", 70)])}
    <div>{para("Un sapin ou pas, des guirlandes qui brillent toute la nuit, des voyageurs qui ne fêtent pas Noël, le temps que ça prend : ce que les hôtes font, et les règles de sécurité à ne pas oublier.", 36, BODY, maxw=860)}
      <div style="width: 260px; height: 10px; border-radius: 5px; background: {ACCENT}; margin-top: 18px"></div></div>
    """,
    "Le quotidien des gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {INK}; font-weight: 900">Glisser {icon("arrow")}</span>',
    body_gap=44, cover=True)

slides["S1.dc.html"] = page("Pourquoi décorer", f"2 / {N}",
    f"""
    {title_plain(["Pourquoi", "se donner la peine"])}
    {numbered([
        ("Parce qu'en décembre, la maison est la destination.", "On ne vient pas visiter la région, on vient se retrouver dedans. Le décor fait partie de ce que les voyageurs achètent."),
        ("Parce que ça se voit avant d'arriver.", "Une photo du salon décoré, mise en avant dans l'annonce dès novembre, dit ce que des lignes de texte ne disent pas."),
        ("Parce que c'est un message.", "Une maison préparée pour les fêtes, c'est quelqu'un qui a pensé à eux. C'est exactement ce que raconte l'avis qui suit."),
    ])}
    """,
    NOSRC, body_gap=34)

slides["S2.dc.html"] = page("Ce qui plaît, ce qui gêne", f"3 / {N}",
    f"""
    {title_plain(["Ce qui plaît,", "ce qui gêne"])}
    <div style="display: flex; flex-direction: column; gap: 12px">
      {item("Une ambiance : lumière chaude, plaid, branches, bougies à LED", "yes")}
      {item("Un sapin, même petit, dans la pièce où l'on vit", "yes")}
      {item("De la place pour leurs propres décorations et cadeaux", "yes")}
      {item("Un salon encombré où l'on n'ose plus rien toucher", "no")}
      {item("Des guirlandes qui clignotent la nuit dans la chambre", "no")}
      {item("Des objets fragiles ou précieux à hauteur d'enfant", "no")}
    </div>
    {para("Il n'existe pas d'enquête publique sur ce que les voyageurs attendent d'un gîte à Noël : cette liste vient des retours d'hôtes, pas d'une statistique.", 27, MUTED)}
    """,
    NOSRC, body_gap=28)

slides["S3.dc.html"] = page("Naturel ou artificiel", f"4 / {N}",
    f"""
    {title_plain(["Sapin naturel", "ou artificiel ?"])}
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px">
      <div style="background: #FFFFFF; border: 2px solid {LINE}; border-radius: 18px; padding: 26px; display: flex; flex-direction: column; gap: 10px">
        <div style="font-size: 36px; line-height: 1; font-weight: 900; color: {VIOLET}">Naturel</div>
        <div style="font-size: 26px; line-height: 1.3; color: {BODY}">L'odeur et la photo. Mais des aiguilles à ramasser entre deux séjours, un pied à arroser pour qu'il reste frais, et un arbre à sortir dès après les fêtes : sec, il devient très inflammable.</div>
      </div>
      <div style="background: {VIOLET}; color: #FFFFFF; border-radius: 18px; padding: 26px; display: flex; flex-direction: column; gap: 10px">
        <div style="font-size: 36px; line-height: 1; font-weight: 900; color: {ACCENT}">Artificiel</div>
        <div style="font-size: 26px; line-height: 1.3">Réutilisable chaque année, zéro aiguille. Au-delà de 60 cm, il doit être certifié NF S 54-200 ; visez la classe anti-feu M0 ou M1 et repliez ou protégez les embouts métalliques des branches.</div>
      </div>
    </div>
    {card("la neige artificielle rend l'arbre encore plus inflammable et dégrade l'air intérieur.", "Évitez le sapin floqué :", light=True)}
    """,
    SRC_SANTE, body_gap=28)

slides["S4.dc.html"] = page("La sécurité", f"5 / {N}",
    f"""
    {title_plain(["La sécurité,", "non négociable"])}
    {numbered([
        ("Le sapin loin de toute chaleur :", "poêle, cheminée, radiateur, bougies. Vérifiez la stabilité du pied, surtout avec des enfants."),
        ("Des guirlandes marquées NF ou CE, en bon état,", "à LED de préférence, et sur une minuterie : elles s'éteignent la nuit et quand la maison est vide, sans compter sur personne."),
        ("Pas de vraies bougies sur la table de Noël d'un logement que vous ne surveillez pas.", "Les bougies à LED font la même lumière sur la photo."),
        ("Le détecteur de fumée testé", "avant le premier séjour de décembre, et son emplacement indiqué dans le livret."),
    ])}
    {para("Selon les pompiers, un sapin sec peut s'embraser en quelques dizaines de secondes.", 27, MUTED)}
    """,
    SRC_FEU, body_gap=26)

slides["S5.dc.html"] = page("Ceux qui ne fêtent pas Noël", f"6 / {N}",
    f"""
    {title_plain(["Et ceux qui ne", "fêtent pas Noël ?"])}
    {para("Tous vos voyageurs de décembre ne célèbrent pas Noël, et certains viennent justement pour y échapper. Un décor d'hiver fait le même effet sans imposer de symbole.", 31)}
    {numbered([
        ("Des lumières, des branches, des pommes de pin :", "chaleureux pour tout le monde. Gardez les symboles religieux pour chez vous."),
        ("Le sapin dans le salon, pas dans les chambres :", "chacun choisit de s'y asseoir ou non."),
        ("Dites-le dans l'annonce :", "« maison décorée pour les fêtes du 1er au 31 décembre ». Qui ne veut pas de sapin le sait avant de réserver, et vous pouvez le retirer sur demande."),
    ])}
    """,
    NOSRC, body_gap=28)

slides["S6.dc.html"] = page("Budget et temps", f"7 / {N}",
    f"""
    {title_plain(["Le budget", "et le temps"])}
    {numbered([
        ("Achetez une fois, en janvier,", "quand tout est soldé, et rangez dans une boîte étiquetée par pièce : l'année suivante, la pose prend une heure."),
        ("Prenez les photos la première année,", "de jour et à la nuit tombée, et réutilisez-les chaque automne dans vos annonces et sur votre site."),
        ("Prévoyez la dépose dans votre planning,", "entre deux séjours de janvier, avec un sac pour les aiguilles et un passage de plus de l'aspirateur."),
        ("Comptez le coût réel :", "quelques dizaines d'euros amortis sur plusieurs années, contre un ou deux séjours de plus réservés sur une photo. Faites votre propre calcul."),
    ])}
    """,
    NOSRC, body_gap=34)

slides["S7.dc.html"] = page("Trois niveaux", f"8 / {N}",
    f"""
    {title_plain(["Jusqu'où aller ?", "Trois niveaux"])}
    <div style="display: flex; flex-direction: column; gap: 14px">
      {card("une guirlande lumineuse sur la cheminée ou la fenêtre, une couronne sur la porte, un plaid. Dix minutes, et la photo change.", "1. Le minimum qui change tout :")}
      {card("un sapin décoré, une table dressée pour le réveillon, un panier avec du vin chaud et des papillotes. La maison de Noël que l'on photographie.", "2. La maison des fêtes :", light=True)}
      {card("un sapin nu et une boîte de décorations à accrocher, des chaussettes au prénom des enfants (demandé dans le message d'avant-séjour). Ce sont ces séjours-là dont on parle encore en mars.", "3. L'expérience :")}
    </div>
    """,
    NOSRC, body_gap=30)

slides["S8.dc.html"] = page("À retenir", f"9 / {N}",
    f"""
    {title_plain(["À retenir"])}
    {numbered([
        ("Décorez le salon, pas les chambres,", "en décor d'hiver plutôt qu'en symboles, et dites-le dans l'annonce."),
        ("Sécurité d'abord :", "sapin loin de la chaleur, guirlandes NF ou CE à LED sur minuterie, bougies à LED, détecteur de fumée testé."),
        ("Photographiez une fois,", "et vendez décembre dès novembre avec ces images."),
    ])}
    {para("Sources : sante.fr, « Quels gestes adopter pour profiter du sapin de Noël en toute sécurité à la maison ? », 24 juil. 2025 (norme NF S 54-200 au-delà de 60 cm, classes M0/M1, guirlandes NF ou CE, flocage) · Groupama, prévention du feu de sapin (conseils des pompiers). Les préférences des voyageurs citées ici ne reposent sur aucune enquête : retours d'hôtes.", 21, MUTED)}
    """,
    "Chaque semaine, le quotidien des gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {VIOLET}; font-weight: 900">Suivez-nous {icon("arrow")}</span>',
    body_gap=30)

order = list(slides.keys())
titles = ["1 · Couverture", "2 · Pourquoi décorer", "3 · Ce qui plaît, ce qui gêne", "4 · Naturel ou artificiel", "5 · La sécurité", "6 · Ceux qui ne fêtent pas Noël", "7 · Budget et temps", "8 · Trois niveaux", "9 · À retenir"]
write_all(slides, PROJ)
json.dump(canvas_json("Carrousel déco de Noël", order, titles), open(PROJ + "/canvas.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
render_all(PROJ, order, work_dir("deco-noel", "png"))
print("ok", len(order))
