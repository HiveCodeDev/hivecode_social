"""HyperFrames version of the 12/12 reel "Antes e depois: florista" (natalverde theme, fictitious). Same voice text as build.py.

python posts/2026-12-12-florista-natal/reel/build_hf.py   -> reel-hf.mp4, cover-hf.jpg
Frame 0: the card with a gold wipe swinging between ANTES (paper order notes, ringing phone) and DEPOIS (the shop
site). Antes holds while it is told, the wipe opens on Depois; a pickup-time sheet is picked and paid; late-night
orders drop in under a moon; logo slam and the site.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import hfkit  # noqa: E402
import reelkit  # noqa: E402
from build import CSS as OLD_CSS, ORDERS, PRODUCTS, SCENES, WORK  # noqa: E402

PINE, GOLD, RED = "#0F3A2C", "#E8B84A", "#C41E3A"
KEEP = ("#card>div", "#site", "#paper", "#ring", ".tag", "#tA", "#tD", "#slot", "#pay", ".or")
CSS = "\n".join(l for l in OLD_CSS.splitlines() if l.startswith(KEEP)).replace("opacity:0;", "").replace("opacity:0}", "}") + f"""
#card{{position:absolute;left:160px;top:400px;width:760px;height:640px;border-radius:40px;overflow:hidden;box-shadow:0 60px 120px -40px rgba(0,0,0,.6)}}
#site .gr{{display:grid;grid-template-columns:1fr 1fr;gap:16px;padding:20px 28px}}
#site .pr{{border-radius:20px;background:#f4f1e8;padding:14px 18px 16px;color:{PINE}}}
#site .pr i{{display:grid;place-items:center;height:86px;border-radius:14px;background:#e3ecdf;font-style:normal;font-size:60px}}
#site .pr b{{display:block;margin-top:8px;font-size:26px;line-height:1.1}}
#site .pr em{{display:block;margin-top:4px;font-style:normal;font-size:28px;font-weight:800;color:{RED}}}
#paper p{{margin:0;padding:0 46px;font-size:48px;line-height:60px}}
#paper p:first-child{{padding-top:110px}}
#line{{position:absolute;top:0;bottom:0;left:0;width:8px;margin-left:-4px;background:{GOLD};z-index:4}}
#slot{{position:absolute;left:190px;top:760px;width:700px}}
.or{{position:absolute;left:150px;width:780px}}
#moon{{position:absolute;left:800px;top:330px;font-size:100px}}
#ring2{{position:absolute;left:340px;top:420px;width:400px;height:400px;border-radius:50%;border:8px solid {GOLD}}}
#logo{{position:absolute;left:420px;top:500px;width:240px;height:240px;filter:brightness(0) invert(1)}}
#cta{{position:absolute;left:0;right:0;top:800px;display:flex;justify-content:center}}
#cta span{{padding:30px 60px;border-radius:999px;background:{GOLD};color:{PINE};font-size:56px;font-weight:800}}
"""


def main():
    total, scenes = reelkit.voice(SCENES, WORK / "voz.mp3")
    at = lambda s, w: reelkit.at(scenes, s, w)  # noqa: E731
    st = [s["start"] for s in scenes]
    E = {"s1": st[1], "tel": at(1, "telefone"), "s2": st[2], "s3": st[3], "hora": at(3, "hora"), "online": at(3, "online."),
         "s4": st[4], "porta": at(4, "porta."), "s5": st[5], "site": at(5, "hivecode.pt.")}
    clip = lambda i, a, b, n: f'id="{i}" class="clip" data-start="{a:.3f}" data-duration="{b - a:.3f}" data-track-index="{n}"'  # noqa: E731
    html = (f'<div {clip("card", 0, E["s4"] + .1, 2)}><div id="site"><div class="hd">Flores da Ribeira<span>Encomendas</span></div>'
            '<div class="bn">🎄 Especial Natal</div><div class="gr">'
            + "".join(f'<div class="pr"><i>{e}</i><b>{n}</b><em>{p}</em></div>' for e, n, p in PRODUCTS)
            + '</div><span class="tag" id="tD">DEPOIS</span></div>'
            '<div id="paper"><p>Sra. Rosa: coroa, sexta?</p><p>Arranjo mesa, 25 € ??</p><p><s>ligar ao Sr. Paulo</s></p>'
            '<p>Ramo… vermelho ou branco?</p><p>Recolhe às 15h? 16h?</p><i id="ring">📞</i><span class="tag" id="tA">ANTES</span></div><span id="line"></span></div>'
            f'<div {clip("slot", E["s3"], E["s4"], 3)}><small>RECOLHA · SEXTA, 18 DE DEZEMBRO</small><div class="ch"><span>10h</span><span>12h</span><span id="h15">15h</span></div>'
            '<div id="pay">Pagar 35 €</div></div>'
            + "".join(f'<div class="or" {clip(f"o{i}", E["s4"], E["s5"], 4 + i)} style="top:{430 + i * 170}px"><i>{h}</i>Nova encomenda: {n}</div>' for i, (h, n) in enumerate(ORDERS))
            + f'<span {clip("moon", E["s4"], E["s5"], 7)}>🌙</span>'
            f'<div {clip("end", E["s5"], total, 8)}><span id="ring2"></span><img id="logo" src="assets/logo_mark.svg" alt=""><div id="cta"><span>hivecode.pt</span></div></div>')
    js = """
const W = { w: 50 };
const paint = () => { document.querySelector("#paper").style.clipPath = `inset(0 ${100 - W.w}% 0 0)`;
  const l = document.querySelector("#line"); l.style.left = W.w + "%"; l.style.opacity = W.w > 1 && W.w < 99 ? 1 : 0; };
tl.fromTo("#card", { scale: .7, opacity: 0 }, { scale: 1, opacity: 1, duration: .5, ease: "back.out(1.7)" }, 0);
tl.fromTo(W, { w: 50 }, { w: 15, duration: .45, ease: "sine.inOut", onUpdate: paint }, .1);
tl.fromTo(W, { w: 15 }, { w: 85, duration: .7, ease: "sine.inOut", onUpdate: paint, immediateRender: false }, .55);
tl.fromTo(W, { w: 85 }, { w: 100, duration: .4, ease: "power2.out", onUpdate: paint, immediateRender: false }, E.s1 - .2);
tl.fromTo("#ring", { rotate: -14 }, { rotate: 14, duration: .05, yoyo: true, repeat: Math.floor((E.s2 - E.tel) / .05), ease: "none" }, E.tel);
tl.fromTo(W, { w: 100 }, { w: 0, duration: .8, ease: "power3.inOut", onUpdate: paint, immediateRender: false }, E.s2);
tl.fromTo("#site .pr", { scale: .8, opacity: 0 }, { scale: 1, opacity: 1, duration: .35, stagger: .1, ease: "back.out(2)" }, E.s2 + .5);
tl.fromTo("#slot", { y: 300, opacity: 0 }, { y: 0, opacity: 1, duration: .5, ease: "back.out(1.6)" }, E.s3);
tl.fromTo("#h15", { backgroundColor: "#fff", color: "#0F3A2C" }, { backgroundColor: "#0F3A2C", color: "#E8B84A", duration: .15, immediateRender: false }, E.hora);
tl.fromTo("#pay", { backgroundColor: "#0F3A2C" }, { backgroundColor: "#C41E3A", duration: .15, immediateRender: false }, E.online);
const P = { v: 0 };
tl.fromTo(P, { v: 0 }, { v: 1, duration: .01, onUpdate: () => { document.querySelector("#pay").textContent = P.v > .5 ? "Pago ✓" : "Pagar 35 €"; } }, E.online);
tl.fromTo("#card", { opacity: 1 }, { opacity: 0, y: -100, duration: .3, ease: "power2.in", immediateRender: false }, E.s4 - .2);
tl.fromTo("#moon", { scale: 0, rotate: -40 }, { scale: 1, rotate: 0, duration: .5, ease: "back.out(2)" }, E.s4);
[E.s4 + .2, E.s4 + .7, E.porta].forEach((a, i) => tl.fromTo("#o" + i, { x: 600, opacity: 0 }, { x: 0, opacity: 1, duration: .45, ease: "expo.out" }, a));
tl.fromTo("#logo", { scale: 2.2, rotate: -90, opacity: 0 }, { scale: 1, rotate: 0, opacity: 1, duration: .55, ease: "expo.out" }, E.s5 + .05);
tl.fromTo("#ring2", { scale: .4, opacity: .95 }, { scale: 2.2, opacity: 0, duration: .7, ease: "power3.out" }, E.s5 + .4);
tl.fromTo("#cta", { scale: .5, opacity: 0 }, { scale: 1, opacity: 1, duration: .45, ease: "back.out(2.4)" }, E.site);
"""
    hits = [("pop", .05), ("whoosh", .4), ("whoosh", 1.0), ("click", E["tel"]), ("click", E["tel"] + .25), ("rise", E["s2"]), ("pop", E["s3"]),
            ("click", E["hora"]), ("thump", E["online"]), ("pop", E["s4"] + .2), ("pop", E["s4"] + .7), ("pop", E["porta"]), ("pop", E["s5"] + .1), ("pop", E["site"])]
    hfkit.build("2026-12-12-florista-natal", HERE.parent / "hf", theme="natalverde", total=total, html=html, css=CSS, js=js, ev=E,
                scenes=scenes, voice=WORK / "voz.mp3", hits=hits, out_mp4=HERE / "reel-hf.mp4", cover=E["s3"] + .3)


if __name__ == "__main__":
    main()
