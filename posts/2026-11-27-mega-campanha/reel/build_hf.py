"""27/11 reel "Mega campanha Black Friday + Natal" (natalnoite, HyperFrames). Replaces the cancelled 20% reel.

python posts/2026-11-27-mega-campanha/reel/build_hf.py   -> reel-hf.mp4, cover-hf.jpg
Frame 0: "MEGA CAMPANHA" in gold; a black BLACK FRIDAY tag and a red NATAL tag slam together; two service cards
get a gold "condições especiais" stamp; a Follow button flips to "A seguir" and a message bubble pops; logo slam.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import hfkit  # noqa: E402
import reelkit  # noqa: E402

WORK = ROOT / "reels" / HERE.parent.name
WORK.mkdir(parents=True, exist_ok=True)
SCENES = [
    ("Mega campanha HiveCode.", 96, {"Mega", "campanha"}),
    ("Black Friday e Natal, juntos.", 96, {"Black", "Friday", "Natal,"}),
    ("Condições especiais em sites e programas à medida.", 92, {"especiais"}),
    ("Acompanhe-nos nas próximas semanas e envie-nos mensagem.", 92, {"Acompanhe-nos", "mensagem."}),
    ("hivecode.pt.", 96, {"hivecode.pt."}),
]
NAVY, GOLD, CREAM, RED, K = "#0E1A33", "#F2C14E", "#F6F1E7", "#C41E3A", "#0A0A0A"
CSS = f"""
#glow{{position:absolute;left:90px;top:330px;width:900px;height:900px;border-radius:50%;background:radial-gradient(circle,rgba(242,193,78,.25),transparent 65%)}}
#hook{{position:absolute;left:0;right:0;top:420px;text-align:center;line-height:.9}}
#hook b{{display:block;font-family:'Archivo Black',sans-serif;font-size:290px;color:{GOLD};letter-spacing:-.04em}}
#hook span{{display:block;font-family:'Archivo Black',sans-serif;font-size:128px;color:{CREAM};letter-spacing:-.02em}}
.tag{{position:absolute;top:560px;padding:34px 44px;border-radius:26px;font-family:'Archivo Black',sans-serif;font-size:76px;line-height:1;box-shadow:0 40px 90px -30px rgba(0,0,0,.7)}}
#tbf{{left:70px;background:{K};color:{GOLD};border:8px solid {GOLD}}}
#tnt{{right:70px;background:{RED};color:#fff;border:8px solid #fff}}
#plus{{position:absolute;left:0;right:0;top:770px;text-align:center;font-size:150px;font-weight:900;color:{GOLD}}}
#star{{position:absolute;left:470px;top:380px;font-size:140px;color:{GOLD};text-shadow:0 0 40px rgba(242,193,78,.9)}}
.svc{{position:absolute;top:450px;width:400px;height:430px;border-radius:40px;background:{CREAM};color:{NAVY};text-align:center;padding-top:60px;box-shadow:0 50px 120px -40px rgba(0,0,0,.7)}}
.svc i{{display:block;font-style:normal;font-size:150px;line-height:1}}
.svc b{{display:block;margin-top:30px;font-size:46px;font-weight:800;line-height:1.05;padding:0 30px}}
#sv1{{left:100px}}#sv2{{right:100px}}
#stamp{{position:absolute;left:260px;top:900px;width:560px;padding:26px 0;border:8px solid {GOLD};border-radius:22px;background:{NAVY};color:{GOLD};
 text-align:center;font-family:'Archivo Black',sans-serif;font-size:50px;letter-spacing:.02em}}
#prof{{position:absolute;left:110px;right:110px;top:420px;height:250px;border-radius:40px;background:{CREAM};color:{NAVY};display:flex;align-items:center;gap:34px;padding:0 44px}}
#prof img{{width:140px;height:140px;border-radius:50%;background:{NAVY};padding:26px;box-sizing:border-box}}
#prof p{{flex:1;font-size:50px;font-weight:800;line-height:1.1}}#prof small{{display:block;font-size:34px;font-weight:600;color:#5a6684}}
#fol{{position:relative;width:250px;height:96px;border-radius:24px;overflow:hidden;font-size:40px;font-weight:800}}
#fol span{{position:absolute;inset:0;display:grid;place-items:center}}
#f1{{background:#265ADF;color:#fff}}#f2{{background:#dfe3ec;color:{NAVY}}}
#msg{{position:absolute;left:190px;top:740px;padding:36px 50px;border-radius:44px 44px 10px 44px;background:{GOLD};color:{NAVY};font-size:56px;font-weight:800;box-shadow:0 40px 90px -30px rgba(0,0,0,.7)}}
#plane{{position:absolute;left:90px;top:880px;font-size:110px}}
#ering{{position:absolute;left:340px;top:440px;width:400px;height:400px;border-radius:50%;border:8px solid {GOLD}}}
#elogo{{position:absolute;left:420px;top:520px;width:240px;height:240px}}
#eurl{{position:absolute;left:0;right:0;top:800px;text-align:center;font-size:84px;font-weight:800;letter-spacing:-.02em}}
"""


def main():
    total, scenes = reelkit.voice(SCENES, WORK / "voz.mp3")
    S = [round(s["start"], 3) for s in scenes] + [round(total, 3)]
    clip = lambda i, a, b, n, extra="": f'<div id="{i}" class="clip" data-start="{a}" data-duration="{b - a:.3f}" data-track-index="{n}"{extra}>'  # noqa: E731
    html = ('<span id="glow"></span>'
            + clip("hook", 0, S[1], 2) + '<b id="hm">MEGA</b><span id="hc">CAMPANHA</span></div>'
            + clip("s1", S[1], S[2], 3) + '<span id="star">★</span><div class="tag" id="tbf">BLACK<br>FRIDAY</div><div class="tag" id="tnt">NATAL<br>🎄</div><div id="plus">+</div></div>'
            + clip("s2", S[2], S[3], 4) + '<div class="svc" id="sv1"><i>🖥️</i><b>Sites</b></div><div class="svc" id="sv2"><i>⚙️</i><b>Programas à medida</b></div>'
            '<div id="stamp">CONDIÇÕES ESPECIAIS</div></div>'
            + clip("s3", S[3], S[4], 5) + '<div id="prof"><img src="assets/logo_mark_white.svg" alt=""><p>hivec0de<small>HiveCode</small></p>'
            '<div id="fol"><span id="f1">Seguir</span><span id="f2">A seguir ✓</span></div></div><span id="plane">✉️</span><div id="msg">Olá! Quero saber mais 👋</div></div>'
            + clip("end", S[4], S[5], 6) + '<span id="ering"></span><img id="elogo" src="assets/logo_mark_white.svg" alt=""/><div id="eurl">hivecode.pt</div></div>')
    js = f"""const S = {S};
tl.fromTo("#glow", {{ scale: .9, opacity: .7 }}, {{ scale: 1.1, opacity: 1, duration: {total:.2f}, ease: "sine.inOut" }}, 0);
tl.fromTo("#hm", {{ scale: 1.3, rotate: -5 }}, {{ scale: 1, rotate: 0, duration: .6, ease: "expo.out" }}, 0);
tl.fromTo("#hc", {{ y: 40, letterSpacing: "0.2em" }}, {{ y: 0, letterSpacing: "-0.02em", duration: .6, ease: "expo.out" }}, .05);
tl.fromTo("#hook", {{ scale: 1 }}, {{ scale: .5, opacity: 0, y: -200, duration: .3, ease: "power3.in", immediateRender: false }}, S[1] - .3);
tl.fromTo("#tbf", {{ x: -700, rotate: -12 }}, {{ x: 0, rotate: -4, duration: .45, ease: "expo.out" }}, S[1]);
tl.fromTo("#tnt", {{ x: 700, rotate: 12 }}, {{ x: 0, rotate: 4, duration: .45, ease: "expo.out" }}, S[1] + .25);
tl.fromTo("#plus", {{ scale: 0 }}, {{ scale: 1, duration: .35, ease: "back.out(3)" }}, S[1] + .6);
tl.fromTo("#star", {{ scale: 0, rotate: -90 }}, {{ scale: 1, rotate: 0, duration: .5, ease: "back.out(2.5)" }}, S[1] + .8);
tl.fromTo("#sv1", {{ y: 500, rotate: -8, opacity: 0 }}, {{ y: 0, rotate: -3, opacity: 1, duration: .5, ease: "back.out(1.6)" }}, S[2]);
tl.fromTo("#sv2", {{ y: 500, rotate: 8, opacity: 0 }}, {{ y: 0, rotate: 3, opacity: 1, duration: .5, ease: "back.out(1.6)" }}, S[2] + .2);
tl.fromTo("#stamp", {{ scale: 2.4, rotate: -14, opacity: 0 }}, {{ scale: 1, rotate: -6, opacity: 1, duration: .35, ease: "power4.in" }}, S[2] + .9);
tl.fromTo("#s2", {{ x: 0 }}, {{ x: 14, duration: .05, yoyo: true, repeat: 5, ease: "none", immediateRender: false }}, S[2] + 1.25);
tl.fromTo("#prof", {{ y: -300, opacity: 0 }}, {{ y: 0, opacity: 1, duration: .5, ease: "back.out(1.6)" }}, S[3]);
tl.fromTo("#f2", {{ y: 96 }}, {{ y: 0, duration: .3, ease: "power3.out" }}, S[3] + 1.1);
tl.fromTo("#fol", {{ scale: 1 }}, {{ scale: .9, duration: .1, yoyo: true, repeat: 1, ease: "power2.out", immediateRender: false }}, S[3] + 1.0);
tl.fromTo("#msg", {{ scale: 0, opacity: 0, transformOrigin: "100% 100%" }}, {{ scale: 1, opacity: 1, duration: .45, ease: "back.out(2.2)" }}, S[3] + 1.9);
tl.fromTo("#plane", {{ x: -200, y: 80, rotate: -20, opacity: 0 }}, {{ x: 0, y: 0, rotate: 0, opacity: 1, duration: .5, ease: "expo.out" }}, S[3] + 2.1);
tl.fromTo("#elogo", {{ scale: 2.2, rotate: -90, opacity: 0 }}, {{ scale: 1, rotate: 0, opacity: 1, duration: .55, ease: "expo.out" }}, S[4] + .05);
tl.fromTo("#ering", {{ scale: .4, opacity: .95 }}, {{ scale: 2.2, opacity: 0, duration: .7, ease: "power3.out" }}, S[4] + .4);
tl.fromTo("#eurl", {{ opacity: 0, y: 40 }}, {{ opacity: 1, y: 0, duration: .45, ease: "back.out(2)" }}, reelkit_url);
""".replace("reelkit_url", f"{reelkit.at(scenes, 4, 'hivecode.pt.'):.3f}")
    hits = [("pop", .05), ("whoosh", S[1]), ("whoosh", S[1] + .25), ("pop", S[1] + .6), ("pop", S[1] + .8), ("whoosh", S[2]),
            ("thump", S[2] + 1.2), ("pop", S[3]), ("click", S[3] + 1.0), ("pop", S[3] + 1.9), ("pop", S[4] + .1)]
    hfkit.build("2026-11-27-mega-campanha", HERE.parent / "hf", theme="natalnoite", total=total, html=html, css=CSS, js=js,
                scenes=scenes, voice=WORK / "voz.mp3", hits=hits, out_mp4=HERE / "reel-hf.mp4", cover=S[1] + 1.4)


if __name__ == "__main__":
    main()
