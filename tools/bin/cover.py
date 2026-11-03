#!/usr/bin/env python3
"""Image de couverture d'article de blog (1600×900, WebP) à partir de la couverture d'un carrousel.

Usage : python3 tools/bin/cover.py <slug> <sortie.webp>
Rend la slide 1 (work/carrousel-<slug>/project/Main.dc.html) à l'échelle 2 avec le même
Chrome que les slides, découpe une bande 16:9 autour du titre, et enregistre en WebP.
"""
import os, re, subprocess, sys
from PIL import Image

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from carrousel_lib import FONT_DIR, WORK, chrome_command  # noqa: E402

# Bande gardée dans la slide (hauteur 1350) : sous le wordmark, titre et sous-titre, avant la courbe du bas.
BAND_TOP, BAND_HEIGHT = 230, 608  # 1080×608 = 16:9

def cover(slug, out):
    project = os.path.join(WORK, f"carrousel-{slug}", "project")
    src = os.path.join(project, "Main.dc.html")
    if not os.path.exists(src):
        raise SystemExit(f"couverture introuvable : {src} (lancer d'abord tools/post_{slug}.py)")
    fontcss = "".join(f"@font-face{{font-family:'Figtree';src:url('file://{FONT_DIR}/Figtree-{n}.ttf');font-weight:{w}}}" for n, w in [("Medium", 500), ("Bold", 700), ("Black", 900)])
    html = open(src, encoding="utf-8").read()
    body = re.search(r"<x-dc>(.*?)</x-dc>", html, re.S).group(1)
    body = re.sub(r"<helmet>.*?</helmet>", "", body, flags=re.S).replace("{{ground}}", "#EDF4FE").replace("{{accent}}", "#00e2ae")
    tmp_dir = os.path.join(WORK, f"png-{slug}", "_html")
    os.makedirs(tmp_dir, exist_ok=True)
    hp = os.path.join(tmp_dir, "cover-2x.html")
    open(hp, "w", encoding="utf-8").write(f"<!doctype html><html lang='fr'><head><meta charset='utf-8'><style>{fontcss}html,body{{margin:0;background:#EDF4FE}}</style></head><body>{body}</body></html>")
    png = os.path.join(tmp_dir, "cover-2x.png")
    subprocess.run([*chrome_command(), "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=2",
                    "--window-size=1080,1500", f"--screenshot={png}", f"file://{hp}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    im = Image.open(png).convert("RGB")
    scale = im.size[0] / 1080
    band = im.crop((0, int(BAND_TOP * scale), im.size[0], int((BAND_TOP + BAND_HEIGHT) * scale)))
    band = band.resize((1600, 900), Image.LANCZOS)
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    band.save(out, "WEBP", quality=85, method=6)
    return out

if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    print(cover(sys.argv[1], sys.argv[2]))
