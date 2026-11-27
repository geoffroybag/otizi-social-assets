#!/usr/bin/env python3
"""Carrousel « Conseil » : les 5 réglages de calendrier qui font perdre des réservations (durée minimum, délai de préparation, préavis, fenêtre, jours d'arrivée)."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from carrousel_lib import *

PROJ = work_dir("reglages-calendrier", "project")
N = 9
SRC_AIR = "Source : Airbnb, aide n° 484 « Personnaliser vos paramètres de réservation » et centre de ressources « Mettre à jour vos disponibilités »"
SRC_AIR2 = "Source : Airbnb, centre de ressources « Mettre à jour vos disponibilités » (options de l'annonce)"
SRC_BKG = "Sources : Booking.com Partner Hub, restrictions de durée de séjour et de réservation anticipée · Airbnb, centre de ressources"
SRC_ACPT = "Source : décret n° 2026-121 du 20 fév. 2026 (acompte versable 12 mois avant l'arrivée depuis le 1er mars 2026)"
NOSRC = "Conseil · gîtes et chambres d'hôtes"
slides = {}

slides["Main.dc.html"] = page("Couverture", category_pill("Conseil", "conseil"),
    f"""
    {title_boxes([("5 réglages", "white", 96), ("de calendrier", "mint", 84), ("qui vous coûtent cher", "white", 60)])}
    <div>{para("Durée minimum, délai de préparation, préavis, fenêtre de réservation, jours d'arrivée : cinq cases cochées un jour et jamais rouvertes, qui rendent votre maison invisible sans que personne ne vous le dise.", 36, BODY, maxw=860)}
      <div style="width: 260px; height: 10px; border-radius: 5px; background: {ACCENT}; margin-top: 18px"></div></div>
    """,
    "Conseils pour les gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {INK}; font-weight: 900">Glisser {icon("arrow")}</span>',
    body_gap=44, cover=True)

slides["S1.dc.html"] = page("Le voyageur ne voit rien", f"2 / {N}",
    f"""
    {title_plain(["Le voyageur ne voit", "jamais vos réglages"], 72)}
    {para("Il tape des dates, un nombre de personnes, et regarde ce qui s'affiche. Si vos règles de disponibilité ne sont pas respectées, votre annonce n'apparaît tout simplement pas : pas de « complet », pas de message, rien.", 32)}
    {card("Airbnb l'écrit noir sur blanc : si le calendrier est bloqué pour les dates demandées, ou si des exigences comme le préavis ou le délai de préparation ne sont pas remplies, l'annonce peut ne pas apparaître dans les résultats.", "Un filtre avant le prix.", light=True)}
    {para("Sur votre propre site, c'est pareil : un moteur de réservation applique vos règles sans explication. Ces cinq réglages se vérifient en dix minutes, canal par canal.", 30, MUTED)}
    """,
    SRC_AIR, body_gap=30)

slides["S2.dc.html"] = page("La durée minimum", f"3 / {N}",
    f"""
    {title_plain(["1 · La durée", "minimum de séjour"])}
    {para("Une semaine minimum en août se comprend. Mais si la règle reste la même en novembre, chaque demande de week-end disparaît avant même d'avoir vu votre prix.", 31)}
    {numbered([
        ("Réglez-la par période,", "pas pour l'année : une valeur pour la haute saison, une autre pour les ailes de saison, une troisième pour l'hiver."),
        ("Posez-vous la question du ménage,", "pas celle de l'habitude : deux nuits valent-elles un changement de draps ? Si oui, ouvrez-les."),
        ("Vérifiez que votre site en direct", "et vos annonces disent la même chose : un minimum différent d'un canal à l'autre finit en double réservation ou en trou invendable."),
    ])}
    """,
    NOSRC, body_gap=30)

slides["S3.dc.html"] = page("Le délai de préparation", f"4 / {N}",
    f"""
    {title_plain(["2 · Le délai", "de préparation"])}
    {para("C'est le nombre de nuits bloquées automatiquement avant et après chaque réservation. Sur Airbnb, trois options : aucune, une ou deux nuits.", 31)}
    <div style="display: flex; flex-direction: column; gap: 12px">
      {item("Une nuit bloquée de chaque côté : un séjour de trois nuits en occupe cinq dans votre calendrier", "no")}
      {item("Deux nuits : vous ne vendez plus que des séjours espacés, même en pleine saison", "no")}
      {item("Aucune, si le ménage se fait entre deux séjours le jour même ; une seule si vous avez besoin de souffler", "yes")}
    </div>
    {para("Le délai de préparation est une assurance contre la fatigue, pas une règle de gestion. Réglez-le au plus juste, et bloquez à la main les jours où vous voulez vraiment fermer.", 29, MUTED)}
    """,
    SRC_AIR2, body_gap=28)

slides["S4.dc.html"] = page("Le préavis", f"5 / {N}",
    f"""
    {title_plain(["3 · Le préavis", "de réservation"])}
    {para("Combien de temps avant l'arrivée acceptez-vous une réservation ? Airbnb propose le jour même, un, deux, trois ou sept jours. À sept jours, vous ne verrez jamais les réservations de dernière minute, celles qui remplissent justement l'hiver.", 31)}
    {numbered([
        ("Un jour de préavis", "suffit à la plupart des maisons : vous êtes prévenu la veille, le ménage est fait, le chauffage est lancé."),
        ("Le jour même, avec une heure limite,", "si l'arrivée est autonome (boîte à clés, serrure connectée) et le logement toujours prêt."),
        ("Sept jours seulement", "si vous êtes loin, sans relais sur place : et acceptez alors de perdre les séjours improvisés."),
    ])}
    """,
    SRC_AIR2, body_gap=30)

slides["S5.dc.html"] = page("La fenêtre de réservation", f"6 / {N}",
    f"""
    {title_plain(["4 · La fenêtre", "de réservation"])}
    {para("Jusqu'à quand dans le futur peut-on réserver chez vous ? Airbnb propose trois, six, neuf, douze ou vingt-quatre mois, et précise qu'une fenêtre plus longue améliore la visibilité dans les recherches.", 31)}
    <div style="display: flex; flex-direction: column; gap: 14px">
      {card("une famille qui organise son été en janvier ne vous trouve pas. Elle réserve ailleurs, et revient l'an prochain… ailleurs.", "Trois mois :", light=True)}
      {card("vos tarifs de l'an prochain sont posés, et vous pouvez encaisser l'acompte dès la réservation : depuis le 1er mars 2026, il peut être versé jusqu'à douze mois avant l'arrivée.", "Douze mois :")}
    </div>
    """,
    "Sources : Airbnb, centre de ressources · décret n° 2026-121 du 20 fév. 2026 (acompte)", body_gap=30)

slides["S6.dc.html"] = page("Les jours d'arrivée", f"7 / {N}",
    f"""
    {title_plain(["5 · Les jours", "d'arrivée imposés"])}
    {para("Le samedi-samedi est une tradition du gîte, et une bonne règle pour juillet-août. Hors saison, il élimine toutes les demandes du milieu de semaine : le couple de retraités du mardi, le télétravailleur du lundi au jeudi.", 31)}
    {numbered([
        ("Un jour d'arrivée imposé", "se règle par période, comme la durée minimum. Sur Booking.com, cela s'appelle « fermé à l'arrivée » ou « fermé au départ » ; sur Airbnb, une règle de disponibilité par dates."),
        ("Relâchez-le dès septembre :", "arrivée libre, et un minimum de nuits adapté. Les trous entre deux séjours se comblent beaucoup mieux."),
        ("Attention aux combinaisons :", "une arrivée fermée le samedi et un départ fermé le dimanche peuvent empêcher un week-end entier sans que vous le voyiez."),
    ])}
    """,
    SRC_BKG, body_gap=28)

slides["S7.dc.html"] = page("Le test", f"8 / {N}",
    f"""
    {title_plain(["Faites le test", "du voyageur"])}
    {para("Prenez votre téléphone, en navigation privée, et cherchez votre maison comme un inconnu : un week-end dans trois semaines, deux nuits en semaine le mois prochain, une semaine l'été prochain.", 31)}
    <div style="display: flex; flex-direction: column; gap: 12px">
      {item("Vous apparaissez pour les trois recherches : vos réglages sont bons", "yes")}
      {item("Vous disparaissez sur l'une d'elles : vous savez maintenant quel réglage la bloque", "no")}
      {item("Refaites le test sur chaque canal, votre site compris : les règles doivent être les mêmes partout", "yes")}
    </div>
    """,
    NOSRC, body_gap=32)

slides["S8.dc.html"] = page("À retenir", f"9 / {N}",
    f"""
    {title_plain(["La check-list", "de la semaine"])}
    {numbered([
        ("Durée minimum :", "une valeur par période, jamais la même toute l'année."),
        ("Délai de préparation :", "aucune nuit ou une seule, et des jours bloqués à la main quand vous fermez."),
        ("Préavis :", "un jour, ou le jour même avec une heure limite si l'arrivée est autonome."),
        ("Fenêtre :", "douze mois au moins, avec les tarifs de l'an prochain déjà posés."),
        ("Jours d'arrivée :", "samedi en haute saison seulement ; libre le reste de l'année."),
    ])}
    {para("Sources : Airbnb, aide n° 484 « Personnaliser vos paramètres de réservation » et centre de ressources « Mettre à jour vos disponibilités » · Booking.com Partner Hub, restrictions de séjour · décret n° 2026-121 du 20 fév. 2026. Sans statistique : aucune étude publique ne mesure l'effet de ces réglages.", 21, MUTED)}
    """,
    "Chaque semaine, ce qui change pour les gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {VIOLET}; font-weight: 900">Suivez-nous {icon("arrow")}</span>',
    body_gap=26)

order = list(slides.keys())
titles = ["1 · Couverture", "2 · Le voyageur ne voit rien", "3 · Durée minimum", "4 · Délai de préparation", "5 · Préavis", "6 · Fenêtre de réservation", "7 · Jours d'arrivée", "8 · Le test", "9 · Check-list"]
write_all(slides, PROJ)
json.dump(canvas_json("Carrousel réglages de calendrier", order, titles), open(PROJ + "/canvas.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
render_all(PROJ, order, work_dir("reglages-calendrier", "png"))
print("ok", len(order))
