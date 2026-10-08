"""Site para negócio local: what a good site does while the shop is closed.

Drawn illustrations only (no screenshots). Each step has its own layout:
1. cover: closed storefront at night next to a lit phone
2. search bar over a map, one pin highlighted
3. phone on the left, the four trust points on the right
4. three large contact buttons, one being tapped
5. typographic close, as in the client cases
"""
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from build_week import page

HERE = Path(__file__).resolve().parent

CSS = """
.count{position:absolute;top:96px;right:88px;font-size:24px;color:var(--muted);letter-spacing:.1em}
.step{width:96px;height:96px;border-radius:50%;display:grid;place-items:center;font-size:48px;font-weight:700;
background:linear-gradient(135deg,var(--pink),var(--blue));box-shadow:0 0 0 12px rgba(215,82,254,.12)}
.s h1{font-size:88px;margin-top:36px}
.s p{margin-top:26px;font-size:34px;line-height:1.42;color:var(--soft);font-weight:300;max-width:880px}
.art{margin-top:56px;position:relative}
.panel{position:absolute;border-radius:26px;background:#1b1638;border:1px solid rgba(255,255,255,.14);box-shadow:0 40px 80px -36px rgba(72,119,254,.55)}
.bar{display:block;height:18px;border-radius:9px;background:rgba(255,255,255,.12)}
.hl{background:linear-gradient(90deg,var(--pink),var(--blue))}
.chip{display:inline-flex;align-items:center;gap:14px;padding:18px 28px;border-radius:999px;background:#1b1638;border:1px solid rgba(255,255,255,.16);font-size:32px;font-weight:500}
.chip i{width:14px;height:14px;border-radius:50%}
.phone{background:#0d0b1c;border-radius:48px;border:2px solid rgba(255,255,255,.2);padding:13px;box-shadow:0 40px 90px -30px rgba(215,82,254,.6)}
.phone .scr{height:100%;border-radius:36px;background:#1b1638;padding:26px 22px;display:flex;flex-direction:column;gap:14px}
.btn{display:inline-flex;align-items:center;justify-content:center;border-radius:999px;background:#265ADF;font-weight:600;color:#fff}
.cover h1{font-size:84px;max-width:900px}
.cover p.lead{margin-top:26px}
.close .content{justify-content:center}
.close h1{font-size:112px;line-height:1}
.close p{margin-top:40px;font-size:38px;color:var(--soft);font-weight:300;max-width:840px;line-height:1.4}
.close .cta{margin-top:64px;align-self:flex-start;padding:28px 46px;border-radius:999px;background:#265ADF;font-size:36px;font-weight:600}
"""

ICON = {
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
    "cal": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M16 3v4M8 3v4M3 10h18M8 14h3"/>',
    "doc": '<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6M8 13h8M8 17h5"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/>',
    "check": '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
}


def icon(name, size=40, stroke="#f3f1fb", width=2):
    return (f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="{stroke}" '
            f'stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round">{ICON[name]}</svg>')


def site_screen(button="Marcar"):
    return f"""<div class="scr">
<span style="height:150px;border-radius:20px;background:linear-gradient(150deg,rgba(239,90,254,.55),rgba(72,119,254,.55))"></span>
<span class="bar" style="height:26px;width:85%;background:rgba(255,255,255,.3)"></span><span class="bar" style="width:65%"></span>
<span style="color:#ffc861;font-size:26px;letter-spacing:4px">★★★★★</span>
<span class="btn" style="margin-top:auto;padding:16px;font-size:24px">{button}</span></div>"""


# 1. Closed shop at night, lit phone in front of it.
ART1 = f"""<div class="art" style="height:500px">
<div class="panel" style="left:0;top:20px;width:620px;height:470px;overflow:hidden;background:#17132f">
<div style="height:70px;background:repeating-linear-gradient(90deg,#3a2a78 0 62px,#251d52 62px 124px)"></div>
<div style="position:absolute;left:44px;top:120px;width:300px;height:250px;border-radius:12px;background:rgba(255,255,255,.04);border:2px solid rgba(255,255,255,.12)"></div>
<div style="position:absolute;right:52px;top:120px;width:170px;height:350px;border-radius:12px 12px 0 0;background:rgba(255,255,255,.05);border:2px solid rgba(255,255,255,.14)">
<div style="position:absolute;left:50%;top:70px;transform:translateX(-50%);width:2px;height:40px;background:rgba(255,255,255,.4)"></div>
<span style="position:absolute;left:50%;top:106px;transform:translateX(-50%) rotate(-4deg);padding:12px 18px;border-radius:10px;background:#f3f1fb;color:#121125;font-size:24px;font-weight:700;letter-spacing:.04em">FECHADO</span></div>
<svg viewBox="0 0 24 24" width="62" height="62" style="position:absolute;left:250px;top:150px" fill="#c9c3e6"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5"/></svg>
</div>
<div class="phone" style="position:absolute;right:20px;top:0;width:290px;height:500px;transform:rotate(5deg)">{site_screen()}</div>
</div>"""

# 2. Search bar over a map; the highlighted pin is the business.
PIN = '<svg viewBox="0 0 24 24" width="{s}" height="{s}" style="position:absolute;left:{x}px;top:{y}px" fill="{c}"><path d="M12 2a7 7 0 0 0-7 7c0 5 7 13 7 13s7-8 7-13a7 7 0 0 0-7-7m0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5"/></svg>'
ART2 = f"""<div class="art" style="height:560px">
<div class="panel" style="inset:70px 0 0 0;overflow:hidden;background:#17132f">
<svg viewBox="0 0 904 490" width="100%" height="100%" style="position:absolute;inset:0" fill="none" stroke="rgba(255,255,255,.08)" stroke-width="18" stroke-linecap="round">
<path d="M-20 140 C200 120 300 260 520 230 S800 120 930 160"/><path d="M180 -20 C210 160 160 330 240 520"/><path d="M640 -20 C600 150 700 320 660 520"/><path d="M-20 400 C220 380 500 430 930 380" stroke-width="10"/></svg>
{PIN.format(s=58, x=120, y=250, c="#4a4478")}{PIN.format(s=58, x=760, y=330, c="#4a4478")}{PIN.format(s=58, x=330, y=90, c="#4a4478")}
<div style="position:absolute;left:470px;top:230px;width:150px;height:150px;border-radius:50%;background:rgba(215,82,254,.22);transform:translate(-50%,-50%)"></div>
{PIN.format(s=110, x=415, y=120, c="#D752FE")}
<span class="chip" style="position:absolute;left:530px;top:110px;background:#265ADF;border:0">O seu negócio</span>
</div>
<div class="chip" style="position:absolute;left:40px;right:40px;top:0;padding:26px 34px;font-size:34px;font-weight:400;color:var(--soft);background:#221c45">
{icon("search", 38, "#c9c3e6")}<span>Serviço <b style="color:#f3f1fb;font-weight:500">perto de mim</b></span></div>
</div>"""

# 3. Phone left, the four things a visitor checks on the right.
POINTS = [("pink", "O que faz"), ("blue", "Onde está"), ("pink", "Fotos reais"), ("blue", "Opiniões de clientes")]
ART3 = f"""<div class="art" style="height:560px;display:flex;align-items:center;gap:60px">
<div class="phone" style="flex:none;width:300px;height:540px;transform:rotate(-4deg)">{site_screen("Contactar")}</div>
<div style="display:flex;flex-direction:column;gap:22px">
{"".join(f'<span class="chip"><i style="background:var(--{c})"></i>{t}</span>' for c, t in POINTS)}
<span class="chip" style="background:#265ADF;border:0">{icon("check", 34, "#fff", 2.6)}Rápido no telemóvel</span>
</div></div>"""

# 4. Three large contact buttons; the middle one is being tapped.
BUTTONS = [("phone", "Ligar"), ("cal", "Marcar"), ("doc", "Pedir orçamento")]
ART4 = f"""<div class="art" style="height:470px;display:flex;flex-direction:column;gap:26px;padding-right:120px">
{"".join(
    f'<span class="btn" style="justify-content:flex-start;gap:26px;padding:30px 44px;font-size:40px;'
    + ("background:#265ADF;box-shadow:0 0 0 12px rgba(38,90,223,.25),0 30px 70px -20px rgba(72,119,254,.8)" if i == 1 else "background:#1b1638;border:1px solid rgba(255,255,255,.16)")
    + f'">{icon(name, 46)}{label}</span>'
    for i, (name, label) in enumerate(BUTTONS)
)}
<div style="position:absolute;right:150px;top:150px;width:110px;height:110px;border-radius:50%;border:3px solid rgba(255,255,255,.55)"></div>
<div style="position:absolute;right:120px;top:120px;width:170px;height:170px;border-radius:50%;border:2px solid rgba(255,255,255,.2)"></div>
</div>"""


def step(n, title, note, art):
    return f"""<div class="s"><div class="step">{n}</div><h1>{title}</h1><p>{note}</p></div>{art}"""


SLIDES = [
    ("cover", f"""<span class="eyebrow"><i></i>Negócios locais</span>
<h1>O seu site trabalha enquanto a loja <em>está fechada</em>.</h1>
<p class="lead">Veja o que um bom site faz por um negócio local.</p>{ART1}"""),
    ("", step(1, "Ajuda-o a ser <em>encontrado</em>.", "Aparece quando procuram o seu serviço na sua zona.", ART2)),
    ("", step(2, "Convence em <em>segundos</em>.", "O que faz, onde está, fotos reais e opiniões de clientes. Rápido no telemóvel.", ART3)),
    ("", step(3, "Torna o contacto <em>fácil</em>.", "Ligar, marcar ou pedir orçamento com um toque. Como nos sites da 4Sons e da clínica Ana Carolina Pereira.", ART4)),
    ("close", """<h1>Tem um projeto <em>em mente</em>?</h1>
<p>Fazemos sites rápidos, pensados para telemóvel, para negócios locais que querem vender mais.</p>
<span class="cta">hivecode.pt</span>"""),
]

if __name__ == "__main__":  # the reel imports the art without rewriting the slides
    shutil.rmtree(HERE / "slides", ignore_errors=True)
    for n, (cls, body) in enumerate(SLIDES, 1):
        d = HERE / "slides" / f"{n:02d}"
        d.mkdir(parents=True)
        html = page(f'<span class="count">{n}/{len(SLIDES)}</span>' + body, CSS)
        if cls:
            html = html.replace("<body>", f'<body class="{cls}">', 1)
        (d / "post.html").write_text(html, encoding="utf-8")
    print("ok")
