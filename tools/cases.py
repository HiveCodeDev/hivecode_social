"""Client showcase carousels: drawn laptop and phone frames around real captures.

Layout varies per slide (impeccable: no repeated kicker, no identical cards):
1. cover: kicker + title, laptop bleeding off the right edge
2. phone, large and tilted, title in the left column
3. laptop centred low, short title above
4. typographic close
"""
import shutil
from pathlib import Path

from build_week import ASSETS
from components import write_slides

CSS = """
.laptop{position:relative}
.laptop .lid{background:#0b0a18;border-radius:26px 26px 6px 6px;padding:18px 18px 22px;border:2px solid rgba(255,255,255,.14);
box-shadow:0 50px 100px -40px rgba(72,119,254,.6)}
.laptop .lid img{display:block;width:100%;border-radius:8px}
.laptop .base{height:26px;margin:0 -60px;border-radius:0 0 26px 26px;background:linear-gradient(#2a2650,#141127);border:2px solid rgba(255,255,255,.1);border-top:0}
.phone{background:#0b0a18;border-radius:58px;padding:16px;border:2px solid rgba(255,255,255,.18);
box-shadow:0 50px 100px -40px rgba(215,82,254,.55)}
.phone img{display:block;width:100%;border-radius:44px}
.s1 .content{justify-content:flex-start;padding-top:40px}
.s1 .laptop{margin:64px -300px 0 40px}
.s1 h1{max-width:820px}
.s2 .content{flex-direction:row;align-items:center;gap:56px;justify-content:flex-start}
.s2 .copy{flex:1}
.s2 .copy h1{margin-top:0;font-size:80px}
.s2 .copy p{margin-top:30px;font-size:34px;line-height:1.4;color:var(--soft);font-weight:300}
.s2 .phone{flex:none;width:400px;transform:rotate(4deg)}
.s3 h1{font-size:76px;max-width:880px}
.s3 .laptop{margin:70px 30px 0}
.s4 .content{justify-content:center}
.s4 h1{font-size:112px;line-height:1}
.s4 p{margin-top:40px;font-size:38px;color:var(--soft);font-weight:300;max-width:820px;line-height:1.4}
.s4 .cta{margin-top:64px}
"""


def laptop(img):
    return f'<div class="laptop"><div class="lid"><img src="{ASSETS}/clients/{img}" alt=""></div><div class="base"></div></div>'


def phone(img):
    return f'<div class="phone"><img src="{ASSETS}/clients/{img}" alt=""></div>'


def build(here, *, title, desktop, mobile, phone_title, phone_note, detail_title=None, detail=None, detail_html=None, extra_css=""):
    """detail_html replaces the third slide's laptop with drawn content."""
    # (layout class, body); a case can skip the detail slide (detail_title=None).
    slides = [
        ("s1", f"""<span class="eyebrow"><i></i>Projeto recente</span><h1>{title}</h1>{laptop(desktop)}"""),
        ("s2", f"""<div class="copy"><h1>{phone_title}</h1><p>{phone_note}</p></div>{phone(mobile)}"""),
        ("s3", f"""<h1>{detail_title}</h1>{detail_html or laptop(detail)}""") if detail_title else None,
        ("s4", """<h1>Tem um projeto <em>em mente</em>?</h1>
<p>Desenhamos e desenvolvemos sites e sistemas à medida, do primeiro contacto ao lançamento.</p>
<span class="cta">hivecode.pt</span>"""),
    ]
    slides = [s for s in slides if s]
    shutil.rmtree(Path(here) / "slides", ignore_errors=True)
    write_slides(here, [body for _, body in slides], CSS + extra_css)
    # Each slide gets its layout class on <body>, by role rather than position.
    for n, (layout, _) in enumerate(slides, 1):
        f = Path(here) / "slides" / f"{n:02d}" / "post.html"
        f.write_text(f.read_text(encoding="utf-8").replace("<body>", f'<body class="{layout}">', 1), encoding="utf-8")
