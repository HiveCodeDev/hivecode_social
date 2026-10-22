"""Reel "Mockup e orçamento gratuitos" (websites), canvas theme (design-tool look), 1080x1920.

python posts/2026-11-mockup-gratuito/reel/build.py
Explains what a mockup is while one is built on screen: an empty browser fills with a hero,
the client's logo, colours and text; it then shows on a laptop and a phone, before any code.
Closes with a clear, no-commitment quote and the call to action.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import reelkit  # noqa: E402

WORK = ROOT / "reels" / HERE.parent.name
WORK.mkdir(parents=True, exist_ok=True)

SCENES = [
    ("Antes de investir num site, quer ver como vai ficar?", 92, {"ver"}),
    ("Fazemos um mockup gratuito.", 104, {"mockup", "gratuito."}),
    ("Um mockup é uma imagem do seu futuro site,", 88, {"imagem"}),
    ("com o seu logótipo, as suas cores e os seus conteúdos.", 80, {"logótipo,", "cores", "conteúdos."}),
    ("Vê como fica no computador e no telemóvel,", 88, {"computador", "telemóvel,"}),
    ("antes de escrevermos uma única linha de código.", 84, {"antes"}),
    ("Com o mockup, recebe um orçamento claro e sem compromisso.", 78, {"orçamento", "sem", "compromisso."}),
    ("Peça o seu em hivecode.pt.", 100, {"hivecode.pt."}),
]

CSS = """
#br{left:150px;top:860px;width:780px;height:540px;border-radius:26px;background:#fff;overflow:hidden;opacity:0;box-shadow:0 30px 60px -30px rgba(18,17,37,.35);outline:4px solid #9B3CF0;outline-offset:10px;transform-origin:0 50%}
#sel{left:150px;top:820px;padding:8px 18px;border-radius:10px;background:#9B3CF0;color:#fff;font-size:26px;font-weight:600;opacity:0}
#br .bar{height:54px;background:#eef1fb;display:flex;align-items:center;gap:10px;padding:0 22px}
#br .bar b{width:14px;height:14px;border-radius:50%;background:#c9d3f5}
#br .empty{position:absolute;inset:80px 30px 30px;border:4px dashed #c9d3f5;border-radius:18px;display:grid;place-items:center;font-size:150px;font-weight:800;color:#c9d3f5}
#hd{position:absolute;left:30px;right:30px;top:76px;height:56px;display:flex;align-items:center;gap:16px;opacity:0}
#lg{width:56px;height:56px;border-radius:16px;background:#121125;display:grid;place-items:center;color:#FFD84D;font-size:30px;font-weight:800}
#hd span{font-size:28px;font-weight:700;color:#121125}
#hero{position:absolute;left:30px;right:30px;top:150px;height:200px;border-radius:18px;background:#dbe5ff;opacity:0}
.tl{position:absolute;left:30px;height:22px;border-radius:11px;background:#dbe5ff;opacity:0;transform-origin:left}
#bt{position:absolute;left:30px;top:460px;width:200px;height:52px;border-radius:14px;background:#c9d3f5;opacity:0}
.sw{width:84px;height:84px;border-radius:50%;border:6px solid #fff;opacity:0;box-shadow:0 20px 40px -16px rgba(18,17,37,.35)}
#ph{left:770px;top:960px;width:220px;height:440px;border-radius:36px;background:#121125;padding:10px;opacity:0;box-shadow:0 40px 80px -30px rgba(18,17,37,.45)}
#ph .s{height:100%;border-radius:28px;background:#fff;overflow:hidden;padding:16px 12px;display:flex;flex-direction:column;gap:10px}
#ph i{display:block;border-radius:8px;background:#dbe5ff}
#code{left:290px;top:1440px;display:flex;align-items:center;gap:18px;padding:22px 34px;border-radius:999px;background:#121125;color:#fff;font-size:38px;font-weight:600;opacity:0}
#code b{font-family:monospace;color:#FFD84D}
#free{left:700px;top:1300px;padding:22px 40px;border-radius:16px;background:#FFD84D;color:#121125;font-size:48px;font-weight:800;opacity:0;box-shadow:0 30px 60px -20px rgba(18,17,37,.35)}
#q{left:240px;top:880px;width:600px;padding:44px 48px;border-radius:26px;background:#fff;color:#121125;opacity:0;box-shadow:0 40px 80px -30px rgba(18,17,37,.35)}
#q h3{font-size:44px;font-weight:800}
#q .r{display:flex;justify-content:space-between;font-size:32px;padding:18px 0;border-bottom:2px solid #eef1fb;color:#4a4560}
#stamp{left:560px;top:1300px;padding:20px 30px;border:6px solid #2fbf71;border-radius:16px;color:#2fbf71;background:#fff;font-size:40px;font-weight:800;opacity:0}
#cta{left:88px;right:88px;top:1220px;display:flex;justify-content:center;opacity:0}
#cta span{padding:36px 60px;border-radius:999px;background:#9B3CF0;color:#fff;font-size:52px;font-weight:700;box-shadow:0 30px 70px -20px rgba(18,17,37,.35)}
"""

ART = """
<div id="sel">Mockup · 1440 × 900</div>
<div id="br"><div class="bar"><b></b><b></b><b></b></div><div class="empty" id="empty"><span id="qm">?</span></div>
<div id="hd"><span id="lg">A</span><span>A sua empresa</span></div><div id="hero"></div>
<span class="tl" id="t0" style="top:376px;width:60%"></span><span class="tl" id="t1" style="top:414px;width:45%"></span><span id="bt"></span></div>
<span class="sw" id="c0" style="left:300px;top:1440px;background:#121125"></span>
<span class="sw" id="c1" style="left:410px;top:1440px;background:#FF8A1F"></span>
<span class="sw" id="c2" style="left:520px;top:1440px;background:#FFD84D"></span>
<div id="ph"><div class="s"><i style="height:30px;width:60%;background:#121125"></i><i style="height:150px;background:linear-gradient(150deg,#FFD84D,#FF8A1F)"></i><i style="height:16px;width:80%"></i><i style="height:16px;width:60%"></i><i style="height:40px;width:70%;background:#121125"></i></div></div>
<div id="code"><b>&lt;/&gt;</b>0 linhas de código</div>
<div id="free">Gratuito</div>
<div id="q"><h3>Orçamento</h3><div class="r">Páginas<span>5</span></div><div class="r">Loja online<span>Não</span></div><div class="r" style="border:0">Manutenção<span>Mensal</span></div></div>
<div id="stamp">Sem compromisso ✓</div>
<div id="cta"><span>hivecode.pt</span></div>
"""

ART_JS = r"""
function art(t, E) {
  // The mockup: an empty browser that fills in as it is explained, then shrinks beside a phone.
  const out = ease((t - E.s7) / .3);
  const v = stage($('#br'), t, .2, E.s7);
  const sm = ease((t - E.comp) / .5);
  $('#br').style.transform += ` scale(${1 - .22 * sm}) translateY(${-40 * sm}px)`;
  $('#br').style.left = `${150 - 70 * sm}px`;
  $('#empty').style.opacity = 1 - ease((t - E.imag) / .3);
  $('#qm').style.display = 'inline-block'; $('#qm').style.transform = `rotate(${8 * Math.sin(t * 4)}deg)`;
  pop($('#hero'), t, E.imag); pop($('#t0'), t, E.imag + .2); pop($('#t1'), t, E.imag + .3); pop($('#bt'), t, E.imag + .4);
  pop($('#hd'), t, E.logo);
  $('#sel').style.opacity = v * (1 - sm);
  // Colours: swatches pop, then the hero and button take them.
  const col = t > E.cores + .6;
  ['#c0', '#c1', '#c2'].forEach((s, i) => { pop($(s), t, E.cores + .15 * i); $(s).style.opacity = cl((t - E.cores - .15 * i) / .1) * (1 - ease((t - E.s5) / .3)); });
  $('#hero').style.background = col ? 'linear-gradient(150deg,#FFD84D,#FF8A1F)' : '#dbe5ff';
  $('#bt').style.background = col ? '#121125' : '#c9d3f5';
  ['#t0', '#t1'].forEach(s => $(s).style.background = t > E.cont ? '#4a4560' : '#dbe5ff');
  // Laptop and phone.
  stage($('#ph'), t, E.tele - .1, E.s7);
  stage($('#code'), t, E.s6 + .3, E.s7);
  pop($('#free'), t, E.grat, 'rotate(-8deg)'); $('#free').style.opacity = cl((t - E.grat) / .1) * (1 - ease((t - E.s3) / .3));
  // The quote, stamped.
  stage($('#q'), t, E.s7 + .2, E.s8);
  pop($('#stamp'), t, E.comp2, 'rotate(-10deg)'); $('#stamp').style.opacity = cl((t - E.comp2) / .1) * (1 - ease((t - E.s8) / .3));
  // Close.
  const ct = back((t - E.site) / .45);
  $('#cta').style.opacity = cl((t - E.site) / .1);
  $('#cta').style.transform = `scale(${ct * (1 + .03 * Math.sin((t - E.site) * 5) * cl(t - E.site - .5))})`;
}
"""


def main():
    total, scenes = reelkit.voice(SCENES, WORK / "voz.mp3")
    at = lambda s, w: reelkit.at(scenes, s, w)  # noqa: E731
    st = [s["start"] for s in scenes]
    ev = {"grat": at(1, "gratuito."), "s3": st[2], "imag": at(2, "imagem"), "logo": at(3, "logótipo,"), "cores": at(3, "cores"),
          "cont": at(3, "conteúdos."), "s5": st[4], "comp": at(4, "computador"), "tele": at(4, "telemóvel,"), "s6": st[5],
          "s7": st[6], "comp2": at(6, "compromisso."), "s8": st[7], "site": at(7, "hivecode.pt.")}
    page = HERE / "reel.html"
    page.write_text(reelkit.page(scenes, ev, ART, CSS, ART_JS, theme="canvas"), encoding="utf-8")
    hits = [("pop", .2), ("thump", ev["grat"]), ("pop", ev["imag"]), ("pop", ev["logo"])]
    hits += [("click", ev["cores"] + .15 * i) for i in range(3)] + [("whoosh", ev["comp"]), ("pop", ev["tele"])]
    hits += [("pop", ev["s6"] + .3), ("whoosh", ev["s7"]), ("thump", ev["comp2"]), ("pop", ev["site"])]
    reelkit.render(page, WORK, total, WORK / "voz.mp3", hits, HERE / "reel.mp4")
    reelkit.cover(HERE / "reel.mp4", ev["grat"] + .8, HERE / "cover.jpg")
    print(f"reel.mp4 {total:.1f}s")


if __name__ == "__main__":
    main()
