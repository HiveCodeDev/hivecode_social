"""HyperFrames versions of the animated stories (no voice): hook title, art, arrow to the profile, logo outro.

python posts/stories/build_hf.py [name ...]   -> posts/stories/<name>/story-hf.mp4
Each entry: theme, title lines [(text, size, {em}, start, end)], arrow (label, at, css), html/css/js (GSAP on `tl`),
hits [(sound, s)]. Body length BODY, then a 1.6 s outro (blur, logo, hivecode.pt).
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import hfkit  # noqa: E402

BODY, OUTRO = 6.5, 1.6
TOTAL = BODY + OUTRO
Y, K = "#FFD400", "#0A0A0A"

STORIES = {
    # 25/11 "saiu hoje": the crossed-out price has rules (carousel). A price tag swings on its string,
    # the old price gets struck through, then a red "?" stamp lands.
    "2026-11-25-saiu": dict(
        theme="canvas", title=[("O preço riscado tem regras.", 130, {"regras."}, 0, BODY)],
        arrow=("Veja as regras no perfil", 3.6, "background:#9B3CF0;color:#fff"),
        css="""#tg{position:absolute;left:190px;top:900px;width:700px;padding:60px 60px 56px 110px;border-radius:28px 60px 60px 28px;background:#fff;
 border:6px solid #121125;box-shadow:0 40px 80px -30px rgba(18,17,37,.45);white-space:nowrap;transform-origin:0 50%}
#tg:before{content:"";position:absolute;left:40px;top:50%;width:34px;height:34px;margin-top:-17px;border-radius:50%;border:6px solid #121125;background:#F4F2FA}
#str{position:absolute;left:-40px;top:50%;width:200px;height:6px;margin-top:-3px;background:#121125;transform-origin:100% 50%;transform:translateX(-100%) rotate(-20deg)}
#old{position:relative;display:inline-block;font-size:70px;color:#8a879c}
#cut{position:absolute;left:-6px;right:-6px;top:50%;height:8px;margin-top:-4px;background:#D7263D;border-radius:4px;transform-origin:0 50%}
#new{display:block;margin-top:10px;font-size:150px;font-weight:800;line-height:1;color:#121125;letter-spacing:-.03em}
#q{position:absolute;left:770px;top:840px;width:140px;height:140px;border-radius:50%;background:#D7263D;color:#fff;display:grid;place-items:center;font-size:96px;font-weight:800}
#qr{position:absolute;left:770px;top:840px;width:140px;height:140px;border-radius:50%;border:6px solid #D7263D}""",
        html='<div id="tg"><span id="str"></span><span id="old">50,00 €<i id="cut"></i></span><span id="new">36,00 €</span></div><span id="qr"></span><span id="q">?</span>',
        js="""tl.fromTo("#tg", { rotate: -28, opacity: 0, y: -200 }, { rotate: 0, opacity: 1, y: 0, duration: 1.1, ease: "elastic.out(1, .45)" }, .25);
tl.fromTo("#cut", { scaleX: 0 }, { scaleX: 1, duration: .3, ease: "power3.inOut" }, 1.0);
tl.fromTo("#new", { scale: 1.3, color: "#D7263D" }, { scale: 1, color: "#121125", duration: .5, ease: "back.out(2)" }, 1.25);
tl.fromTo("#q", { scale: 3, opacity: 0, rotate: -40 }, { scale: 1, opacity: 1, rotate: 12, duration: .25, ease: "power4.in" }, 1.6);
tl.fromTo("#qr", { scale: 1, opacity: .9 }, { scale: 2.4, opacity: 0, duration: .6, ease: "power2.out" }, 1.85);
tl.fromTo("#tg", { x: 0 }, { x: 8, duration: .05, yoyo: true, repeat: 3, ease: "none", immediateRender: false }, 1.85);""",
        hits=[("whoosh", .25), ("click", 1.0), ("pop", 1.25), ("thump", 1.85), ("pop", 3.6)]),

    # 26/11 "amanhã": a yellow box drops, shakes, and its lid blows off with light rays.
    "2026-11-26-amanha": dict(
        theme="blackfriday", title=[("Amanhã: Black Friday na HiveCode.", 124, {"Black", "Friday"}, 0, BODY)],
        arrow=("Siga o perfil", 3.8, f"background:{Y};color:{K}"),
        css=f"""#rays{{position:absolute;left:40px;top:700px;width:1000px;height:1000px;border-radius:50%;
 background:repeating-conic-gradient(rgba(255,212,0,.32) 0 8deg,transparent 8deg 22deg);-webkit-mask-image:radial-gradient(circle,#000 20%,transparent 68%)}}
#bx{{position:absolute;left:290px;top:980px;width:500px;height:460px;border-radius:40px;background:{Y};display:grid;place-items:center;
 font-family:'Archivo Black',sans-serif;font-size:280px;color:{K};line-height:1;transform-origin:50% 100%}}
#bx:before{{content:"";position:absolute;left:220px;top:0;width:60px;height:100%;background:{K};opacity:.85}}
#bx span{{position:relative}}
#lid{{position:absolute;left:260px;top:910px;width:560px;height:110px;border-radius:30px;background:#fff}}
#lid:before{{content:"";position:absolute;left:250px;top:0;width:60px;height:100%;background:{K};opacity:.85}}""",
        html='<span id="rays"></span><div id="bx"><span id="qm">?</span></div><div id="lid"></div>',
        js="""tl.fromTo(["#bx", "#lid"], { y: -900 }, { y: 0, duration: .6, ease: "bounce.out" }, .2);
tl.fromTo("#bx", { scaleY: 1 }, { scaleY: .9, duration: .08, yoyo: true, repeat: 1 }, .55);
tl.fromTo(["#bx", "#lid"], { rotate: 0 }, { rotate: 5, duration: .07, yoyo: true, repeat: 11, ease: "none", immediateRender: false }, 1.5);
tl.fromTo("#lid", { y: 0, rotate: 0, x: 0 }, { y: -520, x: 260, rotate: 70, opacity: 0, duration: .6, ease: "power2.out", immediateRender: false }, 2.5);
tl.fromTo("#rays", { scale: .3, opacity: 0, rotate: 0 }, { scale: 1, opacity: 1, rotate: 40, duration: 1.2, ease: "power2.out" }, 2.5);
tl.fromTo("#rays", { rotate: 40 }, { rotate: 120, duration: 4, ease: "none", immediateRender: false }, 3.7);
tl.fromTo("#qm", { scale: 1 }, { scale: 1.25, duration: .25, yoyo: true, repeat: 1, ease: "power2.out" }, 2.55);""",
        hits=[("whoosh", .2), ("thump", .6), ("click", 1.55), ("click", 1.85), ("click", 2.15), ("rise", 2.45), ("pop", 3.8)]),

    # 27/11 "saiu hoje": a site window builds; a -20% stamp slams with a flash and a shake.
    "2026-11-27-saiu": dict(
        theme="blackfriday", title=[("Black Friday: −20% na criação de sites.", 116, {"−20%"}, 0, BODY)],
        arrow=("Veja a oferta no perfil", 3.6, f"background:{Y};color:{K}"),
        css=f"""#shk{{position:absolute;inset:0}}
#win{{position:absolute;left:140px;right:140px;top:1000px;height:480px;border-radius:30px;background:#fff;overflow:hidden}}
#win .bar{{height:70px;background:#f1f1f1}}
#win .wb{{position:absolute;border-radius:14px;background:#ececec;transform-origin:0 50%}}
#hero{{background:linear-gradient(150deg,#fff3a6,{Y}) !important}}
#st{{position:absolute;left:470px;top:930px;padding:22px 38px;border:12px solid {Y};border-radius:28px;background:{K};color:{Y};
 font-family:'Archivo Black',sans-serif;font-size:140px;letter-spacing:-.03em;line-height:1}}
#fl{{position:absolute;inset:0;background:#fff;z-index:45}}""",
        html='<div id="shk"><div id="win"><div class="bar"></div><span class="wb" id="hero" style="left:30px;right:30px;top:100px;height:200px"></span>'
             '<span class="wb" style="left:30px;width:380px;top:330px;height:34px"></span><span class="wb" style="left:30px;width:240px;top:390px;height:60px;background:#0A0A0A"></span></div>'
             '<div id="st">−20%</div></div><span id="fl" class="clip" data-start="1.3" data-duration=".15" data-track-index="9"></span>',
        js="""tl.fromTo("#win", { y: 300, opacity: 0, rotate: 4 }, { y: 0, opacity: 1, rotate: 0, duration: .6, ease: "back.out(1.6)" }, .2);
tl.fromTo("#win .wb", { scaleX: 0 }, { scaleX: 1, duration: .3, stagger: .1, ease: "power3.out" }, .55);
tl.fromTo("#st", { scale: 3.2, rotate: -30, opacity: 0 }, { scale: 1, rotate: -10, opacity: 1, duration: .25, ease: "power4.in" }, 1.05);
tl.fromTo("#fl", { opacity: .85 }, { opacity: 0, duration: .15 }, 1.3);
tl.fromTo("#shk", { x: 0, y: 0 }, { x: 14, y: -10, duration: .05, yoyo: true, repeat: 5, ease: "none" }, 1.32);""",
        hits=[("whoosh", .2), ("click", .55), ("click", .65), ("click", .75), ("thump", 1.3), ("pop", 3.6)]),
}


def main(names):
    for name in names or STORIES:
        s = STORIES[name]
        hfkit.build(f"story-{name}", HERE / name / "hf", theme=s["theme"], total=TOTAL, html=s["html"], css=s["css"], js=s["js"],
                    title=s["title"], arrow=s["arrow"], outro=BODY, hits=s["hits"] + [("whoosh", BODY)], out_mp4=HERE / name / "story-hf.mp4")


if __name__ == "__main__":
    main(sys.argv[1:])
