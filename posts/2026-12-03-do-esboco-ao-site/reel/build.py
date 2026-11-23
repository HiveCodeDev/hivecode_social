"""Reel "Do esboço ao site" (natalnoite theme: night-blue Christmas scenery, 1080x1920).

python posts/2026-12-03-do-esboco-ao-site/reel/build.py
One window: a pencil sketch draws itself on paper (wobbly boxes, an X for the photo), turns into a
clean grey wireframe with labels, then gets colours, a "photo" and real text for a fictional bakery;
a cursor clicks "Encomendar" and a new-order toast pops. Then a "Mockup e orçamento 0 €" chip, logo, CTA.
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
    ("Todos os sites começam assim: um esboço.", 100, {"esboço."}),
    ("Primeiro, a estrutura: o que o cliente procura e onde o encontra.", 86, {"estrutura:"}),
    ("Depois, as cores, as fotografias e os textos do seu negócio.", 86, {"cores,", "fotografias"}),
    ("No fim, um site que trabalha por si.", 104, {"trabalha"}),
    ("O mockup e o orçamento são gratuitos.", 100, {"gratuitos."}),
    ("Peça o seu em hivecode.pt.", 110, {"hivecode.pt."}),
]

# Boxes of the page (left, top, width, height) inside an 840 x 700 window body.
BOX = {"nav": (30, 26, 780, 56), "hero": (30, 110, 780, 270), "t1": (30, 410, 420, 40), "t2": (30, 466, 320, 28),
       "btn": (30, 524, 250, 72), "c1": (470, 410, 160, 186), "c2": (650, 410, 160, 186)}

CSS = """
#win{left:120px;top:780px;width:840px;height:760px;border-radius:26px;background:#fff;overflow:hidden;opacity:0;box-shadow:0 60px 120px -40px rgba(242,193,78,.3)}
#win .tb{height:60px;background:#F2F3F6;display:flex;align-items:center;gap:12px;padding:0 24px}
#win .tb i{width:16px;height:16px;border-radius:50%;background:#d6d8e0}
#body{position:absolute;left:0;top:60px;width:840px;height:700px}
#paper{position:absolute;inset:0;background:#FBF8F1;background-image:linear-gradient(#e7e1d3 2px,transparent 2px);background-size:100% 46px}
#sk{position:absolute;inset:0}
#sk path{fill:none;stroke:#3b3b46;stroke-width:4;stroke-linecap:round;stroke-linejoin:round}
.wf{position:absolute;border-radius:12px;background:#E6E8EE;opacity:0;display:flex;align-items:center;padding-left:20px;font-size:22px;font-weight:600;color:#8a8f9c;box-sizing:border-box}
#fin{position:absolute;inset:0;opacity:0}
#fin .nav{position:absolute;left:30px;top:26px;width:780px;height:56px;display:flex;align-items:center;justify-content:space-between;font-size:26px;font-weight:800;color:#3d2a1e}
#fin .nav small{font-size:20px;font-weight:600;color:#8a6a55;letter-spacing:.02em}
#fin .hero{position:absolute;left:30px;top:110px;width:780px;height:270px;border-radius:18px;overflow:hidden;background:linear-gradient(160deg,#f6c98a,#d98b4a 55%,#8a4b2a)}
#fin .hero b{position:absolute;border-radius:50%;background:rgba(255,236,200,.55)}
#fin .hero span{position:absolute;left:34px;bottom:30px;color:#fff;font-size:44px;font-weight:800;line-height:1.05;text-shadow:0 4px 20px rgba(60,30,10,.4)}
#fin .t1{position:absolute;left:30px;top:410px;font-size:34px;font-weight:800;color:#3d2a1e}
#fin .t2{position:absolute;left:30px;top:462px;font-size:24px;color:#8a6a55}
#fin .btn{position:absolute;left:30px;top:524px;width:250px;height:72px;border-radius:14px;background:#3d2a1e;color:#fff;display:grid;place-items:center;font-size:26px;font-weight:700}
#fin .c{position:absolute;top:410px;width:160px;height:186px;border-radius:16px;overflow:hidden;background:#f3e6d4}
#fin .c i{display:block;height:120px}
#fin .c em{display:block;padding:12px 14px;font-style:normal;font-size:20px;font-weight:700;color:#3d2a1e}
#toast{left:500px;top:1440px;padding:26px 34px;border-radius:20px;background:#1f8a4c;color:#fff;font-size:34px;font-weight:700;opacity:0;box-shadow:0 30px 60px -20px rgba(0,0,0,.5)}
#cur{left:0;top:0;width:54px;height:54px;opacity:0;z-index:6}
#lbl{left:120px;top:1560px;padding:14px 26px;border-radius:999px;font-size:32px;font-weight:700;color:#fff;background:rgba(255,255,255,.12)}
#free{left:0;right:0;top:1580px;display:flex;justify-content:center;opacity:0}
#free span{padding:26px 46px;border-radius:999px;background:#fff;color:#121125;font-size:50px;font-weight:800}
#free b{color:#fff;background:#F2C14E;color:#0E1A33;padding:0 16px;border-radius:12px;margin-left:12px}
#logo{left:440px;top:930px;width:200px;height:200px;opacity:0}
#cta{left:88px;right:88px;top:1220px;display:flex;justify-content:center;opacity:0}
#cta span{padding:32px 56px;border-radius:999px;background:#F2C14E;color:#0E1A33;font-size:50px;font-weight:700}
"""


def wobble(x, y, w, h, seed):
    """A hand-drawn rectangle: corners nudged, edges slightly bowed, start overshooting."""
    j = lambda k: ((seed * 7 + k * 13) % 9 - 4)  # noqa: E731
    p = [(x + j(1), y + j(2)), (x + w + j(3), y + j(4)), (x + w + j(5), y + h + j(6)), (x + j(7), y + h + j(8))]
    d = f"M{p[0][0] - 6},{p[0][1] + 2}"
    for a, b in zip(p, p[1:] + p[:1] + [p[1]]):
        mx, my = (a[0] + b[0]) / 2 + j(9) / 2, (a[1] + b[1]) / 2 + j(10) / 2
        d += f" Q{mx},{my} {b[0]},{b[1]}"
    return d


def sketch():
    paths = []
    for i, (k, (x, y, w, h)) in enumerate(BOX.items()):
        paths.append(wobble(x, y, w, h, i))
        if k == "hero":
            paths.append(f"M{x + 20},{y + 20} L{x + w - 20},{y + h - 20} M{x + w - 20},{y + 20} L{x + 20},{y + h - 20}")
        if k in ("c1", "c2"):
            paths.append(f"M{x + 16},{y + 120} L{x + w - 16},{y + 118}")
    return "".join(f'<path id="p{i}" d="{d}" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>' for i, d in enumerate(paths)), len(paths)


SK, NSK = sketch()
LABELS = {"nav": "Menu", "hero": "Fotografia", "t1": "O que fazemos", "t2": "", "btn": "Encomendar", "c1": "Produto", "c2": "Produto"}
WF = "".join(f'<span class="wf" id="f{i}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">{LABELS[k]}</span>'
             for i, (k, (x, y, w, h)) in enumerate(BOX.items()))
FIN = ('<div id="fin"><div class="nav">Padaria do Largo<small>Pão · Bolos · Contactos</small></div>'
       '<div class="hero"><b style="left:520px;top:-60px;width:300px;height:300px"></b><b style="left:640px;top:150px;width:160px;height:160px"></b>'
       '<span>Pão quente<br>todas as manhãs</span></div><div class="t1">Feito aqui, desde 1987</div>'
       '<div class="t2">Encomendas para festas e eventos</div><div class="btn">Encomendar</div>'
       '<div class="c" style="left:470px"><i style="background:linear-gradient(150deg,#e9b77a,#b8743f)"></i><em>Broa</em></div>'
       '<div class="c" style="left:650px"><i style="background:linear-gradient(150deg,#f3d9a4,#d9a05a)"></i><em>Bolo-rei</em></div></div>')
CURSOR = ('<svg id="cur" viewBox="0 0 24 24"><path d="M4 2l16 9-7 2-3 7z" fill="#121125" stroke="#fff" stroke-width="1.5" stroke-linejoin="round"/></svg>')
ART = (f'<div id="win"><div class="tb"><i></i><i></i><i></i></div><div id="body"><div id="paper"></div>'
       f'<svg id="sk" viewBox="0 0 840 700">{SK}</svg>{WF}{FIN}</div></div>'
       f'<span id="lbl">Esboço</span><div id="toast">✓ Nova encomenda</div>{CURSOR}'
       '<div id="free"><span>Mockup e orçamento<b>0 €</b></span></div>'
       f'<img id="logo" src="{ASSETS}/logo_mark.svg" alt=""><div id="cta"><span>hivecode.pt</span></div>')

ART_JS = r"""
const NSK = __NSK__;
function art(t, E) {
  stage($('#win'), t, .3, E.s5 - .1);
  // 1. pencil sketch draws itself, one stroke after another
  for (let i = 0; i < NSK; i++) { const a = .7 + i * (E.s2 - 1.1) / NSK;
    $('#p' + i).style.strokeDashoffset = 1 - ease((t - a) / .45); }
  const sk = 1 - ease((t - E.est) / .5);
  $('#sk').style.opacity = sk; $('#paper').style.opacity = sk;
  // 2. clean wireframe blocks
  for (let i = 0; i < 7; i++) { const a = E.est + .12 * i, el = $('#f' + i);
    el.style.opacity = cl((t - a) / .2) * (1 - ease((t - E.cor) / .4));
    el.style.transform = `scale(${.94 + .06 * back((t - a) / .4)})`; }
  // 3. colours, photo, text
  const f = $('#fin'); f.style.opacity = ease((t - E.cor) / .5);
  f.querySelector('.hero').style.transform = `scale(${1 + .04 * (1 - ease((t - E.fot) / .8))})`;
  // label under the window follows the phase
  const L = $('#lbl'); L.textContent = t < E.est ? 'Esboço' : t < E.cor ? 'Estrutura' : t < E.s3 ? 'Design' : 'Site no ar';
  L.style.opacity = cl((t - .7) / .2) * (1 - ease((t - E.s4 + .2) / .3));
  // 4. cursor clicks "Encomendar" and an order comes in
  const c = $('#cur'), cm = ease((t - E.s3) / .7), click = t > E.tra && t < E.tra + .15 ? .85 : 1;
  c.style.opacity = cl((t - E.s3) / .2) * (1 - ease((t - E.s4) / .3));
  c.style.transform = `translate(${880 - 600 * cm}px,${1500 - 140 * cm}px) scale(${click})`;
  stage($('#toast'), t, E.tra + .1, E.s4 - .1, 40);
  stage($('#free'), t, E.s4, E.s5 - .1);
  const lg = back((t - E.s5 - .1) / .5);
  $('#logo').style.opacity = cl((t - E.s5 - .1) / .1);
  $('#logo').style.transform = `rotate(${-120 * (1 - lg)}deg) scale(${lg})`;
  const ct = back((t - E.site) / .45);
  $('#cta').style.opacity = cl((t - E.site) / .1);
  $('#cta').style.transform = `scale(${ct})`;
}
""".replace("__NSK__", str(NSK))


def main():
    total, scenes = reelkit.voice(SCENES, WORK / "voz.mp3")
    at = lambda s, w: reelkit.at(scenes, s, w)  # noqa: E731
    st = [s["start"] for s in scenes]
    ev = {"s2": st[1], "est": at(1, "estrutura:"), "cor": at(2, "cores,"), "fot": at(2, "fotografias"), "s3": st[3],
          "tra": at(3, "trabalha"), "s4": st[4], "s5": st[5], "site": at(5, "hivecode.pt.")}
    page = HERE / "reel.html"
    page.write_text(reelkit.page(scenes, ev, ART, CSS, ART_JS, theme="natalnoite"), encoding="utf-8")
    hits = [("pop", .3)] + [("click", .7 + i * (ev["s2"] - 1.1) / NSK) for i in range(0, NSK, 2)]
    hits += [("whoosh", ev["est"]), ("whoosh", ev["cor"]), ("click", ev["tra"]), ("pop", ev["tra"] + .1),
             ("pop", ev["s4"]), ("pop", ev["s5"] + .1), ("pop", ev["site"])]
    reelkit.render(page, WORK, total, WORK / "voz.mp3", hits, HERE / "reel.mp4")
    reelkit.cover(HERE / "reel.mp4", ev["tra"] + .6, HERE / "cover.jpg")
    print(f"reel.mp4 {total:.1f}s")


if __name__ == "__main__":
    main()
