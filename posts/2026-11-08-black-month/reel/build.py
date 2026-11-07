"""Reel "Black Month: não é só um dia" (websites), blackmonth theme (yellow, black type), 1080x1920.

python posts/2026-11-08-black-month/reel/build.py
A November calendar: Black Friday (27) turns black, then every other day follows until the whole
month is black. Four weekly bars stand well above a dashed "normal" line. A site stuck loading
sends its visitors to the competition. Then logo and the free mockup and quote offer.
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
    ("Novembro já não é só Black Friday.", 120, {"Black", "Friday."}),
    ("Muitas lojas fazem promoções o mês inteiro: é o Black Month.", 92, {"Black", "Month."}),
    ("São quatro semanas com mais visitas do que o normal.", 92, {"quatro", "semanas"}),
    ("Se o site é lento ou confuso, essas visitas vão para a concorrência.", 86, {"concorrência."}),
    ("Ainda vai a tempo: mockup e orçamento gratuitos em hivecode.pt.", 84, {"gratuitos", "hivecode.pt."}),
]
OFFSET = 6  # 1 November 2026 is a Sunday; the grid starts on Monday.

CSS = """
#cal{left:120px;right:120px;top:800px;padding:36px 34px 40px;border-radius:40px;background:#fff;opacity:0;box-shadow:0 50px 100px -40px rgba(0,0,0,.45)}
#cal h4{margin:0 0 22px;font-size:46px;font-weight:800;letter-spacing:.08em;color:#0A0A0A;text-align:center}
#cal .g{display:grid;grid-template-columns:repeat(7,1fr);gap:10px}
#cal .wd{text-align:center;font-size:28px;font-weight:700;color:#8a8a8a;padding-bottom:6px}
#cal .d{height:84px;border-radius:16px;display:grid;place-items:center;font-size:36px;font-weight:700;color:#0A0A0A;background:#f2f2f2}
#cal .d.on{background:#0A0A0A;color:#FFD400}
#chart{left:120px;right:120px;top:820px;height:700px;opacity:0}
#chart .b{position:absolute;bottom:80px;width:150px;border-radius:22px 22px 0 0;background:#0A0A0A;transform-origin:bottom}
#chart .l{position:absolute;bottom:20px;width:150px;text-align:center;font-size:32px;font-weight:700;color:#0A0A0A}
#norm{position:absolute;left:-20px;right:-20px;bottom:230px;border-top:6px dashed #fff;z-index:2}
#norm span{position:absolute;left:30px;top:-70px;padding:6px 18px;border-radius:12px;background:#FFD400;font-size:34px;font-weight:700;color:#0A0A0A}
#site{left:120px;right:120px;top:820px;height:420px;border-radius:32px;background:#fff;overflow:hidden;opacity:0;box-shadow:0 50px 100px -40px rgba(0,0,0,.45)}
#site .tb{height:58px;background:#eee;display:flex;align-items:center;gap:12px;padding:0 22px}
#site .tb b{width:16px;height:16px;border-radius:50%;background:#ccc}
#spin{position:absolute;left:50%;top:150px;width:110px;height:110px;margin-left:-55px;border-radius:50%;border:12px solid #e6e6e6;border-top-color:#0A0A0A;box-sizing:border-box}
#load{position:absolute;left:0;right:0;top:300px;text-align:center;font-size:40px;font-weight:600;color:#8a8a8a}
.v{left:0;top:0;font-size:70px;opacity:0}
#comp{left:560px;top:1400px;padding:26px 40px;border-radius:999px;background:#0A0A0A;color:#FFD400;font-size:44px;font-weight:700;opacity:0}
#logo{left:440px;top:930px;width:200px;height:200px;opacity:0;filter:brightness(0)}
#cta{left:88px;right:88px;top:1220px;display:flex;justify-content:center;opacity:0}
#cta span{padding:32px 56px;border-radius:999px;background:#0A0A0A;color:#FFD400;font-size:46px;font-weight:700}
"""

WD = "STQQSSD"
BARS = [(0, .78), (1, .86), (2, .82), (3, 1.0)]
ART = ('<div id="cal"><h4>NOVEMBRO</h4><div class="g">' + "".join(f'<span class="wd">{w}</span>' for w in WD)
       + "<span></span>" * OFFSET + "".join(f'<span class="d" id="d{d}">{d}</span>' for d in range(1, 31)) + "</div></div>"
       + '<div id="chart"><div id="norm"><span>normal</span></div>'
       + "".join(f'<i class="b" id="b{i}" style="left:{20 + 215 * i}px"></i><span class="l" style="left:{20 + 215 * i}px">Sem. {i + 1}</span>' for i, _ in BARS)
       + "</div>"
       + '<div id="site"><div class="tb"><b></b><b></b><b></b></div><span id="spin"></span><span id="load">A carregar…</span></div>'
       + "".join(f'<span class="v" id="v{i}">🛒</span>' for i in range(5))
       + '<div id="comp">Concorrência</div>'
       + f'<img id="logo" src="{ASSETS}/logo_mark.svg" alt=""><div id="cta"><span>hivecode.pt</span></div>')

ART_JS = f"const BARS = {[h for _, h in BARS]};" + r"""
function art(t, E) {
  stage($('#cal'), t, .15, E.s3);
  for (let d = 1; d <= 30; d++) {
    // Black Friday first, then the rest of the month in a quick cascade.
    const a = d === 27 ? E.friday : E.mes + .05 * d;
    $('#d' + d).className = 'd' + (t > a ? ' on' : '');
    $('#d' + d).style.transform = `scale(${t > a && t < a + .3 ? back((t - a) / .3) : 1})`;
  }
  stage($('#chart'), t, E.s3, E.s4);
  BARS.forEach((h, i) => { $('#b' + i).style.height = `${520 * h * ease((t - E.quatro - .15 * i) / .6)}px`; });
  stage($('#site'), t, E.s4, E.s5);
  $('#spin').style.transform = `rotate(${t * 400}deg)`;
  // Visitors (carts) arrive at the slow site and walk off to the competition.
  [0, 1, 2, 3, 4].forEach(i => {
    const a = E.essas + .3 * i, k = ease((t - a) / 1.1), el = $('#v' + i);
    el.style.opacity = cl((t - E.s4 - .2 - .1 * i) / .2) * (1 - cl((k - .85) / .15));
    el.style.transform = `translate(${180 + 140 * i + (620 - 140 * i) * k}px,${1290 + 110 * k}px)`;
  });
  stage($('#comp'), t, E.essas - .2, E.s5);
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
    ev = {"friday": at(0, "Friday."), "mes": at(1, "inteiro:"), "s3": st[2], "quatro": at(2, "quatro"), "s4": st[3],
          "essas": at(3, "essas"), "s5": st[4], "site": at(4, "hivecode.pt.")}
    page = HERE / "reel.html"
    page.write_text(reelkit.page(scenes, ev, ART, CSS, ART_JS, theme="blackmonth"), encoding="utf-8")
    hits = [("pop", .15), ("thump", ev["friday"])] + [("click", ev["mes"] + .05 * d) for d in range(1, 31, 3)]
    hits += [("rise", ev["quatro"]), ("error", ev["essas"]), ("whoosh", ev["essas"] + .3)]
    hits += [("pop", ev["s5"] + .15), ("pop", ev["site"])]
    reelkit.render(page, WORK, total, WORK / "voz.mp3", hits, HERE / "reel.mp4")
    reelkit.cover(HERE / "reel.mp4", ev["s3"] - .3, HERE / "cover.jpg")
    print(f"reel.mp4 {total:.1f}s")


if __name__ == "__main__":
    main()
