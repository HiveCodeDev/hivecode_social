"""Reel "O seu site está pronto para o Natal? 5 coisas a rever" (natalnoite theme, 1080x1920).

python posts/2026-12-08-natal-checklist/reel/build.py
From the first frame a checklist card with five empty boxes is on screen (the hook); each item
lights up and gets ticked as the voice names it, with a small detail chip; then logo and CTA.
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
    ("O seu site está pronto para o Natal? Cinco coisas a rever.", 92, {"Natal?"}),
    ("Um: o horário de Natal, à vista.", 96, {"horário"}),
    ("Dois: até quando as encomendas chegam a tempo.", 92, {"encomendas"}),
    ("Três: vales-oferta para quem decide à última hora.", 92, {"vales-oferta"}),
    ("Quatro: um destaque de Natal na página inicial.", 92, {"destaque"}),
    ("Cinco: um contacto rápido, sempre visível.", 96, {"contacto", "rápido,"}),
    ("Precisa de ajuda? Mockup e orçamento gratuitos em hivecode.pt.", 88, {"gratuitos", "hivecode.pt."}),
]

NAVY, GOLD, CREAM = "#0E1A33", "#F2C14E", "#F6F1E7"
ITEMS = [("Horário de Natal", "24/12 · 9h às 13h"), ("Prazo de entrega", "Encomendas até 18/12"),
         ("Vales-oferta", "25 € · 50 € · 75 €"), ("Destaque de Natal", "Na página inicial"),
         ("Contacto rápido", "Telefone e WhatsApp")]

CSS = f"""
#list{{left:88px;right:88px;top:840px;padding:26px 40px;border-radius:40px;background:{CREAM};opacity:0;
 box-shadow:0 60px 120px -40px rgba(0,0,0,.6)}}
.row{{position:relative;display:flex;align-items:center;gap:30px;height:124px;border-bottom:3px dashed #d9d2c2;opacity:.38}}
.row:last-child{{border-bottom:0}}
.row .n{{flex:none;width:72px;height:72px;border-radius:50%;background:{NAVY};color:{GOLD};display:grid;place-items:center;font-size:38px;font-weight:800}}
.row .l{{flex:1;font-size:46px;font-weight:700;color:{NAVY};line-height:1.05}}
.row .l small{{display:block;margin-top:6px;font-size:28px;font-weight:600;color:#6a738c}}
.row .ck{{flex:none;width:70px;height:70px;border-radius:18px;border:6px solid {NAVY};box-sizing:border-box;position:relative}}
.row .ck b{{position:absolute;inset:-6px;border-radius:18px;background:{GOLD};color:{NAVY};display:grid;place-items:center;font-size:48px;font-weight:900;opacity:0}}
#logo{{left:440px;top:900px;width:200px;height:200px;opacity:0}}
#cta{{left:88px;right:88px;top:1190px;display:flex;justify-content:center;opacity:0}}
#cta span{{padding:32px 56px;border-radius:999px;background:{GOLD};color:{NAVY};font-size:50px;font-weight:800}}
"""

ART = ('<div id="list">'
       + "".join(f'<div class="row" id="r{i}"><span class="n">{i + 1}</span><span class="l">{n}<small>{d}</small></span>'
                 f'<span class="ck"><b>✓</b></span></div>' for i, (n, d) in enumerate(ITEMS))
       + f'</div><img id="logo" src="{ASSETS}/logo_mark.svg" alt=""><div id="cta"><span>hivecode.pt</span></div>')

ART_JS = r"""
function art(t, E) {
  stage($('#list'), t, .15, E.s6 - .1);
  E.items.forEach((a, i) => {
    const r = $('#r' + i), on = cl((t - a) / .25), ck = r.querySelector('b'), k = back((t - a - .35) / .4);
    r.style.opacity = .38 + .62 * on;
    r.style.transform = `scale(${1 + .04 * Math.sin(Math.PI * cl((t - a) / .5))})`;
    ck.style.opacity = cl((t - a - .35) / .1);
    ck.style.transform = `scale(${k}) rotate(${-25 * (1 - k)}deg)`;
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
    items = [st[k] + .15 for k in range(1, 6)]
    ev = {"items": items, "s6": st[6], "site": at(6, "hivecode.pt.")}
    page = HERE / "reel.html"
    page.write_text(reelkit.page(scenes, ev, ART, CSS, ART_JS, theme="natalnoite"), encoding="utf-8")
    hits = [("pop", .15)] + [h for a in items for h in (("whoosh", a - .1), ("click", a + .4))]
    hits += [("pop", ev["s6"] + .1), ("pop", ev["site"])]
    reelkit.render(page, WORK, total, WORK / "voz.mp3", hits, HERE / "reel.mp4")
    reelkit.cover(HERE / "reel.mp4", ev["s6"] - .3, HERE / "cover.jpg")
    print(f"reel.mp4 {total:.1f}s")


if __name__ == "__main__":
    main()
