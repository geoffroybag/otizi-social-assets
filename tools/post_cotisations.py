#!/usr/bin/env python3
"""Carrousel « Actu » : chambres d'hôtes, 21,2 % de cotisations sociales depuis le 1er janvier 2026."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from carrousel_lib import *

PROJ = work_dir("cotisations", "project")
N = 9
SRC_CO = "Source : Compta Online, taux micro-social 2026 (d'après l'Urssaf)"
SRC_CX = "Source : The Connexion, 23 déc. 2025 (maj 6 janv. 2026)"
SRC_AN = "Source : Assemblée nationale, réponse ministérielle du 20 mai 2025 (QE n° 6664)"
SRC_PLF = "Sources : MySweetimmo, 9 oct. 2026 · Olympe, suivi du PLF 2027"
slides = {}

slides["Main.dc.html"] = page("Couverture", category_pill("Actu", "actu"),
    f"""
    {title_boxes([("Chambres d'hôtes :", "white", 72), ("21,2 % de", "mint", 112), ("cotisations", "white", 92)])}
    <div>{para("Depuis le 1er janvier 2026, les cotisations sociales des chambres d'hôtes en micro-entreprise ont presque doublé. Ce qui a changé, qui est concerné, et ce que le budget 2027 pourrait corriger.", 36, BODY, maxw=860)}
      <div style="width: 260px; height: 10px; border-radius: 5px; background: {ACCENT}; margin-top: 18px"></div></div>
    """,
    "L'actu des gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {INK}; font-weight: 900">Glisser {icon("arrow")}</span>',
    body_gap=44, cover=True)

slides["S1.dc.html"] = page("Ce qui a changé", f"2 / {N}",
    f"""
    {title_plain(["Ce qui a changé", "le 1er janvier 2026"])}
    {stat("21,2 %", "du chiffre d'affaires en cotisations sociales pour une chambre d'hôtes en micro-entreprise, contre 12,3 % jusqu'en 2025", 110)}
    {para("La raison : en micro-social, les recettes d'hébergement des chambres d'hôtes sont passées de la catégorie « ventes de marchandises » à celle des « prestations de services ». Même activité, même déclaration, taux presque doublé.", 32)}
    """,
    SRC_CO, body_gap=36)

slides["S2.dc.html"] = page("Gîte classé vs chambre d'hôtes", f"3 / {N}",
    f"""
    {title_plain(["Gîte classé : 6 %.", "Chambre d'hôtes : 21,2 %."], 70)}
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px">
      <div style="background: #FFFFFF; border: 2px solid {LINE}; border-radius: 18px; padding: 28px; display: flex; flex-direction: column; gap: 10px">
        <div style="font-size: 110px; line-height: 0.9; font-weight: 900; letter-spacing: -0.04em; color: {VIOLET}">6 %</div>
        <div style="font-size: 27px; line-height: 1.3; color: {BODY}">pour un meublé de tourisme classé en micro-entreprise. Taux inchangé en 2026.</div>
      </div>
      <div style="background: {VIOLET}; color: #FFFFFF; border-radius: 18px; padding: 28px; display: flex; flex-direction: column; gap: 10px">
        <div style="font-size: 110px; line-height: 0.9; font-weight: 900; letter-spacing: -0.04em; color: {ACCENT}">21,2 %</div>
        <div style="font-size: 27px; line-height: 1.3">pour une chambre d'hôtes, petit-déjeuner compris dans la nuitée.</div>
      </div>
    </div>
    {card("l'écart représente 1 520 € de cotisations par an. Pour une activité qui, par définition, ne dépasse pas cinq chambres.", "Sur 10 000 € de recettes,")}
    """,
    "Sources : Compta Online, taux 2026 · The Connexion, déc. 2025", body_gap=30)

slides["S3.dc.html"] = page("Qui est concerné", f"4 / {N}",
    f"""
    {title_plain(["Qui est concerné,", "et à partir de quand"])}
    {numbered([
        ("Les chambres d'hôtes déclarées en micro-entreprise :", "c'est le taux du régime micro-social qui a changé, pas celui du régime réel."),
        ("Dès un revenu modeste :", "l'affiliation devient obligatoire quand le revenu net de l'activité dépasse 13 % du plafond de la Sécurité sociale, soit environ 6 248 € en 2026."),
        ("Pas la table d'hôtes :", "les repas restent dans la catégorie « ventes ». Seules les recettes d'hébergement changent de case."),
    ])}
    {para("Les hôtes contestent cette lecture, qui applique aux chambres d'hôtes une réforme pensée pour les meublés de tourisme. L'Urssaf l'applique quand même.", 27, MUTED)}
    """,
    SRC_CO, body_gap=32)

slides["S4.dc.html"] = page("Combien de maisons", f"5 / {N}",
    f"""
    {title_plain(["21 000 chambres d'hôtes,", "la moitié touchée"], 70)}
    {stat("21 000", "chambres d'hôtes en France, environ. La moitié seraient concernées par la hausse, selon The Connexion", 100)}
    <div style="display: flex; flex-direction: column; gap: 14px">
      {card("ne garderait que 6 € de bénéfice par client après la réforme, d'après son propre calcul.", "Une hôte bretonne, à 75 € la nuit,")}
      {card("Un chiffre de l'association, pas une statistique officielle.", "L'ANCH, association née pour défendre les hôtes, affirme que 60 % des maisons d'hôtes sont menacées.", light=True)}
    </div>
    """,
    SRC_CX, body_gap=30)

slides["S5.dc.html"] = page("L'abattement fiscal", f"6 / {N}",
    f"""
    {title_plain(["Le deuxième coup :", "l'abattement fiscal"])}
    {para("Depuis les revenus 2025, la loi Le Meur a aussi ramené l'abattement micro-BIC des chambres d'hôtes de 71 % à 50 %. Résultat : la part des recettes imposée passe de 29 % à 50 %.", 33)}
    {stat("50 %", "d'abattement au lieu de 71 %. Le gouvernement renvoie les hôtes dont les charges dépassent l'abattement vers le régime réel.", 140)}
    """,
    SRC_AN, body_gap=36)

slides["S6.dc.html"] = page("Budget 2027", f"7 / {N}",
    f"""
    {title_plain(["Le budget 2027", "pourrait corriger… en partie"], 70)}
    {para("Le 8 octobre 2026, la commission des finances de l'Assemblée a adopté un amendement du député Iñaki Echaniz qui rétablirait l'abattement à 71 % pour les chambres d'hôtes.", 32)}
    <div style="display: flex; flex-direction: column; gap: 14px">
      {card("il doit encore passer en séance publique, puis au Sénat. Vote de l'ensemble en première lecture prévu le 17 novembre.", "Ce n'est pas voté :")}
      {card("l'amendement porte sur l'impôt sur le revenu, pas sur le taux de 21,2 %.", "Il ne touche pas les cotisations :", light=True)}
    </div>
    """,
    SRC_PLF, body_gap=30)

slides["S7.dc.html"] = page("Ce que vous pouvez faire", f"8 / {N}",
    f"""
    {title_plain(["Ce que vous pouvez", "faire dès maintenant"])}
    {numbered([
        ("Vérifiez votre déclaration Urssaf :", "la catégorie de vos recettes d'hébergement a changé en 2026. Ce que vous cochez doit correspondre."),
        ("Comparez micro et réel :", "au réel, vous déduisez vos charges réelles (travaux, énergie, amortissement). Au-delà d'un certain niveau de charges, c'est souvent plus avantageux."),
        ("Refaites vos prix 2027 avec le bon taux :", "une nuitée calculée avec 12,3 % de cotisations ne tient plus à 21,2 %."),
    ])}
    """,
    "Un expert-comptable ou l'Urssaf pour trancher votre cas", body_gap=36)

slides["S8.dc.html"] = page("À retenir", f"9 / {N}",
    f"""
    {title_plain(["À retenir"])}
    <div style="display: flex; flex-direction: column; gap: 14px">
      {item("21,2 % de cotisations depuis le 1er janvier 2026, contre 6 % pour un gîte classé", "no")}
      {item("Abattement fiscal ramené de 71 % à 50 % depuis les revenus 2025", "no")}
      {item("Un amendement voté en commission veut rétablir les 71 % : décision en séance, puis au Sénat", "yes")}
    </div>
    {para("Sources : Compta Online, taux micro-social 2026 (maj 14 sept. 2026) · The Connexion, 23 déc. 2025 · Assemblée nationale, réponse à la QE n° 6664, 20 mai 2025 · MySweetimmo, 9 oct. 2026 · Olympe, suivi du PLF 2027.", 22, MUTED)}
    """,
    "Chaque semaine, ce qui change pour les gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {VIOLET}; font-weight: 900">Suivez-nous {icon("arrow")}</span>',
    body_gap=30)

order = list(slides.keys())
titles = ["1 · Couverture", "2 · Ce qui a changé", "3 · 6 % vs 21,2 %", "4 · Qui est concerné", "5 · 21 000 maisons", "6 · Abattement", "7 · Budget 2027", "8 · Que faire", "9 · À retenir"]
write_all(slides, PROJ)
json.dump(canvas_json("Carrousel cotisations chambres d'hôtes", order, titles), open(PROJ + "/canvas.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
render_all(PROJ, order, work_dir("cotisations", "png"))
print("ok", len(order))
