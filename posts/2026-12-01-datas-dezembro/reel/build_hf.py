"""HyperFrames version of the 1/12 reel "Dezembro: as datas que contam" (natal theme). Same voice text as build.py.

python posts/2026-12-01-datas-dezembro/reel/build_hf.py   -> reel-hf.mp4, cover-hf.jpg
Frame 0: a giant gold "Dezembro" over the calendar flipping in. Each date is marked as it is said (8 red ring,
25 red fill, 24/31 green fill, 26 green ring) with a tag flying out of it; the calendar flips to a search
result for an open shop ("Aberto agora", Christmas hours); logo slam and greeting.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import hfkit  # noqa: E402
import reelkit  # noqa: E402
from build import SCENES, WORK  # noqa: E402

RED, GREEN, GOLD = "#C41E3A", "#0F3B2C", "#F2B233"
CSS = f"""
#cal{{position:absolute;left:150px;top:400px;width:780px;border-radius:34px;background:#fff;overflow:hidden;box-shadow:0 50px 100px -40px rgba(15,59,44,.45)}}
#cal .hd{{height:96px;background:{RED};color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 40px;font-size:42px;font-weight:800;letter-spacing:.08em}}
#cal .hd small{{font-size:30px;font-weight:600;opacity:.8}}
#cal .wd,#cal .gr{{display:grid;grid-template-columns:repeat(7,1fr);padding:0 18px}}
#cal .wd span{{height:52px;display:grid;place-items:center;font-size:24px;font-weight:700;color:#6f8a7d}}
#cal .gr{{padding-bottom:18px}}
#cal .gr span{{position:relative;height:84px;display:grid;place-items:center;font-size:36px;font-weight:600;color:{GREEN}}}
#cal .gr span i{{position:absolute;inset:6px 12px;border-radius:20px;border:6px solid transparent}}
#cal .gr span b{{position:relative}}
.tag{{position:absolute;border:5px solid #fff;padding:12px 28px;border-radius:999px;font-size:38px;font-weight:800;white-space:nowrap;box-shadow:0 20px 40px -15px rgba(15,59,44,.5);z-index:6}}
#big{{position:absolute;left:0;right:0;top:500px;text-align:center;font-family:'Playfair Display',serif;font-style:italic;font-weight:700;font-size:200px;color:{RED};z-index:7}}
#srch{{position:absolute;left:150px;top:420px;width:780px;border-radius:34px;background:#fff;padding:40px 44px;box-shadow:0 50px 100px -40px rgba(15,59,44,.45)}}
#srch .q{{padding:24px 32px;border-radius:999px;background:#F5EEE2;font-size:38px;color:#2f5646}}
#srch .r{{margin-top:30px;padding:32px;border-radius:24px;border:4px solid #e9e1d2}}
#srch h3{{font-size:46px;color:{GREEN}}}
#srch p{{margin-top:12px;font-size:34px;color:#2f5646}}
#ok{{display:inline-block;margin-top:20px;padding:14px 26px;border-radius:14px;background:{GREEN};color:#fff;font-size:32px;font-weight:700}}
#hr{{margin-top:16px;font-size:32px;font-weight:700;color:{RED}}}
#ring{{position:absolute;left:340px;top:440px;width:400px;height:400px;border-radius:50%;border:8px solid {GOLD}}}
#logo{{position:absolute;left:420px;top:520px;width:240px;height:240px}}
#bf{{position:absolute;left:0;right:0;top:810px;text-align:center;font-family:'Playfair Display',serif;font-style:italic;font-weight:700;font-size:96px;color:{RED}}}
"""

DAYS = [""] + [str(d) for d in range(1, 32)]  # 1 Dec 2026 is a Tuesday; weeks start on Monday
# tag: (id, text, left, top, colours) placed next to its day in the grid
TAGS = [("t8", "Feriado", 150, 560, f"background:{RED};color:#fff"), ("t25", "📦 Natal", 600, 790, f"background:{RED};color:#fff"),
        ("t24", "Horário especial", 380, 870, f"background:{GREEN};color:#fff"), ("t26", "Trocas", 640, 870, f"background:#fff;color:{GREEN};border:5px solid {GREEN}")]


def main():
    total, scenes = reelkit.voice(SCENES, WORK / "voz.mp3")
    at = lambda s, w: reelkit.at(scenes, s, w)  # noqa: E731
    st = [s["start"] for s in scenes]
    E = {"s1": st[1], "fer": at(1, "feriado:"), "nat": at(2, "Natal"), "h24": at(3, "24"), "h31": at(3, "31,"), "tro": at(4, "26,"),
         "onl": at(5, "online."), "vis": at(5, "vista"), "s3": st[2], "s4": st[3], "s5": st[4], "s6": st[5], "s7": st[6]}
    html = (f'<div id="big" class="clip" data-start="0" data-duration="{E["s1"]:.3f}" data-track-index="2">Dezembro</div>'
            f'<div id="cal" class="clip" data-start="{E["s1"] - .3:.3f}" data-duration="{E["s6"] - E["s1"] + .4:.3f}" data-track-index="3"><div class="hd">DEZEMBRO</div><div class="wd">'
            + "".join(f"<span>{d}</span>" for d in "STQQSSD") + '</div><div class="gr">'
            + "".join(f'<span id="d{d}"><i></i><b>{d}</b></span>' if d else "<span></span>" for d in DAYS) + "</div></div>"
            # one tag at a time, on the calendar header, from its date until the next one
            + "".join(f'<span class="tag clip" id="{i}" data-start="{a:.3f}" data-duration="{b - a:.3f}" data-track-index="4" style="right:170px;top:418px;{c}">{t}</span>'
                      for (i, t, _, _, c), (a, b) in zip(TAGS, [(E["fer"], E["nat"]), (E["nat"], E["h24"]), (E["h24"], E["tro"]), (E["tro"], E["s6"])]))
            + f'<div id="srch" class="clip" data-start="{E["s6"]:.3f}" data-duration="{E["s7"] - E["s6"]:.3f}" data-track-index="5"><div class="q">🔍 loja aberta perto de mim</div>'
            '<div class="r"><h3>A Sua Loja</h3><p>Rua do Comércio, 12 · ★ 4,8</p><div id="ok">Aberto agora</div><div id="hr">Horário de Natal: 9h–20h</div></div></div>'
            f'<div id="end" class="clip" data-start="{E["s7"]:.3f}" data-duration="{total - E["s7"]:.3f}" data-track-index="6">'
            '<span id="ring"></span><img id="logo" src="assets/logo_mark.svg" alt=""><div id="bf">Boas festas</div></div>')
    js = f"""
tl.fromTo("#big", {{ scale: 1.6, opacity: 0, y: 40 }}, {{ scale: 1, opacity: 1, y: 0, duration: .6, ease: "expo.out" }}, 0);
tl.fromTo("#big", {{ y: 0, opacity: 1 }}, {{ y: -260, scale: .5, opacity: 0, duration: .35, ease: "power3.in", immediateRender: false }}, E.s1 - .35);
tl.fromTo("#cal", {{ rotateX: -80, opacity: 0, transformPerspective: 1400, transformOrigin: "50% 0" }}, {{ rotateX: 0, opacity: 1, duration: .8, ease: "back.out(1.3)" }}, E.s1 - .3);
tl.fromTo("#cal .gr span b", {{ opacity: 0, y: 12 }}, {{ opacity: 1, y: 0, duration: .25, stagger: .015, ease: "power2.out" }}, E.s1);
const mark = (d, a, col, fill) => {{
  tl.fromTo(`#d${{d}} i`, {{ scale: 0, borderColor: col, backgroundColor: fill ? col : "rgba(0,0,0,0)" }}, {{ scale: 1, duration: .4, ease: "back.out(3)" }}, a);
  if (fill) tl.fromTo(`#d${{d}} b`, {{ color: "{GREEN}" }}, {{ color: "#fff", duration: .1, immediateRender: false }}, a);
}};
mark(8, E.fer, "{RED}", false); mark(25, E.nat, "{RED}", true); mark(24, E.h24, "{GREEN}", true); mark(31, E.h31, "{GREEN}", true); mark(26, E.tro, "{GREEN}", false);
[["#t8", E.fer], ["#t25", E.nat], ["#t24", E.h24], ["#t26", E.tro]].forEach(([id, a]) =>
  tl.fromTo(id, {{ scale: 0, rotate: -15, opacity: 0 }}, {{ scale: 1, rotate: -4, opacity: 1, duration: .45, ease: "back.out(2.5)" }}, a));
tl.fromTo("#cal", {{ rotateY: 0, opacity: 1 }}, {{ rotateY: 90, opacity: 0, duration: .35, ease: "power2.in", immediateRender: false }}, E.s6 - .25);
tl.fromTo("#srch", {{ rotateY: -90, opacity: 0, transformPerspective: 1400 }}, {{ rotateY: 0, opacity: 1, duration: .45, ease: "power2.out" }}, E.s6 + .05);
tl.fromTo("#srch .q", {{ clipPath: "inset(0 100% 0 0)" }}, {{ clipPath: "inset(0 0% 0 0)", duration: .7, ease: "steps(14)" }}, E.s6 + .4);
tl.fromTo("#ok", {{ scale: 0 }}, {{ scale: 1, duration: .4, ease: "back.out(3)" }}, E.onl);
tl.fromTo("#hr", {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: .3 }}, E.vis);
tl.fromTo("#logo", {{ scale: 2.2, rotate: -90, opacity: 0 }}, {{ scale: 1, rotate: 0, opacity: 1, duration: .55, ease: "expo.out" }}, E.s7 + .05);
tl.fromTo("#ring", {{ scale: .4, opacity: .95 }}, {{ scale: 2.2, opacity: 0, duration: .7, ease: "power3.out" }}, E.s7 + .4);
tl.fromTo("#bf", {{ opacity: 0, y: 30 }}, {{ opacity: 1, y: 0, duration: .45, ease: "back.out(2)" }}, E.s7 + .6);
"""
    hits = [("pop", .05), ("whoosh", .3), ("thump", E["fer"]), ("pop", E["nat"]), ("click", E["h24"]), ("click", E["h31"]),
            ("pop", E["tro"]), ("whoosh", E["s6"] - .25), ("pop", E["onl"]), ("pop", E["s7"] + .1), ("pop", E["s7"] + .6)]
    hfkit.build("2026-12-01-datas-dezembro", HERE.parent / "hf", theme="natal", total=total, html=html, css=CSS, js=js, ev=E,
                scenes=scenes, voice=WORK / "voz.mp3", hits=hits, out_mp4=HERE / "reel-hf.mp4", cover=E["tro"] + .8)


if __name__ == "__main__":
    main()
