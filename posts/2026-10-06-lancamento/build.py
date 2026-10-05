import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from build_week import page, ASSETS

HERE = Path(__file__).resolve().parent
COUNT = '<span class="count">{n}/5</span>'
CSS = """
.count{position:absolute;top:96px;right:88px;font-size:24px;color:var(--muted);letter-spacing:.1em}
.shot{margin-top:56px}
.split{margin-top:56px;display:grid;gap:22px}
.split div{padding:34px 36px;border-radius:22px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.12)}
.split strong{display:block;font-size:44px;font-weight:600}
.split span{display:block;margin-top:10px;font-size:30px;color:var(--soft);font-weight:300;line-height:1.35}
.split ul{margin-top:18px;list-style:none;display:flex;flex-wrap:wrap;gap:10px}
.split li{font-size:24px;padding:8px 16px;border-radius:999px;background:rgba(215,82,254,.16);color:var(--ink)}
.art{margin-top:56px;border-radius:24px;overflow:hidden;border:1px solid rgba(255,255,255,.14);box-shadow:0 40px 90px -30px rgba(72,119,254,.55)}
.art img{display:block;width:100%;max-height:640px;object-fit:cover}
.diagram{position:relative;width:904px;height:660px;margin-top:34px}
.diagram svg{position:absolute;inset:0;width:100%;height:100%}
.core{position:absolute;left:452px;top:330px;transform:translate(-50%,-50%);width:300px;height:180px;border-radius:30px;
display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;
background:linear-gradient(160deg,#2a1f5c,#1a1538);border:2px solid rgba(215,82,254,.65);
box-shadow:0 0 0 10px rgba(215,82,254,.08),0 0 90px rgba(215,82,254,.45)}
.core img{width:70px;height:70px}.core b{font-size:36px;font-weight:600}
.node{position:absolute;transform:translate(-50%,-50%);display:flex;align-items:center;gap:14px;white-space:nowrap;
padding:20px 28px;border-radius:20px;background:#191433;border:1px solid rgba(255,255,255,.16);font-size:32px;font-weight:500;
box-shadow:0 18px 40px -18px rgba(0,0,0,.7)}
.node i{width:14px;height:14px;border-radius:50%}
.cta{margin-top:56px;align-self:flex-start;padding:28px 46px;border-radius:999px;background:#265ADF;font-size:36px;font-weight:600}
.promises{margin-top:50px;display:flex;flex-direction:column;gap:18px}
.promises div{display:flex;align-items:center;gap:24px;font-size:38px}
.promises b{flex:none;width:18px;height:18px;transform:rotate(30deg);background:linear-gradient(135deg,var(--pink),var(--blue));
clip-path:polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%)}
"""
SLIDES = [
    f"""<span class="eyebrow"><i></i>Novo site</span>
<h1>O novo hivecode.pt <em>está no ar</em>.</h1>
<div class="shot"><div class="bar"><b></b><b></b><b></b><span>hivecode.pt</span></div><img src="{ASSETS}/site-home.png" alt=""></div>""",
    """<span class="eyebrow"><i></i>Duas formas de trabalharmos juntos</span>
<h1>Um site para se apresentar. <em>Um sistema</em> para trabalhar.</h1>
<div class="split">
<div><strong>Websites</strong><span>Sites institucionais e landing pages rápidos, acessíveis e claros.</span>
<ul><li>Pensados para telemóvel</li><li>SEO técnico e velocidade</li></ul></div>
<div><strong>HiveCode Business</strong><span>CRMs, ERPs, portais e integrações à medida da forma como a sua empresa trabalha.</span>
<ul><li>CRM</li><li>ERP</li><li>Portais de cliente</li><li>Automação</li></ul></div>
</div>""",
    f"""<span class="eyebrow"><i></i>Em qualquer ecrã</span>
<h1>Pensado primeiro para <em>o telemóvel</em>.</h1>
<div class="art"><img src="{ASSETS}/site-devices.png" alt=""></div>""",
    f"""<span class="eyebrow"><i></i>HiveCode Business</span>
<h1>Sistemas à medida da forma como <em>a sua empresa</em> trabalha.</h1>
<div class="diagram"><svg viewBox="0 0 904 660"><defs><linearGradient id="ln" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="904" y2="660"><stop offset="0" stop-color="#EF5AFE"/><stop offset="1" stop-color="#4877FE"/></linearGradient></defs><g stroke="url(#ln)" stroke-width="3" stroke-linecap="round" opacity=".75"><line x1="452" y1="330" x2="452" y2="48"/><circle cx="452" cy="175" r="6" fill="var(--pink)" stroke="none"/><line x1="452" y1="330" x2="751" y2="189"/><circle cx="616" cy="252" r="6" fill="var(--blue)" stroke="none"/><line x1="452" y1="330" x2="751" y2="471"/><circle cx="616" cy="408" r="6" fill="var(--pink)" stroke="none"/><line x1="452" y1="330" x2="452" y2="612"/><circle cx="452" cy="485" r="6" fill="var(--blue)" stroke="none"/><line x1="452" y1="330" x2="153" y2="471"/><circle cx="288" cy="408" r="6" fill="var(--pink)" stroke="none"/><line x1="452" y1="330" x2="153" y2="189"/><circle cx="288" cy="252" r="6" fill="var(--blue)" stroke="none"/></g></svg><span class="core"><img src="{ASSETS}/logo_side.png" alt=""><b>O seu sistema</b></span><span class="node" style="left:452px;top:48px"><i style="background:var(--pink)"></i>CRM</span><span class="node" style="left:751px;top:189px"><i style="background:var(--blue)"></i>ERP</span><span class="node" style="left:751px;top:471px"><i style="background:var(--pink)"></i>Faturação</span><span class="node" style="left:452px;top:612px"><i style="background:var(--blue)"></i>Stock</span><span class="node" style="left:153px;top:471px"><i style="background:var(--pink)"></i>Portal de cliente</span><span class="node" style="left:153px;top:189px"><i style="background:var(--blue)"></i>Integrações</span></div>""",
    """<span class="eyebrow"><i></i>Vamos falar</span>
<h1>Fale com quem <em>desenha e programa</em>.</h1>
<div class="promises"><div><b></b>Resposta em 24 horas</div><div><b></b>Proposta com âmbito, prazo e preço claros</div>
<div><b></b>Sem compromisso até fazer sentido</div></div>
<span class="cta">hivecode.pt/contacto</span>""",
]
for n, body in enumerate(SLIDES, 1):
    d = HERE / "slides" / f"{n:02d}"
    d.mkdir(parents=True, exist_ok=True)
    (d / "post.html").write_text(page(COUNT.format(n=n) + body, CSS), encoding="utf-8")
print("ok")
