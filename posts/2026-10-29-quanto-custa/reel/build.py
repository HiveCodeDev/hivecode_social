"""Reel "Quanto custa um site?" (websites), blue theme, 1080x1920.

python posts/2026-10-29-quanto-custa/reel/build.py
A price tag with a spinning question mark, then the four factors pile up as white cards:
pages stacking, a shop checkout, content (text, photo, PT/EN), monthly care. A small and a
large site side by side; close on the logo.
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
    ("Quanto custa um site?", 120, {"custa"}),
    ("Depende de quatro coisas.", 100, {"quatro"}),
    ("Primeiro, o número de páginas.", 92, {"páginas."}),
    ("Segundo, se precisa de loja online, com pagamentos e encomendas.", 76, {"loja", "online,"}),
    ("Terceiro, os conteúdos: textos, fotografias e traduções.", 80, {"conteúdos:"}),
    ("Quarto, a manutenção depois de o site estar no ar.", 80, {"manutenção"}),
    ("Um site de apresentação e uma loja com centenas de produtos não custam o mesmo.", 70, {"não", "custam", "o", "mesmo."}),
    ("Fale connosco em hivecode.pt e saiba quanto custa o seu.", 76, {"hivecode.pt"}),
]

CSS = """
.wc{border-radius:28px;background:#fff;color:#121125;opacity:0;box-shadow:0 40px 80px -30px rgba(10,20,80,.7)}
#tag{left:330px;top:900px;width:420px;height:300px;border-radius:30px 30px 30px 30px;display:grid;place-items:center;font-size:220px;font-weight:800;color:#265ADF}
#tag:before{content:"";position:absolute;left:-46px;top:105px;width:90px;height:90px;border-radius:50%;background:#265ADF;border:14px solid #fff}
.pg{left:340px;top:930px;width:400px;height:500px;border-radius:22px;background:#fff;opacity:0;padding:40px 36px;box-shadow:0 30px 60px -30px rgba(10,20,80,.8)}
.pg b{display:block;height:26px;border-radius:13px;background:#dbe5ff;margin-bottom:22px}
#shop{left:200px;top:900px;width:680px;padding:40px;display:flex;flex-direction:column;gap:22px}
#shop .r{display:flex;justify-content:space-between;align-items:center;font-size:38px;font-weight:600}
#pay{padding:26px;border-radius:18px;background:#265ADF;color:#fff;font-size:38px;font-weight:600;text-align:center}
#cont{left:170px;top:900px;width:740px;height:520px}
#cont>*{position:absolute}
.ph{left:0;top:0;width:340px;height:260px;border-radius:22px;background:linear-gradient(150deg,#FFD84D,#ff9f43);opacity:0}
.ln{left:380px;width:360px;height:26px;border-radius:13px;background:#fff;opacity:0}
.lang{padding:18px 30px;border-radius:999px;background:#121125;color:#fff;font-size:36px;font-weight:700;opacity:0}
#care{left:240px;top:900px;width:600px;padding:40px;display:grid;grid-template-columns:repeat(6,1fr);gap:16px}
#care .m{height:110px;border-radius:16px;background:#eef1fb;display:grid;place-items:center;font-size:26px;font-weight:600;color:#8a8fb0}
#care .m.on{background:#2fbf71;color:#fff}
#care .h{grid-column:1/-1;font-size:36px;font-weight:700}
.cmp{display:flex;flex-direction:column;align-items:center;gap:20px;opacity:0;font-size:34px;font-weight:600}
.cmp .wc{opacity:1;display:grid;place-items:center;font-size:90px}
#logo{left:440px;top:930px;width:200px;height:200px;opacity:0}
#cta{left:88px;right:88px;top:1220px;display:flex;justify-content:center;opacity:0}
#cta span{padding:32px 54px;border-radius:999px;background:#fff;color:#265ADF;font-size:44px;font-weight:700;box-shadow:0 30px 70px -20px rgba(10,20,80,.7)}
"""

ART = f"""
<div class="wc" id="tag"><span id="q">?</span></div>
{''.join(f'<div class="pg" id="p{i}"><b style="width:60%"></b><b></b><b style="width:85%"></b><b style="width:70%"></b></div>' for i in range(5))}
<div class="wc" id="shop"><div class="r">🛒 Carrinho<span>3</span></div><div class="r" style="color:#8a8499;font-size:32px">Entrega · Pagamento · Fatura</div><div id="pay">Pagar</div></div>
<div id="cont"><span class="ph" id="ph"></span>
<span class="ln" id="l0" style="top:20px"></span><span class="ln" id="l1" style="top:80px;width:300px"></span><span class="ln" id="l2" style="top:140px;width:330px"></span>
<span class="lang" id="pt" style="left:40px;top:330px">PT</span><span class="lang" id="en" style="left:200px;top:330px">EN</span><span class="lang" id="es" style="left:360px;top:330px">ES</span></div>
<div class="wc" id="care"><div class="h">Manutenção</div>{''.join(f'<span class="m" id="m{i}">{m}</span>' for i, m in enumerate(["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]))}</div>
<div class="cmp" id="c0" style="left:150px;top:960px"><div class="wc" style="width:260px;height:320px">📄</div>Apresentação</div>
<div class="cmp" id="c1" style="left:520px;top:880px"><div class="wc" style="width:400px;height:400px">🏬</div>Loja com 500 produtos</div>
<img id="logo" src="{ASSETS}/logo_mark_white.svg" alt="">
<div id="cta"><span>hivecode.pt</span></div>
"""

ART_JS = r"""
function art(t, E) {
  // The question: a price tag whose "?" wobbles.
  stage($('#tag'), t, .2, E.s3);
  $('#q').style.display = 'inline-block';
  $('#q').style.transform = `rotate(${12 * Math.sin(t * 5)}deg)`;
  // 1. Pages stack up one by one.
  for (let i = 0; i < 5; i++) {
    const el = $('#p' + i), a = E.pag - .6 + .22 * i;
    const v = stage(el, t, a, E.s4, 40);
    el.style.transform += ` translate(${(i - 2) * 26}px,${(i - 2) * -22}px) rotate(${(i - 2) * 3}deg)`;
    el.style.opacity = v;
  }
  // 2. The shop: the pay button pulses as the sentence says "pagamentos".
  stage($('#shop'), t, E.s4 + .2, E.s5);
  $('#pay').style.transform = `scale(${1 + .06 * Math.max(0, 1 - Math.abs(t - E.pagam) / .3)})`;
  // 3. Content: photo, text lines, languages.
  const cv = 1 - ease((t - E.s6) / .3);
  pop($('#ph'), t, E.textos - .2); $('#ph').style.opacity = cl((t - E.textos + .2) / .1) * cv;
  ['#l0', '#l1', '#l2'].forEach((s, i) => { const a = E.textos + .1 * i; $(s).style.opacity = cl((t - a) / .15) * cv; $(s).style.transform = `scaleX(${ease((t - a) / .4)})`; $(s).style.transformOrigin = 'left'; });
  ['#pt', '#en', '#es'].forEach((s, i) => { pop($(s), t, E.trad + .18 * i); $(s).style.opacity = cl((t - E.trad - .18 * i) / .1) * cv; });
  // 4. Care: months tick green.
  stage($('#care'), t, E.s6 + .2, E.s7);
  for (let i = 0; i < 6; i++) $('#m' + i).className = 'm' + (t > E.manut + .3 * i ? ' on' : '');
  // Small vs large.
  stage($('#c0'), t, E.s7 + .3, E.s8); stage($('#c1'), t, E.s7 + .6, E.s8);
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
    ev = {"s3": st[2], "pag": at(2, "páginas."), "s4": st[3], "pagam": at(3, "pagamentos"), "s5": st[4],
          "textos": at(4, "textos,"), "trad": at(4, "traduções."), "s6": st[5], "manut": at(5, "manutenção"),
          "s7": st[6], "s8": st[7], "site": at(7, "hivecode.pt")}
    page = HERE / "reel.html"
    page.write_text(reelkit.page(scenes, ev, ART, CSS, ART_JS, theme="blue"), encoding="utf-8")
    hits = [("pop", .2)] + [("whoosh", s - .1) for s in (ev["s3"], ev["s4"], ev["s5"], ev["s6"], ev["s7"])]
    hits += [("click", ev["pag"] - .6 + .22 * i) for i in range(5)] + [("click", ev["pagam"])]
    hits += [("pop", ev["trad"] + .18 * i) for i in range(3)] + [("click", ev["manut"] + .3 * i) for i in range(6)]
    hits += [("pop", ev["s7"] + .3), ("thump", ev["s7"] + .6), ("pop", ev["s8"] + .15), ("pop", ev["site"])]
    reelkit.render(page, WORK, total, WORK / "voz.mp3", hits, HERE / "reel.mp4")
    reelkit.cover(HERE / "reel.mp4", 1.2, HERE / "cover.jpg")
    print(f"reel.mp4 {total:.1f}s")


if __name__ == "__main__":
    main()
