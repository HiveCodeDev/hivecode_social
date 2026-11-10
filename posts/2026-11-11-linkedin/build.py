"""Instagram post: "Agora também estamos no LinkedIn" (blue theme, single image 1080x1350).

python posts/2026-11-11-linkedin/build.py && node tools/render_one.mjs posts/2026-11-11-linkedin/post.html posts/2026-11-11-linkedin/post.jpg 1080 1350
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools"))
from build_week import ASSETS, page  # noqa: E402

CSS = """
h1{font-size:104px;line-height:1}
.card{margin-top:64px;border-radius:36px;background:#fff;overflow:hidden;box-shadow:0 60px 120px -40px rgba(0,0,0,.45);position:relative}
.card .cv{height:150px;background:linear-gradient(120deg,#D752FE,#4877FE)}
.card .lg{position:absolute;left:48px;top:78px;width:150px;height:150px;border-radius:26px;background:#fff;display:grid;place-items:center;box-shadow:0 6px 20px rgba(0,0,0,.15)}
.card .lg img{width:112px;height:112px}
.card .bd{padding:96px 48px 44px;color:#191919}
.card h3{font-size:56px;font-weight:700}
.card p{font-size:32px;color:#555;margin-top:8px}
.card small{display:block;font-size:26px;color:#888;margin-top:6px}
.fol{display:inline-block;margin-top:30px;padding:20px 46px;border-radius:999px;background:#0A66C2;color:#fff;font-size:34px;font-weight:700}
.url{margin-top:48px;align-self:flex-start;padding:22px 34px;border-radius:20px;background:rgba(255,255,255,.14);border:2px solid rgba(255,255,255,.35);font-size:38px;font-weight:600}
"""

BODY = f"""<h1>Agora também estamos no <em>LinkedIn</em>.</h1>
<div class="card"><div class="cv"></div><div class="lg"><img src="{ASSETS}/logo_mark.svg" alt=""></div>
<div class="bd"><h3>HiveCode</h3><p>Sites e software à medida</p><small>Desenvolvimento de software · Viseu</small><span class="fol">+ Seguir</span></div></div>
<span class="url">linkedin.com/company/hivecode-pt</span>"""

(HERE / "post.html").write_text(page(BODY, CSS, theme="blue"), encoding="utf-8")
print("ok")
