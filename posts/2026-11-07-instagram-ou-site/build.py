"""Já tenho Instagram. Preciso de um site? Blue theme: what Instagram does well, what only a site
gives (Google, orders, your own rules), and why both work together.
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
.s h1{font-size:84px;margin-top:0}
.s p{margin-top:22px;font-size:34px;line-height:1.42;color:var(--soft);font-weight:300;max-width:880px}
.art{margin-top:56px;position:relative;height:560px}
.w{position:absolute;border-radius:28px;background:#fff;color:#121125;box-shadow:0 40px 80px -30px rgba(10,20,80,.75);overflow:hidden}
.ph{width:300px;height:560px;border-radius:44px;border:12px solid #121125;background:#fff}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:4px;padding:4px}
.grid i{aspect-ratio:1;background:linear-gradient(150deg,#FFD84D,#ff9f43)}
.grid i:nth-child(3n+2){background:linear-gradient(150deg,#9fb6ff,#265ADF)}
.grid i:nth-child(4n){background:linear-gradient(150deg,#ffb3c7,#e5484d)}
.pf{display:flex;align-items:center;gap:14px;padding:22px 18px 14px;font-size:22px;font-weight:700}
.pf b{width:56px;height:56px;border-radius:50%;background:linear-gradient(135deg,#FFD84D,#e5484d);flex:none}
.bar{height:46px;background:#eef1fb;display:flex;align-items:center;gap:9px;padding:0 18px}
.bar b{width:13px;height:13px;border-radius:50%;background:#c9d3f5}
.btn{display:inline-block;padding:16px 26px;border-radius:14px;background:#265ADF;color:#fff;font-size:24px;font-weight:600}
.btn.g{background:#eef1fb;color:#265ADF}
.chip{display:inline-flex;align-items:center;gap:10px;padding:10px 18px;border-radius:999px;background:#dff5e8;color:#127a43;font-size:22px;font-weight:600}
.res{padding:22px 28px;border-bottom:2px solid #eef1fb}
.res small{display:block;font-size:20px;color:#127a43}.res b{display:block;font-size:30px;color:#1a3fb0;margin-top:4px}.res span{font-size:22px;color:#6b6685}
.close .content{justify-content:center}
.close h1{font-size:108px;line-height:1}
.close p{margin-top:40px;font-size:38px;color:var(--soft);font-weight:300;max-width:860px;line-height:1.4}
.close .cta{margin-top:64px;align-self:flex-start;padding:28px 46px;border-radius:999px;background:#fff;color:#265ADF;font-size:36px;font-weight:700}
"""

PHONE = """<div class="w ph" style="{pos}"><div class="pf"><b></b>o_seu_salao</div><div class="grid">{tiles}</div></div>"""
TILES = "<i></i>" * 12
BROWSER = """<div class="w" style="{pos}"><div class="bar"><b></b><b></b><b></b></div>
<div style="height:170px;background:linear-gradient(150deg,#f7c6d9,#b45bd6);display:grid;place-items:center;font-size:80px">💇</div>
<div style="padding:22px 26px;display:flex;flex-direction:column;gap:14px"><b style="font-size:30px">Salão do Bairro</b><span class="chip">● Aberto · 9h–19h</span>
<div style="display:flex;gap:10px"><span class="btn">Marcar</span><span class="btn g">Direções</span></div></div></div>"""

COVER_ART = f"""<div class="art" style="height:600px;margin-top:40px">
{PHONE.format(pos="left:40px;top:20px;transform:rotate(-5deg)", tiles=TILES)}
{BROWSER.format(pos="left:400px;top:90px;width:500px;transform:rotate(3deg)")}
<span style="position:absolute;left:330px;top:250px;width:110px;height:110px;border-radius:50%;background:#FFD84D;color:#121125;display:grid;place-items:center;font-size:56px;font-weight:800;box-shadow:0 20px 40px -10px rgba(0,0,0,.4)">+</span></div>"""

SHOWS = f"""<div class="art">{PHONE.format(pos="left:60px;top:0", tiles=TILES)}
<div class="w" style="left:420px;top:60px;padding:28px 34px;font-size:30px;font-weight:600">❤️ 128 gostos</div>
<div class="w" style="left:460px;top:200px;padding:28px 34px;font-size:30px;font-weight:600">💬 “Que corte bonito!”</div>
<div class="w" style="left:420px;top:340px;padding:28px 34px;font-size:30px;font-weight:600">👀 Novos seguidores</div></div>"""

GOOGLE = """<div class="art"><div class="w" style="left:0;right:0;top:0">
<div style="padding:26px 30px;display:flex;align-items:center;gap:18px;font-size:32px;color:#4a4560;border-bottom:2px solid #eef1fb">
<svg viewBox="0 0 24 24" width="38" height="38" fill="none" stroke="#4a4560" stroke-width="2.4" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/></svg>cabeleireiro perto de mim</div>
<div class="res"><small>salao-exemplo.pt</small><b>Salão Central · Marcações online</b><span>Aberto · 350 m</span></div>
<div class="res"><small>barbearia-exemplo.pt</small><b>Barbearia Avenida · Preços e horário</b><span>Aberto · 600 m</span></div>
<div class="res" style="border:0;opacity:.45"><small>Publicações raramente aparecem</small><b style="color:#6b6685">@o_seu_salao</b><span>—</span></div></div></div>"""

SELLS = f"""<div class="art">{BROWSER.format(pos="left:0;top:0;width:560px")}
<div class="w" style="left:600px;top:40px;padding:26px 30px;font-size:28px;font-weight:600">🕘 Horário</div>
<div class="w" style="left:620px;top:170px;padding:26px 30px;font-size:28px;font-weight:600">📍 Morada</div>
<div class="w" style="left:600px;top:300px;padding:26px 30px;font-size:28px;font-weight:600">💶 Preços</div>
<div class="w" style="left:620px;top:430px;padding:26px 30px;font-size:28px;font-weight:600">📅 Marcações</div></div>"""

OWN = """<div class="art">
<div class="w" style="left:0;top:20px;width:430px;padding:36px 38px"><div style="font-size:24px;color:#6b6685;letter-spacing:.08em;text-transform:uppercase">Instagram</div>
<div style="font-size:38px;font-weight:700;margin-top:14px;line-height:1.2">O algoritmo decide quem vê.</div>
<svg viewBox="0 0 200 80" width="350" height="140" style="margin-top:20px"><polyline points="0,15 50,30 100,22 150,55 200,70" fill="none" stroke="#e5484d" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
<div class="w" style="left:474px;top:20px;width:430px;padding:36px 38px"><div style="font-size:24px;color:#6b6685;letter-spacing:.08em;text-transform:uppercase">O seu site</div>
<div style="font-size:38px;font-weight:700;margin-top:14px;line-height:1.2">O endereço e as regras são seus.</div>
<div style="margin-top:34px;padding:18px 22px;border-radius:14px;background:#eef1fb;font-size:24px;font-weight:600;color:#265ADF;white-space:nowrap">www.o-seu-negocio.pt</div></div></div>"""


def slide(title, text, art):
    return f'<div class="s"><h1>{title}</h1><p>{text}</p></div>{art}'


SLIDES = [
    ("cover", f"""<span class="eyebrow"><i></i>Instagram e site</span>
<h1>Já tenho Instagram. <em>Preciso de um site?</em></h1>
<p class="lead">A resposta curta é sim. Deslize. 👉</p>{COVER_ART}"""),
    ("", slide("O Instagram <em>mostra</em>.", "Fotografias, novidades e o dia a dia do negócio. É ótimo para ser descoberto.", SHOWS)),
    ("", slide("Mas não aparece no <em>Google</em>.", "Quem pesquisa “cabeleireiro perto de mim” encontra sobretudo sites, não publicações.", GOOGLE)),
    ("", slide("O site <em>vende</em>.", "Horário, morada, preços e marcações, tudo num só lugar.", SELLS)),
    ("", slide("E é <em>seu</em>.", "No Instagram, o alcance muda de um dia para o outro. O site está sempre lá.", OWN)),
    ("close", """<h1>Os dois juntos <em>funcionam melhor</em>.</h1>
<p>O Instagram traz pessoas. O site transforma-as em clientes.</p>
<span class="cta">hivecode.pt</span>"""),
]

if __name__ == "__main__":
    shutil.rmtree(HERE / "slides", ignore_errors=True)
    for n, (cls, body) in enumerate(SLIDES, 1):
        d = HERE / "slides" / f"{n:02d}"
        d.mkdir(parents=True)
        html = page(f'<span class="count">{n}/{len(SLIDES)}</span>' + body, CSS, theme="blue")
        if cls:
            html = html.replace("<body>", f'<body class="{cls}">', 1)
        (d / "post.html").write_text(html, encoding="utf-8")
    print("ok")
