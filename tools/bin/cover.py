#!/usr/bin/env python3
"""Image de couverture d'article de blog (1600×900, WebP) à partir de la couverture d'un carrousel.

Usage : python3 tools/bin/cover.py <slug> <sortie.webp>
Reprend le titre de la slide 1 (work/carrousel-<slug>/project/Main.dc.html) : les lignes
colorées et leur éclat, sans le paragraphe ni le wordmark (demande de Geoffroy, 13 novembre
2026 : « le titre seulement »), centrées sur un fond 16:9, rendues avec le même Chrome que
les slides, et enregistrées en WebP.
"""
import os, re, subprocess, sys
from PIL import Image

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from carrousel_lib import FONT_DIR, WORK, chrome_command  # noqa: E402

WIDTH, HEIGHT = 1600, 900
SCALE = 1.35  # le titre est composé pour une slide de 1080 px de large ; agrandi pour remplir la couverture
GROUND, ACCENT = "#EDF4FE", "#00e2ae"

def title_block(slide_html):
    """Le bloc des lignes du titre de la slide 1, tel quel (fond, rotation, éclat), sans le paragraphe qui suit."""
    body = re.search(r"<x-dc>(.*?)</x-dc>", slide_html, re.S).group(1)
    m = re.search(r'(<div style="position: relative; display: flex; flex-direction: column; gap: 2px; padding-right: 120px">.*?</div>)\s*<div><p style="margin: 0; font-size: \d+px', body, re.S)
    if not m:
        raise SystemExit("titre introuvable dans la slide 1 : le gabarit de couverture a changé, adapter cover.py")
    return m.group(1).replace("{{ground}}", GROUND).replace("{{accent}}", ACCENT)

def cover(slug, out):
    project = os.path.join(WORK, f"carrousel-{slug}", "project")
    src = os.path.join(project, "Main.dc.html")
    if not os.path.exists(src):
        raise SystemExit(f"couverture introuvable : {src} (lancer d'abord tools/post_{slug}.py)")
    fontcss = "".join(f"@font-face{{font-family:'Figtree';src:url('file://{FONT_DIR}/Figtree-{n}.ttf');font-weight:{w}}}" for n, w in [("Medium", 500), ("Bold", 700), ("Black", 900)])
    title = title_block(open(src, encoding="utf-8").read())
    tmp_dir = os.path.join(WORK, f"png-{slug}", "_html")
    os.makedirs(tmp_dir, exist_ok=True)
    hp = os.path.join(tmp_dir, "cover-2x.html")
    open(hp, "w", encoding="utf-8").write(
        f"<!doctype html><html lang='fr'><head><meta charset='utf-8'><style>{fontcss}html,body{{margin:0;background:{GROUND}}}</style></head><body>"
        f"<div style='width:{WIDTH}px;height:{HEIGHT}px;box-sizing:border-box;background:{GROUND};color:#2B2F45;font-family:Figtree,Arial,sans-serif;display:flex;align-items:center;justify-content:center;overflow:hidden'>"
        f"<div style='transform:scale({SCALE});transform-origin:center'>{title}</div></div></body></html>")
    png = os.path.join(tmp_dir, "cover-2x.png")
    subprocess.run([*chrome_command(), "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=2",
                    f"--window-size={WIDTH},{HEIGHT}", f"--screenshot={png}", f"file://{hp}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    im = Image.open(png).convert("RGB").resize((WIDTH, HEIGHT), Image.LANCZOS)
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    im.save(out, "WEBP", quality=85, method=6)
    return out

if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    print(cover(sys.argv[1], sys.argv[2]))
