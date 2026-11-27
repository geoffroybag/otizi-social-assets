#!/usr/bin/env python3
"""Carrousel « Actu » : taxe de séjour 2027, barème national inchangé, tarifs communaux, non classés, taxes additionnelles, qui collecte quoi."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from carrousel_lib import *

PROJ = work_dir("taxe-sejour-2027", "project")
N = 9
SRC_BAR = "Source : DGCL, « Taxe de séjour : barème applicable pour 2027 », collectivites-locales.gouv.fr (IPC 2025 : +0,9 %)"
SRC_CGCT = "Sources : CGCT art. L2333-30 (délibération avant le 1er juillet) · collectivites-locales.gouv.fr (application DELTA)"
SRC_ADD = "Sources : collectivites-locales.gouv.fr, taxe de séjour (taxes additionnelles) · CGCT art. L3333-1"
SRC_COLL = "Sources : CGCT art. L2333-33 et L2333-34 · Airbnb, aide « Collecte et versement de la taxe de séjour en France »"
SRC_SP = "Source : service-public.gouv.fr, fiche F743 « Taxe de séjour sur les hébergements touristiques »"
slides = {}

slides["Main.dc.html"] = page("Couverture", category_pill("Actu", "actu"),
    f"""
    {title_boxes([("Taxe de séjour 2027 :", "white", 62), ("ce qui change", "mint", 92), ("au 1er janvier", "white", 78)])}
    <div>{para("Le barème national ne bouge pas, mais votre commune a peut-être voté un nouveau tarif avant le 1er juillet. Fourchettes, non classés à 1-5 %, taxes additionnelles, qui collecte quoi : ce qu'il faut vérifier avant d'ouvrir 2027.", 36, BODY, maxw=860)}
      <div style="width: 260px; height: 10px; border-radius: 5px; background: {ACCENT}; margin-top: 18px"></div></div>
    """,
    "L'actu des gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {INK}; font-weight: 900">Glisser {icon("arrow")}</span>',
    body_gap=44, cover=True)

slides["S1.dc.html"] = page("Le barème 2027", f"2 / {N}",
    f"""
    {title_plain(["Le barème national :", "rien ne bouge"], 70)}
    {stat("+0,9&nbsp;%", "d'inflation retenue (indice des prix 2025) : après arrondi au dixième d'euro, le barème 2027 est identique à celui de 2026", 120)}
    <div style="display: flex; flex-direction: column; gap: 12px">
      {card("0,20&nbsp;€ à 0,80&nbsp;€ par personne et par nuit", "Chambres d'hôtes, meublés 1 étoile :", light=True)}
      {card("2 étoiles 0,30 à 1,00&nbsp;€ · 3 étoiles 0,50 à 1,70&nbsp;€", "Meublés classés :")}
      {card("4 étoiles 0,70 à 2,60&nbsp;€ · 5 étoiles 0,70 à 3,60&nbsp;€", "Meublés classés :")}
    </div>
    {para("Ce sont des fourchettes : votre commune ou votre intercommunalité fixe son tarif à l'intérieur, par délibération.", 28, MUTED)}
    """,
    SRC_BAR, body_gap=26)

slides["S2.dc.html"] = page("Les non classés", f"3 / {N}",
    f"""
    {title_plain(["Non classé :", "un pourcentage du prix"], 70)}
    {para("Pour un meublé sans classement ou en attente de classement, la taxe n'est pas un montant fixe : c'est un taux de 1 % à 5 % du coût hors taxes de la nuitée par personne, dans la limite du tarif le plus élevé adopté par la collectivité.", 31)}
    {card("un gîte à 120 € la nuit pour quatre personnes, soit 30 € par personne. À 5 %, la taxe est de 1,50 € par personne et par nuit : 6 € par nuit pour la famille, 42 € sur la semaine, avant taxes additionnelles.", "Exemple :", light=True)}
    {para("Le classement remplace ce pourcentage par un tarif fixe en euros, qui ne monte pas avec vos prix. C'est un calcul à faire, surtout si vous vendez cher.", 29, MUTED)}
    """,
    SRC_BAR, body_gap=30)

slides["S3.dc.html"] = page("Les taxes additionnelles", f"4 / {N}",
    f"""
    {title_plain(["Les taxes", "qui s'ajoutent"])}
    {numbered([
        ("La taxe additionnelle départementale : 10 %", "du montant communal, dans les départements qui l'ont instituée. Un tarif voté à 1 € devient 1,10 € sur la facture."),
        ("En Île-de-France : 15 % pour la Société des grands projets, et 200 %", "pour Île-de-France Mobilités. Un tarif de 1 € y monte à plus de 3 €."),
        ("34 % pour trois lignes ferroviaires :", "Provence-Côte d'Azur, Grand Projet du Sud-Ouest, Montpellier-Perpignan, dans les territoires concernés."),
    ])}
    {para("Les plateformes qui collectent les ajoutent automatiquement. En direct, c'est à vous de les intégrer à votre calcul et à votre reversement.", 29, MUTED)}
    """,
    SRC_ADD, body_gap=30)

slides["S4.dc.html"] = page("Le calendrier", f"5 / {N}",
    f"""
    {title_plain(["D'où vient", "votre tarif 2027 ?"])}
    {numbered([
        ("Avant le 1er juillet 2026,", "votre commune ou intercommunalité a pu voter de nouveaux tarifs, applicables au 1er janvier 2027. Sans vote, les tarifs précédents continuent de s'appliquer."),
        ("Du 1er janvier au 15 septembre,", "elle saisit sa délibération dans l'application DELTA de la DGFiP : c'est là que les plateformes lisent les tarifs."),
        ("Vous, maintenant :", "demandez la délibération à votre office de tourisme ou à la mairie, ou consultez le tarif de votre commune sur le téléservice de la DGFiP, accessible depuis la fiche F743 de service-public.gouv.fr."),
    ])}
    """,
    SRC_CGCT, body_gap=34)

slides["S5.dc.html"] = page("Qui collecte", f"6 / {N}",
    f"""
    {title_plain(["Qui collecte,", "qui reverse"])}
    <div style="display: flex; flex-direction: column; gap: 14px">
      {card("depuis 2019, les plateformes qui encaissent le paiement doivent collecter et reverser la taxe pour les loueurs non professionnels. Airbnb le fait pour tous ses hôtes en France, particuliers et professionnels, et la reverse aux communes.", "Sur une plateforme qui encaisse :", light=True)}
      {card("c'est vous qui collectez : la taxe est perçue avant le départ, figure sur une ligne distincte de la facture, hors TVA, et vous la reversez aux dates fixées par votre collectivité.", "En direct, ou si le voyageur paie sur place :")}
    </div>
    {para("Vérifiez dans chaque extranet qui fait quoi : une taxe collectée deux fois se rembourse, une taxe collectée par personne se redresse.", 28, MUTED)}
    """,
    SRC_COLL, body_gap=28)

slides["S6.dc.html"] = page("Exonérations", f"7 / {N}",
    f"""
    {title_plain(["Qui ne la paie pas"])}
    <div style="display: flex; flex-direction: column; gap: 12px">
      {item("Les personnes mineures : un enfant ne paie jamais la taxe de séjour", "yes")}
      {item("Les titulaires d'un contrat de travail saisonnier employés dans la commune", "yes")}
      {item("Les personnes en hébergement d'urgence ou en relogement temporaire", "yes")}
      {item("Les occupants d'un logement dont le loyer est inférieur au seuil fixé par la commune", "yes")}
    </div>
    {para("Le tarif doit être affiché chez vous, et la taxe ne peut pas être « incluse » dans le prix de la chambre au réel : elle s'ajoute, sur sa propre ligne.", 29, MUTED)}
    """,
    SRC_SP, body_gap=30)

slides["S7.dc.html"] = page("En cas d'oubli", f"8 / {N}",
    f"""
    {title_plain(["Et si vous oubliez", "de déclarer ?"])}
    {numbered([
        ("La taxation d'office :", "après une mise en demeure restée sans réponse, le maire ou le président de l'intercommunalité peut vous taxer d'office, avec un avis motivé trente jours avant la mise en recouvrement."),
        ("L'intérêt de retard :", "0,20 % par mois de retard sur les sommes dues."),
        ("Des amendes", "sont prévues par le Code général des collectivités territoriales (art. L2333-34-1) pour l'absence de déclaration ou de reversement."),
    ])}
    {para("Dans la pratique, les collectivités commencent par une relance. Un état déclaratif à jour et des reversements aux bonnes dates vous évitent tout cela.", 29, MUTED)}
    """,
    SRC_SP, body_gap=30)

slides["S8.dc.html"] = page("À retenir", f"9 / {N}",
    f"""
    {title_plain(["Avant le 1er janvier"])}
    {numbered([
        ("Vérifiez le tarif 2027 de votre commune,", "délibération ou téléservice de la DGFiP : le barème national n'a pas changé, le vôtre peut-être."),
        ("Mettez-le à jour partout :", "site de réservation, annonces (la catégorie de classement sur les plateformes), livret d'accueil, affichage."),
        ("Relisez votre facture :", "taxe sur une ligne distincte, hors TVA, taxes additionnelles comprises."),
        ("Notez vos dates de reversement,", "et, si vous n'êtes pas classé, faites le calcul du classement."),
    ])}
    {para("Sources : DGCL, barème 2027 et page taxe de séjour (collectivites-locales.gouv.fr) · CGCT art. L2333-30, L2333-31, L2333-33, L2333-34, L2333-34-1, L3333-1 · service-public.gouv.fr, fiche F743 · Airbnb, aide « Collecte et versement de la taxe de séjour en France ».", 21, MUTED)}
    """,
    "Chaque semaine, ce qui change pour les gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {VIOLET}; font-weight: 900">Suivez-nous {icon("arrow")}</span>',
    body_gap=26)

order = list(slides.keys())
titles = ["1 · Couverture", "2 · Barème 2027", "3 · Non classés", "4 · Taxes additionnelles", "5 · Calendrier", "6 · Qui collecte", "7 · Exonérations", "8 · En cas d'oubli", "9 · Avant le 1er janvier"]
write_all(slides, PROJ)
json.dump(canvas_json("Carrousel taxe de séjour 2027", order, titles), open(PROJ + "/canvas.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
render_all(PROJ, order, work_dir("taxe-sejour-2027", "png"))
print("ok", len(order))
