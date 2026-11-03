#!/usr/bin/env python3
"""Photo libre de droits (Unsplash, Pexels ou Pixabay) pour la couverture d'un carrousel et de son article.

Usage :
  python3 tools/bin/photo.py search "<requête>" [--n 8]
      Cherche (paysage, requête en anglais de préférence), liste les candidates (numéro, id, photographe,
      description) et enregistre un aperçu de chacune dans work/photos/candidats/<id>.jpg : regarde-les
      (outil Read) et choisis la plus pertinente. Une photo déjà utilisée pour un autre carrousel est écartée.
  python3 tools/bin/photo.py get <slug> <id>
      Télécharge la photo choisie en grand format dans work/photos/<slug>.jpg et ses crédits dans
      work/photos/<slug>.json (photographe, lien). C'est ce fichier que lisent carrousel_lib.photo()
      pour la slide 1 et tools/bin/cover.py pour la couverture de l'article.

Banque d'images : la première dont la clé existe, dans cet ordre : Unsplash (~/.config/otizi-social/unsplash.key
ou UNSPLASH_ACCESS_KEY), Pexels (pexels.key ou PEXELS_API_KEY), Pixabay (pixabay.key ou PIXABAY_API_KEY).
Variable PHOTO_SOURCE=unsplash|pexels|pixabay pour forcer. La clé n'est jamais affichée.
Crédits : Unsplash demande « Photo : Prénom Nom · Unsplash » avec lien, et un appel de comptage au
téléchargement (fait par `get`) ; Pexels et Pixabay apprécient le crédit. Il est affiché en bas de la
slide 1 et en fin d'article.
"""
import glob, json, os, sys, urllib.parse, urllib.request

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from carrousel_lib import WORK  # noqa: E402

PHOTOS = os.path.join(WORK, "photos")
CONF = os.path.expanduser("~/.config/otizi-social")
UTM = "?utm_source=otizi_decrypte&utm_medium=referral"
SOURCES = [("unsplash", "UNSPLASH_ACCESS_KEY"), ("pexels", "PEXELS_API_KEY"), ("pixabay", "PIXABAY_API_KEY")]


def read_key(name, var):
    key = os.environ.get(var, "").strip()
    path = os.path.join(CONF, f"{name}.key")
    if not key and os.path.exists(path):
        key = open(path, encoding="utf-8").read().strip()
    return key


def source():
    forced = os.environ.get("PHOTO_SOURCE", "").strip().lower()
    for name, var in SOURCES:
        if forced and name != forced:
            continue
        key = read_key(name, var)
        if key:
            return name, key
    raise SystemExit("Clé de banque d'images absente : fichier ~/.config/otizi-social/unsplash.key (ou pexels.key, pixabay.key), "
                     "voir tools/ozi-tache-hebdo.md.")


def fetch(url, out=None, headers=None):
    req = urllib.request.Request(url, headers={"User-Agent": "otizi-social-assets/1.0", "Accept-Version": "v1", **(headers or {})})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    if out:
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "wb").write(data)
    return data


def used_ids():
    ids = set()
    for p in glob.glob(os.path.join(PHOTOS, "*.json")):
        try:
            ids.add(str(json.load(open(p, encoding="utf-8"))["id"]))
        except Exception:
            pass
    return ids


# Chaque banque renvoie des candidates normalisées :
# {id, photographer, photographer_url, url, alt, width, height, preview, large, download_ping}
def search_unsplash(key, query, n):
    q = urllib.parse.urlencode({"query": query, "per_page": n, "orientation": "landscape", "content_filter": "high"})
    data = json.loads(fetch(f"https://api.unsplash.com/search/photos?{q}", headers={"Authorization": f"Client-ID {key}"}))
    return [norm_unsplash(p) for p in data.get("results", [])]


def norm_unsplash(p):
    return {"id": str(p["id"]), "photographer": p["user"]["name"], "photographer_url": p["user"]["links"]["html"] + UTM,
            "url": p["links"]["html"] + UTM, "alt": p.get("alt_description") or p.get("description") or "",
            "width": p["width"], "height": p["height"], "preview": p["urls"]["small"],
            "large": p["urls"]["raw"] + "&w=1920&q=85&fm=jpg", "download_ping": p["links"]["download_location"], "source": "Unsplash"}


def get_unsplash(key, photo_id):
    p = norm_unsplash(json.loads(fetch(f"https://api.unsplash.com/photos/{photo_id}", headers={"Authorization": f"Client-ID {key}"})))
    try:  # comptage de téléchargement demandé par les règles de l'API Unsplash
        fetch(p["download_ping"], headers={"Authorization": f"Client-ID {key}"})
    except Exception:
        pass
    return p


def norm_pexels(p):
    return {"id": str(p["id"]), "photographer": p["photographer"], "photographer_url": p["photographer_url"], "url": p["url"],
            "alt": p.get("alt") or "", "width": p["width"], "height": p["height"], "preview": p["src"]["medium"],
            "large": p["src"]["large2x"], "source": "Pexels"}


def search_pexels(key, query, n):
    q = urllib.parse.urlencode({"query": query, "per_page": n, "orientation": "landscape", "size": "large"})
    return [norm_pexels(p) for p in json.loads(fetch(f"https://api.pexels.com/v1/search?{q}", headers={"Authorization": key})).get("photos", [])]


def get_pexels(key, photo_id):
    return norm_pexels(json.loads(fetch(f"https://api.pexels.com/v1/photos/{int(photo_id)}", headers={"Authorization": key})))


def norm_pixabay(p):
    return {"id": str(p["id"]), "photographer": p["user"], "photographer_url": f"https://pixabay.com/users/{p['user']}-{p['user_id']}/",
            "url": p["pageURL"], "alt": p.get("tags") or "", "width": p["imageWidth"], "height": p["imageHeight"],
            "preview": p["webformatURL"], "large": p.get("fullHDURL") or p["largeImageURL"], "source": "Pixabay"}


def search_pixabay(key, query, n):
    q = urllib.parse.urlencode({"key": key, "q": query, "per_page": max(n, 3), "image_type": "photo", "orientation": "horizontal",
                                "safesearch": "true", "min_width": 1280})
    return [norm_pixabay(p) for p in json.loads(fetch(f"https://pixabay.com/api/?{q}")).get("hits", [])]


def get_pixabay(key, photo_id):
    hits = json.loads(fetch(f"https://pixabay.com/api/?{urllib.parse.urlencode({'key': key, 'id': int(photo_id)})}")).get("hits", [])
    if not hits:
        raise SystemExit(f"Photo Pixabay {photo_id} introuvable.")
    return norm_pixabay(hits[0])


BANKS = {"unsplash": (search_unsplash, get_unsplash), "pexels": (search_pexels, get_pexels), "pixabay": (search_pixabay, get_pixabay)}


def search(query, n=8):
    name, key = source()
    photos = BANKS[name][0](key, query, min(max(n, 1), 15))
    if not photos:
        print(f"Aucune photo sur {name.capitalize()} pour « {query} » : essayez une requête plus simple, en anglais (ex. « bed and breakfast france »).")
        return
    used = used_ids()
    shown = 0
    for p in photos:
        if p["id"] in used:
            continue
        shown += 1
        preview = os.path.join(PHOTOS, "candidats", f"{p['id']}.jpg")
        fetch(p["preview"], preview)
        print(f"{shown}. id {p['id']} — {p['photographer']} ({p['source']}) — {p['width']}×{p['height']} — {p['alt'] or '(sans description)'}\n   aperçu : {preview}")
    if not shown:
        print("Toutes les photos trouvées ont déjà servi : changez de requête.")


def get(slug, photo_id):
    name, key = source()
    p = BANKS[name][1](key, photo_id)
    if p["id"] in used_ids() and not os.path.exists(os.path.join(PHOTOS, f"{slug}.json")):
        raise SystemExit(f"La photo {photo_id} a déjà servi pour un autre carrousel : choisissez-en une autre.")
    path = os.path.join(PHOTOS, f"{slug}.jpg")
    fetch(p["large"], path)
    meta = {k: p[k] for k in ("id", "photographer", "photographer_url", "url", "alt", "width", "height", "source")}
    meta.update({"slug": slug, "path": path})
    json.dump(meta, open(os.path.join(PHOTOS, f"{slug}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"ok : {path} — Photo : {p['photographer']} · {p['source']} — {p['url']}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) >= 2 and args[0] == "search":
        n = int(args[args.index("--n") + 1]) if "--n" in args else 8
        search(args[1], n)
    elif len(args) == 3 and args[0] == "get":
        get(args[1], args[2])
    else:
        raise SystemExit(__doc__)
