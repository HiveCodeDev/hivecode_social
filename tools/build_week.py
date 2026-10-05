"""Builds one week of posts: posts/<week>/<NN-date>/post.html + caption.txt, and plan.json.

usage: python tools/build_week.py weeks/2026-10-05.py
The week file defines WEEK (folder name) and POSTS (list of dicts with
date, time, theme, html, caption, hashtags).
"""
import json
import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = (ROOT / "assets").as_uri()

BASE_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Geologica:wght@300;400;500;600;700&display=block');
:root{--night:#121125;--deep:#16132f;--ink:#f3f1fb;--soft:#c9c3e6;--muted:#9a93c0;
--pink:#EF5AFE;--violet:#D752FE;--blue:#4877FE;}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;overflow:hidden}
body{background:var(--night);color:var(--ink);font-family:'Geologica',sans-serif;position:relative}
.hex{position:absolute;inset:0;opacity:.5}
.glow{position:absolute;border-radius:50%;filter:blur(120px);opacity:.45}
.frame{position:absolute;inset:0;padding:96px 88px;display:flex;flex-direction:column}
.eyebrow{display:inline-flex;align-items:center;gap:14px;font-size:24px;font-weight:500;letter-spacing:.14em;
text-transform:uppercase;color:var(--soft)}
.eyebrow i{width:14px;height:14px;transform:rotate(30deg);background:linear-gradient(135deg,var(--pink),var(--blue));
clip-path:polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%)}
h1{font-weight:600;font-size:84px;line-height:1.04;letter-spacing:-.025em;margin-top:40px;text-wrap:balance}
h1 em{font-style:normal;color:var(--violet)}
p.lead{font-size:34px;line-height:1.4;color:var(--soft);font-weight:300;margin-top:32px;max-width:860px}
.content{flex:1;display:flex;flex-direction:column;justify-content:center;padding-bottom:40px}
.content>.eyebrow{align-self:flex-start}
.foot{display:flex;align-items:center;justify-content:space-between;font-size:26px;color:var(--muted)}
.brand{display:flex;align-items:center;gap:16px;font-weight:600;font-size:30px;color:var(--ink)}
.brand img{width:52px;height:52px}
.shot{border-radius:22px;overflow:hidden;border:1px solid rgba(255,255,255,.14);
box-shadow:0 40px 90px -30px rgba(72,119,254,.55);background:#000}
.shot .bar{height:44px;background:#1d1a3a;display:flex;align-items:center;gap:10px;padding:0 18px;font-size:19px;color:var(--muted)}
.shot .bar b{width:12px;height:12px;border-radius:50%;background:#3a3566}
.shot .bar span{margin-left:14px}
.shot img{display:block;width:100%}
"""


def hex_svg():
    import math
    r, w, h = 70, 1080, 1350
    out = []
    dx, dy = math.sqrt(3) * r, 1.5 * r
    row = 0
    y = 0
    while y <= h + r:
        off = dx / 2 if row % 2 else 0
        x = -off
        while x <= w + dx:
            pts = " ".join(
                f"{x + r * math.cos(math.pi / 3 * i - math.pi / 2):.1f},{y + r * math.sin(math.pi / 3 * i - math.pi / 2):.1f}"
                for i in range(6)
            )
            out.append(f'<polygon points="{pts}"/>')
            x += dx
        row += 1
        y = row * dy
    return (
        '<svg class="hex" viewBox="0 0 1080 1350"><defs><linearGradient id="e" x1="0" y1="0" x2="1080" y2="1350" '
        'gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#EF5AFE" stop-opacity=".22"/>'
        '<stop offset="1" stop-color="#4877FE" stop-opacity=".22"/></linearGradient></defs>'
        '<g fill="none" stroke="url(#e)" stroke-width="1.2">' + "".join(out) + "</g></svg>"
    )


HEX = hex_svg()


def page(body, extra_css=""):
    # @import is only valid at the top of a stylesheet, so hoist any from extra_css.
    lines = extra_css.splitlines()
    imports = "\n".join(line for line in lines if line.strip().startswith("@import"))
    extra_css = "\n".join(line for line in lines if not line.strip().startswith("@import"))
    return f"""<!doctype html><html lang="pt"><head><meta charset="utf-8">
<style>{imports}
{BASE_CSS}{extra_css}</style></head><body>
{HEX}
<span class="glow" style="width:620px;height:620px;left:-180px;top:-160px;background:#4877FE"></span>
<span class="glow" style="width:560px;height:560px;right:-200px;bottom:-120px;background:#D752FE"></span>
<div class="frame"><div class="content">{body}</div>
<div class="foot"><span class="brand"><img src="{ASSETS}/logo_side.png" alt="">HiveCode</span><span>hivecode.pt</span></div>
</div></body></html>"""


def main():
    spec = runpy.run_path(sys.argv[1], init_globals={"ASSETS": ASSETS})
    week_dir = ROOT / "posts" / spec["WEEK"]
    plan = []
    for n, post in enumerate(spec["POSTS"], 1):
        folder = week_dir / f"{n:02d}-{post['date']}"
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "post.html").write_text(page(post["html"], post.get("css", "")), encoding="utf-8")
        caption = post["caption"].strip() + "\n\n" + " ".join(post["hashtags"])
        (folder / "caption.txt").write_text(caption, encoding="utf-8")
        plan.append(
            {
                "id": folder.name,
                "date": post["date"],
                "time": post["time"],
                "theme": post["theme"],
                "image": f"posts/{spec['WEEK']}/{folder.name}/post.jpg",
                "caption": caption,
                "status": "draft",
                "media_id": None,
            }
        )
    (week_dir / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{len(plan)} posts in {week_dir}")


if __name__ == "__main__":
    main()
