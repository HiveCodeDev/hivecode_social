"""Reel "Black Friday: o seu site inspira confiança?" (websites), blackfriday theme, 1080x1920.

python posts/2026-11-21-bf-confianca/reel/build.py
A warning shield shakes (fear of scams); a shop window appears with an address bar and three trust
signals tick one by one (padlock, contacts, returns policy); then the countdown and the offer.
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
    ("Na Black Friday, muitos clientes têm receio de fraudes.", 96, {"fraudes."}),
    ("Antes de comprar, procuram sinais de confiança.", 100, {"confiança."}),
    ("Cadeado e endereço seguro.", 120, {"Cadeado"}),
    ("Contactos e morada à vista.", 120, {"Contactos"}),
    ("Política de devolução clara.", 120, {"devolução"}),
    ("Faltam seis dias. Mockup e orçamento gratuitos em hivecode.pt.", 84, {"seis", "gratuitos"}),
]
ROWS = [("🔒", "Ligação segura"), ("📍", "Contactos e morada"), ("↩️", "Devoluções claras")]

CSS = """
#warn{left:390px;top:900px;width:300px;height:340px;opacity:0}
#win{left:88px;right:88px;top:820px;border-radius:30px;background:#fff;color:#0A0A0A;overflow:hidden;opacity:0;box-shadow:0 60px 120px -40px rgba(255,212,0,.35)}
#bar{display:flex;align-items:center;gap:16px;height:96px;padding:0 30px;background:#f1f1f1;font-size:34px;color:#555}
#lock{font-size:36px;opacity:.15}
#url{flex:1;padding:14px 22px;border-radius:999px;background:#fff;font-weight:600}
.row{display:flex;align-items:center;gap:28px;height:150px;margin:0 40px;font-size:46px;font-weight:700;border-bottom:3px solid #eee}
.row:last-child{border:0}
.row .ic{font-size:56px;width:80px;text-align:center}
.row .bx{margin-left:auto;width:80px;height:80px;border-radius:18px;border:6px solid #ccc;display:grid;place-items:center;color:#0A0A0A;font-size:52px;font-weight:800}
.row.on .bx{background:#FFD400;border-color:#FFD400}
#days{left:0;right:0;top:900px;text-align:center;opacity:0}
#days b{display:block;font-size:360px;line-height:1;color:#FFD400;font-weight:800}
#days span{font-size:64px;font-weight:800;letter-spacing:.08em}
#cta{left:88px;right:88px;top:1460px;display:flex;justify-content:center;opacity:0}
#cta span{padding:32px 56px;border-radius:999px;background:#FFD400;color:#0A0A0A;font-size:46px;font-weight:800}
"""

WARN = ('<svg id="warn" viewBox="0 0 100 114"><path d="M50 4 92 20v34c0 28-18 46-42 56C26 100 8 82 8 54V20Z" fill="#1a1a1a" stroke="#e5484d" stroke-width="5"/>'
        '<path d="M50 30v34" stroke="#e5484d" stroke-width="9" stroke-linecap="round"/><circle cx="50" cy="80" r="6" fill="#e5484d"/></svg>')
ART = (WARN + '<div id="win"><div id="bar"><span id="lock">🔒</span><span id="url">https://a-sua-loja.pt</span></div>'
       + "".join(f'<div class="row" id="r{i}"><span class="ic">{ic}</span>{t}<span class="bx">✓</span></div>' for i, (ic, t) in enumerate(ROWS))
       + '</div><div id="days"><b>6</b><span>DIAS</span></div><div id="cta"><span>hivecode.pt</span></div>')

ART_JS = r"""
function art(t, E) {
  const w = $('#warn');
  w.style.opacity = cl((t - .2) / .2) * (1 - cl((t - E.s2) / .3));
  w.style.transform = `translateX(${t > E.fraudes && t < E.fraudes + .5 ? 16 * Math.sin(t * 60) : 0}px) scale(${back((t - .2) / .5)})`;
  stage($('#win'), t, E.s2 + .1, E.s6);
  const ticks = [E.cadeado, E.contactos, E.devolucao];
  ticks.forEach((a, i) => {
    const r = $('#r' + i), on = t > a + .2;
    r.className = 'row' + (on ? ' on' : '');
    r.querySelector('.bx').style.transform = `scale(${on ? back((t - a - .2) / .35) : 1})`;
  });
  $('#lock').style.opacity = t > E.cadeado ? 1 : .15;
  stage($('#days'), t, E.s6, E.gratuitos - .1);
  const ct = back((t - E.gratuitos) / .45);
  $('#cta').style.opacity = cl((t - E.gratuitos) / .1);
  $('#cta').style.transform = `scale(${ct})`;
}
"""


def main():
    total, scenes = reelkit.voice(SCENES, WORK / "voz.mp3")
    at = lambda s, w: reelkit.at(scenes, s, w)  # noqa: E731
    st = [s["start"] for s in scenes]
    ev = {"fraudes": at(0, "fraudes."), "s2": st[1], "cadeado": at(2, "Cadeado"), "contactos": at(3, "Contactos"),
          "devolucao": at(4, "devolução"), "s6": st[5], "gratuitos": at(5, "gratuitos")}
    page = HERE / "reel.html"
    page.write_text(reelkit.page(scenes, ev, ART, CSS, ART_JS, theme="blackfriday"), encoding="utf-8")
    hits = [("pop", .2), ("error", ev["fraudes"]), ("pop", ev["s2"] + .1)]
    hits += [("click", ev[k] + .2) for k in ("cadeado", "contactos", "devolucao")]
    hits += [("thump", ev["s6"]), ("pop", ev["gratuitos"])]
    reelkit.render(page, WORK, total, WORK / "voz.mp3", hits, HERE / "reel.mp4")
    reelkit.cover(HERE / "reel.mp4", ev["devolucao"] + .8, HERE / "cover.jpg")
    print(f"reel.mp4 {total:.1f}s")


if __name__ == "__main__":
    main()
