#!/usr/bin/env python3
"""Image de couverture d'article de blog (1600×900, WebP).

Usage : python3 tools/bin/cover.py <slug> <sortie.webp>
Si une photo a été choisie pour le carrousel (tools/bin/photo.py get <slug> …, fichier
work/photos/<slug>.jpg), la couverture est cette photo recadrée en 16:9. Sinon, rend la slide 1
(work/carrousel-<slug>/project/Main.dc.html) à l'échelle 2 et découpe une bande 16:9 autour du titre.
"""
import os, re, subprocess, sys
from PIL import Image

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from carrousel_lib import FONT_DIR, WORK, chrome_command, photo  # noqa: E402

# Bande gardée dans la slide (hauteur 1350) : sous le wordmark, titre et sous-titre, avant la courbe du bas.
BAND_TOP, BAND_HEIGHT = 230, 608  # 1080×608 = 16:9

def save_webp(im, out):
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    im.save(out, "WEBP", quality=85, method=6)
    return out

def cover_from_photo(p, out):
    """Recadrage centré de la photo en 16:9, puis 1600×900."""
    im = Image.open(p["path"]).convert("RGB")
    w, h = im.size
    if w / h > 16 / 9:
        nw = int(h * 16 / 9); box = ((w - nw) // 2, 0, (w - nw) // 2 + nw, h)
    else:
        nh = int(w * 9 / 16); box = (0, (h - nh) // 2, w, (h - nh) // 2 + nh)
    return save_webp(im.crop(box).resize((1600, 900), Image.LANCZOS), out)

def cover(slug, out):
    p = photo(slug)
    if p:
        return cover_from_photo(p, out)
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
    return save_webp(band.resize((1600, 900), Image.LANCZOS), out)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    print(cover(sys.argv[1], sys.argv[2]))
