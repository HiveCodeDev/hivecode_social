"""HyperFrames version of the 10/12 reel Business "Dezembro" (natal theme). Same voice text as build.py.

python posts/2026-12-10-business-dezembro/reel/build_hf.py   -> reel-hf.mp4, cover-hf.jpg
Frame 0: an "orders today" counter already racing, order notifications piling in. Email, a stock notebook and a
separate invoicing app scatter and shake; they get pulled into one HiveCode Business dashboard whose tiles light
up as they are named; a January page gets a "Fecho do ano ✓" stamp; logo slam and the site.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import hfkit  # noqa: E402
import reelkit  # noqa: E402
from build import NOTES, SCENES, WORK  # noqa: E402

INK, RED, GREEN = "#0F3B2C", "#C41E3A", "#0F7B4F"
CSS = f"""
#cnt{{position:absolute;left:240px;top:400px;width:600px;padding:30px 0 36px;border-radius:36px;background:{INK};color:#fff;text-align:center}}
#cnt small{{display:block;font-size:28px;font-weight:700;letter-spacing:.16em;opacity:.75}}
#cnt b{{display:block;font-size:170px;line-height:1;margin-top:8px;font-variant-numeric:tabular-nums}}
.nt{{position:absolute;left:160px;width:760px;padding:22px 32px;border-radius:24px;background:#fff;font-size:32px;font-weight:600;color:{INK};
 box-shadow:0 30px 60px -25px rgba(15,59,44,.45);display:flex;justify-content:space-between}}
.nt i{{font-style:normal;color:{RED};font-weight:800}}
.wd{{position:absolute;width:500px;border-radius:28px;background:#fff;overflow:hidden;box-shadow:0 40px 80px -30px rgba(15,59,44,.5)}}
.wd .h{{padding:18px 26px;font-size:28px;font-weight:800;color:#fff}}
.wd .b{{padding:20px 26px 26px;font-size:30px;line-height:1.5;color:{INK}}}
#w0{{left:100px;top:420px}}#w0 .h{{background:#2C6FD1}}
#w1{{left:480px;top:600px}}#w1 .h{{background:#8a6a3c}}
#w1 .b{{background:repeating-linear-gradient(#fffdf6 0 44px,#e6dcc4 44px 46px);font-family:'Playfair Display',serif;font-style:italic;font-size:36px}}
#w2{{left:150px;top:790px}}#w2 .h{{background:#6c4bb5}}
#db{{position:absolute;left:120px;top:400px;width:840px;border-radius:36px;background:#fff;overflow:hidden;box-shadow:0 60px 120px -40px rgba(15,59,44,.5)}}
#db .h{{display:flex;align-items:center;gap:18px;padding:24px 32px;background:{INK};color:#fff;font-size:32px;font-weight:700}}
#db .h img{{width:44px;height:44px;filter:brightness(0) invert(1)}}
#db .tl{{display:flex;gap:18px;padding:26px 28px 8px}}
#db .tl div{{flex:1;padding:22px 0;border-radius:24px;background:#f3efe6;text-align:center;font-size:28px;font-weight:700;color:#5d7569}}
#db .tl b{{display:block;font-size:80px;line-height:1.05;color:{INK}}}
#db .ls{{padding:8px 28px 26px}}
#db .ls p{{display:flex;justify-content:space-between;margin-top:14px;padding:18px 22px;border-radius:18px;background:#faf8f3;font-size:30px;color:{INK}}}
#db .ls p span{{padding:4px 18px;border-radius:999px;font-size:24px;font-weight:800;color:#fff}}
#jan{{position:absolute;left:340px;top:420px;width:400px;border-radius:30px;background:#fff;overflow:hidden;text-align:center;box-shadow:0 50px 100px -40px rgba(15,59,44,.5)}}
#jan .m{{padding:22px 0;background:{RED};color:#fff;font-size:40px;font-weight:800;letter-spacing:.1em}}
#jan .d{{padding:26px 0 36px;font-size:190px;font-weight:800;line-height:1;color:{INK}}}
#stamp{{position:absolute;left:250px;top:870px;padding:20px 36px;border-radius:20px;border:8px solid {GREEN};color:{GREEN};font-size:56px;font-weight:900;white-space:nowrap;background:#fff}}
#ring{{position:absolute;left:340px;top:420px;width:400px;height:400px;border-radius:50%;border:8px solid {RED}}}
#logo{{position:absolute;left:420px;top:500px;width:240px;height:240px}}
#cta{{position:absolute;left:0;right:0;top:800px;display:flex;justify-content:center}}
#cta span{{padding:30px 60px;border-radius:999px;background:{INK};color:#fff;font-size:56px;font-weight:800}}
"""


def main():
    total, scenes = reelkit.voice(SCENES, WORK / "voz.mp3")
    at = lambda s, w: reelkit.at(scenes, s, w)  # noqa: E731
    st = [s["start"] for s in scenes]
    E = {"s1": st[1], "mail": at(1, "email,"), "cad": at(1, "caderno,"), "prog": at(1, "programa."), "s2": st[2],
         "en": at(3, "entrou,"), "fa": at(3, "falta"), "ft": at(3, "faturado."), "s4": st[4], "feito": at(4, "feito."), "s5": st[5], "site": at(5, "hivecode.pt.")}
    clip = lambda i, a, b, n: f'id="{i}" class="clip" data-start="{a:.3f}" data-duration="{b - a:.3f}" data-track-index="{n}"'  # noqa: E731
    html = (f'<div {clip("cnt", 0, E["s1"], 2)}><small>ENCOMENDAS HOJE</small><b id="num">12</b></div>'
            + "".join(f'<div class="nt" {clip(f"n{i}", 0, E["s1"], 3 + i)} style="top:{690 + i * 110}px"><span>✉ {a}</span><i>{b}</i></div>' for i, (a, b) in enumerate(NOTES))
            + f'<div class="wd" {clip("w0", E["mail"], E["s2"] + .5, 6)}><div class="h">Email · 23 por ler</div><div class="b">Encomenda Sra. Rosa<br>RE: RE: encomenda?</div></div>'
            f'<div class="wd" {clip("w1", E["cad"], E["s2"] + .5, 7)}><div class="h">Stock · caderno</div><div class="b">Papel de embrulho: 3?<br>Velas: <s>12</s> 4</div></div>'
            f'<div class="wd" {clip("w2", E["prog"], E["s2"] + .5, 8)}><div class="h">Faturas · outro programa</div><div class="b">Fatura 2026/318<br>Por emitir: 9</div></div>'
            f'<div {clip("db", E["s2"] + .3, E["s4"], 9)}><div class="h"><img src="assets/logo_mark.svg" alt="">HiveCode Business · dezembro</div>'
            '<div class="tl"><div id="t0"><b>48</b>Entrou</div><div id="t1"><b>7</b>Falta</div><div id="t2"><b>41</b>Faturado</div></div>'
            '<div class="ls"><p>#1047 · Cabaz de Natal<span style="background:#F2B233">Em preparação</span></p>'
            f'<p>#1046 · Vale-oferta 50 €<span style="background:{GREEN}">Faturada</span></p><p>#1045 · Bolo-rei grande<span style="background:{GREEN}">Faturada</span></p></div></div>'
            f'<div {clip("jan", E["s4"], E["s5"], 10)}><div class="m">JANEIRO</div><div class="d">2</div></div><span {clip("stamp", E["feito"], E["s5"], 11)}>Fecho do ano ✓</span>'
            f'<div {clip("end", E["s5"], total, 12)}><span id="ring"></span><img id="logo" src="assets/logo_mark.svg" alt=""><div id="cta"><span>hivecode.pt</span></div></div>')
    js = f"""
const N = {{ v: 12 }};
tl.fromTo(N, {{ v: 12 }}, {{ v: 47, duration: E.s1 - .3, ease: "power1.in", onUpdate: () => {{ document.querySelector("#num").textContent = Math.round(N.v); }} }}, 0);
tl.fromTo("#cnt", {{ scale: 1 }}, {{ scale: 1.05, duration: .1, yoyo: true, repeat: Math.floor(E.s1 / .2), ease: "none" }}, 0);
[2, 1, 0].forEach((i, k) => tl.fromTo("#n" + i, {{ y: -120, opacity: 0, rotate: (k - 1) * 3 }}, {{ y: 0, opacity: 1, rotate: (k - 1) * 2, duration: .45, ease: "back.out(2)" }}, .3 + .5 * k));
[["#w0", E.mail, -5], ["#w1", E.cad, 4], ["#w2", E.prog, -3]].forEach(([id, a, r]) => {{
  tl.fromTo(id, {{ scale: .4, opacity: 0, rotate: 0 }}, {{ scale: 1, opacity: 1, rotate: r, duration: .45, ease: "back.out(2.2)" }}, a);
  tl.fromTo(id, {{ x: 0 }}, {{ x: 6, duration: .05, yoyo: true, repeat: Math.max(1, Math.floor((E.s2 - a - .5) / .05)), ease: "none", immediateRender: false }}, a + .5);
  tl.fromTo(id, {{ scale: 1, opacity: 1 }}, {{ scale: .2, opacity: 0, x: 0, duration: .45, ease: "power3.in", immediateRender: false }}, E.s2);
}});
tl.fromTo("#db", {{ scale: .6, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: .55, ease: "back.out(1.8)" }}, E.s2 + .3);
[[E.en, "{GREEN}"], [E.fa, "{RED}"], [E.ft, "{INK}"]].forEach(([a, c], i) => {{
  tl.fromTo(`#t${{i}}`, {{ backgroundColor: "#f3efe6", color: "#5d7569" }}, {{ backgroundColor: c, color: "#fff", duration: .15, immediateRender: false }}, a);
  tl.fromTo(`#t${{i}} b`, {{ color: "{INK}" }}, {{ color: "#fff", duration: .15, immediateRender: false }}, a);
  tl.fromTo(`#t${{i}}`, {{ scale: 1 }}, {{ scale: 1.1, duration: .15, yoyo: true, repeat: 1, immediateRender: false }}, a);
}});
tl.fromTo("#jan", {{ rotateX: -90, transformPerspective: 1200, transformOrigin: "50% 0" }}, {{ rotateX: 0, duration: .6, ease: "back.out(1.6)" }}, E.s4);
tl.fromTo("#stamp", {{ scale: 2.2, rotate: -20, opacity: 0 }}, {{ scale: 1, rotate: -8, opacity: 1, duration: .25, ease: "power4.in" }}, E.feito - .2);
tl.fromTo("#logo", {{ scale: 2.2, rotate: -90, opacity: 0 }}, {{ scale: 1, rotate: 0, opacity: 1, duration: .55, ease: "expo.out" }}, E.s5 + .05);
tl.fromTo("#ring", {{ scale: .4, opacity: .95 }}, {{ scale: 2.2, opacity: 0, duration: .7, ease: "power3.out" }}, E.s5 + .4);
tl.fromTo("#cta", {{ scale: .5, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: .45, ease: "back.out(2.4)" }}, E.site);
"""
    hits = [("pop", .3), ("pop", .8), ("pop", 1.3), ("whoosh", E["s1"]), ("error", E["mail"]), ("error", E["cad"]), ("error", E["prog"]),
            ("rise", E["s2"]), ("pop", E["s2"] + .3), ("click", E["en"]), ("click", E["fa"]), ("click", E["ft"]), ("pop", E["s4"]),
            ("thump", E["feito"]), ("pop", E["s5"] + .1), ("pop", E["site"])]
    hfkit.build("2026-12-10-business-dezembro", HERE.parent / "hf", theme="natal", total=total, html=html, css=CSS, js=js, ev=E,
                scenes=scenes, voice=WORK / "voz.mp3", hits=hits, out_mp4=HERE / "reel-hf.mp4", cover=E["s4"] - .3)


if __name__ == "__main__":
    main()
