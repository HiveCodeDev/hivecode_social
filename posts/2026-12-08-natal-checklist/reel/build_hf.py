"""HyperFrames version of the 8/12 reel "5 coisas antes do Natal" (natalnoite theme), from the approved hf-test.

python posts/2026-12-08-natal-checklist/reel/build_hf.py   -> reel-hf.mp4, cover-hf.jpg
Frame 0: a giant gold "5". A tracker of five hexagons; each item is a card that whips in with its own motion
(clock, calendar, voucher shine, banner drop, call rings), gets a gold check and fills its hexagon; logo slam,
hivecode.pt and the free offer chip.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import hfkit  # noqa: E402
import reelkit  # noqa: E402
from build import SCENES, WORK  # noqa: E402

NAVY, GOLD, CREAM = "#0E1A33", "#F2C14E", "#F6F1E7"
ITEMS = [
    ("Horário de Natal", '<div class="clock"><i class="hh"></i><i class="mh"></i></div><p>24/12<br><small>9h às 13h</small></p>'),
    ("Prazo de entrega", '<div class="cal"><span>DEZ</span><b>18</b></div><p>Encomendas<br><small>chegam a tempo</small></p>'),
    ("Vales-oferta", '<div class="vou"><small>VALE-OFERTA</small><b>50 €</b><i class="shine"></i></div>'),
    ("Destaque de Natal", '<div class="site"><span class="bar"></span><span class="ban">🎄 Especial Natal</span><span class="ln"></span><span class="ln s"></span></div>'),
    ("Contacto rápido", '<div class="call"><i class="pr"></i><i class="pr p2"></i><span>📞 Ligar agora</span></div>'),
]
CSS = f"""
#glow{{position:absolute;left:140px;top:420px;width:800px;height:800px;border-radius:50%;background:radial-gradient(circle,rgba(242,193,78,.22),transparent 65%)}}
#track{{position:absolute;left:0;right:0;top:370px;display:flex;justify-content:center;gap:22px}}
.hx{{position:relative;width:96px;height:110px;clip-path:polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%);background:rgba(246,241,231,.16);display:grid;place-items:center}}
.hx i{{position:absolute;inset:0;background:{GOLD};transform-origin:50% 100%}}
.hx b{{position:relative;font-size:40px;font-weight:800;color:{CREAM}}}
.card{{position:absolute;left:150px;top:540px;width:780px;height:470px}}
.cin{{position:absolute;inset:0;border-radius:44px;background:{CREAM};color:{NAVY};padding:40px 48px;box-shadow:0 60px 140px -40px rgba(0,0,0,.7)}}
.cin h3{{font-size:58px;font-weight:800;letter-spacing:-.02em;margin-left:120px;line-height:96px}}
.num{{position:absolute;left:40px;top:36px;width:100px;height:100px;border-radius:50%;background:{NAVY};color:{GOLD};display:grid;place-items:center;font-size:56px;font-weight:900}}
.art{{position:absolute;left:48px;right:48px;top:170px;bottom:40px;display:flex;align-items:center;gap:40px}}
.art p{{font-size:64px;font-weight:800;line-height:1}}.art small{{font-size:40px;font-weight:600;color:#5a6684}}
.clock{{position:relative;width:200px;height:200px;border-radius:50%;border:14px solid {NAVY}}}
.clock i{{position:absolute;left:86px;bottom:86px;width:14px;border-radius:7px;background:{NAVY};transform-origin:50% 100%}}
.clock .hh{{height:56px}}.clock .mh{{height:76px;background:#C41E3A}}
.cal{{width:200px;border-radius:24px;overflow:hidden;text-align:center;border:6px solid {NAVY}}}
.cal span{{display:block;background:#C41E3A;color:#fff;font-size:34px;font-weight:800;padding:8px 0}}.cal b{{display:block;font-size:110px;font-weight:900;line-height:1.1}}
.vou{{position:relative;overflow:hidden;width:100%;height:220px;border-radius:30px;background:linear-gradient(135deg,#C41E3A,#8f1228);color:#fff;padding:30px 40px}}
.vou small{{font-size:30px;font-weight:700;letter-spacing:.16em}}.vou b{{display:block;font-size:120px;font-weight:900;line-height:1.1;color:{GOLD}}}
.shine{{position:absolute;top:0;bottom:0;left:0;width:160px;background:linear-gradient(90deg,transparent,rgba(255,255,255,.45),transparent)}}
.site{{position:relative;width:100%;height:230px;border-radius:24px;border:6px solid {NAVY};overflow:hidden;background:#fff}}
.site .bar{{display:block;height:40px;background:{NAVY}}}
.site .ban{{position:absolute;left:24px;right:24px;top:58px;padding:20px 26px;border-radius:16px;background:#C41E3A;color:#fff;font-size:40px;font-weight:800}}
.site .ln{{position:absolute;left:24px;top:170px;width:60%;height:18px;border-radius:9px;background:#dfe3ec}}.site .ln.s{{top:200px;width:40%}}
.call{{position:relative;margin:0 auto;display:grid;place-items:center;width:100%;height:220px}}
.call span{{position:relative;padding:36px 60px;border-radius:999px;background:#1f8a4c;color:#fff;font-size:52px;font-weight:800}}
.call .pr{{position:absolute;left:50%;top:50%;width:420px;height:150px;margin:-75px 0 0 -210px;border-radius:999px;border:6px solid #1f8a4c}}
.ok{{position:absolute;right:-30px;top:-30px;display:grid;place-items:center;width:130px;height:130px;border-radius:999px;background:{GOLD};color:{NAVY};box-shadow:0 20px 50px -10px rgba(0,0,0,.5)}}
.ok svg{{width:100px;height:100px;fill:none;stroke:currentColor;stroke-width:6;stroke-linecap:round;stroke-linejoin:round}}
.ok circle{{opacity:.25}}.ok path{{stroke-dasharray:36}}
#hook{{position:absolute;left:0;right:0;top:500px;text-align:center}}
#hook b{{display:block;font-size:420px;font-weight:900;line-height:1;color:{GOLD};letter-spacing:-.04em}}
#hook span{{display:block;font-size:64px;font-weight:700;margin-top:-10px}}
#ering{{position:absolute;left:340px;top:440px;width:400px;height:400px;border-radius:50%;border:8px solid {GOLD}}}
#elogo{{position:absolute;left:420px;top:520px;width:240px;height:240px}}
#eurl{{position:absolute;left:0;right:0;top:790px;text-align:center;font-size:84px;font-weight:800;letter-spacing:-.02em}}
#echip{{position:absolute;left:190px;right:190px;top:920px;text-align:center;padding:26px 0;border-radius:999px;background:{GOLD};color:{NAVY};font-size:44px;font-weight:800}}
"""


def main():
    total, scenes = reelkit.voice(SCENES, WORK / "voz.mp3")
    S = [round(s["start"], 3) for s in scenes] + [round(total, 3)]
    cards = "".join(
        f'<div class="card clip" id="c{i}" data-start="{S[i + 1]}" data-duration="{S[i + 2] - S[i + 1]:.3f}" data-track-index="{3 + i}">'
        f'<div class="cin" id="ci{i}"><span class="num">{i + 1}</span><h3>{n}</h3><div class="art">{a}</div>'
        f'<div class="ok" id="ok{i}"><svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="27"/><path d="M20 33.5l8 8L45 23"/></svg></div></div></div>'
        for i, (n, a) in enumerate(ITEMS))
    html = ('<span id="glow"></span><div id="track">' + "".join(f'<span class="hx" id="hx{i}"><i id="hf{i}"></i><b>{i + 1}</b></span>' for i in range(5)) + "</div>"
            f'<div id="hook" class="clip" data-start="0" data-duration="{S[1]}" data-track-index="2"><b id="h5">5</b><span id="hsub">coisas a rever</span></div>{cards}'
            f'<div id="end" class="clip" data-start="{S[6]}" data-duration="{total - S[6]:.3f}" data-track-index="9">'
            '<span id="ering"></span><img id="elogo" src="assets/logo_mark_white.svg" alt=""/><div id="eurl">hivecode.pt</div><div id="echip">Mockup e orçamento gratuitos</div></div>')
    js = f"""const S = {S};
tl.fromTo("#h5", {{ scale: 1.25, rotate: -6 }}, {{ scale: 1, rotate: 0, duration: .6, ease: "expo.out" }}, 0);
tl.fromTo("#hsub", {{ opacity: 0, y: 30 }}, {{ opacity: 1, y: 0, duration: .4, ease: "power3.out" }}, S[1] - 1.6);
tl.fromTo("#hook", {{ scale: 1 }}, {{ scale: .4, opacity: 0, y: -260, duration: .35, ease: "power3.in" }}, S[1] - .35);
tl.fromTo("#glow", {{ scale: .9, opacity: .7 }}, {{ scale: 1.1, opacity: 1, duration: {total:.2f}, ease: "sine.inOut" }}, 0);
tl.fromTo(".hx", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: .5, stagger: .06, ease: "back.out(2)" }}, .1);
tl.fromTo(".hx i", {{ scaleY: 0 }}, {{ scaleY: 0, duration: .01 }}, 0);
for (let i = 0; i < 5; i++) {{
  const a = S[i + 1], b = S[i + 2];
  tl.fromTo(`#ci${{i}}`, {{ x: 900, rotate: 8, filter: "blur(14px)" }}, {{ x: 0, rotate: 0, filter: "blur(0px)", duration: .45, ease: "expo.out" }}, a);
  tl.fromTo(`#ci${{i}}`, {{ x: 0, filter: "blur(0px)" }}, {{ x: -900, rotate: -8, filter: "blur(14px)", duration: .3, ease: "power3.in", immediateRender: false }}, b - .3);
  tl.fromTo(`#ok${{i}}`, {{ scale: 0 }}, {{ scale: 1, duration: .3, ease: "back.out(2.5)" }}, a + .45);
  tl.fromTo(`#ok${{i}} path`, {{ strokeDashoffset: 36 }}, {{ strokeDashoffset: 0, duration: .4, ease: "power2.out" }}, a + .58);
  tl.fromTo(`#hf${{i}}`, {{ scaleY: 0 }}, {{ scaleY: 1, duration: .35, ease: "power3.out", immediateRender: false }}, a + .6);
  tl.fromTo(`#hx${{i}} b`, {{ color: "{CREAM}" }}, {{ color: "{NAVY}", duration: .1, immediateRender: false }}, a + .7);
  tl.fromTo(`#hx${{i}}`, {{ scale: 1 }}, {{ scale: 1.25, duration: .15, yoyo: true, repeat: 1, ease: "power2.out", immediateRender: false }}, a + .6);
}}
tl.fromTo("#c0 .mh", {{ rotate: 0 }}, {{ rotate: 720, duration: 2.6, ease: "power2.out" }}, S[1]);
tl.fromTo("#c0 .hh", {{ rotate: 0 }}, {{ rotate: 60, duration: 2.6, ease: "power2.out" }}, S[1]);
tl.fromTo("#c1 .cal", {{ rotateX: 90 }}, {{ rotateX: 0, duration: .6, ease: "back.out(1.6)" }}, S[2] + .25);
tl.fromTo("#c2 .shine", {{ x: -200 }}, {{ x: 900, duration: .9, ease: "power2.inOut" }}, S[3] + .7);
tl.fromTo("#c2 .vou", {{ rotate: -4 }}, {{ rotate: 2, duration: 2.5, ease: "sine.inOut" }}, S[3]);
tl.fromTo("#c3 .ban", {{ y: -90, opacity: 0 }}, {{ y: 0, opacity: 1, duration: .5, ease: "bounce.out" }}, S[4] + .4);
tl.fromTo("#c4 .pr", {{ scale: .9, opacity: .8 }}, {{ scale: 1.35, opacity: 0, duration: 1.2, stagger: .5, repeat: 1, ease: "power2.out" }}, S[5] + .3);
tl.fromTo("#elogo", {{ scale: 2.2, rotate: -90, opacity: 0 }}, {{ scale: 1, rotate: 0, opacity: 1, duration: .55, ease: "expo.out" }}, S[6] + .1);
tl.fromTo("#ering", {{ scale: .4, opacity: .95 }}, {{ scale: 2.2, opacity: 0, duration: .7, ease: "power3.out" }}, S[6] + .45);
tl.fromTo("#eurl", {{ opacity: 0, y: 40 }}, {{ opacity: 1, y: 0, duration: .45, ease: "back.out(2)" }}, S[6] + .7);
tl.fromTo("#echip", {{ opacity: 0, scale: .6 }}, {{ opacity: 1, scale: 1, duration: .45, ease: "back.out(2.4)" }}, S[6] + 1.2);
"""
    items = [S[k] + .15 for k in range(1, 6)]
    hits = [("pop", .15)] + [h for a in items for h in (("whoosh", a - .1), ("click", a + .4))] + [("pop", S[6] + .1), ("pop", reelkit.at(scenes, 6, "hivecode.pt."))]
    hfkit.build("2026-12-08-natal-checklist", HERE.parent / "hf", theme="natalnoite", total=total, html=html, css=CSS, js=js,
                scenes=scenes, voice=WORK / "voz.mp3", hits=hits, out_mp4=HERE / "reel-hf.mp4", cover=S[6] - .3)


if __name__ == "__main__":
    main()
