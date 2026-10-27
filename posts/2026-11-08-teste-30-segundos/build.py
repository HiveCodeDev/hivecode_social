"""Teste de 30 segundos: o seu site está a perder clientes? Paper theme: five yes/no questions,
one drawn hint each, then the free mockup and quote offer.
"""
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from build_week import page

HERE = Path(__file__).resolve().parent

CSS = """
.count{position:absolute;top:96px;right:88px;font-size:24px;color:var(--muted);letter-spacing:.1em}
.cover h1{font-size:100px;margin-top:30px}
.qn{font-size:30px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--violet)}
.s h1{font-size:76px;margin-top:22px}
.s p{margin-top:22px;font-size:34px;line-height:1.42;color:var(--soft);font-weight:300;max-width:880px}
.art{margin-top:50px;position:relative;height:500px}
.card{position:absolute;border-radius:28px;background:#fff;color:#121125;box-shadow:0 30px 60px -28px rgba(18,17,37,.45)}
.yn{position:absolute;left:0;bottom:0;display:flex;gap:22px}
.yn span{padding:24px 54px;border-radius:999px;font-size:38px;font-weight:700;border:3px solid #121125}
.yn .y{background:#121125;color:#F6F1E7}
.box{display:flex;align-items:center;gap:22px;padding:18px 0;font-size:32px;border-bottom:2px solid #efe9dc}
.box i{width:46px;height:46px;border-radius:10px;border:3px solid #121125;flex:none}
.close .content{justify-content:center}
.close h1{font-size:104px;line-height:1}
.close p{margin-top:36px;font-size:38px;color:var(--soft);font-weight:300;max-width:860px;line-height:1.4}
.offer{margin-top:50px;padding:34px 40px;border-radius:26px;background:#fff;color:#121125;font-size:36px;font-weight:600;max-width:860px;box-shadow:0 30px 60px -28px rgba(18,17,37,.45)}
.close .cta{margin-top:40px;align-self:flex-start;padding:28px 46px;border-radius:999px;background:#265ADF;color:#fff;font-size:36px;font-weight:600}
"""

YN = '<div class="yn"><span class="y">Sim</span><span>Não</span></div>'

COVER_ART = """<div class="card" style="position:relative;margin-top:50px;padding:20px 40px;max-width:760px">""" + "".join(
    f'<div class="box"{" style=\"border:0\"" if i == 4 else ""}><i></i>{t}</div>'
    for i, t in enumerate(["Rápido no telemóvel", "Contacto à vista", "Fácil de ler", "Aparece no Google", "Atualizado"])) + "</div>"

HINTS = [
    """<div class="card" style="left:0;top:0;width:520px;padding:34px 40px"><div style="font-size:26px;color:#8a8499">A carregar…</div>
<div style="height:22px;border-radius:11px;background:#efe9dc;margin-top:20px;overflow:hidden"><div style="width:35%;height:100%;background:#e5484d"></div></div>
<div style="font-size:64px;font-weight:800;margin-top:24px;color:#e5484d">7 s</div></div>""",
    """<div class="card" style="left:0;top:0;width:620px;padding:30px 36px;display:flex;gap:16px;flex-wrap:wrap">
<span style="padding:16px 24px;border-radius:14px;background:#265ADF;color:#fff;font-size:28px;font-weight:600">📞 Ligar</span>
<span style="padding:16px 24px;border-radius:14px;background:#eef1fb;color:#265ADF;font-size:28px;font-weight:600">🕘 9h–19h</span>
<span style="padding:16px 24px;border-radius:14px;background:#eef1fb;color:#265ADF;font-size:28px;font-weight:600">📍 Morada</span></div>""",
    """<div class="card" style="left:0;top:0;width:300px;height:330px;padding:24px;font-size:13px;color:#8a8499;line-height:1.4">Texto muito pequeno que obriga o visitante a aumentar o ecrã para conseguir ler o que a empresa faz…</div>
<div class="card" style="left:340px;top:0;width:300px;height:330px;padding:28px;font-size:34px;font-weight:700;line-height:1.25">Lê-se à primeira.</div>""",
    """<div class="card" style="left:0;top:0;width:700px;padding:26px 32px;display:flex;align-items:center;gap:18px;font-size:32px;color:#4a4560">
<svg viewBox="0 0 24 24" width="38" height="38" fill="none" stroke="#4a4560" stroke-width="2.4" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/></svg>o seu serviço + a sua cidade</div>""",
    """<div class="card" style="left:0;top:0;width:420px;padding:30px 36px"><div style="font-size:26px;color:#8a8499">Última atualização</div>
<div style="font-size:56px;font-weight:800;margin-top:10px">março de 2021</div></div>""",
]

QUESTIONS = [
    ("Abre em menos de <em>3 segundos</em> no telemóvel?", "Muitas visitas desistem antes de a página abrir."),
    ("O horário e o contacto estão <em>à vista</em>?", "Sem ter de procurar em menus ou no rodapé."),
    ("Lê-se bem no telemóvel, <em>sem zoom</em>?", "Letra pequena e botões apertados afastam visitas."),
    ("Aparece no <em>Google</em> quando pesquisa o seu serviço?", "Experimente: o seu serviço e a sua cidade."),
    ("Foi atualizado nos <em>últimos 6 meses</em>?", "Preços, fotografias e horários antigos geram desconfiança."),
]


def question(n, title, note, hint):
    return (f'<div class="s"><div class="qn">Pergunta {n} de 5</div><h1>{title}</h1><p>{note}</p></div>'
            f'<div class="art">{hint}{YN}</div>')


SLIDES = [("cover", f"""<span class="eyebrow"><i></i>Teste de 30 segundos</span>
<h1>O seu site está a <em>perder clientes</em>?</h1>
<p class="lead">Responda sim ou não e conte os “não”. 👉</p>{COVER_ART}""")]
SLIDES += [("", question(n, t, p, h)) for n, ((t, p), h) in enumerate(zip(QUESTIONS, HINTS), 1)]
SLIDES += [("close", """<h1>Contou algum <em>não</em>?</h1>
<p>Cada “não” pode ser um cliente a escolher outra empresa.</p>
<div class="offer">🎁 Peça um mockup e um orçamento gratuitos, sem compromisso.</div>
<span class="cta">hivecode.pt</span>""")]

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
