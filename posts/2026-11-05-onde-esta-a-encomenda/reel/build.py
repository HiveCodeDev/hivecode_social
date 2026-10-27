"""Reel "Onde está a encomenda? 5 minutos ou 5 segundos" (HiveCode Business), forest theme (receipt-style cards on deep green), 1080x1920.

python posts/2026-11-05-onde-esta-a-encomenda/reel/build.py
A customer calls; the search runs through email, Excel and a notebook while a red timer climbs
to 5:00. Then a custom system: the name is typed and the order appears; the timer reads 0:05.
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
    ("Um cliente liga: onde está a minha encomenda?", 88, {"encomenda?"}),
    ("Procura no email.", 104, {"email."}),
    ("No Excel.", 110, {"Excel."}),
    ("No caderno.", 110, {"caderno."}),
    ("Cinco minutos depois, ainda não sabe.", 92, {"Cinco", "minutos"}),
    ("Com um sistema à medida, escreve o nome do cliente", 84, {"nome"}),
    ("e a resposta aparece em cinco segundos.", 88, {"cinco", "segundos."}),
    ("Saiba mais em hivecode.pt/business.", 76, {"hivecode.pt/business."}),
]

CSS = """
#call{left:240px;top:960px;width:600px;padding:34px 40px;background:#fff;color:#111;border:3px solid #111;box-shadow:10px 10px 0 #082a1f;display:flex;align-items:center;gap:28px;opacity:0}
#call i{width:110px;height:110px;border-radius:50%;background:#111;display:grid;place-items:center;font-style:normal;font-size:56px;flex:none}
#call small{display:block;font-size:28px;color:#555}#call b{font-size:44px}
#tm{left:690px;top:820px;padding:14px 28px;background:#fff;border:3px solid #D7263D;color:#D7263D;font-size:52px;font-weight:700;font-variant-numeric:tabular-nums;opacity:0}
.src{width:620px;height:430px;background:#fff;color:#111;border:3px solid #111;padding:30px 34px;opacity:0;box-shadow:10px 10px 0 #082a1f}
.src h4{font-size:32px;font-weight:700;margin-bottom:22px;padding-bottom:16px;border-bottom:3px dashed #111}
.src .r{height:22px;background:#e4e1d8;margin-bottom:20px}
.x{position:absolute;right:-24px;top:-24px;width:80px;height:80px;border-radius:50%;background:#D7263D;color:#fff;display:grid;place-items:center;font-size:44px;font-weight:800;opacity:0}
#xl{display:grid;grid-template-columns:repeat(4,1fr);gap:0;border:2px solid #111}#xl span{height:44px;border:1px solid #bbb}
#nb{background:repeating-linear-gradient(#fff 0 50px,#c9d6f0 50px 52px);color:#2a2550}
#nb p{font-size:34px;font-style:italic;line-height:52px;font-family:Georgia,serif}
#q{left:140px;top:960px;width:800px;padding:30px 36px;background:#fff;color:#111;border:3px solid #111;box-shadow:10px 10px 0 #082a1f;display:flex;align-items:center;gap:22px;font-size:46px;font-weight:600;opacity:0}
#cur{display:inline-block;width:4px;height:52px;background:#111;margin-left:4px}
#res{left:140px;top:1130px;width:800px;padding:34px 40px;background:#fff;color:#111;border:3px solid #111;box-shadow:10px 10px 0 #082a1f;opacity:0}
#res small{display:block;font-size:26px;color:#555;padding-bottom:14px;border-bottom:3px dashed #111}#res b{display:block;font-size:46px;margin-top:16px}
#res span{display:inline-block;margin-top:18px;padding:10px 20px;background:#111;color:#fff;font-size:28px;font-weight:600}
#logo{left:440px;top:930px;width:200px;height:200px;opacity:0}
#cta{left:88px;right:88px;top:1220px;display:flex;justify-content:center;opacity:0}
#cta span{padding:30px 52px;background:#F3EFE6;color:#0F3D2E;font-size:42px;font-weight:700;box-shadow:10px 10px 0 #F4C542}
"""

ART = f"""
<div id="call"><i>📞</i><div><small>Chamada recebida</small><b>Cliente</b></div></div>
<div id="tm">0:00</div>
<div class="src" id="s0" style="left:150px;top:960px"><h4>✉️ Email</h4><div class="r" style="width:90%"></div><div class="r" style="width:70%"></div><div class="r" style="width:80%"></div><div class="r" style="width:60%"></div><span class="x" id="x0">✕</span></div>
<div class="src" id="s1" style="left:230px;top:1020px"><h4><span style="color:#2fbf71">■</span> Excel</h4><div id="xl">{'<span></span>' * 16}</div><span class="x" id="x1">✕</span></div>
<div class="src" id="nb" style="left:310px;top:1080px;position:absolute"><h4>Caderno</h4><p>Encomenda… Silva?<br>ou terça?</p><span class="x" id="x2">✕</span></div>
<div id="q">🔍 <span id="typed"></span><span id="cur"></span></div>
<div id="res"><small>Encomenda nº 214 · Silva</small><b>Em preparação</b><span>Entrega amanhã</span></div>
<img id="logo" src="{ASSETS}/logo_mark.svg" alt="">
<div id="cta"><span>hivecode.pt/business</span></div>
"""

ART_JS = r"""
const mmss = s => `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, '0')}`;
function art(t, E) {
  // The call rings.
  stage($('#call'), t, .2, E.s2);
  $('#call i').style.transform = `rotate(${t < E.s2 ? 14 * Math.sin(t * 30) * (Math.sin(t * 3) > 0 ? 1 : 0) : 0}deg)`;
  // The search: three places pile up, each crossed out when the next opens; a red timer climbs to 5:00.
  const gone = 1 - ease((t - E.s6) / .3), dim = 1 - .6 * cl((t - E.s5) / .3);
  [['#s0', E.s2, E.s3], ['#s1', E.s3, E.s4], ['#nb', E.s4, E.s5]].forEach(([s, a, b], i) => {
    pop($(s), t, a + .1); $(s).style.opacity = cl((t - a - .1) / .1) * gone * dim;
    pop($('#x' + i), t, b - .25); $('#x' + i).style.opacity *= gone;
  });
  const tm = $('#tm'), slow = t < E.s6;
  tm.style.opacity = cl((t - E.s2) / .2) * (1 - ease((t - E.s8) / .3));
  if (slow) {
    tm.textContent = mmss(300 * ease((t - E.s2) / (E.s5 + .6 - E.s2)));
    tm.style.transform = `translateX(${t > E.s5 ? 6 * Math.sin(t * 40) : 0}px)`;
    tm.style.color = tm.style.borderColor = '#D7263D';
  } else {
    tm.textContent = t < E.seg ? mmss(Math.min(5, (t - E.s6) * 2)) : '0:05';
    tm.style.transform = '';
    tm.style.color = tm.style.borderColor = '#1f8a4c';
  }
  // The system: type the name, the order appears.
  stage($('#q'), t, E.s6 + .1, E.s8);
  const name = 'Silva', k = Math.floor(cl((t - E.nome) / .6) * name.length);
  $('#typed').textContent = name.slice(0, k);
  $('#cur').style.opacity = Math.sin(t * 12) > 0 ? 1 : 0;
  stage($('#res'), t, E.resp, E.s8);
  // Close.
  const lg = back((t - E.s8 - .1) / .5);
  $('#logo').style.opacity = cl((t - E.s8 - .1) / .1);
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
    ev = {"s2": st[1], "s3": st[2], "s4": st[3], "s5": st[4], "s6": st[5], "nome": at(5, "nome"),
          "resp": at(6, "resposta"), "seg": at(6, "segundos."), "s8": st[7], "site": at(7, "hivecode.pt/business.")}
    page = HERE / "reel.html"
    page.write_text(reelkit.page(scenes, ev, ART, CSS, ART_JS, corner="Business", theme="forest"), encoding="utf-8")
    hits = [("pop", .2), ("click", .5), ("click", .8)] + [("pop", s + .1) for s in (ev["s2"], ev["s3"], ev["s4"])]
    hits += [("error", s - .25) for s in (ev["s3"], ev["s4"], ev["s5"])] + [("thump", ev["s5"] + .1)]
    hits += [("whoosh", ev["s6"]), ("click", ev["nome"]), ("click", ev["nome"] + .2), ("click", ev["nome"] + .4),
             ("pop", ev["resp"]), ("pop", ev["s8"] + .15), ("pop", ev["site"])]
    reelkit.render(page, WORK, total, WORK / "voz.mp3", hits, HERE / "reel.mp4")
    reelkit.cover(HERE / "reel.mp4", ev["s5"] + .5, HERE / "cover.jpg")
    print(f"reel.mp4 {total:.1f}s")


if __name__ == "__main__":
    main()
