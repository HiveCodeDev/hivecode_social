"""Black Friday: faltam 14 dias. Black and yellow: a four-point site checklist to save, then the
free mockup and quote offer (HiveCode has no Black Friday promotion).
"""
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1].parent / "tools"))
from build_week import page

HERE = Path(__file__).resolve().parent

CSS = """
body{font-weight:500}
.tape{position:absolute;left:-40px;right:-40px;height:56px;background:repeating-linear-gradient(-45deg,#FFD400 0 40px,#0A0A0A 40px 80px);z-index:3}
.tape.t{top:0}.tape.b{bottom:0}
.count{position:absolute;top:96px;right:88px;font-size:24px;color:var(--muted);letter-spacing:.1em}
.cover h1{font-size:200px;line-height:.86;font-weight:800;letter-spacing:-.04em;color:#FFD400;margin-top:30px;text-transform:uppercase}
.days{display:inline-block;margin-top:44px;padding:22px 38px;border-radius:999px;background:#FFD400;color:#0A0A0A;font-size:44px;font-weight:800;align-self:flex-start}
.cover .lead{font-size:52px;color:#fff;font-weight:600;margin-top:40px}
.num{font-size:150px;font-weight:800;line-height:1;color:#FFD400;letter-spacing:-.05em}
.s h1{font-size:76px;margin-top:20px}
.s p{margin-top:24px;font-size:36px;line-height:1.4;color:var(--soft);font-weight:300;max-width:880px}
.art{margin-top:56px;position:relative;height:330px}
.card{position:absolute;border-radius:28px;background:#fff;color:#0A0A0A}
.close .content{justify-content:center}
.close h1{font-size:104px;line-height:1}
.close p{margin-top:36px;font-size:38px;color:var(--soft);font-weight:300;max-width:860px;line-height:1.4}
.offer{margin-top:50px;padding:34px 40px;border-radius:26px;background:#FFD400;color:#0A0A0A;font-size:36px;font-weight:700;max-width:860px}
.close .cta{margin-top:40px;align-self:flex-start;padding:28px 46px;border-radius:999px;border:4px solid #fff;color:#fff;font-size:36px;font-weight:600}
"""

TAPE = '<span class="tape t"></span><span class="tape b"></span>'

ARTS = [
    """<div class="card" style="left:0;top:0;width:560px;padding:34px 40px"><div style="font-size:28px;color:#666">Tempo de abertura no telemóvel</div>
<div style="display:flex;align-items:baseline;gap:20px;margin-top:14px"><span style="font-size:110px;font-weight:800;color:#1f8a4c">2,1 s</span><span style="font-size:34px;color:#e5484d;text-decoration:line-through">7 s</span></div></div>""",
    """<div class="card" style="left:0;top:0;width:700px;height:320px;overflow:hidden"><div style="height:46px;background:#eee"></div>
<div style="margin:24px;height:150px;border-radius:18px;background:#0A0A0A;color:#FFD400;display:grid;place-items:center;font-size:52px;font-weight:800">BLACK FRIDAY</div>
<div style="margin:0 24px;height:24px;width:55%;border-radius:12px;background:#eee"></div></div>""",
    """<div style="position:absolute;left:0;top:40px;display:flex;gap:24px;align-items:center">
<span style="padding:34px 64px;border-radius:22px;background:#FFD400;color:#0A0A0A;font-size:52px;font-weight:800">Comprar agora</span>
<span style="font-size:90px">👆</span></div>""",
    """<svg viewBox="0 0 700 300" width="700" height="300" style="position:absolute;left:0;top:0">
<path d="M0 260 L120 250 L240 245 L360 238 L470 225 L560 60 L620 200 L700 230" fill="none" stroke="#FFD400" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/>
<circle cx="560" cy="60" r="18" fill="#FFD400"/><text x="560" y="300" fill="#fff" font-size="30" font-family="Geologica" text-anchor="middle">27 nov</text>
<text x="0" y="300" fill="#8f8f8f" font-size="26" font-family="Geologica">visitas</text></svg>""",
]

POINTS = [
    ("O site abre em menos de <em>3 segundos</em> no telemóvel?", "Com mais visitas, um site lento perde vendas."),
    ("As promoções estão na <em>página inicial</em>?", "O cliente não procura: se não vê, sai."),
    ("O botão de compra ou de contacto está <em>à vista</em>?", "Um clique a mais é um cliente a menos."),
    ("O site aguenta o <em>pico de visitas</em>?", "Teste antes, não no dia 27."),
]

SLIDES = [("cover", f"""{TAPE}<h1>Black<br>Friday</h1><span class="days">Faltam 14 dias</span>
<p class="lead">O seu site está pronto? 👉</p>""")]
SLIDES += [("", f'{TAPE}<div class="s"><div class="num">0{n}</div><h1>{t}</h1><p>{p}</p></div><div class="art">{a}</div>')
           for n, ((t, p), a) in enumerate(zip(POINTS, ARTS), 1)]
SLIDES += [("close", f"""{TAPE}<h1>Guarde esta <em>lista</em> 🔖</h1>
<p>Para rever na semana da Black Friday.</p>
<div class="offer">🎁 Peça um mockup e um orçamento gratuitos, sem compromisso.</div>
<span class="cta">hivecode.pt</span>""")]

if __name__ == "__main__":
    shutil.rmtree(HERE / "slides", ignore_errors=True)
    for n, (cls, body) in enumerate(SLIDES, 1):
        d = HERE / "slides" / f"{n:02d}"
        d.mkdir(parents=True)
        html = page(f'<span class="count">{n}/{len(SLIDES)}</span>' + body, CSS, theme="blackfriday")
        if cls:
            html = html.replace("<body>", f'<body class="{cls}">', 1)
        (d / "post.html").write_text(html, encoding="utf-8")
    print("ok")
