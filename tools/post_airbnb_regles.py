#!/usr/bin/env python3
"""Carrousel « Actu » : Airbnb, les nouvelles règles de la maison s'appliquent (réservations dès le 20 nov. 2026)."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from carrousel_lib import *

PROJ = work_dir("airbnb-regles", "project")
N = 9
SRC_POL = "Source : Airbnb, politique « Règles de la maison et demandes raisonnables » (via Rental Scale-Up, 21 oct. 2026)"
SRC_TEST = "Source : Rental Scale-Up, test de l'éditeur d'annonce (23 oct. 2026)"
SRC_TM = "Sources : TourMaG (28 oct. 2026) · Mediaterranee (28 oct. 2026)"
slides = {}

slides["Main.dc.html"] = page("Couverture", category_pill("Actu", "actu"),
    f"""
    {title_boxes([("Airbnb :", "white", 84), ("c'est aujourd'hui", "mint", 80), ("que ça change", "white", 80)])}
    <div>{para("Les nouvelles règles de la maison s'appliquent aux réservations faites à partir de ce 20 novembre. Ce qui change vraiment, comment Airbnb contrôle, et pourquoi des hôtes manifestent à 16 h.", 36, BODY, maxw=860)}
      <div style="width: 260px; height: 10px; border-radius: 5px; background: {ACCENT}; margin-top: 18px"></div></div>
    """,
    "L'actu des gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {INK}; font-weight: 900">Glisser {icon("arrow")}</span>',
    body_gap=44, cover=True)

slides["S1.dc.html"] = page("Depuis ce matin", f"2 / {N}",
    f"""
    {title_plain(["Ce qui s'applique", "depuis ce matin"])}
    {para("Annoncée le 20 octobre, la politique « Règles de la maison et demandes raisonnables » vaut pour toute réservation faite à partir du 20 novembre 2026, partout dans le monde. Une réservation prise avant garde les règles affichées à ce moment-là.", 31)}
    <div style="display: flex; flex-direction: column; gap: 12px">
      {item("Laver et ranger la vaisselle", "no")}
      {item("Retirer les draps, lancer une machine", "no")}
      {item("Sortir les poubelles hors du logement", "no")}
      {item("Facturer une pénalité pour une tâche non faite", "no")}
    </div>
    """,
    SRC_POL, body_gap=28)

slides["S2.dc.html"] = page("Ce qui reste permis", f"3 / {N}",
    f"""
    {title_plain(["Ce que vous pouvez", "encore demander"], 72)}
    <div style="display: flex; flex-direction: column; gap: 12px">
      {item("La vaisselle sale dans l'évier", "yes")}
      {item("Les serviettes utilisées regroupées", "yes")}
      {item("Les déchets triés dans les bacs du logement", "yes")}
      {item("La clim éteinte, la porte fermée à clé", "yes")}
      {item("Une pièce d'identité montrée à l'arrivée, si l'annonce le dit, sans en garder de copie", "yes")}
    </div>
    {para("Sept règles standard restent des règles (nombre de dormeurs, heures calmes, fêtes, animaux, tabac, tournages, fermeture à clé). Tout le reste devient une demande, sans sanction possible.", 27, MUTED)}
    """,
    SRC_POL, body_gap=28)

slides["S3.dc.html"] = page("Comment Airbnb contrôle", f"4 / {N}",
    f"""
    {title_plain(["Comment Airbnb", "contrôle"])}
    {numbered([
        ("L'éditeur d'annonce surligne", "la phrase qui semble enfreindre la politique, au moment où vous l'enregistrez."),
        ("Si vous l'enregistrez quand même,", "la règle part en examen et Airbnb vous écrit par e-mail."),
        ("Vous pouvez faire appel une fois,", "avec une preuve : arrêté municipal, règlement de copropriété."),
        ("Sinon, les voyageurs voient un bandeau", "du type « inclut des demandes de ménage », puis l'annonce perd en visibilité dans les recherches."),
    ])}
    """,
    SRC_POL, body_gap=34)

slides["S4.dc.html"] = page("L'outil à l'épreuve", f"5 / {N}",
    f"""
    {title_plain(["L'outil à l'épreuve :", "accepté, refusé"], 70)}
    <div style="display: flex; flex-direction: column; gap: 12px">
      {item("« Merci de mettre la vaisselle sale dans l'évier et de regrouper les serviettes »", "yes")}
      {item("« Petit-déjeuner proposé à 15 € par personne, sur demande »", "yes")}
      {item("« Vérification d'identité à l'arrivée, en personne »", "yes")}
      {item("« Merci de remplir puis démarrer le lave-vaisselle avant de partir »", "no")}
      {item("« 100 € de frais de ménage si la maison est sale »", "no")}
      {item("« Merci d'envoyer une photo du passeport avant l'arrivée »", "no")}
    </div>
    {para("Test réalisé sur un seul logement : l'outil lit les mots, pas toujours le contexte. Un signalement n'est pas une sanction.", 26, MUTED)}
    """,
    SRC_TEST, body_gap=26)

slides["S5.dc.html"] = page("La colère des hôtes", f"6 / {N}",
    f"""
    {title_plain(["La colère des hôtes :", "vaisselle sale à 16 h"], 70)}
    {stat("21 000", "signataires, et plus, pour une pétition qui demande le retrait de la règle sur la vaisselle, selon TourMaG", 110)}
    <div style="display: flex; flex-direction: column; gap: 14px">
      {card("devant le siège d'Airbnb France, vaisselle sale en main, à remettre à son directeur général. Certains hôtes ont bloqué leurs calendriers à partir d'aujourd'hui.", "Rassemblement ce 20 novembre à 16 h")}
      {card("la commission de 15,5 % payée par l'hôte depuis le 13 octobre. La vaisselle est la goutte d'eau.", "La vraie cause, selon la presse :", light=True)}
    </div>
    {para("Aucune enquête représentative : des hôtes soutiennent aussi ces règles, plus simples pour les voyageurs.", 25, MUTED)}
    """,
    SRC_TM, body_gap=26)

slides["S6.dc.html"] = page("La version d'Airbnb", f"7 / {N}",
    f"""
    {title_plain(["La version", "d'Airbnb"])}
    <div style="display: flex; flex-direction: column; gap: 14px">
      {card("des règles « source de confusion, contraignantes et difficiles à gérer ». D'où une liste fermée de sept règles, et des demandes « raisonnables » pour le reste.", "Les voyageurs se plaignaient :")}
      {card("ils doivent couvrir un nettoyage standard entre deux séjours, c'est-à-dire le travail réel, pas celui que faisait le voyageur.", "Les frais de ménage restent autorisés :")}
      {card("« Les hôtes conservent le contrôle de leurs règles et de leurs demandes », répond la plateforme aux critiques.", "Et sur la liberté des hôtes :", light=True)}
    </div>
    """,
    "Sources : Euronews (21 oct. 2026) · TourMaG (28 oct. 2026)", body_gap=32)

slides["S7.dc.html"] = page("Vos trois chantiers", f"8 / {N}",
    f"""
    {title_plain(["Vos trois chantiers", "de la semaine"])}
    {numbered([
        ("Rouvrez l'éditeur d'annonce :", "cochez vos règles parmi les sept, et passez tout le reste en « demandes », rattachées à « avant le départ ». Laissez l'outil surligner."),
        ("Recalculez vos frais de ménage :", "s'ils couvrent le travail que vous récupérez, ils sont légitimes. Rappel : depuis le 23 octobre, la commission de 15,5 % s'applique aussi à ces frais."),
        ("Booking et vos réservations en direct ne sont pas concernés :", "vos conditions s'appliquent. Mais relisez votre livret d'accueil, lui aussi gagne à demander plutôt qu'à exiger."),
    ])}
    """,
    "Sources : Airbnb (politique du 20 oct. 2026) · TourMaG (28 oct. 2026)", body_gap=34)

slides["S8.dc.html"] = page("À retenir", f"9 / {N}",
    f"""
    {title_plain(["À retenir"])}
    <div style="display: flex; flex-direction: column; gap: 14px">
      {item("C'est la date de réservation qui compte : à partir du 20 novembre 2026", "no")}
      {item("Vaisselle, draps, machine, poubelles hors du logement, pénalités : plus possible", "no")}
      {item("Évier, serviettes, tri, clim, clé : des demandes, toujours possibles", "yes")}
      {item("Signalement, e-mail, un appel, puis bandeau et visibilité réduite", "no")}
    </div>
    {para("Sources : Airbnb, politique « Règles de la maison et demandes raisonnables » (20 oct. 2026) · Rental Scale-Up (21 et 23 oct. 2026) · Euronews (21 oct. 2026) · TourMaG (28 oct. 2026) · Mediaterranee (28 oct. 2026) · Toutsurmesfinances (28 oct. 2026).", 21, MUTED)}
    """,
    "Chaque semaine, ce qui change pour les gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {VIOLET}; font-weight: 900">Suivez-nous {icon("arrow")}</span>',
    body_gap=30)

order = list(slides.keys())
titles = ["1 · Couverture", "2 · Depuis ce matin", "3 · Encore permis", "4 · Comment Airbnb contrôle", "5 · L'outil à l'épreuve", "6 · Colère des hôtes", "7 · Version d'Airbnb", "8 · Trois chantiers", "9 · À retenir"]
write_all(slides, PROJ)
json.dump(canvas_json("Carrousel Airbnb règles 20 novembre", order, titles), open(PROJ + "/canvas.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
render_all(PROJ, order, work_dir("airbnb-regles", "png"))
print("ok", len(order))
