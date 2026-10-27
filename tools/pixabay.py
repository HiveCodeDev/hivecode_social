"""Free stock video (b-roll) from Pixabay: commercial use, no attribution needed.

python tools/pixabay.py "<query>" [n]   lists clips: id, seconds, size, tags
fetch(clip_id, out_mp4) downloads the largest rendition of one clip.
The key comes from the PIXABAY_API_KEY environment variable and is never printed.
"""
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://pixabay.com/api/videos/"
UA = "Mozilla/5.0 (hivecode_social reel builder)"


def _get(**params):
    key = os.environ.get("PIXABAY_API_KEY")
    if not key:
        raise SystemExit("Missing PIXABAY_API_KEY")
    url = API + "?" + urllib.parse.urlencode({"key": key, **params})
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        raise SystemExit(f"Pixabay HTTP {e.code}") from None  # never echo the URL: it carries the key


def search(query, n=10):
    """Vertical-friendly first: longer, high-resolution clips, safe search on."""
    data = _get(q=query, per_page=max(3, n), safesearch="true", order="popular")
    return [{"id": h["id"], "seconds": h["duration"], "size": f'{h["videos"]["large"]["width"]}x{h["videos"]["large"]["height"]}',
             "tags": h["tags"], "videos": h["videos"]} for h in data["hits"] if "ai generated" not in h["tags"]]


def fetch(clip_id, out):
    hit = _get(id=clip_id)["hits"][0]
    best = next(v for k in ("large", "medium", "small") if (v := hit["videos"][k])["url"])
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(best["url"], headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as r, open(out, "wb") as f:
        f.write(r.read())
    return out


if __name__ == "__main__":
    for c in search(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 10):
        print(f'{c["id"]:>10}  {c["seconds"]:>3}s  {c["size"]:>9}  {c["tags"]}')
