"""Reel "Black Friday: o seu site está preparado?" (websites/online shops), 1080x1920.

python posts/2026-10-25-black-friday/reel/build.py
A calendar opens on 27 November, then three checks play out as they are asked: traffic spike
with the speed gauge holding, a three-step phone checkout, stock counting down to "Esgotado".
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import reelkit  # noqa: E402
from build_week import ASSETS  # noqa: E402

WORK = ROOT / "reels" / HERE.parent.name
WORK.mkdir(parents=True, exist_ok=True)

SCENES = [
    ("Falta um mês para a Black Friday.", 92, {"Black", "Friday."}),
    ("O seu site está preparado?", 100, {"preparado?"}),
    ("Primeiro: aguenta muitas visitas ao mesmo tempo, sem ficar lento?", 76, {"muitas", "visitas"}),
    ("Segundo: comprar no telemóvel é simples e rápido?", 80, {"telemóvel"}),
    ("Terceiro: o stock está sempre certo, para não vender o que já não tem?", 72, {"stock"}),
    ("Se a resposta a alguma for não, ainda vai a tempo.", 84, {"tempo."}),
    ("Fale connosco em hivecode.pt.", 88, {"hivecode.pt."}),
]

CSS = """
.cal{left:340px;top:870px;width:400px;height:420px;border-radius:30px;background:#f3f1fb;color:#121125;overflow:hidden;opacity:0;text-align:center;box-shadow:0 40px 90px -30px rgba(0,0,0,.9)}
.cal .ctop{height:110px;background:#121125;color:#f3f1fb;font-size:40px;font-weight:700;display:grid;place-items:center;border:4px solid #f3f1fb;border-radius:30px 30px 0 0}
.cal b{display:block;font-size:180px;font-weight:800;line-height:1.1;margin-top:20px}
.cal span{font-size:40px;font-weight:600}
.panel{border-radius:28px;background:#1b1638;border:1px solid rgba(255,255,255,.16);opacity:0;box-shadow:0 40px 80px -30px rgba(0,0,0,.8)}
#vis{left:120px;top:880px;width:840px;height:220px;padding:30px 40px}
#vis small{font-size:30px;color:var(--soft)}#vis b{display:block;font-size:110px;font-weight:800;letter-spacing:-.03em}
#gauge{left:300px;top:1150px;width:480px;height:280px;padding-top:20px;text-align:center}
.ok{width:96px;height:96px;border-radius:50%;background:#2fbf71;display:grid;place-items:center;opacity:0}
.ph{left:350px;top:860px;width:380px;height:600px;border-radius:52px;background:#0d0b1c;border:2px solid rgba(255,255,255,.2);padding:14px;opacity:0;box-shadow:0 40px 90px -30px rgba(215,82,254,.6)}
.ph .scr{height:100%;border-radius:40px;background:#1b1638;padding:34px 26px;display:flex;flex-direction:column;gap:22px}
.step{display:flex;align-items:center;gap:18px;padding:22px 24px;border-radius:20px;background:rgba(255,255,255,.06);font-size:32px;font-weight:600}
.step i{width:44px;height:44px;border-radius:50%;border:3px solid rgba(255,255,255,.4);display:grid;place-items:center;font-style:normal;font-size:24px}
#stock{left:220px;top:880px;width:640px;height:520px;padding:40px;display:flex;flex-direction:column;gap:26px}
#stock .prod{height:200px;border-radius:20px;background:linear-gradient(150deg,rgba(239,90,254,.55),rgba(72,119,254,.55))}
#stock .row{display:flex;justify-content:space-between;align-items:center;font-size:40px;font-weight:700}
#sold{padding:12px 24px;border-radius:999px;background:#ff4d6d;font-size:30px;opacity:0}
.li{left:150px;display:flex;align-items:center;gap:22px;padding:26px 36px;border-radius:999px;background:#1b1638;border:1px solid rgba(255,255,255,.16);font-size:38px;font-weight:600;opacity:0;white-space:nowrap}
.li i{width:52px;height:52px;border-radius:50%;background:#2fbf71;display:grid;place-items:center}
#logo{left:440px;top:930px;width:200px;height:200px;opacity:0}
#cta{left:88px;right:88px;top:1220px;display:flex;justify-content:center;opacity:0}
#cta span{padding:32px 54px;border-radius:999px;background:#265ADF;font-size:44px;font-weight:600;box-shadow:0 30px 70px -20px rgba(72,119,254,.8)}
"""

CHECK = '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>'
GAUGE = """<svg viewBox="0 0 200 110" width="400" height="220"><path d="M20 100 A80 80 0 0 1 180 100" fill="none" stroke="rgba(255,255,255,.12)" stroke-width="18" stroke-linecap="round"/>
<path d="M20 100 A80 80 0 0 1 100 20" fill="none" stroke="#2fbf71" stroke-width="18" stroke-linecap="round"/>
<line id="needle" x1="100" y1="100" x2="100" y2="34" stroke="#f3f1fb" stroke-width="7" stroke-linecap="round" style="transform-origin:100px 100px"/><circle cx="100" cy="100" r="10" fill="#f3f1fb"/></svg>"""

ART = f"""
<div class="cal" id="cal"><div class="ctop">Novembro</div><b>27</b><span>Black Friday</span></div>
<div class="panel" id="vis"><small>Visitas agora</small><b id="visv">0</b></div>
<div class="panel" id="gauge">{GAUGE}<div style="font-size:32px;font-weight:600;margin-top:-6px">Rápido</div></div>
<span class="ok" id="ok1" style="left:830px;top:1180px">{CHECK.format(s=52)}</span>
<div class="ph" id="ph"><div class="scr">
<div class="step" id="st0"><i>1</i>Carrinho</div><div class="step" id="st1"><i>2</i>Pagamento</div><div class="step" id="st2"><i>3</i>Concluído</div></div></div>
<span class="ok" id="ok2" style="left:760px;top:880px">{CHECK.format(s=52)}</span>
<div class="panel" id="stock"><div class="prod"></div><div class="row">Produto A<span id="stv">Stock: 5</span></div>
<div class="row"><span style="font-size:32px;color:var(--soft)">Atualizado em tempo real</span><span id="sold">Esgotado</span></div></div>
<span class="ok" id="ok3" style="left:820px;top:860px">{CHECK.format(s=52)}</span>
<div class="li" id="l0" style="top:900px"><i>{CHECK.format(s=30)}</i>Aguenta muitas visitas</div>
<div class="li" id="l1" style="top:1040px"><i>{CHECK.format(s=30)}</i>Compra simples no telemóvel</div>
<div class="li" id="l2" style="top:1180px"><i>{CHECK.format(s=30)}</i>Stock sempre certo</div>
<img id="logo" src="{ASSETS}/logo_mark.svg" alt="">
<div id="cta"><span>hivecode.pt</span></div>
"""

ART_JS = r"""
const fmt = n => String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
function art(t, E) {
  stage($('#cal'), t, .15, E.s3);
  // 1. Traffic climbs, the gauge holds in the green.
  stage($('#vis'), t, E.s3 + .2, E.s4); stage($('#gauge'), t, E.s3 + .45, E.s4);
  $('#visv').textContent = fmt(4873 * ease((t - E.visitas) / 1.8));
  $('#needle').style.transform = `rotate(${-55 + 6 * Math.sin(t * 9)}deg)`;
  pop($('#ok1'), t, E.s4 - .6); $('#ok1').style.opacity *= 1 - ease((t - E.s4) / .3);
  // 2. Three-step checkout lights up across the sentence.
  stage($('#ph'), t, E.s4 + .2, E.s5);
  const span = Math.max(.6, (E.s5 - E.s4 - 1) / 3);
  [0, 1, 2].forEach(i => {
    const on = t > E.tel + span * i, el = $('#st' + i);
    el.style.background = on ? 'rgba(38,90,223,.9)' : 'rgba(255,255,255,.06)';
    el.style.transform = `scale(${1 + .05 * Math.max(0, 1 - Math.abs(t - E.tel - span * i) / .2)})`;
  });
  pop($('#ok2'), t, E.s5 - .5); $('#ok2').style.opacity *= 1 - ease((t - E.s5) / .3);
  // 3. Stock counts down with each order, then shows "Esgotado".
  stage($('#stock'), t, E.s5 + .2, E.s6);
  const left = Math.max(0, 5 - Math.floor(Math.max(0, t - E.stock) * 2.2));
  $('#stv').textContent = `Stock: ${left}`;
  pop($('#sold'), t, E.stock + 2.4);
  pop($('#ok3'), t, E.s6 - .5); $('#ok3').style.opacity *= 1 - ease((t - E.s6) / .3);
  // Recap checklist.
  ['#l0', '#l1', '#l2'].forEach((s, i) => stage($(s), t, E.s6 + .25 + .3 * i, E.s7));
  // Close.
  const lg = back((t - E.s7 - .1) / .5);
  $('#logo').style.opacity = cl((t - E.s7 - .1) / .1);
  $('#logo').style.transform = `rotate(${-120 * (1 - lg)}deg) scale(${lg})`;
  const ct = back((t - E.site) / .45);
  $('#cta').style.opacity = cl((t - E.site) / .1);
  $('#cta').style.transform = `scale(${ct * (1 + .03 * Math.sin((t - E.site) * 5) * cl(t - E.site - .5))})`;
}
"""


def main():
    total, scenes = reelkit.voice(SCENES, WORK / "voz.mp3")
    at = lambda s, w: reelkit.at(scenes, s, w)  # noqa: E731
    st = [s["start"] for s in scenes]
    ev = {"s3": st[2], "visitas": at(2, "visitas"), "s4": st[3], "tel": at(3, "telemóvel"), "s5": st[4], "stock": at(4, "stock"),
          "s6": st[5], "s7": st[6], "site": at(6, "hivecode.pt.")}
    page = HERE / "reel.html"
    page.write_text(reelkit.page(scenes, ev, ART, CSS, ART_JS), encoding="utf-8")
    hits = [("pop", .15)] + [("whoosh", s - .1) for s in (ev["s3"], ev["s4"], ev["s5"], ev["s6"])]
    hits += [("pop", ev["s4"] - .6), ("click", ev["tel"]), ("pop", ev["s5"] - .5), ("error", ev["stock"] + 2.4), ("pop", ev["s6"] - .5)]
    hits += [("pop", ev["s6"] + .25 + .3 * i) for i in range(3)] + [("pop", ev["s7"] + .15), ("pop", ev["site"])]
    reelkit.render(page, WORK, total, WORK / "voz.mp3", hits, HERE / "reel.mp4")
    reelkit.cover(HERE / "reel.mp4", 1.6, HERE / "cover.jpg")
    print(f"reel.mp4 {total:.1f}s")


if __name__ == "__main__":
    main()
