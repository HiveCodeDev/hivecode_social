"""HyperFrames version of the 27/11 reel "Black Friday: 20% em sites" (blackfriday theme). Same voice text as build.py.

python posts/2026-11-27-bf-desconto/reel/build_hf.py   -> reel-hf.mp4, cover-hf.jpg
Frame 0: BLACK / FRIDAY slams in. The words fold into a browser window that builds itself; on "20%" a -20% stamp
slams with a white flash and a shake; a date chip drops; the window leaves and a price rolls down to 0 €; logo
slam with a ring and the site.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import hfkit  # noqa: E402
import reelkit  # noqa: E402
from build import SCENES, WORK  # noqa: E402  (same voice text as the reelkit version)

Y = "#FFD400"
CSS = f"""
#stage{{position:absolute;inset:0}}
#bf{{position:absolute;left:0;right:0;top:470px;text-align:center;font-family:'Archivo Black',sans-serif;font-size:210px;line-height:.92;letter-spacing:-.02em;color:{Y}}}
#bf span{{display:block}}#bf span+span{{color:#fff}}
#win{{position:absolute;left:150px;top:440px;width:780px;height:500px;border-radius:30px;background:#fff;overflow:hidden;box-shadow:0 60px 140px -40px rgba(255,212,0,.45)}}
#bar{{height:70px;background:#f1f1f1;display:flex;align-items:center;gap:12px;padding:0 28px}}
#bar i{{width:18px;height:18px;border-radius:50%;background:#d0d0d0}}
.wb{{position:absolute;border-radius:14px;background:#ececec}}
#hero{{background:linear-gradient(150deg,#fff3a6,{Y})}}
#stamp{{position:absolute;left:560px;top:380px;padding:18px 34px;border:12px solid {Y};border-radius:28px;background:#0A0A0A;color:{Y};
 font-family:'Archivo Black',sans-serif;font-size:140px;line-height:1;letter-spacing:-.03em}}
#flash{{position:absolute;inset:0;background:#fff;z-index:40}}
#date{{position:absolute;left:0;right:0;top:975px;display:flex;justify-content:center}}
#date span{{padding:20px 40px;border-radius:999px;border:5px solid {Y};color:#fff;font-size:46px;font-weight:800;background:#0A0A0A}}
#free{{position:absolute;left:190px;right:190px;top:470px;padding:44px 0 50px;border-radius:40px;background:#fff;color:#0A0A0A;text-align:center}}
#free small{{display:block;font-size:40px;font-weight:700;color:#555}}
#price{{display:block;margin-top:6px;font-family:'Archivo Black',sans-serif;font-size:190px;line-height:1;letter-spacing:-.04em}}
#ring{{position:absolute;left:340px;top:420px;width:400px;height:400px;border-radius:50%;border:8px solid {Y}}}
#logo{{position:absolute;left:420px;top:500px;width:240px;height:240px;filter:brightness(0) invert(1)}}
#cta{{position:absolute;left:0;right:0;top:800px;display:flex;justify-content:center}}
#cta span{{padding:30px 60px;border-radius:999px;background:{Y};color:#0A0A0A;font-size:56px;font-weight:800}}
"""

BLOCKS = [("w0", "left:30px;right:30px;top:96px;height:50px"), ("hero", "left:30px;right:30px;top:170px;height:190px"),
          ("w2", "left:30px;width:380px;top:385px;height:28px"), ("w3", "left:30px;width:260px;top:430px;height:46px")]


def main():
    total, scenes = reelkit.voice(SCENES, WORK / "voz.mp3")
    at = lambda s, w: reelkit.at(scenes, s, w)  # noqa: E731
    st = [s["start"] for s in scenes]
    E = {"s1": st[1], "pct": at(1, "20%"), "dom": at(2, "domingo,"), "s4": st[3], "s5": st[4], "site": at(4, "hivecode.pt.")}
    html = (f'<div id="stage">'
            f'<div id="bf" class="clip" data-start="0" data-duration="{E["s1"] + .3:.3f}" data-track-index="2"><span>BLACK</span><span>FRIDAY</span></div>'
            f'<div id="win" class="clip" data-start="{E["s1"] - .1:.3f}" data-duration="{E["s4"] - E["s1"] + .5:.3f}" data-track-index="3"><div id="bar"><i></i><i></i><i></i></div>'
            + "".join(f'<span class="wb" id="{i}" style="{s}"></span>' for i, s in BLOCKS) + "</div>"
            f'<div id="stamp" class="clip" data-start="{E["pct"]:.3f}" data-duration="{E["s4"] - E["pct"] + .4:.3f}" data-track-index="4">−20%</div>'
            f'<div id="date" class="clip" data-start="{E["dom"]:.3f}" data-duration="{E["s4"] - E["dom"]:.3f}" data-track-index="5"><span>até domingo, 29/11</span></div>'
            f'<div id="free" class="clip" data-start="{E["s4"]:.3f}" data-duration="{E["s5"] - E["s4"]:.3f}" data-track-index="6"><small>Mockup e orçamento</small><b id="price">350 €</b></div>'
            f'<div id="end" class="clip" data-start="{E["s5"]:.3f}" data-duration="{total - E["s5"]:.3f}" data-track-index="7">'
            f'<span id="ring"></span><img id="logo" src="assets/logo_mark.svg" alt=""><div id="cta"><span>hivecode.pt</span></div></div>'
            f'</div><span id="flash" class="clip" data-start="{E["pct"]:.3f}" data-duration=".12" data-track-index="8"></span>')
    js = """
tl.fromTo("#bf span", { scale: 2.4, opacity: 0, rotate: (i) => i ? 6 : -6 }, { scale: 1, opacity: 1, rotate: 0, duration: .45, stagger: .25, ease: "expo.out" }, 0);
tl.fromTo("#bf", { scale: 1, opacity: 1 }, { scale: .3, opacity: 0, y: -120, duration: .3, ease: "power3.in" }, E.s1);
tl.fromTo("#win", { scale: .5, opacity: 0, rotate: -6 }, { scale: 1, opacity: 1, rotate: 0, duration: .55, ease: "back.out(1.8)" }, E.s1);
tl.fromTo("#win .wb", { scaleX: 0, transformOrigin: "0 50%" }, { scaleX: 1, duration: .35, stagger: .12, ease: "power3.out" }, E.s1 + .3);
tl.fromTo("#hero", { filter: "grayscale(1) brightness(1.6)" }, { filter: "grayscale(0) brightness(1)", duration: .2, immediateRender: false }, E.pct);
tl.fromTo("#stamp", { scale: 3.2, rotate: -25, opacity: 0 }, { scale: 1, rotate: -10, opacity: 1, duration: .28, ease: "power4.in" }, E.pct - .2);
tl.fromTo("#stage", { x: 0, y: 0 }, { x: 14, y: -10, duration: .05, yoyo: true, repeat: 5, ease: "none" }, E.pct + .08);
tl.fromTo("#flash", { opacity: .9 }, { opacity: 0, duration: .12 }, E.pct);
tl.fromTo("#date", { y: -80, opacity: 0 }, { y: 0, opacity: 1, duration: .5, ease: "bounce.out" }, E.dom);
tl.fromTo(["#win", "#stamp"], { x: 0 }, { x: -1100, rotate: -12, duration: .4, ease: "power3.in", immediateRender: false }, E.s4 - .2);
tl.fromTo("#free", { scale: .6, opacity: 0 }, { scale: 1, opacity: 1, duration: .45, ease: "back.out(2)" }, E.s4 + .1);
const P = { v: 350 };
tl.fromTo(P, { v: 350 }, { v: 0, duration: 1.4, ease: "power3.out", onUpdate: () => { document.querySelector("#price").textContent = Math.round(P.v) + " €"; } }, E.s4 + .4);
tl.fromTo("#price", { color: "#0A0A0A" }, { color: "#0b8a3e", duration: .2, immediateRender: false }, E.s4 + 1.7);
tl.fromTo("#logo", { scale: 2.2, rotate: -90, opacity: 0 }, { scale: 1, rotate: 0, opacity: 1, duration: .55, ease: "expo.out" }, E.s5 + .05);
tl.fromTo("#ring", { scale: .4, opacity: .95 }, { scale: 2.2, opacity: 0, duration: .7, ease: "power3.out" }, E.s5 + .4);
tl.fromTo("#cta", { scale: .5, opacity: 0 }, { scale: 1, opacity: 1, duration: .45, ease: "back.out(2.4)" }, E.site);
"""
    hits = [("thump", .05), ("thump", .3), ("whoosh", E["s1"])] + [("click", E["s1"] + .3 + .12 * i) for i in range(4)]
    hits += [("thump", E["pct"]), ("pop", E["dom"]), ("whoosh", E["s4"] - .2), ("rise", E["s4"] + .4), ("pop", E["s5"] + .1), ("pop", E["site"])]
    hfkit.build("2026-11-27-bf-desconto", HERE.parent / "hf", theme="blackfriday", total=total, html=html, css=CSS, js=js, ev=E,
                scenes=scenes, voice=WORK / "voz.mp3", hits=hits, out_mp4=HERE / "reel-hf.mp4", cover=E["dom"] + .6)


if __name__ == "__main__":
    main()
