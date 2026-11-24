"""HyperFrames version of the 5/12 reel "Vales-oferta" (neve theme). Same voice text as build.py.

python posts/2026-12-05-vales-oferta/reel/build_hf.py   -> reel-hf.mp4, cover-hf.jpg
Frame 0: a red gift box with "?" already on screen, shaking. The lid blows off and three vouchers fan out as they
are named; a phone at 23:47 taps "Comprar vale"; an email with the voucher drops in; a January page gets a
"+1 cliente novo" sticker; logo slam and the site.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import hfkit  # noqa: E402
import reelkit  # noqa: E402
from build import SCENES, VOUCHERS, WORK  # noqa: E402

INK, RED, GOLD = "#10233F", "#C41E3A", "#FFD84D"
CSS = f"""
#box{{position:absolute;left:340px;top:560px;width:400px;height:360px;border-radius:30px;background:{RED};transform-origin:50% 100%}}
#box:before{{content:"";position:absolute;left:170px;top:0;width:60px;height:100%;background:{GOLD}}}
#box b{{position:absolute;left:0;right:0;top:100px;text-align:center;font-size:170px;font-weight:800;color:#fff}}
#lid{{position:absolute;left:310px;top:480px;width:460px;height:110px;border-radius:26px;background:#a3172f}}
#lid:before{{content:"";position:absolute;left:200px;top:0;width:60px;height:100%;background:{GOLD}}}
.v{{position:absolute;left:300px;top:560px;width:480px;height:270px;border-radius:30px;padding:30px 36px;color:#fff;box-shadow:0 40px 80px -30px rgba(16,35,63,.45)}}
.v small{{display:block;font-size:24px;font-weight:700;letter-spacing:.14em;opacity:.8}}
.v strong{{display:block;margin-top:16px;font-size:54px;font-weight:800;line-height:1.05}}
.v em{{position:absolute;right:32px;bottom:26px;font-style:normal;font-size:70px}}
#ph{{position:absolute;left:350px;top:390px;width:380px;height:660px;border-radius:56px;background:{INK};padding:16px}}
#ph .sc{{width:100%;height:100%;border-radius:42px;background:#fff;overflow:hidden;position:relative}}
#ph .clk{{height:64px;display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:700;color:{INK}}}
#ph .hd{{margin:6px 22px;height:150px;border-radius:22px;background:linear-gradient(150deg,#ffd9de,{RED})}}
#ph h4{{margin:20px 22px 0;font-size:32px;color:{INK}}}
#ph p{{margin:8px 22px 0;font-size:22px;color:#33476a}}
#ph .am{{display:flex;gap:10px;margin:20px 22px 0}}
#ph .am span{{flex:1;padding:12px 0;text-align:center;border-radius:14px;border:3px solid #d6e0ea;font-size:24px;font-weight:700;color:{INK}}}
#ph .am span.on{{border-color:{RED};background:#fde8eb}}
#buy{{position:absolute;left:22px;right:22px;bottom:34px;height:84px;border-radius:20px;background:{RED};color:#fff;display:grid;place-items:center;font-size:30px;font-weight:800}}
#tap{{position:absolute;left:480px;top:920px;width:110px;height:110px;border-radius:50%;background:rgba(255,216,77,.7)}}
#mail{{position:absolute;left:150px;top:470px;width:780px;border-radius:30px;background:#fff;overflow:hidden;box-shadow:0 50px 100px -40px rgba(16,35,63,.45)}}
#mail .h{{padding:28px 36px;border-bottom:3px solid #e3ebf2;font-size:30px;color:#33476a}}
#mail .h b{{display:block;margin-top:8px;font-size:40px;color:{INK}}}
#mail .vc{{margin:30px 36px 36px;padding:32px;border-radius:24px;background:{RED};color:#fff;display:flex;justify-content:space-between;align-items:center}}
#mail .vc strong{{font-size:46px}}
#mail .vc i{{width:120px;height:120px;border-radius:12px;background:repeating-conic-gradient(#fff 0 25%,{RED} 0 50%) 0 0/24px 24px;border:10px solid #fff}}
#jan{{position:absolute;left:340px;top:470px;width:400px;border-radius:30px;background:#fff;overflow:hidden;text-align:center;box-shadow:0 50px 100px -40px rgba(16,35,63,.45)}}
#jan .m{{padding:22px 0;background:{RED};color:#fff;font-size:40px;font-weight:800;letter-spacing:.1em}}
#jan .d{{padding:30px 0 40px;font-size:200px;font-weight:800;line-height:1;color:{INK}}}
#plus{{position:absolute;left:560px;top:430px;padding:20px 32px;border-radius:999px;background:{GOLD};color:{INK};font-size:44px;font-weight:800;white-space:nowrap}}
#ring{{position:absolute;left:340px;top:420px;width:400px;height:400px;border-radius:50%;border:8px solid {RED}}}
#logo{{position:absolute;left:420px;top:500px;width:240px;height:240px}}
#cta{{position:absolute;left:0;right:0;top:800px;display:flex;justify-content:center}}
#cta span{{padding:30px 60px;border-radius:999px;background:{INK};color:#fff;font-size:56px;font-weight:800}}
"""


def main():
    total, scenes = reelkit.voice(SCENES, WORK / "voz.mp3")
    at = lambda s, w: reelkit.at(scenes, s, w)  # noqa: E731
    st = [s["start"] for s in scenes]
    E = {"s2": st[1], "jan": at(1, "jantar,"), "cor": at(1, "corte"), "mas": at(1, "massagem:"), "s3": st[2],
         "hor": at(2, "hora,"), "s4": st[3], "mail": at(3, "email"), "s5": st[4], "cli": at(4, "cliente"), "s6": st[5], "site": at(5, "hivecode.pt.")}
    clip = lambda i, a, b, n: f'id="{i}" class="clip" data-start="{a:.3f}" data-duration="{b - a:.3f}" data-track-index="{n}"'  # noqa: E731
    html = (f'<div {clip("box", 0, E["s2"] + .4, 2)}><b>?</b></div><div {clip("lid", 0, E["s2"] + .6, 3)}></div>'
            + "".join(f'<div class="v" {clip(f"v{i}", E[k], E["s3"] + .1, 4 + i)} style="background:{c}"><small>VALE-OFERTA</small><strong>{n}</strong><em>{e}</em></div>'
                      for i, ((n, e, c), k) in enumerate(zip(VOUCHERS, ["jan", "cor", "mas"])))
            + f'<div {clip("ph", E["s3"], E["mail"] - .1, 8)}><div class="sc"><div class="clk">23:47</div><div class="hd"></div><h4>Vales-oferta</h4>'
            '<p>Ofereça um jantar no Largo</p><div class="am"><span>25 €</span><span class="on">50 €</span><span>75 €</span></div><div id="buy">Comprar vale</div></div></div>'
            f'<span {clip("tap", E["hor"], E["hor"] + .6, 9)}></span>'
            f'<div {clip("mail", E["mail"] - .2, E["s5"], 10)}><div class="h">Para: Ana<b>🎁 O seu vale-oferta chegou</b></div><div class="vc"><strong>Jantar para dois<br>50 €</strong><i></i></div></div>'
            f'<div {clip("jan", E["s5"], E["s6"], 11)}><div class="m">JANEIRO</div><div class="d">12</div></div><span {clip("plus", E["cli"], E["s6"], 12)}>+1 cliente novo</span>'
            f'<div {clip("end", E["s6"], total, 13)}><span id="ring"></span><img id="logo" src="assets/logo_mark.svg" alt=""><div id="cta"><span>hivecode.pt</span></div></div>')
    js = """
tl.fromTo(["#box", "#lid"], { rotate: 0 }, { rotate: 5, duration: .06, yoyo: true, repeat: Math.floor((E.s2 - .2) / .06), ease: "none" }, .1);
tl.fromTo("#box", { scaleY: 1 }, { scaleY: .92, duration: .1, yoyo: true, repeat: 1, immediateRender: false }, E.s2 - .1);
tl.fromTo("#lid", { x: 0, y: 0, rotate: 0 }, { x: 260, y: -420, rotate: 60, opacity: 0, duration: .55, ease: "power2.out", immediateRender: false }, E.s2);
tl.fromTo("#box", { opacity: 1, scale: 1 }, { opacity: 0, scale: .6, duration: .35, immediateRender: false }, E.s2 + .05);
[[E.jan, -8, -160, -150], [E.cor, 3, 20, 50], [E.mas, 9, 180, 250]].forEach(([a, r, x, y], i) =>
  tl.fromTo("#v" + i, { scale: .4, x: 0, y: 200, rotate: 0, opacity: 0 }, { scale: .82, x, y, rotate: r, opacity: 1, duration: .5, ease: "back.out(1.8)" }, a));
tl.fromTo(".v", { xPercent: 0 }, { xPercent: -250, duration: .35, stagger: .05, ease: "power3.in", immediateRender: false }, E.s3 - .3);
tl.fromTo("#ph", { y: 600, rotate: 8 }, { y: 0, rotate: 0, duration: .6, ease: "back.out(1.5)" }, E.s3);
tl.fromTo("#tap", { scale: .3, opacity: .9 }, { scale: 1.8, opacity: 0, duration: .6, ease: "power2.out" }, E.hor);
tl.fromTo("#buy", { backgroundColor: "#C41E3A" }, { backgroundColor: "#1f8a4c", duration: .1, immediateRender: false }, E.hor);
tl.fromTo("#mail", { y: -500, opacity: 0, rotate: -6 }, { y: 0, opacity: 1, rotate: 0, duration: .6, ease: "bounce.out" }, E.mail - .2);
tl.fromTo("#jan", { rotateX: -90, transformPerspective: 1200, transformOrigin: "50% 0" }, { rotateX: 0, duration: .6, ease: "back.out(1.6)" }, E.s5);
tl.fromTo("#plus", { scale: 2.5, rotate: -20, opacity: 0 }, { scale: 1, rotate: 8, opacity: 1, duration: .3, ease: "power4.in" }, E.cli);
tl.fromTo("#logo", { scale: 2.2, rotate: -90, opacity: 0 }, { scale: 1, rotate: 0, opacity: 1, duration: .55, ease: "expo.out" }, E.s6 + .05);
tl.fromTo("#ring", { scale: .4, opacity: .95 }, { scale: 2.2, opacity: 0, duration: .7, ease: "power3.out" }, E.s6 + .4);
tl.fromTo("#cta", { scale: .5, opacity: 0 }, { scale: 1, opacity: 1, duration: .45, ease: "back.out(2.4)" }, E.site);
"""
    hits = [("click", .3), ("click", .7), ("click", 1.1), ("whoosh", E["s2"]), ("pop", E["jan"]), ("pop", E["cor"]), ("pop", E["mas"]),
            ("whoosh", E["s3"] - .3), ("click", E["hor"]), ("whoosh", E["mail"] - .2), ("pop", E["s5"]), ("thump", E["cli"] + .3),
            ("pop", E["s6"] + .1), ("pop", E["site"])]
    hfkit.build("2026-12-05-vales-oferta", HERE.parent / "hf", theme="neve", total=total, html=html, css=CSS, js=js, ev=E,
                scenes=scenes, voice=WORK / "voz.mp3", hits=hits, out_mp4=HERE / "reel-hf.mp4", cover=E["s3"] + .8)


if __name__ == "__main__":
    main()
