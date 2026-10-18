"""Reel "Quanto tempo perde a copiar dados?" (HiveCode Business), 1080x1920.

python posts/2026-10-21-tempo-a-copiar/reel/build.py
The sum is built on screen as the voice says it (10 orders x 3 min = 30 min a day = 2h30 a
week = 10h+ a month); then a custom system brings the counter back to zero.
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
    ("Quanto tempo perde por semana a copiar dados?", 88, {"tempo"}),
    ("Vamos fazer as contas.", 96, {"contas."}),
    ("Dez encomendas por dia.", 96, {"Dez"}),
    ("Três minutos para passar cada uma do email para o Excel.", 80, {"Três", "minutos"}),
    ("São trinta minutos por dia, duas horas e meia por semana.", 80, {"duas", "horas", "e", "meia"}),
    ("Mais de dez horas por mês.", 100, {"dez", "horas"}),
    ("Com um sistema à medida, as encomendas entram sozinhas e esse tempo volta para o seu negócio.", 72, {"sozinhas"}),
    ("Saiba mais em hivecode.pt/business.", 76, {"hivecode.pt/business."}),
]

CSS = """
.clock{left:390px;top:880px;width:300px;height:300px;border-radius:50%;border:12px solid #f3f1fb;background:#1b1638;opacity:0}
.clock i{position:absolute;left:50%;bottom:50%;width:12px;margin-left:-6px;border-radius:6px;background:#f3f1fb;transform-origin:50% 100%}
#envs{left:170px;top:860px;width:740px;display:grid;grid-template-columns:repeat(5,1fr);gap:24px}
.env{height:96px;border-radius:14px;background:#f3f1fb;position:relative;opacity:0}
.env:before{content:"";position:absolute;left:0;right:0;top:0;border-left:66px solid transparent;border-right:66px solid transparent;border-top:48px solid #c9c3e6}
.chip{display:flex;align-items:center;justify-content:center;gap:16px;padding:22px 38px;border-radius:999px;background:#1b1638;border:1px solid rgba(255,255,255,.18);font-size:44px;font-weight:700;opacity:0;white-space:nowrap}
#lab{left:88px;right:88px;top:1100px;display:flex;justify-content:center;font-size:34px;color:var(--soft);opacity:0}
#mul{left:0;right:0;top:1170px;margin:0 auto;width:360px}
#r1{left:0;right:0;top:1290px;margin:0 auto;width:560px}
#r2{left:0;right:0;top:1400px;margin:0 auto;width:660px;background:#265ADF;border:0}
#big{left:88px;right:88px;top:930px;text-align:center;opacity:0}
#big b{display:block;font-size:260px;font-weight:800;letter-spacing:-.05em;line-height:1}
#big span{font-size:40px;color:var(--soft)}
#ok{left:740px;top:930px;width:120px;height:120px;border-radius:50%;background:#2fbf71;display:grid;place-items:center;opacity:0}
.flash{inset:0;background:#fff;opacity:0;z-index:9}
#logo{left:440px;top:930px;width:200px;height:200px;opacity:0}
#cta{left:88px;right:88px;top:1220px;display:flex;justify-content:center;opacity:0}
#cta span{padding:32px 54px;border-radius:999px;background:#265ADF;font-size:44px;font-weight:600;box-shadow:0 30px 70px -20px rgba(72,119,254,.8)}
"""

CHECK = '<svg viewBox="0 0 24 24" width="64" height="64" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>'
ART = f"""
<div class="clock" id="clock"><i id="hh" style="height:80px"></i><i id="mh" style="height:110px;width:9px;margin-left:-4px"></i></div>
<div id="envs">{'<span class="env"></span>' * 10}</div>
<div id="lab">10 encomendas por dia</div>
<div class="chip" id="mul">× 3 minutos</div>
<div class="chip" id="r1">= 30 minutos por dia</div>
<div class="chip" id="r2">= 2h30 por semana</div>
<div id="big"><b id="bigv">10 h+</b><span id="bigl">por mês a copiar dados</span></div>
<div id="ok">{CHECK}</div>
<div class="flash" id="flash"></div>
<img id="logo" src="{ASSETS}/logo_side.png" alt="">
<div id="cta"><span>hivecode.pt/business</span></div>
"""

ART_JS = r"""
function art(t, E) {
  // The question: a clock spinning fast.
  const ck = $('#clock'), ck1 = 1 - ease((t - E.s3) / .3);
  pop(ck, t, .15); ck.style.opacity = cl((t - .15) / .1) * ck1;
  $('#hh').style.transform = `rotate(${t * 200}deg)`; $('#mh').style.transform = `rotate(${t * 1300}deg)`;
  // The sum, piece by piece; dimmed under the monthly total, gone on the glitch.
  const dim = 1 - .85 * cl((t - E.s6) / .3), gone = 1 - ease((t - E.s7) / .3);
  $$('.env').forEach((e, i) => { pop(e, t, E.dez + .08 * i); e.style.opacity = cl((t - E.dez - .08 * i) / .1) * dim * gone; });
  const lab = $('#lab'); lab.style.opacity = cl((t - E.dez - .9) / .2) * dim * gone;
  [['#mul', E.tres], ['#r1', E.trinta], ['#r2', E.duas]].forEach(([s, a]) => {
    pop($(s), t, a); $(s).style.opacity = cl((t - a) / .1) * dim * gone;
  });
  // The month: a huge red total that shakes, then counts back to zero once the system takes over.
  const big = $('#big'), bk = back((t - E.s6 - .1) / .5), fin = 1 - ease((t - E.s8) / .35);
  const down = ease((t - E.sozinhas) / 1.2);
  big.style.opacity = cl((t - E.s6 - .1) / .1) * fin;
  const sh = t < E.s7 ? 6 * Math.sin(t * 40) * cl((t - E.s6 - .6) / .2) : 0;
  big.style.transform = `translateX(${sh}px) scale(${bk})`;
  $('#bigv').textContent = t < E.sozinhas ? '10 h+' : `${Math.round(10 * (1 - down))} h`;
  $('#bigv').style.color = t < E.sozinhas ? '#ff4d6d' : `rgb(${255 - 208 * down},${77 + 114 * down},${109 + 4 * down})`;
  $('#bigl').textContent = t < E.sozinhas ? 'por mês a copiar dados' : 'a copiar dados';
  pop($('#ok'), t, E.sozinhas + 1.2); $('#ok').style.opacity = cl((t - E.sozinhas - 1.2) / .1) * fin;
  $('#flash').style.opacity = .5 * Math.max(0, 1 - Math.abs(t - E.s7 - .1) / .12);
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
    ev = {"s3": st[2], "dez": at(2, "Dez"), "tres": at(3, "Três"), "trinta": at(4, "trinta"), "duas": at(4, "duas"),
          "s6": st[5], "s7": st[6], "sozinhas": at(6, "sozinhas"), "s8": st[7], "site": at(7, "hivecode.pt/business.")}
    page = HERE / "reel.html"
    page.write_text(reelkit.page(scenes, ev, ART, CSS, ART_JS, corner="Business"), encoding="utf-8")
    hits = [("pop", .15)] + [("click", ev["dez"] + .08 * i) for i in range(10)]
    hits += [("pop", ev["tres"]), ("pop", ev["trinta"]), ("pop", ev["duas"]), ("thump", ev["s6"] + .1), ("error", ev["s6"] + .6)]
    hits += [("rise", ev["s7"] - .4), ("whoosh", ev["s7"]), ("pop", ev["sozinhas"] + 1.2), ("pop", ev["s8"] + .15), ("pop", ev["site"])]
    reelkit.render(page, WORK, total, WORK / "voz.mp3", hits, HERE / "reel.mp4")
    reelkit.cover(HERE / "reel.mp4", ev["s6"] + 1.2, HERE / "cover.jpg")
    print(f"reel.mp4 {total:.1f}s")


if __name__ == "__main__":
    main()
