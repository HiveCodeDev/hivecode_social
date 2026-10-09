"""Reel "O site parou no tempo?" (websites), 1080x1920, formal tone.

python posts/2026-10-13-site-parado-no-tempo/reel/build.py
An outdated company site is shown failing on each problem as the voice names it (slow, not
mobile, contact hidden), visitors leave, then it glitches into a modern mobile site whose three
strengths light up on their words.
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
    ("O site da sua empresa parou no tempo?", 96, {"parou", "no", "tempo?"}),
    ("Demora a abrir, não se adapta ao telemóvel e o contacto é difícil de encontrar.", 80, set()),
    ("Cada visita perdida é um cliente que não chega.", 92, {"cliente"}),
    ("A HiveCode cria sites rápidos, pensados para telemóvel e fáceis de contactar.", 80, {"rápidos,", "telemóvel", "contactar."}),
    ("Fale connosco em hivecode.pt.", 88, {"hivecode.pt."}),
]

CSS = """
.old{left:88px;top:830px;width:904px;height:600px;background:#fff;border:3px solid #c0c0c0;box-shadow:0 40px 90px -30px rgba(0,0,0,.9);
font-family:'Times New Roman',serif;color:#000;overflow:hidden;opacity:0}
.old .tb{height:48px;background:linear-gradient(90deg,#000080,#1084d0);color:#fff;font:bold 22px Tahoma,sans-serif;display:flex;align-items:center;justify-content:space-between;padding:0 14px}
.old .tb i{display:inline-block;width:30px;height:28px;margin-left:6px;background:#c0c0c0;border:2px outset #fff}
.old .mq{background:#000080;color:#ffff00;font-size:28px;padding:8px 0;white-space:nowrap;overflow:hidden}
.old .mq span{display:inline-block}
.old h2{font-size:56px;text-align:center;margin:26px 0 8px;color:#800000}
.old .nav{text-align:center;font-size:28px;color:#0000ee;text-decoration:underline}
.old .uc{margin:26px auto 0;width:420px;padding:14px;text-align:center;font:bold 28px Arial,sans-serif;
background:repeating-linear-gradient(45deg,#ffd400 0 22px,#111 22px 44px);color:#fff;text-shadow:0 0 6px #000}
.old .cnt{margin:26px auto 0;text-align:center;font-size:26px}
.old .cnt b{font-family:'Courier New',monospace;background:#000;color:#0f0;padding:2px 8px;letter-spacing:3px}
.old .ft{position:absolute;left:0;right:0;bottom:16px;text-align:center;font-size:18px;color:#555}
.old .ft u{color:#0000ee}
.old .load{position:absolute;left:0;right:0;top:48px;bottom:0;background:rgba(255,255,255,.88);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:22px;font:28px Tahoma,sans-serif;color:#333;opacity:0}
.old .load .pb{width:520px;height:30px;border:2px inset #c0c0c0;background:#fff}
.old .load .pb i{display:block;height:100%;background:repeating-linear-gradient(90deg,#000080 0 22px,#fff 22px 26px)}
.x{width:84px;height:84px;border-radius:50%;background:#ff4d6d;display:grid;place-items:center;box-shadow:0 0 0 10px rgba(255,77,109,.2);opacity:0;z-index:3}
.oph{left:660px;top:960px;width:250px;height:470px;border-radius:44px;background:#0d0b1c;border:2px solid rgba(255,255,255,.25);padding:12px;opacity:0;z-index:2;
box-shadow:0 40px 80px -30px rgba(0,0,0,.9)}
.oph .scr{height:100%;border-radius:32px;background:#fff;overflow:hidden;position:relative}
.oph .mini{position:absolute;left:0;top:0;width:904px;transform-origin:0 0;transform:scale(.36)}
.oph .hs{position:absolute;left:14px;right:60px;bottom:16px;height:10px;border-radius:5px;background:#aaa}
.mag{width:170px;height:170px;border-radius:50%;border:12px solid #f3f1fb;background:rgba(255,255,255,.12);opacity:0;z-index:2}
.mag:after{content:"";position:absolute;right:-56px;bottom:-30px;width:80px;height:20px;border-radius:10px;background:#f3f1fb;transform:rotate(40deg)}
.ppl{left:88px;right:88px;top:930px;display:flex;justify-content:center;gap:34px;opacity:0}
.ppl svg{width:110px;height:110px}
.stat{left:88px;right:88px;top:1120px;text-align:center;font-size:44px;font-weight:600;opacity:0}
.stat b{color:#ff4d6d}
.nph{left:110px;top:850px;width:330px;height:600px;border-radius:52px;background:#0d0b1c;border:2px solid rgba(255,255,255,.2);padding:14px;opacity:0;
box-shadow:0 40px 90px -30px rgba(215,82,254,.65)}
.nph .scr{height:100%;border-radius:40px;background:#1b1638;padding:28px 22px;display:flex;flex-direction:column;gap:16px}
.bar{display:block;height:18px;border-radius:9px;background:rgba(255,255,255,.14)}
.hl{background:linear-gradient(90deg,var(--pink),var(--blue))}
.btn{display:inline-flex;align-items:center;justify-content:center;border-radius:999px;background:#265ADF;font-weight:600;color:#fff}
.ok{left:490px;display:flex;align-items:center;gap:18px;padding:24px 32px;border-radius:999px;background:#1b1638;border:1px solid rgba(255,255,255,.16);font-size:36px;font-weight:600;opacity:0}
.ok i{width:46px;height:46px;border-radius:50%;background:#2fbf71;display:grid;place-items:center}
.flash{inset:0;background:#fff;opacity:0;z-index:9}
#logo{left:440px;top:930px;width:200px;height:200px;opacity:0}
#cta{left:88px;right:88px;top:1220px;display:flex;justify-content:center;opacity:0}
#cta span{padding:32px 54px;border-radius:999px;background:#265ADF;font-size:44px;font-weight:600;box-shadow:0 30px 70px -20px rgba(72,119,254,.8)}
"""

XMARK = '<svg viewBox="0 0 24 24" width="44" height="44" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>'
PERSON = '<svg viewBox="0 0 24 24" fill="none" stroke="#c9c3e6" stroke-width="1.6"><circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4.5 4.5-6.5 8-6.5s6.5 2 8 6.5"/></svg>'

OLD_PAGE = """<div class="mq"><span>&#9733; Bem-vindo ao nosso site! &#9733; Melhor visualizado em 800x600 &#9733; Bem-vindo ao nosso site! &#9733;</span></div>
<h2>A Sua Empresa, Lda.</h2>
<div class="nav">Início | Quem Somos | Serviços | Galeria | Livro de Visitas</div>
<div class="uc">PÁGINA EM CONSTRUÇÃO</div>
<div class="cnt">Visitante nº <b>000127</b></div>
<div class="ft">Última atualização: 12/03/2015 · <u>contactos</u></div>"""

ART = f"""
<div class="old" id="old"><div class="tb"><span>A Sua Empresa, Lda. - Página Inicial</span><span><i></i><i></i><i></i></span></div>
{OLD_PAGE}
<div class="load" id="load"><span>A carregar…</span><div class="pb"><i id="pbi"></i></div></div></div>
<div class="oph" id="oph"><div class="scr"><div class="mini old" style="opacity:1;position:absolute;left:0;top:0;height:600px;border:0;box-shadow:none">{OLD_PAGE}</div><span class="hs"></span></div></div>
<div class="mag" id="mag" style="left:560px;top:1300px"></div>
<span class="x" id="x1" style="left:820px;top:1105px">{XMARK}</span>
<span class="x" id="x2" style="left:870px;top:925px">{XMARK}</span>
<span class="x" id="x3" style="left:700px;top:1330px">{XMARK}</span>
<div class="ppl" id="ppl">{PERSON * 6}</div>
<div class="stat" id="stat">127 visitas · <b>0 contactos</b></div>
<div class="nph" id="nph"><div class="scr">
<span style="height:190px;border-radius:22px;background:linear-gradient(150deg,rgba(239,90,254,.6),rgba(72,119,254,.6))"></span>
<span class="bar" style="height:28px;width:85%;background:rgba(255,255,255,.32)"></span><span class="bar" style="width:65%"></span><span class="bar" style="width:75%"></span>
<span class="btn" style="margin-top:auto;padding:18px;font-size:26px">Contactar</span></div></div>
<div class="ok" id="ok1" style="top:900px"><i>{CHECK}</i>Rápido</div>
<div class="ok" id="ok2" style="top:1040px"><i>{CHECK}</i>Pensado para telemóvel</div>
<div class="ok" id="ok3" style="top:1180px"><i>{CHECK}</i>Contacto a um toque</div>
<div class="flash" id="flash"></div>
<img id="logo" src="{ASSETS}/logo_side.png" alt="">
<div id="cta"><span>hivecode.pt</span></div>
"""

ART_JS = r"""
function art(t, E) {
  // The old site: in from the start, dimmed while visitors leave, glitches away on "A HiveCode".
  const old = $('#old'), g = cl((t - E.s4) / .45);
  const k = back((t - .15) / .5);
  old.style.opacity = cl((t - .15) / .12) * (1 - cl((t - E.s3) / .3)) * (1 - g);
  const jit = g > 0 && g < 1 ? 26 * Math.sin(t * 90) : 0;
  old.style.transform = `translate(${jit}px,${50 * (1 - k)}px) scale(${(.92 + .08 * k) * (1 - .15 * g)})`;
  old.style.filter = g > 0 ? `hue-rotate(${300 * g}deg) contrast(${1 + 2 * g})` : 'none';
  $('.old .mq span').style.transform = `translateX(${900 - (t * 140) % 1900}px)`;
  // Slow: a loading screen that crawls.
  const ld = cl((t - E.demora) / .2) * (1 - cl((t - E.tel + .1) / .2));
  $('#load').style.opacity = ld;
  $('#pbi').style.width = `${Math.min(38, Math.max(0, (t - E.demora) * 14))}%`;
  // Problems get a red cross as they are named.
  [['#x1', E.demora + .35], ['#x2', E.tel + .25], ['#x3', E.contacto + .3]].forEach(([s, a]) => {
    pop($(s), t, a);
    $(s).style.opacity = cl((t - a) / .1) * (1 - cl((t - E.s3) / .25));
  });
  // Not mobile: the desktop page crammed into a phone.
  const ph = $('#oph'), pk = back((t - E.tel) / .45);
  ph.style.opacity = cl((t - E.tel) / .1) * (1 - cl((t - E.s3) / .25));
  ph.style.transform = `translateY(${60 * (1 - pk)}px) rotate(${4 * pk}deg) scale(${.9 + .1 * pk})`;
  $('#oph .mini').style.transform = `translateX(${-120 * (.5 + .5 * Math.sin((t - E.tel) * 1.8))}px) scale(.36)`;
  // Contact hidden: a magnifier searching the footer.
  const mg = $('#mag');
  mg.style.opacity = cl((t - E.contacto) / .12) * (1 - cl((t - E.s3) / .25));
  mg.style.transform = `translate(${-120 + 60 * Math.sin((t - E.contacto) * 2.4)}px,${10 * Math.cos((t - E.contacto) * 3)}px)`;
  // Visitors leave one by one.
  const ppl = $('#ppl'), pv = cl((t - E.s3) / .3) * (1 - cl((t - E.s4) / .25));
  ppl.style.opacity = pv;
  [...ppl.children].forEach((p, j) => {
    const lv = ease((t - E.s3 - .5 - .22 * j) / .4);
    p.style.opacity = 1 - .85 * lv;
    p.style.transform = `translateY(${70 * lv}px)`;
  });
  const st = $('#stat');
  st.style.opacity = cl((t - E.cliente) / .15) * (1 - cl((t - E.s4) / .25));
  st.style.transform = `translateY(${30 * (1 - ease((t - E.cliente) / .4))}px)`;
  // Glitch flash, then the modern phone and its three strengths on their words.
  $('#flash').style.opacity = .55 * Math.max(0, 1 - Math.abs(t - E.s4 - .38) / .12);
  const nk = back((t - E.s4 - .4) / .55), gone = ease((t - E.s5) / .4);
  const nph = $('#nph');
  nph.style.opacity = cl((t - E.s4 - .4) / .12) * (1 - gone);
  nph.style.transform = `translateY(${80 * (1 - nk) + 12 * Math.sin(t * 1.6) - 120 * gone}px) rotate(${-4 * nk}deg) scale(${.85 + .15 * nk})`;
  [['#ok1', E.rap], ['#ok2', E.tel2], ['#ok3', E.cont]].forEach(([s, a]) => {
    const el = $(s), kk = back((t - a) / .45);
    el.style.opacity = cl((t - a) / .1) * (1 - gone);
    el.style.transform = `translateX(${120 * (1 - kk)}px) scale(${.9 + .1 * kk})`;
  });
  // Close.
  const lg = back((t - E.s5 - .1) / .5);
  $('#logo').style.opacity = cl((t - E.s5 - .1) / .1);
  $('#logo').style.transform = `rotate(${-120 * (1 - lg)}deg) scale(${lg})`;
  const ct = back((t - E.site) / .45);
  $('#cta').style.opacity = cl((t - E.site) / .1);
  $('#cta').style.transform = `scale(${ct * (1 + .03 * Math.sin((t - E.site) * 5) * cl(t - E.site - .5))})`;
}
"""


def main():
    total, scenes = reelkit.voice(SCENES, WORK / "voz.mp3")
    at = lambda s, w: reelkit.at(scenes, s, w)  # noqa: E731
    ev = {
        "demora": at(1, "Demora"), "tel": at(1, "telemóvel"), "contacto": at(1, "contacto"),
        "s3": scenes[2]["start"], "cliente": at(2, "cliente"),
        "s4": scenes[3]["start"], "rap": at(3, "rápidos,"), "tel2": at(3, "telemóvel"), "cont": at(3, "contactar."),
        "s5": scenes[4]["start"], "site": at(4, "hivecode.pt."),
    }
    page = HERE / "reel.html"
    page.write_text(reelkit.page(scenes, ev, ART, CSS, ART_JS), encoding="utf-8")
    hits = [("whoosh", s["start"] - .12) for s in scenes[1:]]
    hits += [("pop", .2)] + [("error", ev[k] + d) for k, d in (("demora", .35), ("tel", .25), ("contacto", .3))]
    hits += [("rise", ev["s4"] - .5), ("thump", ev["s4"] + .4)] + [("pop", ev[k]) for k in ("rap", "tel2", "cont")]
    hits += [("pop", ev["s5"] + .15), ("pop", ev["site"])]
    reelkit.render(page, WORK, total, WORK / "voz.mp3", hits, HERE / "reel.mp4")
    reelkit.cover(HERE / "reel.mp4", ev["contacto"] + .6, HERE / "cover.jpg")
    print(f"reel.mp4 {total:.1f}s")


if __name__ == "__main__":
    main()
