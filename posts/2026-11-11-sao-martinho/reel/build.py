"""Reel "São Martinho: o seu restaurante aparece?" (websites), kraft theme, 1080x1920.

python posts/2026-11-11-sao-martinho/reel/build.py
Chestnuts fall, someone types "magusto perto de mim" on a phone, three (fictional) restaurants
show up and a dashed fourth slot for "o seu restaurante" stays empty with a red cross; with a
site it fills in and climbs to the top. Then logo and hivecode.pt.
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
    ("Dia de São Martinho.", 130, {"Martinho."}),
    ("Alguém pesquisa: magusto perto de mim.", 96, {"magusto"}),
    ("Aparecem três restaurantes.", 104, {"três"}),
    ("O seu não está lá.", 124, {"não"}),
    ("Hoje, quem não aparece na pesquisa não entra na escolha.", 86, {"pesquisa"}),
    ("Um site rápido e bem feito ajuda o seu negócio a ser encontrado.", 82, {"encontrado."}),
    ("Saiba mais em hivecode.pt.", 100, {"hivecode.pt."}),
]
QUERY = "magusto perto de mim"
RESULTS = [("Tasca do Largo", "4,7", "350 m"), ("Adega Velha", "4,5", "600 m"), ("Casa das Castanhas", "4,6", "900 m")]

CSS = """
.nut{left:0;top:0;opacity:0}
#ph{left:200px;top:760px;width:680px;height:1060px;box-sizing:border-box;padding:70px 34px 0;border-radius:80px;background:#fff;border:16px solid #2B1B12;opacity:0;overflow:hidden;box-shadow:0 60px 120px -40px rgba(43,27,18,.7)}
#q{display:flex;align-items:center;gap:16px;padding:22px 26px;border-radius:999px;background:#f3ede4;font-size:34px;color:#2B1B12;height:44px}
#q i{width:3px;height:40px;background:#8E1F35}
.res{position:absolute;left:34px;right:34px;height:150px;box-sizing:border-box;padding:24px 28px;border-radius:26px;background:#f7f2ea;opacity:0}
.res b{display:block;font-size:36px;color:#2B1B12}.res small{font-size:28px;color:#7a5c45}
.res .img{position:absolute;right:24px;top:24px;width:102px;height:102px;border-radius:18px;background:linear-gradient(140deg,#c9a77b,#8a5a33)}
#mine{border:5px dashed #8E1F35;background:transparent}
#mine b{color:#8E1F35}
#x{position:absolute;right:30px;top:30px;width:90px;height:90px;border-radius:50%;background:#8E1F35;color:#fff;display:grid;place-items:center;font-size:56px;font-weight:800;opacity:0}
#logo{left:440px;top:930px;width:200px;height:200px;opacity:0}
#cta{left:88px;right:88px;top:1220px;display:flex;justify-content:center;opacity:0}
#cta span{padding:32px 56px;border-radius:999px;background:#2B1B12;color:#F3EBDD;font-size:46px;font-weight:600}
"""

NUT = ('<svg viewBox="0 0 100 100" width="120" height="120"><path d="M50 6C22 28 6 58 16 80c12 16 56 16 68 0C94 58 78 28 50 6Z" fill="#6B3A1E"/>'
       '<path d="M16 80c12 16 56 16 68 0-4 10-64 10-68 0Z" fill="#C9A77B"/><path d="M38 24c-6 10-10 22-10 34" stroke="#8a5434" stroke-width="5" fill="none" stroke-linecap="round"/></svg>')
NUTS = [(80, 0), (330, .3), (600, .1), (860, .45), (200, .6), (720, .75)]
ART = "".join(f'<span class="nut" id="n{i}">{NUT}</span>' for i in range(len(NUTS))) + \
    '<div id="ph"><div id="q"><span>🔍</span><span id="qt"></span><i id="caret"></i></div>' + \
    "".join(f'<div class="res" id="r{i}"><b>{n}</b><small>★ {s} · {d}</small><span class="img"></span></div>' for i, (n, s, d) in enumerate(RESULTS)) + \
    '<div class="res" id="mine"><b>O seu restaurante</b><small>sem site</small><span id="x">✕</span></div></div>' + \
    f'<img id="logo" src="{ASSETS}/logo_mark.svg" alt=""><div id="cta"><span>hivecode.pt</span></div>'

ART_JS = f"const NUTS = {[list(n) for n in NUTS]}, Q = {QUERY!r};" + r"""
function art(t, E) {
  NUTS.forEach(([x, d], i) => {
    const p = t - d, el = $('#n' + i), y = 520 + 700 * p * p, out = cl((t - E.s2 + .3) / .4);
    el.style.opacity = cl(p / .1) * (1 - out);
    el.style.transform = `translate(${x}px,${Math.min(y, 1650 - 60 * i)}px) rotate(${p * 200 * (i % 2 ? 1 : -1)}deg)`;
  });
  stage($('#ph'), t, E.s2 - .2, E.s7);
  const n = Math.max(0, Math.min(Q.length, Math.floor((t - E.s2 - .1) * 16)));
  $('#qt').textContent = Q.slice(0, n);
  $('#caret').style.opacity = Math.floor(t * 3) % 2 && t < E.s3 ? 1 : 0;
  // Results slide in; the empty slot for "o seu restaurante" stays below until the site arrives.
  const climb = ease((t - E.found) / .8);
  [0, 1, 2].forEach(i => {
    const el = $('#r' + i), k = back((t - E.tres - .25 * i) / .45);
    el.style.opacity = cl((t - E.tres - .25 * i) / .1);
    el.style.top = `${170 + 175 * (i + climb)}px`;
    el.style.transform = `scale(${k})`;
  });
  const m = $('#mine');
  m.style.opacity = cl((t - E.s4) / .15);
  m.style.top = `${170 + 175 * 3 * (1 - climb)}px`;
  m.style.transform = `translateX(${t > E.nao && t < E.nao + .4 ? 14 * Math.sin(t * 70) : 0}px)`;
  const fixed = t > E.found;
  m.style.borderStyle = fixed ? 'solid' : 'dashed';
  m.style.background = fixed ? '#fff' : 'transparent';
  m.querySelector('small').textContent = fixed ? '★ 4,8 · 200 m · Site' : 'sem site';
  const x = $('#x'); x.style.opacity = fixed ? 0 : cl((t - E.nao) / .1);
  x.style.transform = `scale(${back((t - E.nao) / .35)})`;
  $('#ph').style.filter = `saturate(${1 - .6 * cl((t - E.s5) / .3) * (1 - cl((t - E.s6) / .3))})`;
  const lg = back((t - E.s7 - .1) / .5);
  $('#logo').style.opacity = cl((t - E.s7 - .1) / .1);
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
    ev = {"s2": st[1], "s3": st[2], "tres": at(2, "três"), "s4": st[3], "nao": at(3, "não"), "s5": st[4], "s6": st[5],
          "found": at(5, "site") + .2, "s7": st[6], "site": at(6, "hivecode.pt.")}
    page = HERE / "reel.html"
    page.write_text(reelkit.page(scenes, ev, ART, CSS, ART_JS, theme="kraft"), encoding="utf-8")
    hits = [("pop", d + .05) for _, d in NUTS] + [("whoosh", ev["s2"] - .2)]
    hits += [("click", ev["s2"] + .1 + i / 16) for i in range(0, len(QUERY), 2)]
    hits += [("pop", ev["tres"] + .25 * i) for i in range(3)] + [("error", ev["nao"])]
    hits += [("rise", ev["found"] - .3), ("pop", ev["found"] + .6), ("pop", ev["s7"] + .15), ("pop", ev["site"])]
    reelkit.render(page, WORK, total, WORK / "voz.mp3", hits, HERE / "reel.mp4")
    reelkit.cover(HERE / "reel.mp4", ev["nao"] + .8, HERE / "cover.jpg")
    print(f"reel.mp4 {total:.1f}s")


if __name__ == "__main__":
    main()
