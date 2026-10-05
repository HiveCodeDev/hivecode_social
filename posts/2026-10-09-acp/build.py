"""Ana Carolina Pereira: case drawn from scratch in the clinic's own identity.

No screenshots. Palette and type taken from the live site: cream #F5F0E4,
petrol #0A6577, turquoise #0BABC5, Fraunces (titles), Allura (script),
Inter (text). The identity is the client's, so it is preserved as is.
Slides 1-4 live in the clinic's world; slide 5 signs off in HiveCode night.
"""
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from build_week import page

HERE = Path(__file__).resolve().parent

CLINIC = """
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500&family=Allura&family=Inter:wght@400;500;600&display=block');
body{background:#F5F0E4;color:#1d2a30}
.hex,.glow{display:none}
.kick{font-family:'Inter';font-size:24px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:#0A6577}
.script{font-family:'Allura',cursive;color:#0BABC5;line-height:1;font-weight:400}
.serif{font-family:'Fraunces',serif;font-weight:500;letter-spacing:-.01em;color:#1d2a30}
.foot{color:#5f6b70}.foot .brand{color:#1d2a30}
.count{position:absolute;top:96px;right:88px;font-size:24px;color:#8a9296;letter-spacing:.1em;font-family:'Inter'}
.soft{font-family:'Inter';font-size:32px;line-height:1.45;color:#4c5a60;max-width:820px}
.blob{position:absolute;border-radius:50%;border:2px solid rgba(11,171,197,.35)}
"""

NIGHT_CLOSE = """
.count{position:absolute;top:96px;right:88px;font-size:24px;color:var(--muted);letter-spacing:.1em}
h1{font-size:112px;line-height:1}
p{margin-top:40px;font-size:38px;color:var(--soft);font-weight:300;max-width:820px;line-height:1.4}
.cta{margin-top:64px;align-self:flex-start;padding:28px 46px;border-radius:999px;background:#265ADF;font-size:36px;font-weight:600}
"""

S1 = """
<span class="blob" style="width:760px;height:760px;right:-260px;top:330px"></span>
<span class="blob" style="width:520px;height:520px;right:-120px;top:450px;border-color:rgba(10,101,119,.25)"></span>
<span class="kick">Projeto recente</span>
<div class="script" style="font-size:210px;margin-top:60px">Bem-vindo</div>
<h1 class="serif" style="font-size:84px;line-height:1.08;margin-top:30px;max-width:860px">Novo site para a clínica Ana Carolina Pereira.</h1>
<p class="soft" style="margin-top:34px">Psicologia e saúde, em Coimbra.</p>
"""

SWATCH = "display:flex;flex-direction:column;justify-content:flex-end;padding:26px;border-radius:26px;height:250px;font-family:Inter;font-size:26px;font-weight:600;line-height:1.3"
S2 = f"""
<h1 class="serif" style="font-size:92px;line-height:1.05">Uma identidade <span class="script" style="font-size:124px">serena</span>.</h1>
<div style="margin-top:56px;display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:18px">
<div style="{SWATCH};background:#FFFEFB;border:1px solid #e6dfcf;color:#1d2a30">Creme<br><small style="font-weight:400;opacity:.7">#F5F0E4</small></div>
<div style="{SWATCH};background:#0A6577;color:#F5F0E4">Petróleo<br><small style="font-weight:400;opacity:.75">#0A6577</small></div>
<div style="{SWATCH};background:#0BABC5;color:#06303a">Turquesa<br><small style="font-weight:400;opacity:.8">#0BABC5</small></div>
</div>
<div style="margin-top:44px;display:flex;flex-direction:column;gap:14px">
<div style="display:flex;align-items:baseline;gap:28px"><span class="serif" style="font-size:66px;width:130px">Aa</span><span class="soft" style="font-size:28px">Fraunces, nos títulos</span></div>
<div style="display:flex;align-items:baseline;gap:28px"><span class="script" style="font-size:84px;width:130px">Aa</span><span class="soft" style="font-size:28px">Allura, nos destaques</span></div>
<div style="display:flex;align-items:baseline;gap:28px"><span style="font-family:Inter;font-size:58px;font-weight:500;width:130px">Aa</span><span class="soft" style="font-size:28px">Inter, no texto</span></div>
</div>
"""

PATH = "flex:1;display:flex;flex-direction:column;align-items:center;text-align:center;gap:18px"
DOT = "width:190px;height:190px;border-radius:50%;background:#FFFEFB;border:2px solid rgba(11,171,197,.45);display:grid;place-items:center;box-shadow:0 20px 40px -24px rgba(10,101,119,.5)"
S3 = f"""
<h1 class="serif" style="font-size:88px;line-height:1.06">Três caminhos, desde a <span class="script" style="font-size:116px">primeira visita</span>.</h1>
<div style="position:relative;margin-top:90px;display:flex;gap:16px">
<span style="position:absolute;left:15%;right:15%;top:95px;height:2px;background:repeating-linear-gradient(90deg,#0BABC5 0 14px,transparent 14px 26px)"></span>
<div style="{PATH}"><div style="{DOT}"><span class="serif" style="font-size:54px;color:#0A6577">1</span></div><b class="serif" style="font-size:38px">Clínica</b><span class="soft" style="font-size:24px">Acompanhamento psicológico</span></div>
<div style="{PATH}"><div style="{DOT}"><span class="serif" style="font-size:54px;color:#0A6577">2</span></div><b class="serif" style="font-size:38px">Serviços clínicos</b><span class="soft" style="font-size:24px">Consultas, avaliação e intervenção</span></div>
<div style="{PATH}"><div style="{DOT}"><span class="serif" style="font-size:54px;color:#0A6577">3</span></div><b class="serif" style="font-size:38px">Academia</b><span class="soft" style="font-size:24px">Formação e partilha de conhecimento</span></div>
</div>
"""

BAR = "height:18px;border-radius:9px;background:#e8e1d2"
S4 = f"""
<div style="display:flex;align-items:center;gap:50px">
<div style="flex:1">
<h1 class="serif" style="font-size:80px;line-height:1.06;margin-top:0">Marcar consulta, <span class="script" style="font-size:104px">a um toque</span>.</h1>
<p class="soft" style="margin-top:34px;font-size:30px">O botão de marcação acompanha o visitante em todas as páginas, no computador e no telemóvel.</p>
</div>
<div style="flex:none;width:390px;height:800px;border-radius:60px;background:#1d2a30;padding:16px;transform:rotate(4deg);box-shadow:0 50px 90px -40px rgba(10,101,119,.6)">
<div style="height:100%;border-radius:46px;background:#FFFEFB;padding:40px 30px;display:flex;flex-direction:column;gap:18px">
<div style="display:flex;justify-content:space-between;align-items:center"><span class="serif" style="font-size:30px">ACP</span><span style="width:34px;height:4px;background:#1d2a30;border-radius:2px;box-shadow:0 10px 0 #1d2a30"></span></div>
<span class="script" style="font-size:84px;margin-top:40px">Bem-vindo</span>
<span style="{BAR};width:92%"></span><span style="{BAR};width:78%"></span><span style="{BAR};width:60%"></span>
<span style="position:relative;margin-top:40px;align-self:flex-start;padding:22px 34px;border-radius:999px;background:#0A6577;color:#fff;font-family:Inter;font-weight:600;font-size:26px">Marcar consulta
<i style="position:absolute;right:-26px;bottom:-30px;width:86px;height:86px;border-radius:50%;border:3px solid rgba(11,171,197,.7)"></i>
<i style="position:absolute;right:-6px;bottom:-10px;width:46px;height:46px;border-radius:50%;background:rgba(11,171,197,.35)"></i></span>
<span style="margin-top:auto;width:100%;height:120px;border-radius:24px;background:#F5F0E4"></span>
</div></div>
</div>
"""

S5 = """<h1>Tem um projeto <em>em mente</em>?</h1>
<p>Desenhamos e desenvolvemos sites e sistemas à medida, do primeiro contacto ao lançamento.</p>
<span class="cta">hivecode.pt</span>"""

shutil.rmtree(HERE / "slides", ignore_errors=True)
slides = [(S1, CLINIC), (S2, CLINIC), (S3, CLINIC), (S4, CLINIC), (S5, NIGHT_CLOSE)]
for n, (body, css) in enumerate(slides, 1):
    d = HERE / "slides" / f"{n:02d}"
    d.mkdir(parents=True)
    counter = f'<span class="count">{n}/{len(slides)}</span>'
    (d / "post.html").write_text(page(counter + body, css), encoding="utf-8")
print("ok")
