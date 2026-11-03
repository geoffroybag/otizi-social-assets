#!/usr/bin/env python3
"""Carrousel Airbnb — style « Otizi décrypte » : couverture expressive, pages intérieures sobres."""
import html, os, shutil

# Racine du dépôt (ce fichier est dans tools/), police et dossier de travail.
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_DIR = os.path.join(REPO, "tools", "fonts", "figtree", "fonts", "ttf")
WORK = os.path.join(REPO, "work")

def chrome_command():
    """Navigateur headless : variable OTIZI_CHROME, sinon le premier trouvé dans le PATH."""
    env = os.environ.get("OTIZI_CHROME")
    if env:
        return env.split()
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser"):
        found = shutil.which(name)
        if found:
            return [found]
    raise RuntimeError("Aucun navigateur headless : installez google-chrome ou chromium, ou renseignez OTIZI_CHROME.")

def work_dir(slug, kind):
    """Dossier de sortie d'un carrousel : work/carrousel-<slug>/project ou work/png-<slug>."""
    if kind == "project":
        return os.path.join(WORK, f"carrousel-{slug}", "project")
    return os.path.join(WORK, f"png-{slug}")

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


def category_pill(label, kind):
    """kind : actu (violet), conseil (blanc liseré), vie (menthe)."""
    styles = {
        "actu": f"background: {VIOLET}; color: #FFFFFF; border: 2px solid {VIOLET}",
        "conseil": f"background: #FFFFFF; color: {VIOLET}; border: 2px solid {LINE}",
        "vie": f"background: {ACCENT}; color: {INK}; border: 2px solid {ACCENT}",
    }[kind]
    return (f'<div style="display: inline-flex; align-items: center; {styles}; font-size: 26px; font-weight: 900; '
            f'letter-spacing: 0.08em; text-transform: uppercase; padding: 12px 22px; border-radius: 999px">{label}</div>')

def numbered(items, accent_last=False):
    """Liste numérotée en cartes blanches : items = [(titre, texte)]."""
    out = []
    for i, (a, b) in enumerate(items):
        out.append(
            f'<div style="display: flex; gap: 22px; align-items: flex-start; background: #FFFFFF; color: {VIOLET}; border: 2px solid {LINE}; border-radius: 18px; padding: 22px 26px">'
            f'<div style="width: 52px; height: 52px; border-radius: 50%; background: {VIOLET}; color: #FFFFFF; font-size: 26px; font-weight: 900; display: flex; align-items: center; justify-content: center; flex-shrink: 0">{i+1}</div>'
            f'<div style="font-size: 29px; line-height: 1.3; color: {BODY}; padding-top: 6px"><span style="font-weight: 900; color: {VIOLET}">{a}</span> {b}</div></div>')
    return '<div style="display: flex; flex-direction: column; gap: 14px">' + "".join(out) + "</div>"

def stat(value, label, size=150):
    return (f'<div style="display: flex; align-items: flex-end; gap: 24px">'
            f'<div style="font-size: {size}px; line-height: 0.88; font-weight: 900; letter-spacing: -0.04em; color: {VIOLET}">{value}</div>'
            f'<div style="font-size: 30px; line-height: 1.25; font-weight: 700; color: {MUTED}; padding-bottom: 8px; max-width: 520px">{label}</div></div>')

def bar(label, pct, maxpct=70):
    w = int(820 * pct / maxpct)
    return (f'<div style="display: flex; flex-direction: column; gap: 8px">'
            f'<div style="display: flex; justify-content: space-between; font-size: 28px; font-weight: 700; color: {BODY}"><span>{label}</span><span style="color: {VIOLET}; font-weight: 900">{pct} %</span></div>'
            f'<div style="height: 18px; border-radius: 9px; background: #FFFFFF; border: 2px solid {LINE}; overflow: hidden"><div style="width: {w}px; height: 100%; background: {VIOLET}"></div></div></div>')

# ---------- photo de couverture (tools/bin/photo.py) ----------
def photo(slug):
    """Photo choisie pour le carrousel (work/photos/<slug>.json écrit par tools/bin/photo.py get), ou None."""
    import json
    meta = os.path.join(WORK, "photos", f"{slug}.json")
    if not os.path.exists(meta):
        return None
    p = json.load(open(meta, encoding="utf-8"))
    p["path"] = os.path.join(WORK, "photos", f"{slug}.jpg")
    return p if os.path.exists(p["path"]) else None

def photo_credit(p):
    """Ligne de crédit à mettre en fin de légende Instagram et d'article : « Photo : Prénom Nom · Unsplash »."""
    return f"Photo : {p['photographer']} · {p.get('source', 'Unsplash')}" if p else ""

def photo_block(p, height=440, credit=False):
    """Bloc photo de la slide 1 : image en couverture, coins arrondis. Le crédit va dans la légende du post
    (photo_credit), pas sur la slide, sauf credit=True. Rend une chaîne vide sans photo."""
    if not p:
        return ""
    chip = ""
    if credit:
        chip = (f'<div style="position: absolute; right: 16px; bottom: 14px; background: rgba(10,10,10,0.55); color: #FFFFFF; font-size: 20px; font-weight: 700; '
                f'padding: 6px 14px; border-radius: 999px">{html.escape(photo_credit(p))}</div>')
    return (f'<div style="position: relative; width: 100%; height: {height}px; border-radius: 28px; overflow: hidden; flex-shrink: 0; '
            f'background: url(\'file://{p["path"]}\') center / cover no-repeat; border: 2px solid {LINE}" role="img" aria-label="{html.escape(p.get("alt") or "")}">{chip}</div>')

def photo_cover(p, category, kind, text, title="Couverture", counter="", size=58, accent_words=None):
    """Couverture « plein écran » (format HugoDécrypte) : la photo remplit la slide, dégradé sombre en bas,
    wordmark en haut à gauche, pastille de catégorie blanche, texte blanc en gras, flèche en bas à droite.
    text : une à trois phrases (4 à 6 lignes au plus à 58 px). accent_words : mots mis en menthe (ex. ["21,2 %"])."""
    if not p:
        raise ValueError("photo_cover demande une photo (tools/bin/photo.py get <slug> <id>)")
    body = html.escape(text)
    for w in accent_words or []:
        body = body.replace(html.escape(w), f'<span style="color: {ACCENT}">{html.escape(w)}</span>')
    pill_fg = {"actu": VIOLET, "conseil": VIOLET, "vie": INK}[kind]
    dot = {"actu": VIOLET, "conseil": "#FFFFFF", "vie": ACCENT}[kind]
    pill = (f'<div style="display: inline-flex; align-items: center; gap: 12px; background: #FFFFFF; color: {pill_fg}; font-size: 28px; font-weight: 900; '
            f'letter-spacing: 0.06em; text-transform: uppercase; padding: 12px 24px; border-radius: 16px; align-self: flex-start">'
            f'<span style="width: 18px; height: 18px; border-radius: 50%; background: {dot}; border: 3px solid {VIOLET}; display: inline-block"></span>{html.escape(category)}</div>')
    cnt = f'<div style="background: rgba(10,10,10,0.6); color: #FFFFFF; font-size: 28px; font-weight: 700; padding: 10px 20px; border-radius: 999px">{counter}</div>' if counter else ""
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
<style>body{{margin:0}}</style>
</helmet>
<div style="width: 1080px; height: 1350px; box-sizing: border-box; position: relative; overflow: hidden; font-family: 'Figtree', Arial, sans-serif; background: #0a0a0a url('file://{p["path"]}') center / cover no-repeat" role="img" aria-label="{html.escape(p.get("alt") or "")}">
  <div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(10,10,20,0.30) 0%, rgba(10,10,20,0) 18%, rgba(10,10,20,0) 36%, rgba(10,10,20,0.45) 50%, rgba(10,10,20,0.80) 62%, rgba(10,10,20,0.93) 75%, rgba(10,10,20,0.97) 100%)"></div>
  <div style="position: absolute; top: 56px; left: 64px; right: 64px; display: flex; justify-content: space-between; align-items: center">
    <div style="display: flex; align-items: center; gap: 12px"><div style="font-size: 44px; font-weight: 900; letter-spacing: -0.02em; color: #FFFFFF; line-height: 1">Otizi</div>
      <div style="background: {ACCENT}; color: {INK}; font-size: 32px; font-weight: 900; line-height: 1; padding: 8px 16px 11px; border-radius: 14px">décrypte</div></div>
    {cnt}
  </div>
  <div style="position: absolute; left: 64px; right: 64px; bottom: 64px; display: flex; flex-direction: column; gap: 30px">
    {pill}
    <p style="margin: 0; font-size: {size}px; line-height: 1.22; font-weight: 800; color: #FFFFFF; letter-spacing: -0.01em; padding-right: 40px">{body}</p>
  </div>
  <div style="position: absolute; right: 40px; bottom: 40px; width: 64px; height: 64px; border-radius: 16px; background: #FFFFFF; color: {INK}; display: flex; align-items: center; justify-content: center">{icon("arrow", 34)}</div>
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

def write_all(slides, outdir):
    os.makedirs(outdir, exist_ok=True)
    for name, src in slides.items():
        with open(os.path.join(outdir, name), "w", encoding="utf-8") as fh:
            fh.write(src)

def render_all(project_dir, order, png_dir, prefix="slide"):
    import re, subprocess
    fontdir = FONT_DIR
    fontcss = "".join(f"@font-face{{font-family:'Figtree';src:url('file://{fontdir}/Figtree-{n}.ttf');font-weight:{w}}}" for n, w in [("Medium",500),("Bold",700),("Black",900)])
    os.makedirs(png_dir, exist_ok=True)
    tmp = os.path.join(png_dir, "_html"); os.makedirs(tmp, exist_ok=True)
    for i, n in enumerate(order, 1):
        h = open(os.path.join(project_dir, n), encoding="utf-8").read()
        body = re.search(r"<x-dc>(.*?)</x-dc>", h, re.S).group(1)
        body = re.sub(r"<helmet>.*?</helmet>", "", body, flags=re.S).replace("{{ground}}", "#EDF4FE").replace("{{accent}}", "#00e2ae")
        hp = os.path.join(tmp, f"{i:02d}.html")
        open(hp, "w", encoding="utf-8").write(f"<!doctype html><html lang='fr'><head><meta charset='utf-8'><style>{fontcss}html,body{{margin:0;background:#EDF4FE}}</style></head><body>{body}</body></html>")
        out = f"{png_dir}/{prefix}-{i:02d}.png"
        # Fenêtre plus haute que la slide : selon le navigateur, --window-size inclut la barre de la fenêtre
        # (Chromium Playwright : ~90 px perdus en bas), puis recadrage exact à 1080×1350.
        subprocess.run([*chrome_command(),"--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars","--window-size=1080,1500",f"--screenshot={out}",f"file://{hp}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        from PIL import Image
        im = Image.open(out)
        if im.size != (1080, 1350):
            im.crop((0, 0, 1080, 1350)).save(out, optimize=True)

def canvas_json(title, order, titles):
    boards = {}
    for i, n in enumerate(order):
        boards[n] = {"x": (i % 5) * 1160, "y": (i // 5) * 1470, "w": 1080, "h": 1350, "title": titles[i]}
    return {"v": 3, "createdOnFiles": {"v": 1, "at": "2026-11-03T13:30:00Z"}, "title": title, "launch": {"view": "canvas"}, "pages": [],
            "boards": boards, "order": order, "notes": {}, "designSystems": []}
