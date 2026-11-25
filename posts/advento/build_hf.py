"""HyperFrames version of the advent stories (1-24 December, 17:30): same tree, doors and facts as build.py.

python posts/advento/build_hf.py [day ...]   -> posts/stories/advento-NN/story-hf.mp4
The HiveCode hexagon tree is on screen from frame 0 (earlier doors open, logo as the star); the camera pushes in
on today's door, which shakes and swings open with a star popping out; the screen dims and the fact card lands;
"Amanhã às 17h30: porta N+1"; arrow to the profile and the logo outro.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import importlib.util  # noqa: E402

import hfkit  # noqa: E402

# loaded under another name: build.py imports build_anim, which imports the Halloween reel's own "build" module
_spec = importlib.util.spec_from_file_location("advento_build", HERE / "build.py")
_adv = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_adv)
OLD_CSS, FACTS, GREENS, ORDER, ORN, SLOTS, door_xy = _adv.CSS, _adv.FACTS, _adv.GREENS, _adv.ORDER, _adv.ORN, _adv.SLOTS, _adv.door_xy

BODY, OUTRO = 11.0, 1.6
# the tree/door/card styles from build.py; positions use absolute here (reelkit gave every #art child absolute)
CSS = OLD_CSS.replace("#cam{", "#cam{position:absolute;").replace("#dim{", "#dim{position:absolute;").replace("#card{", "#card{position:absolute;").replace("#next{", "#next{position:absolute;") \
    .replace("opacity:0;", "").replace("opacity:0}", "}")


def story(day):
    cells = ""
    for i, n in enumerate(ORDER):
        x, y, r = SLOTS[i]
        col = "#6b4226" if r >= 6 else ORN.get(i, GREENS[i % 3])
        ink = "#0F3B2C" if col == "#F2B233" else "#fff"
        opened = "transform:rotateY(-108deg)" if n < day else ""
        star = '<span id="star" style="display:inline-block">★</span>' if n == day else "★" if n < day else ""
        cells += (f'<div class="dc" style="left:{x:.0f}px;top:{y:.0f}px"><div class="in">{star}</div>'
                  f'<div class="lf" id="{"today" if n == day else f"d{n}"}" style="background:{col};color:{ink};{opened}">{n}</div></div>')
    cx, cy = door_xy(day)
    nxt = f"Amanhã às 17h30: porta {day + 1}" if day < 24 else "Boas festas! 🎄"
    html = (f'<div id="cam"><div id="tree"><img id="tstar" src="assets/logo_mark.svg" alt="">{cells}</div></div>'
            f'<span id="dim" class="clip" data-start="5" data-duration="{BODY - 5}" data-track-index="5"></span>'
            f'<div id="card" class="clip" data-start="5.2" data-duration="{BODY - 5.2}" data-track-index="6"><small>PORTA {day} · SABIA QUE…</small><p>{FACTS[day]}</p></div>'
            f'<div id="next" class="clip" data-start="8" data-duration="{BODY - 8}" data-track-index="7"><span>{nxt}</span></div>')
    # camera: scale s around today's door, keeping it at (540, 1000)
    s = 3.8
    js = f"""
tl.fromTo("#tree", {{ scale: .85, opacity: 0, transformOrigin: "540px 1100px" }}, {{ scale: 1, opacity: 1, duration: .6, ease: "back.out(1.6)" }}, 0);
tl.fromTo("#tstar", {{ rotate: -8, scale: 1 }}, {{ rotate: 8, scale: 1.06, duration: 1, yoyo: true, repeat: 10, ease: "sine.inOut" }}, 0);
tl.fromTo("#cam", {{ x: 0, y: 0, scale: 1, transformOrigin: "0 0" }}, {{ x: {540 - cx * s:.1f}, y: {1000 - cy * s:.1f}, scale: {s}, duration: 1.4, ease: "power3.inOut" }}, 1.6);
tl.fromTo("#today", {{ rotateY: 0 }}, {{ rotateY: -6, duration: .06, yoyo: true, repeat: 7, ease: "none" }}, 3.0);
tl.fromTo("#today", {{ rotateY: 0 }}, {{ rotateY: -108, duration: .7, ease: "power3.inOut", immediateRender: false }}, 3.5);
tl.fromTo("#star", {{ scale: 0, rotate: -60 }}, {{ scale: 1, rotate: 0, duration: .5, ease: "back.out(3)" }}, 3.9);
tl.fromTo("#star", {{ textShadow: "0 0 0px rgba(242,178,51,0)" }}, {{ textShadow: "0 0 30px rgba(242,178,51,.95)", duration: .5 }}, 3.9);
tl.fromTo("#dim", {{ opacity: 0 }}, {{ opacity: .82, duration: .4 }}, 5.0);
tl.fromTo("#card", {{ y: 120, opacity: 0, scale: .85 }}, {{ y: 0, opacity: 1, scale: 1, duration: .55, ease: "back.out(1.8)" }}, 5.2);
tl.fromTo("#next", {{ y: 40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: .45, ease: "back.out(2.2)" }}, 8.0);
"""
    return dict(theme="natal", html=html, css=CSS, js=js,
                title=[(f"Dezembro, dia {day}.", 100, {"Dezembro,"}, 0, 1.6), (f"Porta {day}", 130, {str(day)}, 5.1, BODY)],
                arrow=("Siga o perfil", 8.6, "background:#C41E3A;color:#fff"),
                hits=[("pop", .2), ("whoosh", 1.6), ("click", 3.05), ("click", 3.3), ("whoosh", 3.5), ("pop", 3.9), ("pop", 5.2), ("pop", 8.0), ("pop", 8.6)])


def main(days):
    for d in days or sorted(FACTS):
        s = story(d)
        out = ROOT / "posts" / "stories" / f"advento-{d:02d}"
        hfkit.build(f"story-advento-{d:02d}", out / "hf", theme=s["theme"], total=BODY + OUTRO, html=s["html"], css=s["css"], js=s["js"],
                    title=s["title"], arrow=s["arrow"], outro=BODY, hits=s["hits"] + [("whoosh", BODY)], out_mp4=out / "story-hf.mp4")


if __name__ == "__main__":
    main([int(d) for d in sys.argv[1:]])
