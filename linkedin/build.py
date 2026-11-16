"""LinkedIn company page: first three posts (presentation, HiveCode Business, recent projects).

python linkedin/build.py
Writes <post>/slides/NN/post.html, renders them with tools/render.mjs, then joins multi-page posts
into <post>/documento.pdf (LinkedIn document carousel). Captions live in <post>/texto.txt.
Posted by hand on the HiveCode company page.
"""
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "tools"))
from build_week import ASSETS, page  # noqa: E402

CSS = """
.card{border-radius:28px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.14);padding:34px 38px}
.card b{display:block;font-size:40px;font-weight:600}
.card span{display:block;margin-top:10px;font-size:28px;line-height:1.4;color:var(--soft);font-weight:300}
.pill{display:inline-block;align-self:flex-start;margin-top:44px;padding:24px 38px;border-radius:999px;
background:linear-gradient(90deg,#D752FE,#4877FE);color:#fff;font-size:32px;font-weight:600}
.next{margin-top:40px;font-size:28px;color:var(--muted)}
.n{font-size:30px;font-weight:700;color:var(--violet);letter-spacing:.06em}
"""

# 1. Presentation (single image).
INTRO = [f"""<img src="{ASSETS}/logo_mark.svg" alt="" style="width:150px;height:150px">
<span class="eyebrow" style="margin-top:50px"><i></i>OlÃ¡, LinkedIn</span>
<h1>Sites e software Ã  medida para <em>empresas portuguesas</em>.</h1>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:56px">
<div class="card"><b>ðŸŒ Sites</b><span>RÃ¡pidos, fÃ¡ceis de encontrar no Google e pensados para o telemÃ³vel.</span></div>
<div class="card"><b>âš™ï¸ Business</b><span>Sistemas de gestÃ£o Ã  medida da forma como a sua empresa trabalha.</span></div></div>
<span class="pill">Mockup e orÃ§amento gratuitos</span>"""]

# 2. HiveCode Business (document).
CHAOS = ["Clientes.xlsx", "Encomendas no email", "Stock no caderno", "Faturas noutro programa", "RelatÃ³rios Ã  mÃ£o", "Dados copiados duas vezes"]
ORDER = ["Clientes", "Encomendas", "Stock", "FaturaÃ§Ã£o", "RelatÃ³rios"]
AREAS = [("ðŸ¤", "CRM Ã  medida", "Clientes, contactos, propostas e oportunidades num sÃ³ lugar."),
         ("ðŸ“¦", "ERP e gestÃ£o interna", "Encomendas, stock e faturaÃ§Ã£o ligados entre si."),
         ("ðŸ”", "Portais e Ã¡reas de cliente", "Acesso privado a documentos, pedidos e estados."),
         ("âš¡", "AutomaÃ§Ã£o e integraÃ§Ãµes", "Menos tarefas repetitivas, nÃºmeros em painÃ©is claros.")]
STEPS = [("Levantamento", "Mapeamos com a equipa o que funciona, o que falha e o que tem de mudar."),
         ("ProtÃ³tipo", "Validamos consigo os ecrÃ£s e fluxos principais antes de programar tudo."),
         ("Entrega por fases", "O sistema entra em uso por partes, comeÃ§ando pelo que traz mais valor."),
         ("FormaÃ§Ã£o e suporte", "Formamos a equipa e acompanhamos o sistema depois de arrancar.")]
STACK = ["Next.js", "React", "JavaScript", "Java", "PHP", "Python", "Node.js", "Firebase", "MySQL", "MongoDB", "PostgreSQL", "Flutter"]

chip = 'display:inline-block;padding:16px 26px;border-radius:999px;font-size:28px;font-weight:500;'
BUSINESS = [
    """<span class="eyebrow"><i></i>HiveCode Business</span>
<h1 style="font-size:96px">Sistemas Ã  medida da forma como a sua <em>empresa trabalha</em>.</h1>
<p class="lead">Para quando as folhas de cÃ¡lculo e o software genÃ©rico jÃ¡ nÃ£o chegam.</p>
<p class="next">Deslize â†’</p>""",
    '<span class="n">O PROBLEMA</span><h1 style="font-size:66px;margin-top:20px">Quando a empresa cresce, as ferramentas soltas deixam de chegar.</h1>'
    '<div style="display:flex;gap:40px;align-items:center;margin-top:60px"><div style="flex:1;display:flex;flex-wrap:wrap;gap:16px">'
    + "".join(f'<span style="{chip}background:rgba(255,255,255,.06);border:2px dashed rgba(255,255,255,.3);color:var(--soft);transform:rotate({(-1) ** i * 2}deg)">{c}</span>' for i, c in enumerate(CHAOS))
    + '</div><span style="font-size:70px;color:var(--violet)">â†’</span><div style="width:340px;border-radius:26px;background:#fff;color:#121125;padding:24px 30px">'
    '<div style="font-size:24px;font-weight:700;color:#4877FE;margin-bottom:10px">O SEU SISTEMA</div>'
    + "".join(f'<div style="font-size:30px;font-weight:600;padding:12px 0;border-top:2px solid #eceaf4">âœ“ {o}</div>' for o in ORDER)
    + "</div></div>",
    '<span class="n">O QUE CONSTRUÃMOS</span><div style="display:flex;flex-direction:column;gap:22px;margin-top:40px">'
    + "".join(f'<div class="card" style="display:flex;gap:30px;align-items:center"><span style="font-size:60px;margin:0">{i}</span><div><b>{t}</b><span>{d}</span></div></div>' for i, t, d in AREAS)
    + "</div>",
    '<span class="n">COMO TRABALHAMOS</span><h1 style="font-size:60px;margin-top:20px">Por fases, para a equipa validar cada passo.</h1><div style="display:flex;flex-direction:column;gap:30px;margin-top:50px">'
    + "".join(f'<div style="display:flex;gap:30px"><span style="flex:none;width:76px;height:76px;border-radius:22px;background:linear-gradient(135deg,#D752FE,#4877FE);display:grid;place-items:center;font-size:36px;font-weight:700">{n}</span>'
              f'<div><b style="font-size:38px;font-weight:600">{t}</b><p style="font-size:28px;line-height:1.4;color:var(--soft);font-weight:300;margin-top:6px">{d}</p></div></div>' for n, (t, d) in enumerate(STEPS, 1))
    + "</div>",
    '<span class="n">TECNOLOGIAS</span><h1 style="font-size:66px;margin-top:20px">Escolhemos a tecnologia pelo que o projeto precisa, <em>nÃ£o por moda</em>.</h1>'
    '<div style="display:flex;flex-wrap:wrap;gap:18px;margin-top:56px">'
    + "".join(f'<span style="{chip}background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.18)">{s}</span>' for s in STACK)
    + "</div>",
    """<h1 style="font-size:92px">Fale connosco sobre o <em>seu sistema</em>.</h1>
<p class="lead">Mostramos como pode ficar antes de qualquer compromisso.</p>
<span class="pill">Mockup e orÃ§amento gratuitos</span>
<p class="next" style="font-size:34px;color:var(--ink)">hivecode.pt/business</p>""",
]

# 3. Recent projects (document): cover, the existing case slides, closing page.
PROJECTS = [
    """<span class="eyebrow"><i></i>PortfÃ³lio</span>
<h1 style="font-size:110px">Projetos <em>recentes</em>.</h1>
<p class="lead">4Sons Â· ClÃ­nica Ana Carolina Pereira</p>
<p class="next">Deslize â†’</p>""",
    ROOT / "posts/2026-10-08-4sons/slides/01/post.jpg", ROOT / "posts/2026-10-08-4sons/slides/02/post.jpg", ROOT / "posts/2026-10-08-4sons/slides/03/post.jpg",
    ROOT / "posts/2026-10-09-acp/slides/01/post.jpg", ROOT / "posts/2026-10-09-acp/slides/02/post.jpg", ROOT / "posts/2026-10-09-acp/slides/03/post.jpg",
    """<h1 style="font-size:96px">O prÃ³ximo pode ser <em>o seu</em>.</h1>
<p class="lead">Sites e sistemas desenhados e desenvolvidos pela HiveCode.</p>
<span class="pill">Mockup e orÃ§amento gratuitos</span>
<p class="next" style="font-size:34px;color:var(--ink)">hivecode.pt</p>""",
]

POSTS = {"2026-11-10-apresentacao": INTRO, "2026-11-11-business": BUSINESS, "2026-11-17-projetos": PROJECTS}


def main():
    for name, pages in POSTS.items():
        out = HERE / name
        shutil.rmtree(out / "slides", ignore_errors=True)
        for n, body in enumerate(pages, 1):
            d = out / "slides" / f"{n:02d}"
            d.mkdir(parents=True)
            if isinstance(body, Path):
                shutil.copy(body, d / "post.jpg")
            else:
                (d / "post.html").write_text(page(body, CSS), encoding="utf-8")
        subprocess.run(["node", str(ROOT / "tools/render.mjs"), str(out / "slides")], check=True)
        jpgs = sorted((out / "slides").glob("*/post.jpg"))
        if len(jpgs) == 1:
            shutil.copy(jpgs[0], out / "imagem.jpg")
        else:
            imgs = [Image.open(j).convert("RGB") for j in jpgs]
            imgs[0].save(out / "documento.pdf", save_all=True, append_images=imgs[1:], resolution=150)
        print(name, len(jpgs))


if __name__ == "__main__":
    main()
