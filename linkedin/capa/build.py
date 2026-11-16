"""LinkedIn dynamic cover: four 2256x382 slides in the night style (python linkedin/capa/build.py)."""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from build_week import ASSETS, HEX  # noqa: E402

SLIDES = [
    ("Sites e software <em>à&nbsp;medida</em> para empresas", ""),
    ("Sites <em>rápidos</em>, no Google e no telemóvel", "HiveCode Websites"),
    ("CRM, ERP e faturação <em>à&nbsp;medida</em>", "HiveCode Business"),
    ("Mockup e orçamento <em>gratuitos</em>, sem compromisso", "hivecode.pt"),
]

PAGE = """<!doctype html><html lang="pt"><head><meta charset="utf-8"><style>
@import url('https://fonts.googleapis.com/css2?family=Geologica:wght@300;500;600;700&display=block');
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:2256px;height:382px;overflow:hidden}}
body{{background:#121125;color:#f3f1fb;font-family:'Geologica',sans-serif;position:relative}}
.hex{{position:absolute;left:0;top:-480px;width:2256px;height:2820px;opacity:.45}}
.glow{{position:absolute;border-radius:50%;filter:blur(120px);opacity:.5}}
.box{{position:absolute;left:640px;right:120px;top:0;bottom:0;display:flex;align-items:center;gap:56px}}
.box img{{width:150px;height:150px;flex:none}}
h1{{font-size:96px;font-weight:600;letter-spacing:-.025em;line-height:1.02}}
h1 em{{font-style:normal;background:linear-gradient(90deg,#EF5AFE,#4877FE);-webkit-background-clip:text;color:transparent}}
small{{display:block;margin-top:18px;font-size:38px;font-weight:500;color:#c9c3e6;letter-spacing:.04em}}
</style></head><body>{hex}
<span class="glow" style="width:700px;height:700px;left:200px;top:-420px;background:#4877FE"></span>
<span class="glow" style="width:700px;height:700px;right:-100px;top:-200px;background:#D752FE"></span>
<div class="box"><img src="{assets}/logo_mark.svg" alt=""><div><h1>{title}</h1>{sub}</div></div>
</body></html>"""

for n, (title, sub) in enumerate(SLIDES, 1):
    html = HERE / f"capa{n}.html"
    html.write_text(PAGE.format(hex=HEX, assets=ASSETS, title=title, sub=f"<small>{sub}</small>" if sub else ""), encoding="utf-8")
    subprocess.run(["node", str(ROOT / "tools/render_one.mjs"), str(html), str(HERE / f"capa{n}.jpg"), "2256", "382"], check=True)
print("ok")
