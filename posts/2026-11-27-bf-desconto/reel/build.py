"""Reel "Black Friday na HiveCode: 20% de desconto em sites" (blackfriday theme, 1080x1920).

python posts/2026-11-27-bf-desconto/reel/build.py
A browser window with a website wireframe swings in on a price tag; a big "-20%" stamp slams on it;
a date chip "até domingo, 29/11" drops in; the tag flips to "Mockup e orçamento: 0 €"; logo and CTA.
Offer (confirmed 2026-11-23): 20% off website creation only, for quotes requested until Sunday 29 Nov.
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
    ("Black Friday na HiveCode.", 130, {"Black", "Friday"}),
    ("20% de desconto na criação do seu site.", 104, {"20%"}),
    ("Para orçamentos pedidos até domingo, 29 de novembro.", 88, {"domingo,"}),
    ("O mockup e o orçamento continuam gratuitos.", 96, {"gratuitos."}),
    ("Peça o seu em hivecode.pt.", 110, {"hivecode.pt."}),
]

CSS = """
#win{left:120px;right:120px;top:820px;height:560px;border-radius:30px;background:#fff;overflow:hidden;opacity:0;box-shadow:0 60px 120px -40px rgba(255,212,0,.35)}
#bar{height:76px;background:#f1f1f1;display:flex;align-items:center;gap:12px;padding:0 28px}
#bar i{width:18px;height:18px;border-radius:50%;background:#d0d0d0}
.wb{position:absolute;border-radius:14px;background:#ececec}
#stamp{left:470px;top:740px;padding:22px 38px;border:12px solid #FFD400;border-radius:28px;background:#0A0A0A;color:#FFD400;font-size:150px;font-weight:800;letter-spacing:-.04em;line-height:1;opacity:0}
#date{left:0;right:0;top:1440px;display:flex;justify-content:center;opacity:0}
#date span{padding:26px 46px;border-radius:999px;border:5px solid #FFD400;color:#fff;font-size:52px;font-weight:800}
#free{left:0;right:0;top:1440px;display:flex;justify-content:center;opacity:0}
#free span{padding:26px 46px;border-radius:999px;background:#fff;color:#0A0A0A;font-size:52px;font-weight:800}
#free b{color:#0A0A0A;background:#FFD400;padding:0 16px;border-radius:12px;margin-left:12px}
#logo{left:440px;top:930px;width:200px;height:200px;opacity:0;filter:brightness(0) invert(1)}
#cta{left:88px;right:88px;top:1220px;display:flex;justify-content:center;opacity:0}
#cta span{padding:32px 56px;border-radius:999px;background:#FFD400;color:#0A0A0A;font-size:50px;font-weight:800}
"""

BLOCKS = ["left:30px;right:30px;top:100px;height:56px", "left:30px;right:30px;top:180px;height:200px",
          "left:30px;width:380px;top:404px;height:30px", "left:30px;width:260px;top:454px;height:60px"]
ART = ('<div id="win"><div id="bar"><i></i><i></i><i></i></div>'
       + "".join(f'<span class="wb" id="w{i}" style="{s}"></span>' for i, s in enumerate(BLOCKS))
       + '</div><div id="stamp">−20%</div><div id="date"><span>até domingo, 29/11</span></div>'
       + '<div id="free"><span>Mockup e orçamento<b>0 €</b></span></div>'
       + f'<img id="logo" src="{ASSETS}/logo_mark.svg" alt=""><div id="cta"><span>hivecode.pt</span></div>')

ART_JS = r"""
function art(t, E) {
  stage($('#win'), t, .3, E.s4 + .6);
  [0, 1, 2, 3].forEach(i => { const el = $('#w' + i), a = .5 + .15 * i;
    el.style.opacity = cl((t - a) / .15);
    el.style.background = t > E.pct ? (i === 1 ? 'linear-gradient(150deg,#fff3a6,#FFD400)' : i === 3 ? '#0A0A0A' : '#ececec') : '#ececec'; });
  const s = $('#stamp'); s.style.opacity = cl((t - E.pct) / .08) * (1 - cl((t - E.s4 - .4) / .3));
  s.style.transform = `rotate(-10deg) scale(${1 + 1.6 * (1 - ease((t - E.pct) / .3))})`;
  stage($('#date'), t, E.dom, E.s4 - .1);
  stage($('#free'), t, E.s4, E.s5 - .1);
  const lg = back((t - E.s5 - .1) / .5);
  $('#logo').style.opacity = cl((t - E.s5 - .1) / .1);
  $('#logo').style.transform = `rotate(${-120 * (1 - lg)}deg) scale(${lg})`;
  const ct = back((t - E.site) / .45);
  $('#cta').style.opacity = cl((t - E.site) / .1);
  $('#cta').style.transform = `scale(${ct})`;
}
"""


def main():
    total, scenes = reelkit.voice(SCENES, WORK / "voz.mp3")
    at = lambda s, w: reelkit.at(scenes, s, w)  # noqa: E731
    st = [s["start"] for s in scenes]
    ev = {"pct": at(1, "20%"), "dom": at(2, "domingo,"), "s4": st[3], "s5": st[4], "site": at(4, "hivecode.pt.")}
    page = HERE / "reel.html"
    page.write_text(reelkit.page(scenes, ev, ART, CSS, ART_JS, theme="blackfriday"), encoding="utf-8")
    hits = [("pop", .3)] + [("click", .5 + .15 * i) for i in range(4)]
    hits += [("thump", ev["pct"]), ("pop", ev["dom"]), ("pop", ev["s4"]), ("pop", ev["s5"] + .1), ("pop", ev["site"])]
    reelkit.render(page, WORK, total, WORK / "voz.mp3", hits, HERE / "reel.mp4")
    reelkit.cover(HERE / "reel.mp4", ev["dom"] + .6, HERE / "cover.jpg")
    print(f"reel.mp4 {total:.1f}s")


if __name__ == "__main__":
    main()
