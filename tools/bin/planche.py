#!/usr/bin/env python3
"""Planche de contrôle d'un carrousel : toutes les slides réduites sur une image.

Usage : python3 tools/bin/planche.py <slug> [<sortie.png>]
Lit work/png-<slug>/slide-NN.png, écrit work/planches/<slug>.png (3 colonnes).
"""
import os, sys, glob
from PIL import Image

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def planche(slug, out=None, cols=3, width=360):
    pngs = sorted(glob.glob(os.path.join(REPO, "work", f"png-{slug}", "slide-*.png")))
    if not pngs:
        raise SystemExit(f"aucune slide dans work/png-{slug}/")
    height = int(width * 1350 / 1080)
    rows = (len(pngs) + cols - 1) // cols
    gap = 16
    sheet = Image.new("RGB", (cols * width + (cols + 1) * gap, rows * height + (rows + 1) * gap), "#FFFFFF")
    for i, p in enumerate(pngs):
        im = Image.open(p).convert("RGB").resize((width, height), Image.LANCZOS)
        x = gap + (i % cols) * (width + gap)
        y = gap + (i // cols) * (height + gap)
        sheet.paste(im, (x, y))
    out = out or os.path.join(REPO, "work", "planches", f"{slug}.png")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    sheet.save(out, optimize=True)
    return out, len(pngs)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    out, n = planche(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
    print(f"{out} ({n} slides)")
