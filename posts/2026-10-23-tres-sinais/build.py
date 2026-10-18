"""3 sinais de que a sua empresa precisa de um sistema próprio: one drawn illustration per sign,
a large numeral as anchor, close with the HiveCode Business call to action.
"""
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from build_week import ASSETS, page

HERE = Path(__file__).resolve().parent

CSS = """
.count{position:absolute;top:96px;right:88px;font-size:24px;color:var(--muted);letter-spacing:.1em}
.num{font-size:220px;font-weight:700;line-height:.8;letter-spacing:-.06em;color:var(--violet)}
.s h1{font-size:80px;margin-top:24px}
.s p{margin-top:24px;font-size:36px;line-height:1.42;color:var(--soft);font-weight:300;max-width:880px}
.cover h1{font-size:92px;margin-top:34px}
.art{margin-top:56px;position:relative;height:470px}
.card{position:absolute;border-radius:24px;background:#1b1638;border:1px solid rgba(255,255,255,.16);box-shadow:0 40px 80px -30px rgba(0,0,0,.8);padding:24px 28px;font-size:30px;font-weight:600}
.card small{display:block;margin-top:14px;height:14px;border-radius:7px;background:rgba(255,255,255,.14)}
.chip{display:inline-flex;align-items:center;gap:18px;padding:24px 34px;border-radius:999px;background:#1b1638;border:1px solid rgba(255,255,255,.16);font-size:36px;font-weight:600}
.chip b{width:56px;height:56px;border-radius:50%;display:grid;place-items:center;font-size:30px;background:linear-gradient(135deg,var(--pink),var(--blue))}
.person{position:absolute;width:150px;height:150px;border-radius:50%;background:linear-gradient(135deg,var(--pink),var(--blue));display:grid;place-items:center}
.close .content{justify-content:center}
.close h1{font-size:112px;line-height:1}
.close p{margin-top:40px;font-size:38px;color:var(--soft);font-weight:300;max-width:860px;line-height:1.4}
.close .cta{margin-top:64px;align-self:flex-start;padding:28px 46px;border-radius:999px;background:#265ADF;font-size:36px;font-weight:600}
"""

PERSON = '<svg viewBox="0 0 24 24" width="84" height="84" fill="none" stroke="#fff" stroke-width="1.8"><circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4.5 4.5-6.5 8-6.5s6.5 2 8 6.5"/></svg>'
GREY = PERSON.replace("#fff", "#6c6694")

# 1. The same data scattered across tools, joined by dashed lines.
ART1 = """<div class="art">
<svg viewBox="0 0 904 470" style="position:absolute;inset:0" fill="none" stroke="rgba(255,255,255,.3)" stroke-width="3" stroke-dasharray="10 12">
<path d="M220 110 C 420 60, 520 120, 680 110"/><path d="M220 140 C 260 300, 330 340, 400 360"/><path d="M700 160 C 680 300, 600 330, 560 360"/></svg>
<div class="card" style="left:0;top:40px;width:300px;transform:rotate(-4deg)"><span style="color:#2fbf71">■</span> clientes.xlsx<small style="width:80%"></small><small style="width:60%"></small></div>
<div class="card" style="right:0;top:30px;width:300px;transform:rotate(4deg)">✉️ Encomendas<small style="width:70%"></small><small style="width:85%"></small></div>
<div class="card" style="left:300px;top:300px;width:300px;background:repeating-linear-gradient(#f3efe2 0 44px,#c9d6f0 44px 46px);color:#2a2550;font-style:italic">Stock: 12? 15?</div></div>"""

# 2. Copying the same record back and forth between two windows.
ART2 = """<div class="art">
<div class="card" style="left:0;top:60px;width:340px;height:330px">✉️ Email<small style="width:80%"></small><small style="width:65%"></small><small style="width:75%"></small></div>
<div class="card" style="right:0;top:60px;width:340px;height:330px"><span style="color:#2fbf71">■</span> Excel<small style="width:70%"></small><small style="width:85%"></small><small style="width:60%"></small></div>
<svg viewBox="0 0 24 24" width="150" height="150" style="position:absolute;left:377px;top:150px" fill="none" stroke="#D752FE" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M4 8h14l-3-3M20 16H6l3 3"/></svg>
<span class="chip" style="position:absolute;left:250px;bottom:0;font-size:30px">Copiar · colar · repetir</span></div>"""

# 3. Everything wired to one person; the rest of the team cannot see it.
ART3 = f"""<div class="art">
<svg viewBox="0 0 904 470" style="position:absolute;inset:0" stroke="url(#g)" stroke-width="4" fill="none">
<defs><linearGradient id="g" x1="0" y1="0" x2="904" y2="470" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#EF5AFE"/><stop offset="1" stop-color="#4877FE"/></linearGradient></defs>
<line x1="452" y1="235" x2="120" y2="60"/><line x1="452" y1="235" x2="784" y2="60"/><line x1="452" y1="235" x2="120" y2="410"/><line x1="452" y1="235" x2="784" y2="410"/></svg>
<div class="person" style="left:377px;top:160px">{PERSON}</div>
{"".join(f'<div class="card" style="left:{x}px;top:{y}px;font-size:26px">{t}</div>' for t, x, y in [("Clientes", 20, 20), ("Encomendas", 650, 20), ("Stock", 40, 370), ("Faturas", 690, 370)])}
<div style="position:absolute;left:300px;top:390px;display:flex;gap:30px;opacity:.7">{GREY}{GREY}{GREY}</div></div>"""

COVER_ART = """<div style="margin-top:60px;display:flex;flex-direction:column;gap:22px">
<span class="chip" style="align-self:flex-start"><b>1</b>Informação espalhada</span>
<span class="chip" style="align-self:flex-start"><b>2</b>Tempo a copiar dados</span>
<span class="chip" style="align-self:flex-start"><b>3</b>Tudo depende de uma pessoa</span></div>"""


def sign(n, title, note, art):
    return f'<div class="s"><div class="num">{n}</div><h1>{title}</h1><p>{note}</p></div>{art}'


SLIDES = [
    ("cover", f"""<span class="eyebrow"><i></i>Business</span>
<h1>3 sinais de que a sua empresa precisa de um <em>sistema próprio</em>.</h1>
<p class="lead">Deslize e veja quantos reconhece. 👉</p>{COVER_ART}"""),
    ("", sign(1, "A mesma informação está em <em>vários sítios</em>.", "Clientes no Excel, encomendas no email, stock num caderno.", ART1)),
    ("", sign(2, "Perde tempo a <em>copiar dados</em>.", "Passar a mesma informação de um lado para o outro, todos os dias.", ART2)),
    ("", sign(3, "Só <em>uma pessoa</em> sabe onde está tudo.", "Quando essa pessoa falta, a empresa fica à espera.", ART3)),
    ("close", """<h1>Reconheceu <em>algum</em>?</h1>
<p>Na HiveCode Business, criamos um sistema à medida da sua empresa.</p>
<span class="cta">hivecode.pt/business</span>"""),
]

if __name__ == "__main__":
    shutil.rmtree(HERE / "slides", ignore_errors=True)
    for n, (cls, body) in enumerate(SLIDES, 1):
        d = HERE / "slides" / f"{n:02d}"
        d.mkdir(parents=True)
        html = page(f'<span class="count">{n}/{len(SLIDES)}</span>' + body, CSS)
        if cls:
            html = html.replace("<body>", f'<body class="{cls}">', 1)
        (d / "post.html").write_text(html, encoding="utf-8")
    print("ok")
