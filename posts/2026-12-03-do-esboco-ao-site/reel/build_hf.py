"""HyperFrames version of the 3/12 reel "Do esboço ao site" (natalnoite theme). Same voice text and page art as build.py.

python posts/2026-12-03-do-esboco-ao-site/reel/build_hf.py   -> reel-hf.mp4, cover-hf.jpg
The window (scaled to fit the safe area) shows the pencil sketch drawing itself, the grey wireframe, then the
finished bakery site; a phase label follows (Esboço, Estrutura, Design, Site no ar); the cursor clicks
"Encomendar" and an order toast pops; a "Mockup e orçamento 0 €" card; logo slam and the site.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import hfkit  # noqa: E402
import reelkit  # noqa: E402
from build import CSS as OLD_CSS, CURSOR, FIN, NSK, SCENES, SK, WF, WORK  # noqa: E402

GOLD, NAVY = "#F2C14E", "#0E1A33"
# the page art styles from build.py (window body, sketch, wireframe, finished site), minus the reelkit-positioned bits
KEEP = ("#win .tb", "#body", "#paper", "#sk", ".wf", "#fin")
CSS = "\n".join(l for l in OLD_CSS.splitlines() if l.startswith(KEEP)).replace("opacity:0;", "") + f"""
#wrap{{position:absolute;left:195px;top:410px;width:840px;height:760px;transform:scale(.82);transform-origin:0 0}}
#win{{position:absolute;inset:0;border-radius:26px;background:#fff;overflow:hidden;box-shadow:0 60px 120px -40px rgba(242,193,78,.35)}}
#cur{{position:absolute;left:0;top:0;width:60px;height:60px;z-index:6}}
#toast{{position:absolute;left:420px;top:640px;padding:24px 32px;border-radius:20px;background:#1f8a4c;color:#fff;font-size:34px;font-weight:700;
 box-shadow:0 30px 60px -20px rgba(0,0,0,.5);z-index:7;white-space:nowrap}}
.ph{{position:absolute;right:150px;top:330px;padding:10px 24px;border-radius:999px;background:rgba(255,255,255,.14);color:#fff;font-size:30px;font-weight:700}}
#free{{position:absolute;left:190px;right:190px;top:470px;padding:44px 0 50px;border-radius:40px;background:#fff;color:{NAVY};text-align:center}}
#free small{{display:block;font-size:40px;font-weight:700;color:#5a6684}}
#free b{{display:inline-block;margin-top:10px;padding:0 30px;border-radius:24px;background:{GOLD};font-family:'Archivo Black',sans-serif;font-size:170px;line-height:1.1}}
#ring{{position:absolute;left:340px;top:420px;width:400px;height:400px;border-radius:50%;border:8px solid {GOLD}}}
#logo{{position:absolute;left:420px;top:500px;width:240px;height:240px;filter:brightness(0) invert(1)}}
#cta{{position:absolute;left:0;right:0;top:800px;display:flex;justify-content:center}}
#cta span{{padding:30px 60px;border-radius:999px;background:{GOLD};color:{NAVY};font-size:56px;font-weight:800}}
"""


def main():
    total, scenes = reelkit.voice(SCENES, WORK / "voz.mp3")
    at = lambda s, w: reelkit.at(scenes, s, w)  # noqa: E731
    st = [s["start"] for s in scenes]
    E = {"s2": st[1], "est": at(1, "estrutura:"), "cor": at(2, "cores,"), "fot": at(2, "fotografias"), "s3": st[3],
         "tra": at(3, "trabalha"), "s4": st[4], "s5": st[5], "site": at(5, "hivecode.pt.")}
    phases = [("Esboço", .7, E["est"]), ("Estrutura", E["est"], E["cor"]), ("Design", E["cor"], E["s3"]), ("Site no ar", E["s3"], E["s4"])]
    html = (f'<div id="wrap" class="clip" data-start=".2" data-duration="{E["s4"] - .2:.3f}" data-track-index="2">'
            f'<div id="win"><div class="tb"><i></i><i></i><i></i></div><div id="body"><div id="paper"></div>'
            f'<svg id="sk" viewBox="0 0 840 700">{SK}</svg>{WF}{FIN}</div></div>{CURSOR}<div id="toast">✓ Nova encomenda</div></div>'
            + "".join(f'<span class="ph clip" id="ph{i}" data-start="{a:.3f}" data-duration="{b - a:.3f}" data-track-index="3">{n}</span>'
                      for i, (n, a, b) in enumerate(phases))
            + f'<div id="free" class="clip" data-start="{E["s4"]:.3f}" data-duration="{E["s5"] - E["s4"]:.3f}" data-track-index="4"><small>Mockup e orçamento</small><b>0 €</b></div>'
            f'<div id="end" class="clip" data-start="{E["s5"]:.3f}" data-duration="{total - E["s5"]:.3f}" data-track-index="5">'
            '<span id="ring"></span><img id="logo" src="assets/logo_mark.svg" alt=""><div id="cta"><span>hivecode.pt</span></div></div>')
    js = f"""
const NSK = {NSK}, step = (E.s2 - 1.1) / NSK;
tl.fromTo("#win", {{ scale: .6, opacity: 0, rotate: -4 }}, {{ scale: 1, opacity: 1, rotate: 0, duration: .55, ease: "back.out(1.7)" }}, .2);
tl.fromTo("#sk path", {{ strokeDashoffset: 1 }}, {{ strokeDashoffset: 0, duration: .45, stagger: step, ease: "power2.out" }}, .7);
tl.fromTo(["#sk", "#paper"], {{ opacity: 1 }}, {{ opacity: 0, duration: .5, immediateRender: false }}, E.est);
tl.fromTo(".wf", {{ opacity: 0, scale: .9 }}, {{ opacity: 1, scale: 1, duration: .35, stagger: .12, ease: "back.out(2)" }}, E.est);
tl.fromTo(".wf", {{ opacity: 1 }}, {{ opacity: 0, duration: .4, immediateRender: false }}, E.cor);
tl.fromTo("#fin", {{ opacity: 0 }}, {{ opacity: 1, duration: .5 }}, E.cor);
tl.fromTo("#fin .hero", {{ scale: 1.08, filter: "saturate(0)" }}, {{ scale: 1, filter: "saturate(1)", duration: .8, ease: "power2.out" }}, E.fot);
{"".join(f'tl.fromTo("#ph{i}", {{ y: -20, opacity: 0 }}, {{ y: 0, opacity: 1, duration: .3, ease: "back.out(2)" }}, {a:.3f});' for i, (_, a, _b) in enumerate(phases))}
tl.fromTo("#cur", {{ x: 800, y: 760, opacity: 0 }}, {{ x: 140, y: 600, opacity: 1, duration: .8, ease: "power2.inOut" }}, E.s3);
tl.fromTo("#cur", {{ scale: 1 }}, {{ scale: .8, duration: .08, yoyo: true, repeat: 1, immediateRender: false }}, E.tra);
tl.fromTo("#fin .btn", {{ backgroundColor: "#3d2a1e" }}, {{ backgroundColor: "#1f8a4c", duration: .15, immediateRender: false }}, E.tra);
tl.fromTo("#toast", {{ y: 60, opacity: 0, scale: .8 }}, {{ y: 0, opacity: 1, scale: 1, duration: .45, ease: "back.out(2.4)" }}, E.tra + .15);
tl.fromTo("#wrap", {{ opacity: 1 }}, {{ opacity: 0, y: -80, duration: .3, ease: "power2.in", immediateRender: false }}, E.s4 - .3);
tl.fromTo("#free", {{ scale: .6, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: .45, ease: "back.out(2)" }}, E.s4);
tl.fromTo("#free b", {{ scale: 1.6, rotate: -8 }}, {{ scale: 1, rotate: 0, duration: .4, ease: "back.out(3)" }}, E.s4 + .4);
tl.fromTo("#logo", {{ scale: 2.2, rotate: -90, opacity: 0 }}, {{ scale: 1, rotate: 0, opacity: 1, duration: .55, ease: "expo.out" }}, E.s5 + .05);
tl.fromTo("#ring", {{ scale: .4, opacity: .95 }}, {{ scale: 2.2, opacity: 0, duration: .7, ease: "power3.out" }}, E.s5 + .4);
tl.fromTo("#cta", {{ scale: .5, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: .45, ease: "back.out(2.4)" }}, E.site);
"""
    step = (E["s2"] - 1.1) / NSK
    hits = [("pop", .2)] + [("click", .7 + i * step) for i in range(0, NSK, 2)]
    hits += [("whoosh", E["est"]), ("whoosh", E["cor"]), ("click", E["tra"]), ("pop", E["tra"] + .15),
             ("pop", E["s4"]), ("thump", E["s4"] + .4), ("pop", E["s5"] + .1), ("pop", E["site"])]
    hfkit.build("2026-12-03-do-esboco-ao-site", HERE.parent / "hf", theme="natalnoite", total=total, html=html, css=CSS, js=js, ev=E,
                scenes=scenes, voice=WORK / "voz.mp3", hits=hits, out_mp4=HERE / "reel-hf.mp4", cover=E["tra"] + .6)


if __name__ == "__main__":
    main()
