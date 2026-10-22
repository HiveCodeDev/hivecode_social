"""Antes e depois: the site of a neighbourhood bakery (fictional example), paper theme.
An old, hard-to-use mobile site next to a clear one; then the two things that change most:
ordering online and being found nearby.
"""
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from build_week import page

HERE = Path(__file__).resolve().parent

CSS = """
.count{position:absolute;top:96px;right:88px;font-size:24px;color:var(--muted);letter-spacing:.1em}
.cover h1{font-size:96px;margin-top:30px}
.s h1{font-size:80px;margin-top:0}
.s p{margin-top:22px;font-size:34px;line-height:1.42;color:var(--soft);font-weight:300;max-width:880px}
.art{margin-top:50px;position:relative;height:640px}
.ph{position:absolute;width:300px;height:600px;border-radius:44px;background:#121125;padding:12px;box-shadow:0 40px 70px -30px rgba(18,17,37,.5)}
.ph .scr{height:100%;border-radius:34px;overflow:hidden;position:relative}
.old{background:#e9e4f7;font-family:'Times New Roman',serif;color:#3b3b3b;padding:22px 14px;font-size:13px;line-height:1.3}
.old .ban{background:#7a1f9c;color:#ffeb3b;font-size:22px;text-align:center;padding:10px 4px;font-weight:700;font-style:italic}
.old .menu{display:flex;gap:6px;color:#1a0dab;text-decoration:underline;font-size:11px;margin:10px 0}
.old .gray{height:120px;background:#c9c2b8;margin:10px 0;display:grid;place-items:center;color:#777;font-size:12px}
.new{background:#fff;color:#121125;font-family:'Geologica',sans-serif}
.new .hero{height:230px;background:linear-gradient(160deg,#f2c27b,#c9772f);display:grid;place-items:center;font-size:110px}
.new .in{padding:20px 18px;display:flex;flex-direction:column;gap:12px}
.new b{font-size:26px;font-weight:700;letter-spacing:-.02em}
.open{align-self:flex-start;padding:7px 14px;border-radius:999px;background:#dff5e8;color:#127a43;font-size:16px;font-weight:600}
.btn{padding:15px;border-radius:14px;background:#265ADF;color:#fff;font-size:19px;font-weight:600;text-align:center}
.btn.ghost{background:#eef1fb;color:#265ADF}
.two{display:flex;gap:10px}.two .btn{flex:1}
.lab{position:absolute;padding:10px 22px;border-radius:999px;font-size:24px;font-weight:600;letter-spacing:.06em;text-transform:uppercase}
.note{position:absolute;display:flex;align-items:center;gap:14px;padding:18px 24px;border-radius:18px;background:#fff;font-size:28px;font-weight:500;box-shadow:0 24px 50px -24px rgba(18,17,37,.45);white-space:nowrap}
.note i{width:40px;height:40px;border-radius:50%;display:grid;place-items:center;font-style:normal;font-size:22px;color:#fff;flex:none}
.bad i{background:#e5484d}.good i{background:#2fbf71}
.card{position:absolute;border-radius:28px;background:#fff;box-shadow:0 30px 60px -28px rgba(18,17,37,.45);padding:34px 38px;color:#121125}
.close .content{justify-content:center}
.close h1{font-size:108px;line-height:1}
.close p{margin-top:40px;font-size:38px;color:var(--soft);font-weight:300;max-width:860px;line-height:1.4}
.close .cta{margin-top:64px;align-self:flex-start;padding:28px 46px;border-radius:999px;background:#265ADF;color:#fff;font-size:36px;font-weight:600}
"""

OLD = """<div class="ph" style="{pos}"><div class="scr old">
<div class="ban">~ Bem-vindo ~</div>
<div class="menu"><span>Início</span><span>Quem somos</span><span>Galeria</span><span>Contactos</span></div>
<p>A Padaria do Bairro foi fundada com o objetivo de servir a comunidade com produtos de qualidade feitos diariamente com os melhores ingredientes e muito carinho pela nossa equipa…</p>
<div class="gray">imagem.jpg</div>
<p>Para mais informações contacte-nos através do formulário. Responderemos com a maior brevidade possível.</p></div></div>"""

NEW = """<div class="ph" style="{pos}"><div class="scr new"><div class="hero">🥐</div><div class="in">
<b>Padaria do Bairro</b><span class="open">Aberto hoje · 7h–20h</span>
<span class="btn">Encomendar para levantar</span>
<div class="two"><span class="btn ghost">Ligar</span><span class="btn ghost">Direções</span></div></div></div></div>"""


def note(kind, text, pos):
    mark = "✕" if kind == "bad" else "✓"
    return f'<div class="note {kind}" style="{pos}"><i>{mark}</i>{text}</div>'


COVER_ART = f"""<div class="art" style="height:640px;margin-top:40px">
{OLD.format(pos="left:60px;top:20px;transform:rotate(-4deg)")}
{NEW.format(pos="left:540px;top:20px;transform:rotate(3deg)")}
<span class="lab" style="left:120px;top:560px;background:#121125;color:#F6F1E7">Antes</span>
<span class="lab" style="left:600px;top:560px;background:#265ADF;color:#fff">Depois</span></div>"""

BEFORE = f"""<div class="art">{OLD.format(pos="left:0;top:20px")}
{note("bad", "Horário? Não aparece.", "left:360px;top:60px")}
{note("bad", "Texto minúsculo", "left:360px;top:220px")}
{note("bad", "Só um formulário", "left:360px;top:380px")}
{note("bad", "Nada para encomendar", "left:360px;top:540px")}</div>"""

AFTER = f"""<div class="art">{NEW.format(pos="left:0;top:20px")}
{note("good", "Horário à vista", "left:360px;top:60px")}
{note("good", "Encomendas num toque", "left:360px;top:220px")}
{note("good", "Ligar ou ir lá, sem procurar", "left:360px;top:380px")}
{note("good", "Feito para o telemóvel", "left:360px;top:540px")}</div>"""

ORDER = """<div class="art">
<div class="card" style="left:0;right:120px;top:20px">
<div style="font-size:24px;color:#8a8499;letter-spacing:.08em;text-transform:uppercase">Nova encomenda · 22h14</div>
<div style="font-size:40px;font-weight:700;margin-top:18px">2 broas de milho<br>6 pães de leite</div>
<div style="display:flex;justify-content:space-between;align-items:center;margin-top:28px;font-size:30px">
<span>Levantar amanhã · <b>8h30</b></span><span class="open" style="font-size:24px">Pago ✓</span></div></div>
<div class="card" style="left:200px;right:0;top:360px;background:#121125;color:#F6F1E7">
<div style="font-size:24px;color:#bdb6a8;letter-spacing:.08em;text-transform:uppercase">Amanhã de manhã</div>
<div style="font-size:40px;font-weight:700;margin-top:18px">Saco pronto, com o nome do cliente. 🛍️</div></div></div>"""

FOUND = """<div class="art">
<div class="card" style="left:0;right:0;top:20px;padding:26px 32px;display:flex;align-items:center;gap:20px;font-size:32px;color:#4a4560">
<svg viewBox="0 0 24 24" width="40" height="40" fill="none" stroke="#4a4560" stroke-width="2.4" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/></svg>padaria perto de mim</div>
<div class="card" style="left:0;right:0;top:190px">
<div style="font-size:42px;font-weight:700">Padaria do Bairro</div>
<div style="font-size:28px;color:#4a4560;margin-top:10px">Padaria · 350 m · <span style="color:#127a43;font-weight:600">Aberto agora</span></div>
<div style="display:flex;gap:16px;margin-top:28px"><span class="btn" style="font-size:26px;padding:18px 30px">Site</span>
<span class="btn ghost" style="font-size:26px;padding:18px 30px">Direções</span><span class="btn ghost" style="font-size:26px;padding:18px 30px">Ligar</span></div></div>
<div class="note good" style="left:120px;top:520px"><i>✓</i>Horário, morada e site sempre certos</div></div>"""


def slide(title, text, art):
    return f'<div class="s"><h1>{title}</h1><p>{text}</p></div>{art}'


SLIDES = [
    ("cover", f"""<span class="eyebrow"><i></i>Antes e depois</span>
<h1>O site de uma <em>padaria de bairro</em>.</h1>
<p class="lead">Exemplo fictício. Deslize para ver o que muda. 👉</p>{COVER_ART}"""),
    ("", slide("<em>Antes:</em> bonito em 2010.", "No telemóvel, quem procura o horário desiste antes de o encontrar.", BEFORE)),
    ("", slide("<em>Depois:</em> tudo à primeira vista.", "O que o cliente procura está no topo, em letra que se lê.", AFTER)),
    ("", slide("Encomendas <em>enquanto dorme</em>.", "O cliente encomenda à noite. De manhã, só tem de levantar.", ORDER)),
    ("", slide("Encontrado por quem está <em>perto</em>.", "Quem pesquisa no telemóvel vê o horário, a morada e o site.", FOUND)),
    ("close", """<h1>O seu negócio merece um site que <em>trabalha</em>.</h1>
<p>Criamos sites para negócios locais, pensados para o telemóvel.</p>
<span class="cta">hivecode.pt</span>"""),
]

if __name__ == "__main__":
    shutil.rmtree(HERE / "slides", ignore_errors=True)
    for n, (cls, body) in enumerate(SLIDES, 1):
        d = HERE / "slides" / f"{n:02d}"
        d.mkdir(parents=True)
        html = page(f'<span class="count">{n}/{len(SLIDES)}</span>' + body, CSS, theme="paper")
        if cls:
            html = html.replace("<body>", f'<body class="{cls}">', 1)
        (d / "post.html").write_text(html, encoding="utf-8")
    print("ok")
