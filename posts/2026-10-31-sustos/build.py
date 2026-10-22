"""5 sustos de quem tem um negócio online (Halloween), spooky theme: near-black and pumpkin orange.
One drawn screen per scare; close with a sober way out.
"""
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from build_week import page

HERE = Path(__file__).resolve().parent

CSS = """
.count{position:absolute;top:96px;right:88px;font-size:24px;color:var(--muted);letter-spacing:.1em}
.num{font-size:200px;font-weight:700;line-height:.8;letter-spacing:-.06em;color:transparent;-webkit-text-stroke:3px var(--violet)}
.cover h1{font-size:98px;margin-top:30px}
.s h1{font-size:80px;margin-top:26px}
.s p{margin-top:22px;font-size:34px;line-height:1.42;color:var(--soft);font-weight:300;max-width:880px}
.art{margin-top:50px;position:relative;height:500px}
.win{position:absolute;border-radius:24px;background:#1a1916;border:1px solid rgba(255,255,255,.12);overflow:hidden;box-shadow:0 40px 80px -30px rgba(255,138,31,.35)}
.win .bar{height:56px;background:#24221e;display:flex;align-items:center;gap:10px;padding:0 22px}
.win .bar b{width:14px;height:14px;border-radius:50%;background:#3d3a33}
.url{margin-left:16px;flex:1;height:36px;border-radius:18px;background:#0B0B0B;display:flex;align-items:center;gap:10px;padding:0 18px;font-size:20px;color:#bdb6a8}
.tomb{position:absolute;bottom:0;width:250px;border-radius:125px 125px 10px 10px;background:#1f1d19;border:2px solid #3d3a33;display:flex;align-items:center;justify-content:center;text-align:center;font-size:30px;font-weight:600;color:#bdb6a8;padding:40px 20px 0}
.row{display:flex;align-items:center;gap:18px;padding:20px 26px;border-bottom:1px solid rgba(255,255,255,.07);font-size:26px;color:#bdb6a8}
.row i{width:16px;height:16px;border-radius:50%;background:#3d3a33;flex:none}
.close .content{justify-content:center}
.close h1{font-size:104px;line-height:1}
.close p{margin-top:40px;font-size:38px;color:var(--soft);font-weight:300;max-width:860px;line-height:1.4}
.close .cta{margin-top:64px;align-self:flex-start;padding:28px 46px;border-radius:999px;background:#FF8A1F;color:#0B0B0B;font-size:36px;font-weight:600}
"""


def win(url, inner, pos, warn=False):
    lock = '<span style="color:#e5484d">⚠ Não seguro</span> ·' if warn else ""
    return (f'<div class="win" style="{pos}"><div class="bar"><b></b><b></b><b></b>'
            f'<span class="url">{lock} {url}</span></div>{inner}</div>')


COVER_ART = """<div class="art" style="height:470px;margin-top:40px">
<div class="tomb" style="left:0;height:330px">Site<br>em baixo</div>
<div class="tomb" style="left:327px;height:420px">Domínio<br>expirado</div>
<div class="tomb" style="right:0;height:300px">Sem<br>backup</div>
<span style="position:absolute;right:20px;top:0;font-size:120px">🎃</span></div>"""

DOWN = f"""<div class="art">{win("www.o-seu-negocio.pt", '''<div style="padding:70px 40px;text-align:center">
<div style="font-size:120px;font-weight:700;color:#FF8A1F;letter-spacing:-.04em">503</div>
<div style="font-size:34px;color:#bdb6a8;margin-top:10px">Este site não está disponível.</div></div>''', "left:0;right:0;top:20px")}</div>"""

DOMAIN = """<div class="art">
<div class="win" style="left:0;right:80px;top:10px;padding:34px 38px">
<div style="font-size:22px;color:#7d776c;letter-spacing:.08em;text-transform:uppercase">Email · há 32 dias</div>
<div style="font-size:36px;font-weight:700;margin-top:16px">O seu domínio expira amanhã</div>
<div style="font-size:26px;color:#bdb6a8;margin-top:10px">Renove para manter o site e o email a funcionar.</div></div>
<div style="position:absolute;left:220px;top:280px;transform:rotate(-5deg);padding:34px 46px;background:#FF8A1F;color:#0B0B0B;border-radius:12px;font-size:44px;font-weight:700;box-shadow:0 30px 60px -20px rgba(0,0,0,.8)">
Domínio à venda 🏷️</div></div>"""

INSECURE = f"""<div class="art">{win("www.o-seu-negocio.pt", '''<div style="padding:50px 40px;display:flex;gap:30px;align-items:center">
<div style="width:140px;height:140px;border-radius:50%;background:rgba(229,72,77,.15);display:grid;place-items:center;font-size:76px;flex:none">⚠</div>
<div style="font-size:34px;line-height:1.35;color:#bdb6a8">A ligação a este site <b style="color:#F6F1E7">não é segura</b>. Não introduza dados de pagamento.</div></div>''', "left:0;right:0;top:20px", warn=True)}</div>"""

ROWS = ["Promoção: −50% em tudo", "Newsletter semanal", "Fatura de eletricidade", "Lembrete de reunião", "Promoção: só hoje!"]
LOST = f"""<div class="art"><div class="win" style="left:0;right:0;top:0">
<div class="bar"><span class="url">Caixa de entrada · 1 284 por ler</span></div>
{"".join(f'<div class="row"><i></i>{r}</div>' for r in ROWS)}
<div class="row" style="opacity:.35;border:0"><i style="background:#FF8A1F"></i>Encomenda nº 214 · urgente</div></div></div>"""

BACKUP = """<div class="art">
<div class="win" style="left:0;right:0;top:20px;padding:44px 44px">
<div style="font-size:30px;color:#bdb6a8">A restaurar cópia de segurança…</div>
<div style="height:24px;border-radius:12px;background:#24221e;margin-top:26px;overflow:hidden"><div style="width:0%;height:100%;background:#FF8A1F"></div></div>
<div style="display:flex;justify-content:space-between;margin-top:30px;font-size:30px"><span style="color:#e5484d;font-weight:600">Nenhuma cópia encontrada</span><span style="color:#7d776c">0 ficheiros</span></div></div></div>"""


def scare(n, title, text, art):
    return f'<div class="s"><div class="num">{n}</div><h1>{title}</h1><p>{text}</p></div>{art}'


SLIDES = [
    ("cover", f"""<span class="eyebrow"><i></i>Halloween</span>
<h1>5 sustos de quem tem um <em>negócio online</em>.</h1>
<p class="lead">Nenhum tem fantasmas. Todos acontecem. 👉</p>{COVER_ART}"""),
    ("", scare(1, "O site <em>em baixo</em>.", "Logo no dia em que mais clientes o procuram.", DOWN)),
    ("", scare(2, "O domínio <em>expirou</em>.", "O aviso ficou esquecido no email, e agora outra pessoa pode comprá-lo.", DOMAIN)),
    ("", scare(3, "“Não <em>seguro</em>”.", "O aviso do browser que faz o cliente fechar a página.", INSECURE)),
    ("", scare(4, "A encomenda <em>perdida</em>.", "Entre promoções e newsletters, ninguém a viu a tempo.", LOST)),
    ("", scare(5, "Sem <em>cópia de segurança</em>.", "Um erro, e anos de trabalho desaparecem.", BACKUP)),
    ("close", """<h1>Um site bem cuidado deixa os sustos <em>lá fora</em>.</h1>
<p>Fale connosco e veja como evitar cada um deles.</p>
<span class="cta">hivecode.pt</span>"""),
]

if __name__ == "__main__":
    shutil.rmtree(HERE / "slides", ignore_errors=True)
    for n, (cls, body) in enumerate(SLIDES, 1):
        d = HERE / "slides" / f"{n:02d}"
        d.mkdir(parents=True)
        html = page(f'<span class="count">{n}/{len(SLIDES)}</span>' + body, CSS, theme="spooky")
        if cls:
            html = html.replace("<body>", f'<body class="{cls}">', 1)
        (d / "post.html").write_text(html, encoding="utf-8")
    print("ok")
