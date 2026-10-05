"""5 perguntas: redesign without screenshots.

Each question gets a drawn illustration and a large numeral as anchor; the
illustration alternates sides so the slides do not repeat one layout.
Kicker only on the cover (impeccable: no repeated kicker). Formal copy.
"""
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from build_week import page

HERE = Path(__file__).resolve().parent

CSS = """
.count{position:absolute;top:96px;right:88px;font-size:24px;color:var(--muted);letter-spacing:.1em}
.num{font-size:260px;font-weight:700;line-height:.8;letter-spacing:-.06em;color:var(--violet)}
.q h1{font-size:92px;margin-top:26px}
.q p{margin-top:26px;font-size:34px;line-height:1.42;color:var(--soft);font-weight:300;max-width:860px}
.art{margin-top:56px;height:430px;position:relative}
.panel{position:absolute;border-radius:26px;background:#1b1638;border:1px solid rgba(255,255,255,.14);box-shadow:0 40px 80px -36px rgba(72,119,254,.55)}
.bar{display:block;height:20px;border-radius:10px;background:rgba(255,255,255,.12)}
.hl{background:linear-gradient(90deg,var(--pink),var(--blue))}
.chip{display:inline-flex;align-items:center;gap:12px;padding:16px 26px;border-radius:999px;background:#1b1638;border:1px solid rgba(255,255,255,.16);font-size:30px;font-weight:500}
.chip i{width:14px;height:14px;border-radius:50%}
.btn{display:inline-flex;padding:20px 34px;border-radius:999px;background:#265ADF;font-size:28px;font-weight:600}
.cover .big{font-size:300px;font-weight:700;line-height:.9;letter-spacing:-.05em;margin-top:40px;color:var(--violet)}
.cover .big small{font-size:96px;color:var(--ink);letter-spacing:-.02em}
.cover h1{font-size:88px}
.close h1{font-size:96px}
.list{margin-top:50px;display:flex;flex-direction:column;gap:20px;font-size:40px}
.list span{display:flex;gap:24px;align-items:center}
.list b{width:52px;height:52px;border-radius:50%;display:grid;place-items:center;font-size:26px;background:linear-gradient(135deg,var(--pink),var(--blue))}
.close .cta{margin-top:60px;align-self:flex-start;padding:28px 46px;border-radius:999px;background:#265ADF;font-size:36px;font-weight:600}
"""

# 1. A browser window whose headline is highlighted: "say what you do".
ART1 = """<div class="art">
<div class="panel" style="inset:0 60px 0 0;padding:34px">
<div style="display:flex;gap:10px"><i class="bar" style="width:16px;height:16px;border-radius:50%"></i><i class="bar" style="width:16px;height:16px;border-radius:50%"></i><i class="bar" style="width:16px;height:16px;border-radius:50%"></i></div>
<div style="margin-top:50px;display:flex;flex-direction:column;gap:18px">
<span class="bar hl" style="height:44px;width:88%;border-radius:12px"></span>
<span class="bar hl" style="height:44px;width:64%;border-radius:12px"></span>
<span class="bar" style="width:72%;margin-top:22px"></span><span class="bar" style="width:58%"></span>
</div></div>
<span class="chip" style="position:absolute;right:0;bottom:40px;background:#265ADF;border:0">O que fazemos, numa frase</span>
</div>"""

# 2. One visitor at the centre of audience rings.
ART2 = """<div class="art" style="display:flex;align-items:center;justify-content:center">
<div style="position:absolute;width:420px;height:420px;border-radius:50%;border:2px dashed rgba(215,82,254,.35)"></div>
<div style="position:absolute;width:270px;height:270px;border-radius:50%;border:2px solid rgba(72,119,254,.45)"></div>
<svg viewBox="0 0 24 24" width="150" height="150" fill="none" stroke="#f3f1fb" stroke-width="1.4"><circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4.5 4.5-6.5 8-6.5s6.5 2 8 6.5"/></svg>
<span class="chip" style="position:absolute;left:0;top:30px"><i style="background:var(--pink)"></i>Empresas</span>
<span class="chip" style="position:absolute;right:0;top:120px"><i style="background:var(--blue)"></i>Clínicas</span>
<span class="chip" style="position:absolute;left:30px;bottom:40px"><i style="background:var(--blue)"></i>Lojas</span>
<span class="chip" style="position:absolute;right:30px;bottom:10px"><i style="background:var(--pink)"></i>Serviços</span>
</div>"""

# 3. Stacked project cards with a check seal.
ART3 = """<div class="art">
<div class="panel" style="left:120px;right:120px;top:60px;bottom:30px;transform:rotate(-5deg);opacity:.55"></div>
<div class="panel" style="left:80px;right:80px;top:30px;bottom:50px;transform:rotate(3deg);opacity:.8"></div>
<div class="panel" style="left:40px;right:40px;top:0;bottom:70px;padding:40px;display:flex;flex-direction:column;gap:18px">
<span class="bar hl" style="height:150px;border-radius:16px;opacity:.85"></span>
<span class="bar" style="width:60%"></span><span class="bar" style="width:40%"></span>
</div>
<div style="position:absolute;right:0;bottom:0;width:170px;height:170px;border-radius:50%;background:#265ADF;display:grid;place-items:center;box-shadow:0 0 0 12px rgba(38,90,223,.18)">
<svg viewBox="0 0 24 24" width="84" height="84" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></div>
</div>"""

# 4. The same contact button on three pages.
PAGE = """<div class="panel" style="position:relative;flex:1;height:380px;padding:24px;display:flex;flex-direction:column;gap:16px">
<div style="display:flex;justify-content:space-between;align-items:center"><span class="bar" style="width:70px"></span><span class="btn" style="padding:12px 18px;font-size:20px">Contacto</span></div>
<span class="bar" style="width:90%;margin-top:30px"></span><span class="bar" style="width:70%"></span><span class="bar" style="width:80%"></span></div>"""
ART4 = f"""<div class="art" style="display:flex;gap:22px;align-items:flex-start">{PAGE}{PAGE}{PAGE}
<svg viewBox="0 0 24 24" width="90" height="90" style="position:absolute;right:30px;top:40px" fill="#f3f1fb"><path d="M5 3l14 8-6 1.5L10 19z"/></svg>
</div>"""

# 5. A phone with a simplified layout.
ART5 = """<div class="art" style="display:flex;justify-content:center">
<div style="width:250px;height:440px;border-radius:44px;background:#0d0b1c;border:2px solid rgba(255,255,255,.2);padding:12px;box-shadow:0 40px 80px -30px rgba(215,82,254,.6)">
<div style="height:100%;border-radius:34px;background:#1b1638;padding:26px 20px;display:flex;flex-direction:column;gap:14px">
<span class="bar hl" style="height:30px;width:85%"></span><span class="bar hl" style="height:30px;width:60%"></span>
<span class="bar" style="width:90%;margin-top:12px;height:14px"></span><span class="bar" style="width:75%;height:14px"></span>
<span class="btn" style="margin-top:20px;align-self:flex-start;padding:14px 22px;font-size:20px">Contactar</span>
<span style="margin-top:auto;height:90px;border-radius:18px;background:rgba(255,255,255,.08)"></span></div></div>
</div>"""


def question(n, title, note, art):
    return f"""<div class="q"><div class="num">{n}</div><h1>{title}</h1><p>{note}</p></div>{art}"""


SLIDES = [
    ("cover", """<span class="eyebrow"><i></i>Guia rápido</span>
<div class="big">5<small> segundos</small></div>
<h1>5 perguntas a que o seu site deve <em>responder de imediato</em>.</h1>"""),
    ("", question(1, "O que <em>faz</em>?", "O título deve indicar com clareza o que a empresa faz, na linguagem do cliente.", ART1)),
    ("", question(2, "Para <em>quem</em>?", "O visitante deve perceber de imediato se o serviço se dirige a si.", ART2)),
    ("", question(3, "Porque <em>confiar</em>?", "Projetos reais e um processo claro transmitem mais confiança do que qualquer promessa.", ART3)),
    ("", question(4, "Como <em>falar consigo</em>?", "O contacto deve estar visível em todas as páginas.", ART4)),
    ("", question(5, "Está adaptado ao <em>telemóvel</em>?", "Grande parte das visitas é feita a partir do telemóvel. O site deve estar preparado para esse ecrã.", ART5)),
    ("close", """<h1>O seu site responde <em>a todas</em>?</h1>
<div class="list"><span><b>1</b>O que faz</span><span><b>2</b>Para quem</span><span><b>3</b>Porque confiar</span>
<span><b>4</b>Como falar consigo</span><span><b>5</b>Adaptado ao telemóvel</span></div>
<span class="cta">Fale connosco em hivecode.pt</span>"""),
]

shutil.rmtree(HERE / "slides", ignore_errors=True)
for n, (cls, body) in enumerate(SLIDES, 1):
    d = HERE / "slides" / f"{n:02d}"
    d.mkdir(parents=True)
    html = page(f'<span class="count">{n}/{len(SLIDES)}</span>' + body, CSS)
    if cls:
        html = html.replace("<body>", f'<body class="{cls}">', 1)
    (d / "post.html").write_text(html, encoding="utf-8")
print("ok")
