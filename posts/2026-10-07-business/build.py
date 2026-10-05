import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from components import diagram, write_slides

HERE = Path(__file__).resolve().parent

CSS = """
h1{font-size:92px}
.scatter{margin-top:70px;display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.scatter div{display:flex;flex-direction:column;align-items:center;gap:22px;padding:44px 20px;border-radius:26px;
background:rgba(255,255,255,.05);border:1px dashed rgba(201,195,230,.4);font-size:34px;font-weight:500;text-align:center}
.scatter svg{width:96px;height:96px}
.big-note{margin-top:60px;font-size:44px;line-height:1.35;color:var(--soft);font-weight:300;max-width:880px}
.big-note strong{color:var(--ink);font-weight:600}
"""

ICON = {
    "sheet": '<svg viewBox="0 0 24 24" fill="none" stroke="#c9c3e6" stroke-width="1.5"><rect x="4" y="3" width="16" height="18" rx="2"/><path d="M4 9h16M4 15h16M10 3v18"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="#c9c3e6" stroke-width="1.5"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
    "paper": '<svg viewBox="0 0 24 24" fill="none" stroke="#c9c3e6" stroke-width="1.5"><path d="M6 3h9l3 3v15H6z"/><path d="M9 10h6M9 14h6M9 18h4"/></svg>',
}

SLIDES = [
    f"""<span class="eyebrow"><i></i>HiveCode Business</span>
<h1>A informação da sua empresa está <em>espalhada</em>?</h1>
<div class="scatter"><div>{ICON["sheet"]}Folhas de cálculo</div><div>{ICON["mail"]}Emails</div><div>{ICON["paper"]}Papéis</div></div>""",
    """<span class="eyebrow"><i></i>A solução</span>
<h1>Reunimos tudo <em>num só lugar</em>.</h1>"""
    + diagram(["Clientes", "Encomendas", "Stock", "Faturas"], center="A sua empresa"),
    """<span class="eyebrow"><i></i>O resultado</span>
<h1>Menos tempo a copiar dados. <em>Mais tempo para o negócio.</em></h1>
<p class="big-note">Um sistema feito à medida, <strong>adaptado à forma como a sua empresa trabalha</strong>.</p>""",
    """<span class="eyebrow"><i></i>HiveCode Business</span>
<h1>Fale <em>connosco</em>.</h1>
<p class="big-note">Respondemos em 24 horas, sem compromisso.</p>
<span class="cta">hivecode.pt/business</span>""",
]

# Drop slides from the previous, longer version before writing the new ones.
shutil.rmtree(HERE / "slides", ignore_errors=True)
write_slides(HERE, SLIDES, CSS)
print("ok")
