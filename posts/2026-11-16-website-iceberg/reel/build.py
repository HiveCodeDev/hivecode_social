"""Reel "Um website não é só um website" (websites), forest theme, 1080x1920.

python posts/2026-11-16-website-iceberg/reel/build.py
An iceberg: above the water only "Website"; the camera dives and each layer below lights up as the
voice names it (domain, email, hosting, backups, responsive design, CTA, SEO, speed, SSL, GDPR,
forms, analytics, accessibility, maintenance). Then it zooms out to the whole iceberg, logo, CTA.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import reelkit  # noqa: E402
from build_week import ASSETS  # noqa: E402

WORK = ROOT / "reels" / HERE.parent.name
WORK.mkdir(parents=True, exist_ok=True)

SCENES = [
    ("Um website não é só um website.", 120, {"só"}),
    ("É o domínio e o email profissional.", 100, {"domínio", "email"}),
    ("O alojamento e as cópias de segurança.", 100, {"alojamento", "cópias"}),
    ("O design, pensado para computador e telemóvel.", 96, {"design,"}),
    ("Os botões de ação, para o cliente saber o que fazer a seguir.", 84, {"botões", "ação,"}),
    ("O SEO, para aparecer no Google.", 104, {"SEO,"}),
    ("A velocidade e o certificado de segurança.", 96, {"velocidade", "certificado"}),
    ("O RGPD: política de privacidade e cookies.", 96, {"RGPD:"}),
    ("Os formulários, as estatísticas e a acessibilidade.", 88, {"formulários,", "estatísticas", "acessibilidade."}),
    ("E a manutenção, para nunca parar no tempo.", 96, {"manutenção,"}),
    ("Na HiveCode tratamos de tudo. Mockup e orçamento gratuitos em hivecode.pt.", 80, {"tudo.", "gratuitos"}),
]
# label, scene index, trigger word
LAYERS = [
    ("Domínio", 1, "domínio"), ("Email profissional", 1, "email"),
    ("Alojamento", 2, "alojamento"), ("Cópias de segurança", 2, "cópias"),
    ("Design responsivo", 3, "design,"), ("CTA · botões de ação", 4, "botões"),
    ("SEO", 5, "SEO,"), ("Velocidade", 6, "velocidade"), ("SSL · ligação segura", 6, "certificado"),
    ("RGPD e cookies", 7, "RGPD:"), ("Formulários", 8, "formulários,"), ("Estatísticas", 8, "estatísticas"),
    ("Acessibilidade", 8, "acessibilidade."), ("Manutenção", 9, "manutenção,"),
]
TOP, STEP = 470, 128           # world y of the first layer, spacing
WATER = 330                    # world y of the waterline
DEPTH = TOP + STEP * len(LAYERS) + 120

CSS = f"""
#view{{left:0;top:760px;width:1080px;height:1160px;overflow:hidden}}
#world{{position:absolute;left:0;top:0;width:1080px;height:{DEPTH}px;transform-origin:540px 0}}
#sea{{position:absolute;left:0;right:0;top:{WATER}px;height:{DEPTH}px;background:linear-gradient(180deg,rgba(6,30,24,.55),rgba(3,18,14,.95));border-top:4px solid rgba(243,239,230,.7)}}
#berg{{position:absolute;left:0;top:0;width:1080px;height:{DEPTH}px}}
.lay{{position:absolute;left:0;right:0;display:flex;justify-content:center;opacity:.18}}
.lay span{{padding:16px 34px;border-radius:999px;background:rgba(243,239,230,.12);border:2px solid rgba(243,239,230,.35);color:#F3EFE6;font-size:40px;font-weight:700;white-space:nowrap}}
.lay.on{{opacity:1}}
.lay.on span{{background:#F4C542;border-color:#F4C542;color:#0F3D2E}}
#tip{{position:absolute;left:0;right:0;top:150px;text-align:center;font-size:76px;font-weight:700;color:#0F3D2E}}
#logo{{left:440px;top:930px;width:200px;height:200px;opacity:0;filter:brightness(0) invert(1)}}
#cta{{left:88px;right:88px;top:1220px;display:flex;justify-content:center;opacity:0}}
#cta span{{padding:32px 56px;border-radius:999px;background:#F4C542;color:#0F3D2E;font-size:46px;font-weight:700}}
"""

# Iceberg outline: small tip above the water, a much wider body below.
BERG = (f'<svg id="berg" viewBox="0 0 1080 {DEPTH}"><path d="M470 70 L610 60 L700 200 L760 {WATER} L960 {WATER + 260} L1010 {DEPTH * .55:.0f} '
        f'L930 {DEPTH - 180} L700 {DEPTH - 40} L380 {DEPTH - 60} L140 {DEPTH - 220} L70 {DEPTH * .5:.0f} L150 {WATER + 220} L330 {WATER} L390 200 Z" '
        f'fill="rgba(232,241,238,.13)" stroke="rgba(243,239,230,.55)" stroke-width="4"/>'
        f'<path d="M470 70 L610 60 L700 200 L760 {WATER} L330 {WATER} L390 200 Z" fill="#E8F1EE"/></svg>')
ART = ('<div id="view"><div id="world"><div id="sea"></div>' + BERG + '<div id="tip">Website</div>'
       + "".join(f'<div class="lay" id="l{i}" style="top:{TOP + STEP * i}px"><span>{t}</span></div>' for i, (t, _, _) in enumerate(LAYERS))
       + f'</div></div><img id="logo" src="{ASSETS}/logo_mark.svg" alt=""><div id="cta"><span>hivecode.pt</span></div>')

ART_JS = f"const TOP = {TOP}, STEP = {STEP}, DEPTH = {DEPTH}, N = {len(LAYERS)};" + r"""
function art(t, E) {
  stage($('#view'), t, .15, E.end);
  // Camera: follows the newest lit layer, keeping it around the middle of the view.
  let lit = -1;
  E.L.forEach((a, i) => { if (t > a) lit = i; $('#l' + i).className = 'lay' + (t > a ? ' on' : ''); });
  E.L.forEach((a, i) => { $('#l' + i).style.transform = `scale(${t > a && t < a + .35 ? back((t - a) / .35) : 1})`; });
  const follow = i => Math.max(0, TOP + STEP * i - 520);
  let y = 0;
  for (let i = 0; i < N; i++) { const k = ease((t - E.L[i] + .25) / .5); y = y + (follow(i) - y) * k; }
  // Before the first layer the camera stays on the tip, so "Website" reads whole above the water.
  y = Math.min(y, follow(N - 1));
  // Zoom out at the end to show the whole iceberg.
  const z = ease((t - E.s11) / .9), s = 1 - (1 - 1160 / DEPTH) * z;
  $('#world').style.transform = `translateY(${-y * (1 - z)}px) scale(${s})`;
  const lg = back((t - E.end - .1) / .5);
  $('#logo').style.opacity = cl((t - E.end - .1) / .1);
  $('#logo').style.transform = `rotate(${-120 * (1 - lg)}deg) scale(${lg})`;
  const ct = back((t - E.site) / .45);
  $('#cta').style.opacity = cl((t - E.site) / .1);
  $('#cta').style.transform = `scale(${ct})`;
}
"""


def main():
    total, scenes = reelkit.voice(SCENES, WORK / "voz.mp3")
    at = lambda s, w: reelkit.at(scenes, s, w)  # noqa: E731
    st = [s["start"] for s in scenes]
    ev = {"so": at(0, "só"), "L": [at(s, w) for _, s, w in LAYERS], "s11": st[10], "end": at(10, "Mockup"),
          "site": at(10, "hivecode.pt.")}
    page = HERE / "reel.html"
    page.write_text(reelkit.page(scenes, ev, ART, CSS, ART_JS, theme="forest"), encoding="utf-8")
    hits = [("pop", .15), ("whoosh", ev["so"])] + [("click", a) for a in ev["L"]]
    hits += [("rise", ev["s11"]), ("pop", ev["end"] + .1), ("pop", ev["site"])]
    reelkit.render(page, WORK, total, WORK / "voz.mp3", hits, HERE / "reel.mp4")
    reelkit.cover(HERE / "reel.mp4", ev["s11"] + 1.0, HERE / "cover.jpg")
    print(f"reel.mp4 {total:.1f}s")


if __name__ == "__main__":
    main()
