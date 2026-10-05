import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from build_week import ASSETS
from components import write_slides

CSS = """
.big{font-size:300px;font-weight:700;line-height:.9;letter-spacing:-.05em;margin-top:40px;color:var(--violet)}
.big small{font-size:90px;color:var(--ink);letter-spacing:-.02em}
.phone{margin:40px auto 0;width:360px;border-radius:52px;padding:14px;background:#0d0b1c;border:2px solid rgba(255,255,255,.18);
box-shadow:0 40px 90px -30px rgba(72,119,254,.6)}
.phone img{display:block;width:100%;border-radius:40px}
.list{margin-top:50px;display:flex;flex-direction:column;gap:18px;font-size:38px}
.list span{display:flex;gap:22px;align-items:center}
.list i{width:16px;height:16px;transform:rotate(30deg);background:linear-gradient(135deg,var(--pink),var(--blue));
clip-path:polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%)}
"""


def art(name):
    return f'<div class="art"><img src="{ASSETS}/{name}" alt=""></div>'


def question(n, title, note, visual):
    return f"""<span class="eyebrow"><i></i>Pergunta {n} de 5</span>
<h1>{title}</h1><p class="note">{note}</p>{visual}"""


SLIDES = [
    """<span class="eyebrow"><i></i>Guia rápido</span>
<div class="big">5<small> segundos</small></div>
<h1>5 perguntas a que o seu site deve <em>responder de imediato</em>.</h1>""",
    question(1, "O que <em>faz</em>?", "O título deve indicar com clareza o que a empresa faz, na linguagem do cliente.", art("crop-title.png")),
    question(2, "Para <em>quem</em>?", "O visitante deve perceber de imediato se o serviço se dirige a si.", art("crop-for.png")),
    question(3, "Porque <em>confiar</em>?", "Projetos reais e um processo claro transmitem mais confiança do que qualquer promessa.", art("crop-method.png")),
    question(4, "Como <em>falar consigo</em>?", "O contacto deve estar visível em todas as páginas.", art("crop-contact.png")),
    question(
        5,
        "Está adaptado ao <em>telemóvel</em>?",
        "Grande parte das visitas é feita a partir do telemóvel. O site deve estar preparado, em primeiro lugar, para esse ecrã.",
        f'<div class="phone"><img src="{ASSETS}/crop-mobile.png" alt=""></div>',
    ),
    """<span class="eyebrow"><i></i>Avaliação</span>
<h1>O seu site responde <em>a todas</em>?</h1>
<div class="list"><span><i></i>O que faz</span><span><i></i>Para quem</span><span><i></i>Porque confiar</span>
<span><i></i>Como falar consigo</span><span><i></i>Adaptado ao telemóvel</span></div>
<span class="cta">Fale connosco em hivecode.pt</span>""",
]

write_slides(Path(__file__).resolve().parent, SLIDES, CSS)
print("ok")
