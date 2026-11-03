#!/usr/bin/env python3
"""Vérifie un article de blog avant la PR sur vr-admin-website.

Usage : python3 tools/bin/article-check.py <chemin/content/articles/slug.md>
Contrôle le front matter (title, description, seoTitle, createdAt, updatedAt, image, author.name, tags),
l'existence de l'image dans static/, la longueur (600 à 1 200 mots), les sections attendues, et que
le slug n'existe pas déjà en ligne.
"""
import os, re, sys, urllib.request

TAGS = {"gestion", "revenus", "marketing", "réglementation", "saison", "fiscalité", "site-internet", "livret-accueil", "création", "référencement", "channel-manager", "chambres d'hôtes", "actualité"}

def fail(msg):
    print(f"KO : {msg}")
    sys.exit(1)

def main(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        fail("front matter absent")
    fm, body = m.group(1), m.group(2)
    for key in ("title", "description", "seoTitle", "createdAt", "updatedAt", "image", "tags"):
        if not re.search(rf"^{key}:", fm, re.M):
            fail(f"champ `{key}` absent du front matter")
    if "name:" not in fm:
        fail("author.name absent")
    for key in ("createdAt", "updatedAt"):
        if not re.search(rf"^{key}: '\d{{4}}-\d{{2}}-\d{{2}}'$", fm, re.M):
            fail(f"`{key}` doit être 'AAAA-MM-JJ' entre apostrophes")
    seo = re.search(r"^seoTitle: \"(.*)\"$", fm, re.M)
    if seo and len(seo.group(1)) > 65:
        fail(f"seoTitle trop long ({len(seo.group(1))} caractères, 65 au plus)")
    desc = re.search(r"^description: \"(.*)\"$", fm, re.M)
    if desc and not 80 <= len(desc.group(1)) <= 170:
        fail(f"description : {len(desc.group(1))} caractères, viser 80 à 170")
    tags = re.findall(r"^  - (.+)$", fm, re.M)
    unknown = [t for t in tags if t not in TAGS]
    if not tags or unknown:
        fail(f"tags : {tags} (inconnus : {unknown}) ; tags connus : {sorted(TAGS)}")
    image = re.search(r"^image: (\S+)$", fm, re.M).group(1)
    repo = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(path))))
    if not image.startswith("http") and not os.path.exists(os.path.join(repo, "static", image.lstrip("/"))):
        fail(f"image introuvable : static{image}")
    words = len(body.split())
    if not 600 <= words <= 1200:
        fail(f"{words} mots : viser 600 à 1 200")
    if body.count("\n## ") < 3:
        fail("moins de trois sections `## `")
    if "## Questions fréquentes" not in body:
        fail("section « ## Questions fréquentes » absente")
    if "Article à visée d'information" not in body:
        fail("ligne finale « _Article à visée d'information. Références : …_ » absente")
    slug = os.path.splitext(os.path.basename(path))[0]
    photos = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "work", "photos")
    meta = os.path.join(photos, f"{slug}.json")
    if os.path.exists(meta):
        import json
        bank = json.load(open(meta, encoding="utf-8")).get("source", "Unsplash")
        if bank not in body:
            fail(f"photo {bank} choisie pour {slug} mais crédit absent de la ligne finale (« Photo de couverture : [Nom](lien) sur {bank} »)")
    try:
        with urllib.request.urlopen(f"https://otizi.fr/blog/{slug}", timeout=10) as r:
            if r.status == 200 and "nuxt-content" in r.read().decode("utf-8", "ignore"):
                fail(f"le slug {slug} existe déjà sur otizi.fr/blog")
    except Exception:
        pass
    print(f"OK : {slug}, {words} mots, tags {tags}, image {image}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    main(sys.argv[1])
