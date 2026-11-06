"""Reel "O seu site está ótimo. *no computador." (websites), screen theme, 1080x1920.

python posts/2026-11-15-letra-pequena/reel/build.py
The "small text zoom" trend: a desktop window says the site is great, the camera dives into
the fine print ("*no computador."), then a phone shows the same site with tiny text and
cramped buttons that a thumb misses. Then logo and the free mockup.
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
    ("O seu site está ótimo.", 130, {"ótimo."}),
    ("No computador.", 130, {"computador."}),
    ("No telemóvel, a letra é minúscula, os botões estão apertados e o cliente desiste.", 80, {"minúscula,", "desiste."}),
    ("Hoje, a maioria das visitas chega pelo telemóvel.", 88, {"telemóvel."}),
    ("Veja como o seu site pode ficar: mockup gratuito em hivecode.pt.", 82, {"gratuito", "hivecode.pt."}),
]

CSS = """
#cam{left:0;top:0;width:1080px;height:1920px;transform-origin:200px 1410px}
#win{position:absolute;left:80px;top:820px;width:920px;height:640px;border-radius:22px;background:#fff;overflow:hidden;opacity:0;box-shadow:0 50px 100px -40px rgba(22,24,29,.5)}
#win .tb{height:58px;background:#F2F3F6;border-bottom:1px solid #E1E3E9;display:flex;align-items:center;gap:12px;padding:0 22px}
#win .tb b{width:16px;height:16px;border-radius:50%}
#win h2{margin:70px 60px 0;font-size:84px;line-height:1.02;letter-spacing:-.03em;color:#16181D}
#win .bt{display:inline-block;margin:40px 60px 0;padding:22px 40px;border-radius:14px;background:#0A84FF;color:#fff;font-size:32px;font-weight:600}
#fine{position:absolute;left:60px;bottom:40px;font-size:13px;color:#8a8f9c}
#ph{left:290px;top:760px;width:500px;height:940px;box-sizing:border-box;padding:70px 26px 0;border-radius:70px;background:#fff;border:14px solid #16181D;opacity:0;overflow:hidden}
#ph h3{font-size:22px;margin:0 0 10px;color:#16181D}
#ph p{font-size:11px;line-height:1.35;color:#4b505c;margin:0 0 8px}
#ph .row{display:flex;gap:4px;margin-top:14px}
#ph .row span{flex:1;padding:6px 0;border-radius:4px;background:#0A84FF;color:#fff;font-size:10px;text-align:center}
#thumb{left:0;top:0;font-size:150px;opacity:0;z-index:5}
#miss{left:560px;top:1210px;width:110px;height:110px;border-radius:50%;background:#e5484d;color:#fff;display:grid;place-items:center;font-size:64px;font-weight:800;opacity:0;z-index:6}
#bars{left:180px;right:180px;top:880px;height:600px;display:flex;align-items:flex-end;gap:120px;opacity:0}
#bars div{flex:1;display:flex;flex-direction:column;align-items:center;gap:20px;font-size:90px}
#bars i{display:block;width:100%;border-radius:24px 24px 0 0;background:#0A84FF;transform-origin:bottom}
#bars .pc i{background:#b9bdc8}
#logo{left:440px;top:930px;width:200px;height:200px;opacity:0}
#cta{left:88px;right:88px;top:1220px;display:flex;justify-content:center;opacity:0}
#cta span{padding:32px 56px;border-radius:999px;background:#0A84FF;color:#fff;font-size:46px;font-weight:600}
"""

LOREM = ("Bem-vindo ao nosso site. Somos uma empresa com mais de vinte anos de experiência e oferecemos "
         "soluções completas para os nossos clientes, com qualidade e rapidez. Consulte os nossos serviços, "
         "os nossos preços e as nossas condições.")
ART = f"""<div id="cam"><div id="win"><div class="tb"><b style="background:#ff5f57"></b><b style="background:#febc2e"></b><b style="background:#28c840"></b></div>
<h2>O Seu Negócio<br>Bem-vindo.</h2><span class="bt">Pedir orçamento</span><span id="fine">*no computador.</span></div></div>
<div id="ph"><h3>O Seu Negócio</h3>{''.join(f'<p>{LOREM}</p>' for _ in range(3))}
<div class="row"><span>Início</span><span>Serviços</span><span>Preços</span><span>Contactos</span><span>Ligar</span></div>
{''.join(f'<p>{LOREM}</p>' for _ in range(4))}</div>
<span id="thumb">👆</span><span id="miss">✕</span>
<div id="bars"><div class="pc"><i id="b0"></i>💻</div><div><i id="b1"></i>📱</div></div>
<img id="logo" src="{ASSETS}/logo_mark.svg" alt=""><div id="cta"><span>hivecode.pt</span></div>"""

ART_JS = r"""
function art(t, E) {
  stage($('#win'), t, .15, E.s3);
  // Dive into the fine print: scale the whole window around the footnote.
  const z = ease(cl((t - E.s2 + .3) / .9)), s = 1 + 6 * z;  // the footnote sits at 200,1410
  $('#cam').style.transform = `translate(${(540 - 200) * z}px,${(1050 - 1410) * z}px) scale(${s})`;
  $('#cam').style.opacity = 1 - cl((t - E.s3 + .2) / .3);
  stage($('#ph'), t, E.s3, E.s4);
  const th = $('#thumb'), a = E.apert - .3;
  th.style.opacity = cl((t - a) / .2) * (1 - cl((t - E.s4 + .3) / .2));
  th.style.transform = `translate(${560 + 30 * Math.sin(t * 3)}px,${1260 - 60 * Math.max(0, Math.sin((t - a) * 5))}px)`;
  $('#miss').style.opacity = cl((t - E.desiste) / .1) * (1 - cl((t - E.s4) / .2));
  $('#miss').style.transform = `scale(${back((t - E.desiste) / .35)})`;
  stage($('#bars'), t, E.s4, E.s5);
  $('#b0').style.height = `${220 * ease((t - E.s4 - .2) / .6)}px`;
  $('#b1').style.height = `${440 * ease((t - E.tel - .1) / .7)}px`;
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
    ev = {"s2": st[1], "s3": st[2], "apert": at(2, "apertados"), "desiste": at(2, "desiste."), "s4": st[3], "tel": at(3, "telemóvel."),
          "s5": st[4], "site": at(4, "hivecode.pt.")}
    page = HERE / "reel.html"
    page.write_text(reelkit.page(scenes, ev, ART, CSS, ART_JS, theme="screen"), encoding="utf-8")
    hits = [("pop", .15), ("whoosh", ev["s2"] - .3), ("thump", ev["s2"] + .6), ("pop", ev["s3"])]
    hits += [("click", ev["apert"] + .1), ("click", ev["apert"] + .7), ("error", ev["desiste"])]
    hits += [("rise", ev["s4"] + .2), ("pop", ev["s5"] + .15), ("pop", ev["site"])]
    reelkit.render(page, WORK, total, WORK / "voz.mp3", hits, HERE / "reel.mp4")
    reelkit.cover(HERE / "reel.mp4", .9, HERE / "cover.jpg")
    print(f"reel.mp4 {total:.1f}s")


if __name__ == "__main__":
    main()
