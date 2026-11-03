#!/usr/bin/env python3
"""Carrousel « Conseil » : basse saison, 6 façons de remplir novembre."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from carrousel_lib import *

PROJ = work_dir("basse-saison", "project")
N = 9
slides = {}

slides["Main.dc.html"] = page("Couverture", category_pill("Conseil", "conseil"),
    f"""
    {photo_block(photo("basse-saison"))}
    {title_boxes([("Basse saison :", "white", 80), ("6 façons", "mint", 112), ("de remplir novembre", "white", 68)])}
    <div>{para("Le calendrier se vide, les charges restent. Six leviers concrets, à activer cette semaine, sans brader vos tarifs.", 38, BODY, maxw=860)}
      <div style="width: 260px; height: 10px; border-radius: 5px; background: {ACCENT}; margin-top: 18px"></div></div>
    """,
    "L'actu des gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {INK}; font-weight: 900">Glisser {icon("arrow")}</span>',
    body_gap=44, cover=True)

slides["S1.dc.html"] = page("Novembre n'est pas août", f"2 / {N}",
    f"""
    {title_plain(["Novembre", "n'est pas août"])}
    {para("Pas de vacances scolaires avant Noël, des jours courts, des voyageurs qui réservent tard et pour peu de nuits. Ce ne sont pas les clients de l'été : il faut leur parler autrement, et leur proposer autre chose.", 34)}
    <div style="display: flex; flex-direction: column; gap: 14px">
      {card("des couples sans enfants, des télétravailleurs, des familles qui se retrouvent, des gens du coin qui cherchent une parenthèse à une heure de chez eux.", "Qui voyage en novembre ?")}
      {card("le calme, le chauffage, une bonne table à côté, une raison de venir.", "Ce qu'ils cherchent :", light=True)}
    </div>
    """,
    "Conseil · gîtes et chambres d'hôtes", body_gap=32)

slides["S2.dc.html"] = page("1 · Séjours longs", f"3 / {N}",
    f"""
    {title_plain(["1. Les séjours longs,", "à tarif dégressif"])}
    {numbered([
        ("Activez une remise à la semaine et au mois", "sur vos plateformes et en direct : une semaine remplie à prix réduit vaut mieux que deux nuits à plein tarif et cinq nuits vides."),
        ("Un séjour long, c'est moins de ménage, moins d'arrivées,", "et un chauffage qui ne tourne pas pour une maison vide."),
        ("Au-delà de quelques semaines, vérifiez votre cadre :", "contrat, taxe de séjour, assurance, règles locales sur la durée des locations."),
    ])}
    """,
    "Conseil · gîtes et chambres d'hôtes", body_gap=36)

slides["S3.dc.html"] = page("2 · Télétravail", f"4 / {N}",
    f"""
    {title_plain(["2. Le télétravail", "au vert"])}
    {numbered([
        ("Un vrai bureau, pas un coin de table :", "une chaise correcte, une lampe, une prise à portée de main, une vue si possible."),
        ("Affichez le débit réel du Wi-Fi,", "testé dans la pièce de travail, et le nom de l'opérateur. Un télétravailleur réserve sur cette ligne."),
        ("Dites-le dans l'annonce :", "« idéal télétravail » dans le titre, et une photo du poste de travail parmi les trois premières."),
    ])}
    """,
    "Conseil · gîtes et chambres d'hôtes", body_gap=36)

slides["S4.dc.html"] = page("3 · Les locaux", f"5 / {N}",
    f"""
    {title_plain(["3. Les locaux,", "votre premier marché"])}
    {numbered([
        ("Les gens à moins d'une heure", "ne pensent pas à vous en novembre… sauf si vous leur donnez un prétexte : anniversaire, week-end entre amis, retrouvailles de famille."),
        ("Une offre « deux nuits, arrivée le vendredi soir »", "sur votre page Facebook ou Instagram, et dans les groupes locaux."),
        ("Les entreprises du coin :", "un recruté qui cherche un logement, un consultant de passage, un stagiaire. Un e-mail à cinq entreprises suffit pour commencer."),
    ])}
    """,
    "Conseil · gîtes et chambres d'hôtes", body_gap=36)

slides["S5.dc.html"] = page("4 · Partenariats", f"6 / {N}",
    f"""
    {title_plain(["4. Restos, caves,", "activités : jouez à deux"], 70)}
    {numbered([
        ("Le restaurateur d'à côté", "a des clients qui cherchent où dormir. Vous avez des voyageurs qui cherchent où manger. Échangez vos cartes."),
        ("Une offre packagée :", "nuit + dégustation, nuit + atelier, nuit + spa du coin. Vous ne vendez plus une chambre, vous vendez un week-end."),
        ("Mettez-vous d'accord sur ce que chacun gagne,", "et sur qui encaisse. Un partenariat flou s'arrête au premier malentendu."),
    ])}
    """,
    "Conseil · gîtes et chambres d'hôtes", body_gap=36)

slides["S6.dc.html"] = page("5 · Offres week-end", f"7 / {N}",
    f"""
    {title_plain(["5. Des offres week-end", "qui ne bradent pas"], 70)}
    {numbered([
        ("Ne baissez pas le prix, ajoutez :", "une nuit offerte pour trois réservées, le petit-déjeuner inclus, un départ tardif le dimanche."),
        ("Un minimum de nuits souple :", "deux en semaine, une le week-end si votre ménage le permet."),
        ("Un prix plancher en dessous duquel vous n'allez pas :", "vos charges fixes ne baissent pas en novembre. Le chauffage, lui, monte."),
    ])}
    """,
    "Conseil · gîtes et chambres d'hôtes", body_gap=36)

slides["S7.dc.html"] = page("6 · Calendrier local", f"8 / {N}",
    f"""
    {title_plain(["6. Le calendrier local,", "date par date"], 72)}
    {numbered([
        ("Listez ce qui se passe à moins de 30 minutes :", "marché de Noël, salon, match, concert, foire, Beaujolais nouveau, pont du 11 novembre."),
        ("Ajustez vos prix et vos minimums sur ces dates", "avant que les autres hébergeurs s'en aperçoivent."),
        ("Mettez à jour l'annonce :", "une phrase sur l'événement et le temps de trajet. C'est ce que tape le voyageur dans la barre de recherche."),
    ])}
    """,
    "Conseil · gîtes et chambres d'hôtes", body_gap=36)

slides["S8.dc.html"] = page("À faire cette semaine", f"9 / {N}",
    f"""
    {title_plain(["À faire", "cette semaine"])}
    {numbered([
        ("Ouvrez vos remises semaine et mois", "et ajoutez une photo du poste de travail dans l'annonce."),
        ("Écrivez à trois commerçants du coin", "pour une offre commune avant Noël."),
        ("Bloquez vos tarifs sur les dates des événements locaux", "de novembre et décembre."),
    ])}
    {para("Et vous, qu'est-ce qui remplit votre calendrier en novembre ? Dites-le en commentaire, les bonnes idées se partagent.", 28, MUTED)}
    """,
    "Chaque semaine, ce qui change pour les gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {VIOLET}; font-weight: 900">Suivez-nous {icon("arrow")}</span>',
    body_gap=30)

order = list(slides.keys())
titles = ["1 · Couverture", "2 · Novembre", "3 · Séjours longs", "4 · Télétravail", "5 · Locaux", "6 · Partenariats", "7 · Week-ends", "8 · Calendrier", "9 · À faire"]
write_all(slides, PROJ)
json.dump(canvas_json("Carrousel basse saison", order, titles), open(PROJ + "/canvas.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
render_all(PROJ, order, work_dir("basse-saison", "png"))
print("ok", len(order))
