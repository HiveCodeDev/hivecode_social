"""Reel "Web Summit: e o básico?" (websites), night base, 1080x1920.

python posts/2026-11-09-web-summit/reel/build.py
Big-tech buzzwords float around and drop away; a three-line checklist (fast on the phone, on
Google, contact in sight) ticks one line per question, then the free mockup and quote offer.
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
    ("Esta semana, a Web Summit fala de inteligência artificial e de startups.", 92, {"inteligência", "artificial"}),
    ("Mas, para a maioria das empresas, o mais importante continua a ser o básico.", 84, {"básico."}),
    ("O seu site abre em três segundos no telemóvel?", 88, {"três", "segundos"}),
    ("Aparece no Google quando procuram o seu serviço?", 88, {"Google"}),
    ("O contacto está à vista?", 104, {"contacto"}),
    ("Se falhou alguma, peça um mockup e um orçamento gratuitos em hivecode.pt.", 80, {"gratuitos", "hivecode.pt."}),
]
CHIPS = [("IA", 120, 860), ("Startups", 560, 800), ("Investidores", 300, 1010), ("Robótica", 640, 1160), ("Cloud", 140, 1250),
         ("Criptomoedas", 420, 1380), ("Metaverso", 120, 1520), ("Agentes de IA", 560, 1560)]
ROWS = [("⚡", "Abre em 3 segundos"), ("🔍", "Aparece no Google"), ("📞", "Contacto à vista")]

CSS = """
.chip{left:0;top:0;padding:22px 36px;border-radius:999px;background:rgba(255,255,255,.08);border:2px solid rgba(255,255,255,.22);color:#f3f1fb;font-size:40px;font-weight:600;opacity:0;white-space:nowrap}
#list{left:88px;right:88px;top:860px;padding:20px 50px;border-radius:36px;background:#fff;color:#121125;opacity:0;box-shadow:0 60px 120px -40px rgba(0,0,0,.7)}
.row{display:flex;align-items:center;gap:30px;height:170px;font-size:50px;font-weight:600;border-bottom:3px solid #eceaf4;transition:none}
.row:last-child{border:0}
.row .ic{font-size:60px;width:80px;text-align:center}
.row .bx{margin-left:auto;width:84px;height:84px;border-radius:20px;border:6px solid #c9c4dc;display:grid;place-items:center;color:#fff;font-size:56px;font-weight:800}
.row.on .bx{background:#1f8a4c;border-color:#1f8a4c}
.row.cur{color:#4877FE}
#logo{left:440px;top:930px;width:200px;height:200px;opacity:0}
#cta{left:88px;right:88px;top:1220px;display:flex;justify-content:center;opacity:0}
#cta span{padding:32px 56px;border-radius:999px;background:linear-gradient(90deg,#D752FE,#4877FE);color:#fff;font-size:46px;font-weight:600}
"""

ART = "".join(f'<span class="chip" id="c{i}">{w}</span>' for i, (w, _, _) in enumerate(CHIPS)) + \
    '<div id="list">' + "".join(f'<div class="row" id="r{i}"><span class="ic">{ic}</span>{t}<span class="bx">✓</span></div>' for i, (ic, t) in enumerate(ROWS)) + "</div>" + \
    f'<img id="logo" src="{ASSETS}/logo_mark.svg" alt=""><div id="cta"><span>hivecode.pt</span></div>'

ART_JS = "const CH = " + str([[x, y] for _, x, y in CHIPS]) + r""";
function art(t, E) {
  // Buzzwords drift in, then fall off the screen when "o básico" is said.
  CH.forEach(([x, y], i) => {
    const a = .2 + .25 * i, k = back((t - a) / .5), fall = ease((t - E.basico - .03 * i) / .7);
    const el = $('#c' + i);
    el.style.opacity = cl((t - a) / .15) * (1 - fall);
    el.style.transform = `translate(${x + 12 * Math.sin(t * 1.3 + i)}px,${y + 10 * Math.cos(t * 1.1 + i) + 900 * fall * fall}px) rotate(${40 * fall * (i % 2 ? 1 : -1)}deg) scale(${k})`;
  });
  stage($('#list'), t, E.basico + .4, E.s6);
  const ticks = [E.tres, E.google, E.contacto];
  [0, 1, 2].forEach(i => {
    const r = $('#r' + i), on = t > ticks[i] + .6;
    r.className = 'row' + (on ? ' on' : '') + (t > ticks[i] - .2 && !on ? ' cur' : '');
    r.querySelector('.bx').style.transform = `scale(${on ? back((t - ticks[i] - .6) / .35) : 1})`;
  });
  const lg = back((t - E.s6 - .1) / .5);
  $('#logo').style.opacity = cl((t - E.s6 - .1) / .1);
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
    ev = {"basico": at(1, "básico."), "tres": at(2, "três"), "google": at(3, "Google"), "contacto": at(4, "contacto"),
          "s6": st[5], "site": at(5, "hivecode.pt.")}
    page = HERE / "reel.html"
    page.write_text(reelkit.page(scenes, ev, ART, CSS, ART_JS), encoding="utf-8")
    hits = [("pop", .2 + .25 * i) for i in range(len(CHIPS))] + [("whoosh", ev["basico"]), ("pop", ev["basico"] + .4)]
    hits += [("click", ev[k] + .6) for k in ("tres", "google", "contacto")]
    hits += [("pop", ev["s6"] + .15), ("pop", ev["site"])]
    reelkit.render(page, WORK, total, WORK / "voz.mp3", hits, HERE / "reel.mp4")
    reelkit.cover(HERE / "reel.mp4", ev["contacto"] + 1.2, HERE / "cover.jpg")
    print(f"reel.mp4 {total:.1f}s")


if __name__ == "__main__":
    main()
