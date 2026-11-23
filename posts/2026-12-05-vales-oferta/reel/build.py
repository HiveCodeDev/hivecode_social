"""Reel "Vales-oferta: o presente de quem não sabe o que oferecer" (neve theme: icy Christmas scenery, 1080x1920).

python posts/2026-12-05-vales-oferta/reel/build.py
A wrapped box shakes with a "?"; it opens into three gift vouchers (dinner, haircut, massage);
a phone shows the shop site at 23:47 with "Comprar vale" being tapped; an email with the voucher
lands; a January calendar page gets "+1 cliente novo"; logo and CTA.
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
    ("No Natal, há sempre quem não saiba o que oferecer.", 92, {"oferecer."}),
    ("Um jantar, um corte de cabelo, uma massagem: um vale-oferta resolve.", 86, {"vale-oferta"}),
    ("Com vales à venda no seu site, o cliente compra a qualquer hora,", 86, {"qualquer", "hora,"}),
    ("recebe o vale por email e oferece no próprio dia.", 92, {"email"}),
    ("E o seu negócio ganha um cliente novo em janeiro.", 96, {"cliente", "novo"}),
    ("Fale connosco em hivecode.pt.", 110, {"hivecode.pt."}),
]

INK, DEEP = "#10233F", "#C41E3A"
CSS = f"""
#box{{left:340px;top:980px;width:400px;height:360px;border-radius:30px;background:{DEEP};opacity:0}}
#box:before{{content:"";position:absolute;left:170px;top:0;width:60px;height:100%;background:#FFD84D}}
#box b{{position:absolute;left:0;right:0;top:110px;text-align:center;font-size:170px;font-weight:800;color:#fff}}
#lid{{left:310px;top:900px;width:460px;height:110px;border-radius:26px;background:#a3172f;opacity:0}}
#lid:before{{content:"";position:absolute;left:200px;top:0;width:60px;height:100%;background:#FFD84D}}
.v{{left:300px;top:740px;width:480px;height:290px;border-radius:30px;padding:34px 38px;box-sizing:border-box;color:#fff;opacity:0;box-shadow:0 40px 80px -30px rgba(16,35,63,.45)}}
.v small{{display:block;font-size:24px;font-weight:700;letter-spacing:.14em;opacity:.8}}
.v strong{{display:block;margin-top:18px;font-size:56px;font-weight:800;line-height:1.05}}
.v em{{position:absolute;right:34px;bottom:30px;font-style:normal;font-size:70px}}
#ph{{left:330px;top:820px;width:420px;height:820px;border-radius:60px;background:{INK};padding:18px;box-sizing:border-box;opacity:0}}
#ph .sc{{width:100%;height:100%;border-radius:44px;background:#fff;overflow:hidden;position:relative}}
#ph .clk{{height:70px;display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:700;color:{INK}}}
#ph .hd{{margin:10px 26px;height:200px;border-radius:24px;background:linear-gradient(150deg,#ffd9de,#C41E3A)}}
#ph h4{{margin:24px 26px 0;font-size:34px;color:{INK}}}
#ph p{{margin:10px 26px 0;font-size:24px;color:#33476a}}
#ph .am{{display:flex;gap:12px;margin:24px 26px 0}}
#ph .am span{{flex:1;padding:14px 0;text-align:center;border-radius:14px;border:3px solid #d6e0ea;font-size:26px;font-weight:700;color:{INK}}}
#ph .am span.on{{border-color:{DEEP};background:#fde8eb}}
#buy{{position:absolute;left:26px;right:26px;bottom:40px;height:90px;border-radius:20px;background:{DEEP};color:#fff;display:grid;place-items:center;font-size:32px;font-weight:800}}
#tap{{left:0;top:0;width:90px;height:90px;border-radius:50%;background:rgba(255,216,77,.6);opacity:0}}
#mail{{left:150px;top:900px;width:780px;border-radius:30px;background:#fff;overflow:hidden;opacity:0;box-shadow:0 50px 100px -40px rgba(16,35,63,.45)}}
#mail .h{{padding:30px 38px;border-bottom:3px solid #e3ebf2;font-size:30px;color:#33476a}}
#mail .h b{{display:block;margin-top:8px;font-size:40px;color:{INK}}}
#mail .vc{{margin:34px 38px 38px;padding:34px;border-radius:24px;background:{DEEP};color:#fff;display:flex;justify-content:space-between;align-items:center}}
#mail .vc strong{{font-size:46px}}
#mail .vc i{{width:130px;height:130px;border-radius:12px;background:repeating-conic-gradient(#fff 0 25%,{DEEP} 0 50%) 0 0/26px 26px;border:10px solid #fff}}
#jan{{left:340px;top:920px;width:400px;border-radius:30px;background:#fff;overflow:hidden;text-align:center;opacity:0;box-shadow:0 50px 100px -40px rgba(16,35,63,.45)}}
#jan .m{{padding:22px 0;background:{DEEP};color:#fff;font-size:40px;font-weight:800;letter-spacing:.1em}}
#jan .d{{padding:30px 0 40px;font-size:200px;font-weight:800;line-height:1;color:{INK}}}
#plus{{left:600px;top:860px;padding:22px 34px;border-radius:999px;background:#FFD84D;color:{INK};font-size:44px;font-weight:800;opacity:0;white-space:nowrap}}
#logo{{left:440px;top:930px;width:200px;height:200px;opacity:0}}
#cta{{left:88px;right:88px;top:1220px;display:flex;justify-content:center;opacity:0}}
#cta span{{padding:32px 56px;border-radius:999px;background:{INK};color:#fff;font-size:50px;font-weight:700}}
"""

VOUCHERS = [("Jantar para dois", "🍽️", "#C41E3A"), ("Corte de cabelo", "✂️", "#10233F"), ("Massagem", "💆", "#1E5A45")]
ART = ('<div id="box"><b>?</b></div><div id="lid"></div>'
       + "".join(f'<div class="v" id="v{i}" style="background:{c}"><small>VALE-OFERTA</small><strong>{n}</strong><em>{e}</em></div>'
                 for i, (n, e, c) in enumerate(VOUCHERS))
       + '<div id="ph"><div class="sc"><div class="clk" id="clk">23:47</div><div class="hd"></div><h4>Vales-oferta</h4>'
       + '<p>Ofereça um jantar no Largo</p><div class="am"><span>25 €</span><span class="on">50 €</span><span>75 €</span></div>'
       + '<div id="buy">Comprar vale</div></div></div><span id="tap"></span>'
       + '<div id="mail"><div class="h">Para: Ana<b>🎁 O seu vale-oferta chegou</b></div><div class="vc"><strong>Jantar para dois<br>50 €</strong><i></i></div></div>'
       + '<div id="jan"><div class="m">JANEIRO</div><div class="d">12</div></div><span id="plus">+1 cliente novo</span>'
       + f'<img id="logo" src="{ASSETS}/logo_mark.svg" alt=""><div id="cta"><span>hivecode.pt</span></div>')

ART_JS = r"""
function art(t, E) {
  // 1. wrapped box shakes, lid flies off
  const shake = t > 1 && t < E.s2 ? Math.sin(t * 38) * 5 * cl((t - 1) / .4) : 0;
  stage($('#box'), t, .3, E.s2 + .1);
  $('#box').style.transform += ` rotate(${shake}deg)`;
  const lo = ease((t - E.s2) / .4);
  $('#lid').style.opacity = cl((t - .3) / .12) * (1 - lo);
  $('#lid').style.transform = `translate(${160 * lo}px,${-300 * lo}px) rotate(${30 * lo}deg) scale(${back((t - .3) / .5)}) rotate(${shake}deg)`;
  // 2. three vouchers fan out
  [[E.jan, -7, -170, 0], [E.cor, 3, 20, 250], [E.mas, 8, 190, 500]].forEach(([a, r, x, y], i) => {
    const el = $('#v' + i), k = back((t - a) / .5), o = ease((t - E.s3) / .3);
    el.style.opacity = cl((t - a) / .12) * (1 - o);
    el.style.transform = `translate(${x * k - 160 * o}px,${y * k}px) rotate(${r * k}deg) scale(${.7 + .3 * k})`; });
  // 3. phone at 23:47, tap "Comprar vale"
  stage($('#ph'), t, E.s3 + .1, E.s4 - .05);
  const tp = $('#tap'); tp.style.opacity = t > E.hor && t < E.hor + .6 ? .9 * (1 - (t - E.hor) / .6) : 0;
  tp.style.transform = `translate(${495}px,${1475}px) scale(${.5 + 1.5 * cl((t - E.hor) / .6)})`;
  $('#buy').style.background = t > E.hor && t < E.hor + .3 ? '#10233F' : '#C41E3A';
  // 4. email with the voucher
  stage($('#mail'), t, E.mail - .2, E.s5 - .05);
  // 5. January + new client
  stage($('#jan'), t, E.s5, E.s6 - .1);
  stage($('#plus'), t, E.cli, E.s6 - .1, 40);
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
    ev = {"s2": st[1], "jan": at(1, "jantar,"), "cor": at(1, "corte"), "mas": at(1, "massagem:"), "s3": st[2],
          "hor": at(2, "hora,"), "s4": st[3], "mail": at(3, "email"), "s5": st[4], "cli": at(4, "cliente"),
          "s6": st[5], "site": at(5, "hivecode.pt.")}
    page = HERE / "reel.html"
    page.write_text(reelkit.page(scenes, ev, ART, CSS, ART_JS, theme="neve"), encoding="utf-8")
    hits = [("pop", .3), ("click", 1.1), ("click", 1.4), ("click", 1.7), ("whoosh", ev["s2"]),
            ("pop", ev["jan"]), ("pop", ev["cor"]), ("pop", ev["mas"]), ("whoosh", ev["s3"]), ("click", ev["hor"]),
            ("pop", ev["mail"] - .2), ("pop", ev["s5"]), ("thump", ev["cli"]), ("pop", ev["s6"] + .1), ("pop", ev["site"])]
    reelkit.render(page, WORK, total, WORK / "voz.mp3", hits, HERE / "reel.mp4")
    reelkit.cover(HERE / "reel.mp4", ev["s3"] - .3, HERE / "cover.jpg")
    print(f"reel.mp4 {total:.1f}s")


if __name__ == "__main__":
    main()
