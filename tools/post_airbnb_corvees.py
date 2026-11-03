#!/usr/bin/env python3
"""Carrousel Airbnb — style « Otizi décrypte » : couverture expressive, pages intérieures sobres."""
import html, os

OUT = "/tmp/claude-0/-home-claude/fc645d01-7205-5ab5-8091-97d967632241/scratchpad/carrousel-airbnb/project"
GROUND, ACCENT = "{{ground}}", "{{accent}}"
VIOLET = "#472ed8"
CARD = VIOLET            # carte d'accent : violet, texte blanc
LINE = "#D3DCF0"         # bordures sur fond clair
MUTED = "#6B7090"
BODY = "#2B2F45"
INK = "#0a0a0a"

SPARKS = ('<svg style="position:absolute; top: -70px; right: 10px" width="110" height="92" viewBox="0 0 130 110" fill="none" '
          'stroke="#00e2ae" stroke-width="14" stroke-linecap="round" aria-hidden="true">'
          '<path d="M22 62 L40 30"></path><path d="M58 50 L76 18"></path><path d="M86 70 L120 52"></path></svg>')

def icon(name, size=30):
    s = f'width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"'
    paths = {
        "x": '<path d="M6 6l12 12"></path><path d="M18 6L6 18"></path>',
        "check": '<path d="M5 12.5l4.5 4.5L19 7"></path>',
        "arrow": '<path d="M5 12h14"></path><path d="M13 6l6 6-6 6"></path>',
        "cal": '<rect x="3" y="5" width="18" height="16" rx="3"></rect><path d="M3 10h18"></path><path d="M8 3v4"></path><path d="M16 3v4"></path>',
        "scale": '<path d="M12 3v18"></path><path d="M5 7h14"></path><path d="M3 15l2.5-8 2.5 8"></path><path d="M3 15a2.5 2.5 0 0 0 5 0"></path><path d="M16 15l2.5-8 2.5 8"></path><path d="M16 15a2.5 2.5 0 0 0 5 0"></path><path d="M8 21h8"></path>',
    }
    return f"<svg {s}>{paths[name]}</svg>"

# ---------- couverture : blocs inclinés ----------
def box(text, kind, rot, size, indent):
    bg, fg = (VIOLET, "#FFFFFF") if kind == "white" else (ACCENT, INK)
    return (f'<div style="display: inline-block; align-self: flex-start; background: {bg}; color: {fg}; font-size: {size}px; '
            f'font-weight: 900; line-height: 1.02; letter-spacing: -0.02em; text-transform: uppercase; padding: 8px 30px 12px; '
            f'border-radius: 20px; transform: rotate({rot}deg); margin-left: {indent}px; white-space: nowrap">{text}</div>')

def title_boxes(parts):
    rots, inds = [-2.2, 1.4, -1.2], [0, 26, 10]
    inner = "".join(box(t, k, rots[i % 3], s, inds[i % 3]) for i, (t, k, s) in enumerate(parts))
    return f'<div style="position: relative; display: flex; flex-direction: column; gap: 2px; padding-right: 120px">{inner}{SPARKS}</div>'

# ---------- pages intérieures : titre droit ----------
def title_plain(lines, size=78):
    return (f'<div><h2 style="margin: 0; font-size: {size}px; line-height: 1.04; font-weight: 900; letter-spacing: -0.02em; color: {VIOLET}">'
            + "<br>".join(lines) + "</h2>"
            f'<div style="width: 140px; height: 10px; border-radius: 5px; background: {ACCENT}; margin-top: 26px"></div></div>')

def header(counter):
    return (
        '<div style="display: flex; justify-content: space-between; align-items: center">'
        '<div style="display: flex; align-items: center; gap: 16px">'
        '<div style="font-size: 56px; font-weight: 900; letter-spacing: -0.02em; color: {VIOLET}; line-height: 1">Otizi</div>'
        f'<div style="background: {ACCENT}; color: {INK}; font-size: 42px; font-weight: 900; line-height: 1; padding: 10px 22px 14px; border-radius: 20px">décrypte</div>'
        '</div>'
        f'<div style="font-size: 28px; font-weight: 700; color: {MUTED}">{counter}</div>'
        '</div>'
    )

def blob(size=640, right=-300, bottom=-400):
    return f'<div style="position: absolute; right: {right}px; bottom: {bottom}px; width: {size}px; height: {size}px; border-radius: 50%; background: {ACCENT}" aria-hidden="true"></div>'

def footer(left, right=""):
    r = f'<div style="font-size: 24px; font-weight: 700; color: {MUTED}; text-align: right">{right}</div>' if right else ""
    return (f'<div style="display: flex; justify-content: space-between; align-items: flex-end; position: relative">'
            f'<div style="font-size: 24px; font-weight: 700; color: {MUTED}">{left}</div>{r}</div>')

def page(title, counter, middle, foot_left, foot_right="", body_gap=40, cover=False):
    b = blob() if cover else ""
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>{html.escape(title)}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@500;700;900&amp;display=swap">
<style>
body{{margin:0}}
a{{color:#00e2ae}}a:hover{{color:#FFFFFF}}
</style>
</helmet>
<div style="width: 1080px; height: 1350px; box-sizing: border-box; padding: 64px 80px 56px; background: {GROUND}; color: {BODY}; font-family: 'Figtree', Arial, sans-serif; display: flex; flex-direction: column; justify-content: space-between; position: relative; overflow: hidden">
  {b}
  {header(counter)}
  <div style="display: flex; flex-direction: column; gap: {body_gap}px; position: relative">
{middle}
  </div>
  {footer(foot_left, foot_right)}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"ground":{{"editor":"color","default":"#EDF4FE","section":"Charte"}},"accent":{{"editor":"color","default":"#00e2ae","section":"Charte"}},"$preview":{{"width":1080,"height":1350}}}}'>
class Component extends DCLogic {{
  renderVals() {{
    return {{ ground: this.props.ground ?? '#EDF4FE', accent: this.props.accent ?? '#00e2ae' }};
  }}
}}
</script>
</body>
</html>
"""

def para(text, size=34, color=BODY, weight=500, maxw=None):
    mw = f" max-width: {maxw}px;" if maxw else ""
    return f'<p style="margin: 0; font-size: {size}px; line-height: 1.32; font-weight: {weight}; color: {color};{mw}">{text}</p>'

def item(text, kind):
    """Carte blanche, texte violet ; pastille d'icône : violet pour « non », menthe pour « oui »."""
    if kind == "no":
        dot_bg, dot_fg, ic = VIOLET, "#FFFFFF", icon("x")
    else:
        dot_bg, dot_fg, ic = ACCENT, INK, icon("check")
    return (f'<div style="display: flex; align-items: center; gap: 22px; background: #FFFFFF; color: {VIOLET}; border: 2px solid {LINE}; border-radius: 18px; padding: 20px 26px">'
            f'<div style="width: 44px; height: 44px; border-radius: 50%; background: {dot_bg}; color: {dot_fg}; display: flex; align-items: center; justify-content: center; flex-shrink: 0">{ic}</div>'
            f'<div style="font-size: 33px; font-weight: 900; line-height: 1.15">{text}</div></div>')

def card(text, strong=None, light=False):
    """Carte sombre par défaut ; light=True : carte blanche pour mettre en avant."""
    bg, fg, sub, bd = (CARD, "#FFFFFF", "#ECE9FC", CARD) if light else ("#FFFFFF", VIOLET, BODY, LINE)
    s = f'<span style="font-weight: 900; color: {fg}">{strong}</span> ' if strong else ""
    return (f'<div style="background: {bg}; border: 2px solid {bd}; border-radius: 18px; padding: 24px 28px; font-size: 30px; line-height: 1.3; font-weight: 500; color: {sub}">'
            f'{s}{text}</div>')

slides = {}

# 1 — Couverture (seule page avec les blocs inclinés, les éclats et la courbe)
slides["Main.dc.html"] = page("Couverture", "20 oct. 2026",
    f"""
    {title_boxes([("Airbnb interdit", "white", 86), ("les corvées", "mint", 104), ("de départ", "white", 90)])}
    <div>{para("Vaisselle, draps, machine à laver : ce que vous ne pourrez plus demander à vos voyageurs à partir du 20 novembre.", 38, BODY, maxw=860)}
      <div style="width: 260px; height: 10px; border-radius: 5px; background: {ACCENT}; margin-top: 18px"></div></div>
    <div style="display: flex; gap: 14px; flex-wrap: wrap">
      <div style="display: flex; align-items: center; gap: 12px; font-size: 28px; font-weight: 700; color: {VIOLET}; background: #FFFFFF; border: 2px solid {LINE}; border-radius: 999px; padding: 12px 24px">{icon("cal")} Plateformes</div>
      <div style="display: flex; align-items: center; gap: 12px; font-size: 28px; font-weight: 700; color: {VIOLET}; background: #FFFFFF; border: 2px solid {LINE}; border-radius: 999px; padding: 12px 24px">{icon("scale")} Réglementation</div>
    </div>
    """,
    "L'actu des gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {INK}; font-weight: 900">Glisser {icon("arrow")}</span>',
    body_gap=44, cover=True)

# 2 — L'annonce
slides["S1.dc.html"] = page("L'annonce", "2 / 9",
    f"""
    {title_plain(["Airbnb change", "ses règles"])}
    {para("Le 20 octobre, Airbnb a prévenu ses hôtes par e-mail. Les demandes de ménage au départ deviennent interdites. La règle s'applique dans le monde entier, France comprise.", 36)}
    <div style="display: flex; align-items: flex-end; gap: 28px">
      <div style="font-size: 170px; line-height: 0.88; font-weight: 900; letter-spacing: -0.04em; color: {VIOLET}">20 nov.</div>
      <div style="font-size: 32px; line-height: 1.2; font-weight: 700; color: {MUTED}; padding-bottom: 10px">2026<br>entrée en vigueur</div>
    </div>
    """,
    "Source : Airbnb, annonce aux hôtes")

# 3 — Interdit
slides["S2.dc.html"] = page("Ce que vous ne pouvez plus exiger", "3 / 9",
    f"""
    {title_plain(["Ce que vous ne", "pouvez plus exiger"], 72)}
    <div style="display: flex; flex-direction: column; gap: 16px">
      {item("Laver et ranger la vaisselle", "no")}
      {item("Retirer les draps des lits", "no")}
      {item("Lancer une machine à laver", "no")}
      {item("Sortir les poubelles hors du logement", "no")}
      {item("Interdire la clim pendant le séjour", "no")}
    </div>
    """,
    "Pour toute réservation faite dès le 20 nov.", body_gap=40)

# 4 — Encore possible
slides["S3.dc.html"] = page("Ce que vous pouvez encore demander", "4 / 9",
    f"""
    {title_plain(["Ce que vous pouvez", "encore demander"], 72)}
    <div style="display: flex; flex-direction: column; gap: 14px">
      {item("Vaisselle sale dans l'évier", "yes")}
      {item("Serviettes utilisées regroupées", "yes")}
      {item("Déchets triés dans les bacs du logement", "yes")}
      {item("Clim éteinte en partant", "yes")}
      {item("Porte fermée à clé", "yes")}
    </div>
    {para("Ce sont des « demandes », pas des règles : un voyageur qui ne les suit pas ne peut pas être sanctionné.", 28, MUTED)}
    """,
    "Exceptions locales possibles", body_gap=32)

# 5 — Argent
slides["S4.dc.html"] = page("Plus de pénalité", "5 / 9",
    f"""
    {title_plain(["Fini les pénalités", "pour une tâche non faite"], 70)}
    <div style="display: flex; align-items: flex-end; gap: 24px">
      <div style="font-size: 190px; line-height: 0.85; font-weight: 900; letter-spacing: -0.05em; color: {VIOLET}">0 €</div>
      <div style="font-size: 30px; line-height: 1.25; font-weight: 700; color: {MUTED}; padding-bottom: 8px; max-width: 560px">de supplément possible si la vaisselle n'est pas faite ou les draps pas retirés</div>
    </div>
    <div style="display: flex; flex-direction: column; gap: 14px">
      {card("Ils doivent couvrir le travail réel, pas celui que faisait le voyageur.", "Les frais de ménage restent autorisés.")}
      {card("photos, vidéos et factures à l'appui, via le centre de résolution.", "Les dégâts réels passent par AirCover,")}
      {card("tout ce qui est facturé doit apparaître avant la réservation.", "Frais cachés interdits :", light=True)}
    </div>
    """,
    "Cautions : très encadrées, hors plateforme", body_gap=32)

# 6 — Les 7 règles
chips = "".join(
    f'<div style="background: {CARD if new else "#FFFFFF"}; color: {"#FFFFFF" if new else VIOLET}; border: 2px solid {CARD if new else LINE}; border-radius: 16px; padding: 18px 22px; display: flex; flex-direction: column; gap: 6px; justify-content: center">'
    + (f'<div style="font-size: 18px; font-weight: 900; letter-spacing: 0.1em; color: {ACCENT}">NOUVEAU</div>' if new else "")
    + f'<div style="font-size: 29px; font-weight: 900; line-height: 1.15">{t}</div></div>'
    for t, new in [("Nombre max de dormeurs", True), ("Fermer à clé au départ", True), ("Heures calmes", False), ("Fêtes et événements", False), ("Animaux", False), ("Fumer et vapoter", False), ("Photos et tournages", False)]
)
slides["S5.dc.html"] = page("Les règles standard", "6 / 9",
    f"""
    {title_plain(["7 règles de la maison,", "pas une de plus"], 70)}
    {para("Les règles qu'un voyageur doit respecter se cochent dans une liste fermée. Le reste devient une simple « demande ».", 30, MUTED)}
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px">
      {chips}
      {card("Contrats séparés et copie de pièce d'identité : interdits par défaut, sauf obligation légale, copropriété ou séjour de 28 nuits et plus.", light=True)}
    </div>
    """,
    "Source : Airbnb, annonce aux hôtes", body_gap=30)

# 7 — Calendrier
slides["S6.dc.html"] = page("Qui est concerné, et quand", "7 / 9",
    f"""
    {title_plain(["C'est la date de", "réservation qui compte"], 70)}
    {para("Les nouvelles règles s'appliquent aux réservations effectuées à partir du 20 novembre 2026, pas aux séjours. Une réservation déjà prise garde les règles affichées au moment de la réservation.", 31)}
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px">
      <div style="background: #FFFFFF; color: {VIOLET}; border: 2px solid {LINE}; border-radius: 18px; padding: 26px; display: flex; flex-direction: column; gap: 10px">
        <div style="display: flex; align-items: center; gap: 10px; font-size: 20px; font-weight: 900; letter-spacing: 0.1em; color: {MUTED}">{icon("cal", 24)} RÉSERVÉ LE 25 OCT.</div>
        <div style="font-size: 36px; font-weight: 900; line-height: 1.05">Anciennes règles</div>
      </div>
      <div style="background: {CARD}; color: #FFFFFF; border-radius: 18px; padding: 26px; display: flex; flex-direction: column; gap: 10px">
        <div style="display: flex; align-items: center; gap: 10px; font-size: 20px; font-weight: 900; letter-spacing: 0.1em; color: {ACCENT}">{icon("cal", 24)} RÉSERVÉ LE 25 NOV.</div>
        <div style="font-size: 36px; font-weight: 900; line-height: 1.05">Nouvelles règles</div>
      </div>
    </div>
    {card("restrictions d'eau en période de sécheresse, bacs anti-animaux… Airbnb n'a pas encore détaillé comment il les tranchera.", "Des exceptions locales existent :")}
    """,
    "Même texte, même date, partout dans le monde", body_gap=30)

# 8 — Sanctions
steps = [("L'éditeur d'annonce signale", "le texte qui semble enfreindre la règle."),
         ("Airbnb examine", "et contacte l'hôte par e-mail."),
         ("L'hôte peut faire appel.", ""),
         ("Un bandeau apparaît pour les voyageurs :", "« inclut des demandes de ménage »."),
         ("Visibilité réduite dans les recherches,", "puis avertissement sur l'annonce et autres mesures prévues par les conditions d'utilisation.")]
steps_html = "".join(
    f'<div style="display: flex; gap: 22px; align-items: flex-start; padding: 18px 0; border-bottom: 2px solid {LINE}">'
    f'<div style="width: 56px; height: 56px; border-radius: 50%; background: {CARD}; color: #FFFFFF; font-size: 28px; font-weight: 900; display: flex; align-items: center; justify-content: center; flex-shrink: 0">{i+1}</div>'
    f'<div style="font-size: 30px; line-height: 1.3; padding-top: 8px"><span style="font-weight: 900; color: {VIOLET}">{a}</span> <span style="color: {BODY}">{b}</span></div></div>'
    for i, (a, b) in enumerate(steps))
slides["S7.dc.html"] = page("Et si vous ne jouez pas le jeu", "8 / 9",
    f"""
    {title_plain(["Et si vous ne", "jouez pas le jeu ?"], 74)}
    <div style="display: flex; flex-direction: column">{steps_html}</div>
    """,
    "Source : Airbnb, annonce aux hôtes", body_gap=32)

# 9 — À retenir
todo = [("Relisez votre check-list de départ", "avant le 20 novembre : tout ce qui est « obligatoire » doit devenir une demande."),
        ("Vérifiez vos frais de ménage :", "ils doivent couvrir le travail que vous récupérez, sans les gonfler."),
        ("Booking et vos réservations en direct", "ne sont pas concernés : là, ce sont vos conditions qui s'appliquent.")]
todo_html = "".join(
    f'<div style="display: flex; gap: 20px; align-items: flex-start; background: #FFFFFF; color: {VIOLET}; border: 2px solid {LINE}; border-radius: 18px; padding: 24px 26px">'
    f'<div style="font-size: 40px; font-weight: 900; line-height: 1; flex-shrink: 0">{i+1}</div>'
    f'<div style="font-size: 30px; line-height: 1.3; color: {BODY}"><span style="font-weight: 900; color: {VIOLET}">{a}</span> {b}</div></div>'
    for i, (a, b) in enumerate(todo))
slides["S8.dc.html"] = page("Ce qui change pour vous", "9 / 9",
    f"""
    {title_plain(["Ce qui change", "pour vous"], 80)}
    <div style="display: flex; flex-direction: column; gap: 14px">{todo_html}</div>
    {para("Sources : Airbnb, annonce aux hôtes et centre de ressources (20 oct. 2026) · Rental Scale-Up (21 oct. 2026) · cacomptepourmoi.fr (2 nov. 2026)", 22, MUTED)}
    """,
    "Chaque semaine, ce qui change pour les gîtes et chambres d'hôtes",
    f'<span style="display: inline-flex; align-items: center; gap: 10px; color: {VIOLET}; font-weight: 900">Suivez-nous {icon("arrow")}</span>',
    body_gap=30)

for name, src in slides.items():
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as fh:
        fh.write(src)
    print("écrit", name)
