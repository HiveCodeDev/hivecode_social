"""Só quem gere uma empresa conhece: four everyday frustrations a business owner recognises,
then the HiveCode Business way out. Drawn art only; each slide has its own illustration.
"""
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from build_week import ASSETS, page

HERE = Path(__file__).resolve().parent

CSS = """
.count{position:absolute;top:96px;right:88px;font-size:24px;color:var(--muted);letter-spacing:.1em}
.s h1{font-size:84px;margin-top:0}
.s p{margin-top:26px;font-size:36px;line-height:1.42;color:var(--soft);font-weight:300;max-width:880px}
.cover h1{font-size:100px;margin-top:34px}
.art{margin-top:60px;position:relative;height:560px}
.card{position:absolute;border-radius:26px;background:#1b1638;border:1px solid rgba(255,255,255,.16);box-shadow:0 40px 80px -30px rgba(0,0,0,.8);overflow:hidden}
.row{display:flex;align-items:center;gap:20px;padding:24px 30px;border-bottom:1px solid rgba(255,255,255,.08);font-size:30px;color:var(--soft)}
.row i{width:40px;height:48px;border-radius:6px;background:#2fbf71;flex:none;position:relative}
.row i:after{content:"";position:absolute;right:0;top:0;border-left:12px solid transparent;border-top:12px solid #121125}
.row.on{background:rgba(215,82,254,.16);color:#f3f1fb;font-weight:600}
.bubble{position:absolute;padding:24px 32px;border-radius:28px;font-size:32px;font-weight:500;box-shadow:0 30px 60px -24px rgba(0,0,0,.8)}
.tag{display:flex;align-items:center;gap:10px;font-size:22px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;opacity:.85;margin-bottom:10px}
.inv{position:absolute;width:300px;height:380px;border-radius:14px;background:#f3f1fb;color:#121125;padding:30px;box-shadow:0 30px 60px -20px rgba(0,0,0,.8)}
.inv b{font-size:30px}.inv .bar{display:block;height:16px;border-radius:8px;background:#d6d2ea;margin-top:18px}
.clock{position:absolute;width:240px;height:240px;border-radius:50%;border:10px solid #f3f1fb;background:#1b1638}
.clock i{position:absolute;left:50%;bottom:50%;width:10px;margin-left:-5px;border-radius:5px;background:#f3f1fb;transform-origin:50% 100%}
.note{position:absolute;width:270px;height:220px;background:#ffd84d;color:#2a2550;font-size:30px;font-weight:700;padding:28px;transform:rotate(6deg);box-shadow:0 30px 60px -20px rgba(0,0,0,.7)}
.mag{position:absolute;width:220px;height:220px;border-radius:50%;border:16px solid #f3f1fb;background:rgba(255,255,255,.08)}
.mag:after{content:"";position:absolute;right:-70px;bottom:-40px;width:100px;height:26px;border-radius:13px;background:#f3f1fb;transform:rotate(40deg)}
.close .content{justify-content:center}
.close h1{font-size:108px;line-height:1}
.close p{margin-top:40px;font-size:38px;color:var(--soft);font-weight:300;max-width:860px;line-height:1.4}
.close .cta{margin-top:64px;align-self:flex-start;padding:28px 46px;border-radius:999px;background:#265ADF;font-size:36px;font-weight:600}
"""

FILES = ["orcamento.xlsx", "orcamento_FINAL.xlsx", "orcamento_FINAL_v2.xlsx", "orcamento_FINAL_v3_agora_sim.xlsx"]
ART_FILES = f"""<div class="art"><div class="card" style="left:0;right:40px;top:20px">
{"".join(f'<div class="row{" on" if i == 3 else ""}"><i></i>{f}</div>' for i, f in enumerate(FILES))}</div>
<div class="bubble" style="right:0;bottom:0;background:#ff4d6d">Qual é a certa? 🤔</div></div>"""

ART_NIGHT = """<div class="art">
<div class="clock" style="left:0;top:40px"><i style="height:70px;transform:rotate(-30deg)"></i><i style="height:96px;width:8px;margin-left:-4px;transform:rotate(0deg)"></i></div>
<span style="position:absolute;left:30px;top:310px;font-size:72px;font-weight:700;color:#f3f1fb">23:00</span>
<div class="inv" style="left:420px;top:60px;transform:rotate(-6deg)"><b>Fatura</b><span class="bar" style="width:80%"></span><span class="bar" style="width:60%"></span><span class="bar" style="width:70%"></span></div>
<div class="inv" style="left:540px;top:120px;transform:rotate(5deg)"><b>Fatura</b><span class="bar" style="width:80%"></span><span class="bar" style="width:55%"></span><span class="bar" style="width:65%"></span></div>
<svg viewBox="0 0 24 24" width="90" height="90" style="position:absolute;left:330px;top:0" fill="#c9c3e6"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5"/></svg></div>"""

ART_CHANNELS = """<div class="art">
<div class="bubble" style="left:0;top:10px;background:#1f8a4c"><div class="tag">WhatsApp</div>Olá! Qual é o preço?</div>
<div class="bubble" style="right:0;top:190px;background:#1b1638;border:1px solid rgba(255,255,255,.16)"><div class="tag">Email</div>Assunto: Preço?</div>
<div class="bubble" style="left:60px;top:380px;background:#265ADF"><div class="tag">Chamada recebida</div>"Era só para saber o preço…"</div></div>"""

ART_WHERE = """<div class="art">
<div class="card" style="left:0;top:30px;width:400px;height:220px"><div class="row"><i style="background:var(--blue)"></i>Encomenda nº 87</div><div class="row" style="border:0">Re: Re: Fwd: encomenda</div></div>
<div class="note" style="left:470px;top:0">Ver encomenda?!</div>
<div class="inv" style="left:90px;top:300px;width:330px;height:240px;transform:rotate(-4deg);background:repeating-linear-gradient(#f3efe2 0 44px,#c9d6f0 44px 46px)"><b style="font-style:italic">Caderno</b></div>
<div class="mag" style="left:560px;top:280px"></div></div>"""

ART_COVER = """<div class="art" style="height:520px">
<div class="card" style="left:0;top:40px;width:400px;white-space:nowrap;padding:24px 28px;font-size:24px;color:var(--soft);transform:rotate(-6deg)">📄 orcamento_FINAL_v3.xlsx</div>
<div class="bubble" style="left:420px;top:0;background:#1f8a4c;transform:rotate(4deg)">Qual é o preço?</div>
<div class="inv" style="left:120px;top:200px;width:260px;height:300px;transform:rotate(5deg)"><b>Fatura</b><span class="bar"></span><span class="bar" style="width:60%"></span></div>
<div class="note" style="left:560px;top:230px">Onde está a encomenda?</div></div>"""


def slide(title, note, art):
    return f'<div class="s"><h1>{title}</h1><p>{note}</p></div>{art}'


SLIDES = [
    ("cover", f"""<span class="eyebrow"><i></i>Conhece?</span><h1>Só quem gere uma empresa <em>conhece</em>.</h1>
<p class="lead">Deslize e conte quantas já lhe aconteceram. 👉</p>{ART_COVER}"""),
    ("", slide("“orcamento_FINAL_v3<br><em>_agora_sim.xlsx</em>”", "Três versões do mesmo ficheiro, e nenhuma é a certa.", ART_FILES)),
    ("", slide("Faturas <em>às 23h</em>.", "Quando o dia acaba, começa a papelada.", ART_NIGHT)),
    ("", slide("O mesmo cliente, <em>três canais</em>.", "Pergunta o preço por WhatsApp, por email e por telefone.", ART_CHANNELS)),
    ("", slide("“Onde está aquela <em>encomenda</em>?”", "Está num email, num caderno ou na memória de alguém.", ART_WHERE)),
    ("close", """<h1>Há uma forma <em>mais simples</em>.</h1>
<p>Na HiveCode Business, juntamos clientes, encomendas e faturação num só sistema.</p>
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
