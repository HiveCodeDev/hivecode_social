"""Encontre os 3 erros: a fictional restaurant site on a phone hides three conversion mistakes.

Slide 1 is the puzzle; slides 2-4 reveal one error each as a before/after pair of large
details; slide 5 puts both phones side by side with numbered marks; slide 6 closes.
All drawn (no screenshots); the business is fictional ("Restaurante Exemplo").
"""
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1].parent / "tools"))
from build_week import page

HERE = Path(__file__).resolve().parent

CSS = """
.count{position:absolute;top:96px;right:88px;font-size:24px;color:var(--muted);letter-spacing:.1em}
.s h1{font-size:80px;margin-top:0}
.s p{margin-top:26px;font-size:34px;line-height:1.42;color:var(--soft);font-weight:300;max-width:880px}
.cover h1{font-size:96px;margin-top:34px}
.cover p.lead{margin-top:24px}
.close .content{justify-content:center}
.close h1{font-size:112px;line-height:1}
.close p{margin-top:40px;font-size:38px;color:var(--soft);font-weight:300;max-width:840px;line-height:1.4}
.close .cta{margin-top:64px;align-self:flex-start;padding:28px 46px;border-radius:999px;background:#265ADF;font-size:36px;font-weight:600}
.tag{display:inline-flex;align-items:center;gap:12px;font-size:26px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#ff6b85}
.tag i{width:16px;height:16px;border-radius:50%;background:#ff4d6d}
/* phone */
.ph{position:relative;width:300px;height:600px;border-radius:46px;background:#0d0b1c;border:2px solid rgba(255,255,255,.22);padding:12px;
box-shadow:0 40px 90px -30px rgba(215,82,254,.55);flex:none}
.scr{position:relative;width:276px;height:576px;border-radius:34px;background:#fff;overflow:hidden;color:#1d1d1d;font-family:Georgia,serif}
.scr>*{position:absolute;left:16px;right:16px}
.sb{top:6px;height:14px;display:flex;justify-content:space-between;font:600 10px Arial,sans-serif;color:#222}
.hd{top:28px;height:40px;display:flex;align-items:center;justify-content:space-between;font-size:17px;font-weight:700;color:#6b2d0f}
.hd b{display:flex;flex-direction:column;gap:3px}
.hd b i{display:block;width:20px;height:2px;background:#333}
.hero{top:76px;left:0;right:0;height:148px;background:linear-gradient(135deg,#f6b26b,#d9622b)}
.hero:after{content:"";position:absolute;left:50%;top:50%;width:96px;height:96px;margin:-48px 0 0 -48px;border-radius:50%;
background:radial-gradient(circle,#fff7ec 0 54%,#f3e3cf 55% 100%);box-shadow:0 10px 24px rgba(0,0,0,.25)}
.h3{top:238px;font-size:20px;font-weight:700;line-height:1.2}
.para{top:296px;font:9px/1.35 Arial,sans-serif;color:#cfcfcf}
.btn0{top:350px;left:16px;right:auto;padding:7px 14px;border-radius:4px;background:#e2e2e2;color:#8a8a8a;font:11px Arial,sans-serif}
.pfoot{top:552px;font:7.5px Arial,sans-serif;color:#c4c4c4;text-align:center}
.call{padding:7px 12px;border-radius:999px;background:#1f8a4c;color:#fff;font:700 12px Arial,sans-serif}
.paraok{top:296px;font:13px/1.4 Arial,sans-serif;color:#333}
.book{top:404px;padding:13px 0;border-radius:12px;background:#265ADF;color:#fff;text-align:center;font:700 16px Arial,sans-serif}
.pfootok{top:546px;font:10px Arial,sans-serif;color:#666;text-align:center}
.mark{position:absolute;border:4px solid #ff4d6d;border-radius:18px;box-shadow:0 0 0 6px rgba(255,77,109,.18)}
.num{position:absolute;width:44px;height:44px;border-radius:50%;background:#ff4d6d;color:#fff;font:700 24px 'Geologica',sans-serif;display:grid;place-items:center}
.okm{position:absolute;width:44px;height:44px;border-radius:50%;background:#2fbf71;display:grid;place-items:center}
/* before/after detail cards */
.pair{margin-top:56px;display:flex;gap:28px}
.card{flex:1;height:600px;border-radius:28px;background:#fff;position:relative;overflow:hidden;color:#1d1d1d}
.card .lb{position:absolute;left:22px;top:20px;padding:8px 18px;border-radius:999px;font:700 22px 'Geologica',sans-serif;color:#fff}
.card .bad{background:#ff4d6d}.card .good{background:#2fbf71}
.card .in{position:absolute;left:30px;right:30px;top:96px;bottom:30px}
.ghost{display:block;height:14px;border-radius:7px;background:#eee;margin-bottom:12px}
"""

XM = '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg>'
OK = '<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>'
PARA = "Bem-vindo ao nosso restaurante. Servimos pratos tradicionais portugueses, feitos com ingredientes frescos e muito cuidado, todos os dias ao almoço e ao jantar."


def phone(fixed=False, marks=False):
    top = '<div class="sb"><span>12:30</span><span>●●● 🔋</span></div>'
    if fixed:
        body = f"""<div class="hd" style="font-size:15px">Restaurante Exemplo<span class="call">Ligar</span></div><div class="hero"></div>
<div class="h3">Cozinha tradicional desde 1987</div><div class="paraok">{PARA}</div>
<div class="book">Reservar mesa</div><div class="pfootok">Rua Exemplo, 1 · Tel. 000 000 000</div>"""
    else:
        body = f"""<div class="hd">Restaurante Exemplo<b><i></i><i></i><i></i></b></div><div class="hero"></div>
<div class="h3">Cozinha tradicional desde 1987</div><div class="para">{PARA}</div>
<div class="btn0">Clique aqui</div><div class="pfoot">Rua Exemplo, 1 · Tel. 000 000 000</div>"""
    extra = ""
    if marks and not fixed:  # numbered rings around the three errors (screen offset 12px)
        for n, (x, y, w, h) in enumerate([(14, 554, 272, 34), (14, 298, 272, 62), (14, 352, 118, 44)], 1):
            extra += f'<span class="mark" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"></span>'
            extra += f'<span class="num" style="left:{x + w + 4}px;top:{y + h // 2 - 22}px">{n}</span>'
    if marks and fixed:
        for x, y in [(-24, 26), (-24, 296), (-24, 410)]:
            extra += f'<span class="okm" style="left:{x}px;top:{y}px">{OK}</span>'
    return f'<div class="ph"><div class="scr">{top}{body}</div>{extra}</div>'


def pair(before, after):
    return f"""<div class="pair">
<div class="card"><span class="lb bad">Antes</span><div class="in">{before}</div></div>
<div class="card"><span class="lb good">Depois</span><div class="in">{after}</div></div></div>"""


GHOSTS = '<span class="ghost" style="width:80%"></span><span class="ghost" style="width:60%"></span><span class="ghost" style="width:70%"></span>'

# Error 1: contact only in the tiny footer vs a call button in the header.
E1 = pair(
    f"""{GHOSTS}{GHOSTS}{GHOSTS}<div style="position:absolute;left:0;right:0;bottom:6px;text-align:center;font:11px Arial,sans-serif;color:#c4c4c4">Rua Exemplo, 1 · Tel. 000 000 000</div>
<span class="mark" style="left:-8px;right:-8px;bottom:-6px;height:36px"></span>""",
    f"""<div style="display:flex;align-items:center;justify-content:space-between;font:700 24px Georgia,serif;color:#6b2d0f">Restaurante<span class="call" style="font-size:22px;padding:12px 22px">Ligar</span></div>
<div style="margin-top:26px">{GHOSTS}{GHOSTS}</div>""",
)
# Error 2: light, tiny text vs readable text.
E2 = pair(
    f'<div style="font:13px/1.4 Arial,sans-serif;color:#d0d0d0">{PARA}</div>',
    f'<div style="font:22px/1.45 Arial,sans-serif;color:#2a2a2a">{PARA}</div>',
)
# Error 3: vague grey button vs a clear action.
E3 = pair(
    f"""{GHOSTS}<div style="margin-top:40px;display:inline-block;padding:14px 26px;border-radius:6px;background:#e2e2e2;color:#8a8a8a;font:20px Arial,sans-serif">Clique aqui</div>""",
    f"""{GHOSTS}<div style="margin-top:40px;padding:22px 0;border-radius:16px;background:#265ADF;color:#fff;text-align:center;font:700 28px Arial,sans-serif">Reservar mesa</div>""",
)


def step(n, title, note, art):
    return f"""<div class="s"><span class="tag"><i></i>Erro {n} de 3</span><h1 style="margin-top:22px">{title}</h1><p>{note}</p></div>{art}"""


SLIDES = [
    ("cover", f"""<div style="display:flex;gap:56px;align-items:center">
<div style="flex:1"><span class="eyebrow"><i></i>Desafio</span>
<h1>Consegue encontrar os <em>3 erros</em>?</h1>
<p class="lead">Este site tem três problemas que afastam clientes. Deslize para ver as respostas. 👉</p></div>
<div style="transform:rotate(3deg)">{phone()}</div></div>"""),
    ("", step(1, "O contacto está <em>escondido</em>.", "O telefone só aparece no fim da página, em letra pequena. O contacto deve estar visível logo no início.", E1)),
    ("", step(2, "O texto não se lê <em>no telemóvel</em>.", "Letra pequena e cinzento claro sobre branco. Com texto maior e bom contraste, lê-se sem esforço.", E2)),
    ("", step(3, "O botão não diz <em>o que faz</em>.", "“Clique aqui” não convida ninguém. “Reservar mesa” diz exatamente o que acontece.", E3)),
    ("", f"""<h1 style="font-size:88px;margin-top:0">Antes e <em>depois</em>.</h1><p style="margin-top:22px;font-size:34px;color:var(--soft);font-weight:300">Os três erros corrigidos.</p>
<div style="margin-top:40px;display:flex;justify-content:center;gap:60px;zoom:1.3">{phone(marks=True)}{phone(fixed=True, marks=True)}</div>"""),
    ("close", """<h1>Quantos <em>encontrou</em>?</h1>
<p>Se o site da sua empresa tem algum destes erros, fale connosco.</p>
<span class="cta">hivecode.pt</span>"""),
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
