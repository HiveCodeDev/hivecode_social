"""Reel "Tudo num só lugar" (HiveCode Business), 1080x1920.

python posts/2026-10-12-tudo-num-so-lugar/reel/build.py
One continuous voice take (Duarte); every move is keyed to the time a word is said:
the scattered tools pop in on their nouns, shake while the problem is named, get pulled
into one dashboard on "junta", and each module lights up as it is said.
Frames, voice and sound effects go to reels/ (not versioned); reel.html and reel.mp4 stay here.
"""
import json
import math
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from build_week import ASSETS, BASE_CSS  # noqa: E402
from voice import say  # noqa: E402

WORK = ROOT / "reels" / HERE.parent.name
WORK.mkdir(parents=True, exist_ok=True)
FPS, HOLD = 30, 1.4

# (scene text, font size, emphasised tokens); the voice reads them as one take.
SCENES = [
    ("Clientes no Excel, encomendas no email, stock num caderno.", 92, {"Excel,", "email,", "caderno."}),
    ("Parece familiar? Perde-se tempo e perdem-se vendas.", 96, {"vendas."}),
    ("A HiveCode junta tudo num só sistema, feito à medida da sua empresa.", 80, {"só", "sistema,"}),
    ("Clientes, encomendas, stock e faturação, num só lugar.", 88, {"lugar."}),
    ("Saiba mais em hivecode.pt/business.", 76, {"hivecode.pt/business."}),
]

CSS = """
html,body{width:1080px;height:1920px}
.top{position:absolute;left:88px;right:88px;top:150px;display:flex;justify-content:space-between;align-items:center;font-size:28px;color:var(--muted);z-index:5}
.txt{position:absolute;left:88px;width:904px;top:300px;font-weight:600;line-height:1.08;letter-spacing:-.025em;z-index:4}
.txt .w{display:inline-block;opacity:0;margin-right:.24em}
.txt .w.em{color:var(--violet)}
#art{position:absolute;inset:0;transform-origin:540px 1140px}
#art>*{position:absolute}
.card{border-radius:26px;background:#1b1638;border:1px solid rgba(255,255,255,.16);box-shadow:0 40px 80px -30px rgba(0,0,0,.8);overflow:hidden;opacity:0}
.card .hd{height:56px;display:flex;align-items:center;gap:12px;padding:0 22px;font-size:24px;font-weight:500;color:var(--soft);border-bottom:1px solid rgba(255,255,255,.1)}
.bar{display:block;height:16px;border-radius:8px;background:rgba(255,255,255,.14)}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;padding:20px 22px}
.grid i{height:26px;border-radius:6px;background:rgba(255,255,255,.08)}
.grid i.h{background:rgba(47,191,113,.45)}
.row{display:flex;align-items:center;gap:14px;padding:16px 22px;border-bottom:1px solid rgba(255,255,255,.06)}
.row b{width:16px;height:16px;border-radius:50%;background:var(--blue);flex:none}
.badge{position:absolute;top:-18px;right:-18px;width:58px;height:58px;border-radius:50%;background:#ff4d6d;color:#fff;font-size:28px;font-weight:700;display:grid;place-items:center;box-shadow:0 0 0 6px rgba(255,77,109,.2)}
.nb{background:repeating-linear-gradient(#f3efe2 0 46px,#c9d6f0 46px 48px);border-radius:14px;color:#2a2550;padding:70px 34px 0;font-size:40px;font-weight:500;font-style:italic;box-shadow:0 40px 80px -30px rgba(0,0,0,.8);opacity:0}
.nb:before{content:"";position:absolute;left:24px;right:24px;top:18px;height:18px;background:radial-gradient(circle,#4a4478 6px,transparent 7px) 0 0/40px 18px repeat-x}
.postit{width:230px;height:210px;background:#ffd84d;color:#2a2550;font-size:34px;font-weight:600;padding:30px 24px;line-height:1.15;box-shadow:0 30px 60px -20px rgba(0,0,0,.7);opacity:0}
.clock{width:170px;height:170px;border-radius:50%;border:8px solid #f3f1fb;background:#1b1638;opacity:0}
.clock i{position:absolute;left:50%;bottom:50%;width:8px;margin-left:-4px;border-radius:4px;background:#f3f1fb;transform-origin:50% 100%}
#db{left:88px;top:850px;width:904px;height:590px;border-radius:30px;background:#18132f;border:1px solid rgba(215,82,254,.5);display:flex;overflow:hidden;opacity:0}
#db .side{width:150px;background:#120f26;display:flex;flex-direction:column;align-items:center;gap:26px;padding-top:32px}
#db .side img{width:62px;height:62px}
#db .side .bar{width:70px}
#db .main{flex:1;padding:30px 32px;display:flex;flex-direction:column;gap:24px}
#db .ttl{font-size:32px;font-weight:600}
#db .tiles{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:22px}
.tile{border-radius:22px;background:#1f1940;border:2px solid rgba(255,255,255,.08);padding:24px 26px;display:flex;flex-direction:column;justify-content:space-between;opacity:.35}
.tile .lb{display:flex;align-items:center;gap:14px;font-size:28px;color:var(--soft)}
.tile .val{font-size:58px;font-weight:700;letter-spacing:-.02em}
#logo{left:440px;top:930px;width:200px;height:200px;opacity:0}
#cta{left:88px;right:88px;top:1220px;display:flex;justify-content:center;opacity:0}
#cta span{padding:32px 54px;border-radius:999px;background:#265ADF;font-size:44px;font-weight:600;box-shadow:0 30px 70px -20px rgba(72,119,254,.8)}
"""

ICONS = {
    "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c.8-3.6 3.3-5.5 6.5-5.5s5.7 1.9 6.5 5.5M16 4.8a3.5 3.5 0 0 1 0 6.4M18.5 14.8c1.6.8 2.6 2.5 3 5.2"/>',
    "box": '<path d="M3 7.5 12 3l9 4.5v9L12 21l-9-4.5z"/><path d="M3 7.5 12 12l9-4.5M12 12v9"/>',
    "layers": '<path d="m12 3 9 5-9 5-9-5z"/><path d="m3 13 9 5 9-5"/>',
    "euro": '<path d="M17 6.5A7 7 0 1 0 17 17.5M4 10h9M4 14h9"/>',
}


def icon(name, color="currentColor"):
    return (f'<svg viewBox="0 0 24 24" width="40" height="40" fill="none" stroke="{color}" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>')


TILES = [("users", "Clientes", 248), ("box", "Encomendas", 36), ("layers", "Stock", 1204), ("euro", "Faturação", 12480)]

ART = f"""<div id="art">
<div class="card" id="xl" style="left:100px;top:860px;width:430px;height:300px"><div class="hd"><i style="width:18px;height:18px;border-radius:4px;background:#2fbf71"></i>clientes.xlsx</div>
<div class="grid">{"".join(f'<i class="{"h" if n < 4 else ""}"></i>' for n in range(20))}</div></div>
<div class="card" id="em" style="left:560px;top:930px;width:420px;height:290px"><div class="hd">Caixa de entrada</div>
<div class="row"><b></b><span style="font-size:26px;font-weight:600">Encomenda nº 214</span></div>
<div class="row"><b style="background:var(--muted)"></b><span class="bar" style="width:70%"></span></div>
<div class="row"><b style="background:var(--muted)"></b><span class="bar" style="width:55%"></span></div></div>
<div class="nb" id="nb" style="left:300px;top:1150px;width:370px;height:320px">Stock:<br>12? 15?</div>
<div class="postit" id="pi" style="left:740px;top:1250px">Ligar ao cliente!</div>
<div class="clock" id="ck" style="left:110px;top:1240px"><i id="hh" style="height:44px"></i><i id="mh" style="height:62px;width:6px;margin-left:-3px"></i></div>
<span class="badge" id="b1" style="left:490px;top:842px">1</span>
<span class="badge" id="b2" style="left:940px;top:912px">1</span>
<div id="db"><div class="side"><img src="{ASSETS}/logo_side.png" alt=""><span class="bar"></span><span class="bar"></span><span class="bar"></span></div>
<div class="main"><div class="ttl">A sua empresa</div><div class="tiles">
{"".join(f'<div class="tile"><span class="lb">{icon(i)}{label}</span><span class="val" data-v="{v}">0</span></div>' for i, label, v in TILES)}
</div></div></div>
<img id="logo" src="{ASSETS}/logo_side.png" alt="">
<div id="cta"><span>hivecode.pt/business</span></div>
</div>"""

SEEK_JS = r"""
const T = __T__, E = T.ev;
const cl = x => Math.min(Math.max(x, 0), 1);
const ease = x => 1 - Math.pow(1 - cl(x), 3);
const back = x => { x = cl(x); const c = 1.9; return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); };
const $ = s => document.querySelector(s);
const blocks = [...document.querySelectorAll('.txt')];
const fmt = n => String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
const glows = [...document.querySelectorAll('.glow')];
// Scattered tools: [id, appears at, base rotation, wobble phase]
const MESS = [['#xl', E.excel, -6, 0], ['#em', E.email, 5, 1.7], ['#nb', E.caderno, -3, 3.1], ['#pi', E.perde, 8, .6], ['#ck', E.tempo, 0, 2.3]];
const CX = 540, CY = 1140;

window.seek = t => {
  glows[0].style.transform = `translate(${40 * Math.sin(t * .5)}px,${30 * Math.cos(t * .4)}px)`;
  glows[1].style.transform = `translate(${-50 * Math.sin(t * .35)}px,${40 * Math.cos(t * .45)}px)`;

  // Text: each word pops as it is said; the block lifts away when its scene ends.
  T.scenes.forEach((s, i) => {
    const b = blocks[i], out = ease((t - s.end) / .25);
    b.style.display = t >= s.start && (t < s.end + .25 || i === T.scenes.length - 1) ? 'block' : 'none';
    b.style.opacity = i === T.scenes.length - 1 ? 1 : 1 - out;
    b.style.transform = `translateY(${-70 * out}px)`;
    b.querySelectorAll('.w').forEach(w => {
      const k = back((t - +w.dataset.s + .08) / .32);
      w.style.opacity = cl((t - +w.dataset.s + .08) / .1);
      w.style.transform = `translateY(${34 * (1 - k)}px) scale(${.88 + .12 * k})`;
    });
  });

  // Camera: slow breathing zoom, and a nervous shake while the problem is named.
  const shake = cl((t - E.s2) / .4) * (1 - cl((t - E.junta) / .3));
  $('#art').style.transform = `translate(${6 * shake * Math.sin(t * 41)}px,${5 * shake * Math.cos(t * 37)}px) scale(${1.02 + .02 * Math.sin(t * .6)})`;

  // The mess: pops in on its noun, wobbles harder in scene 2, then is pulled into the centre.
  const pull = ease((t - E.junta) / .5);
  const amp = 2 + 4 * cl((t - E.s2) / .5);
  MESS.forEach(([sel, at, rot, ph]) => {
    const el = $(sel), k = back((t - at) / .45);
    const x0 = parseFloat(el.style.left) + el.offsetWidth / 2, y0 = parseFloat(el.style.top) + el.offsetHeight / 2;
    const dx = (CX - x0) * pull, dy = (CY - y0) * pull + 10 * Math.sin(t * 1.4 + ph) * (1 - pull);
    el.style.opacity = cl((t - at) / .1) * (1 - pull);
    el.style.transform = `translate(${dx}px,${dy}px) rotate(${(rot + amp * Math.sin(t * 2.2 + ph)) * (1 - pull)}deg) scale(${k * (1 - .8 * pull)})`;
  });
  $('#hh').style.transform = `rotate(${t * 240}deg)`;
  $('#mh').style.transform = `rotate(${t * 1400}deg)`;
  [['#b1', E.excel], ['#b2', E.email]].forEach(([sel, at], j) => {
    const el = $(sel), k = back((t - at - .35) / .35);
    el.style.opacity = cl((t - at - .35) / .1) * (1 - pull);
    el.style.transform = `translate(${(CX - parseFloat(el.style.left)) * pull}px,${(CY - parseFloat(el.style.top)) * pull}px) scale(${k * (1 - pull)})`;
    el.textContent = Math.max(1, Math.min(9, 1 + Math.floor(Math.max(0, t - at - .35) * (j ? 2.6 : 2))));
  });

  // The dashboard lands, each module lights up as it is said, then everything glows on "lugar".
  const land = back((t - E.junta - .3) / .55), gone = ease((t - E.s5) / .45);
  const db = $('#db'), glow = Math.max(0, 1 - Math.abs(t - E.lugar - .25) / .6);
  db.style.opacity = cl((t - E.junta - .3) / .15) * (1 - gone);
  db.style.transform = `translateY(${-140 * gone}px) scale(${(.7 + .3 * land) * (1 - .12 * gone)})`;
  db.style.boxShadow = `0 0 ${40 + 80 * glow}px rgba(215,82,254,${.25 + .45 * glow})`;
  document.querySelectorAll('.tile').forEach((tile, j) => {
    const at = E.mod[j], on = ease((t - at) / .3);
    tile.style.opacity = .35 + .65 * on;
    tile.style.borderColor = `rgba(215,82,254,${.08 + .7 * on})`;
    tile.style.background = `rgba(${31 + 20 * on},${25 + 8 * on},${64 + 40 * on},1)`;
    tile.style.transform = `scale(${1 + .06 * Math.max(0, 1 - Math.abs(t - at - .12) / .2)})`;
    const v = tile.querySelector('.val');
    v.textContent = fmt(+v.dataset.v * ease((t - at) / .7)) + (j === 3 ? ' €' : '');
  });

  // Close: logo pops, the address follows the voice and keeps a gentle pulse.
  const lg = back((t - E.s5 - .1) / .5);
  $('#logo').style.opacity = cl((t - E.s5 - .1) / .1);
  $('#logo').style.transform = `rotate(${-120 * (1 - lg)}deg) scale(${lg})`;
  const ct = back((t - E.site) / .45);
  $('#cta').style.opacity = cl((t - E.site) / .1);
  $('#cta').style.transform = `scale(${ct * (1 + .03 * Math.sin((t - E.site) * 5) * cl(t - E.site - .5))})`;
};
seek(0);
"""


def sfx():
    """Small synthesized sound effects (no third-party audio)."""
    lav = {
        "whoosh": ("anoisesrc=color=pink:duration=0.45:amplitude=0.5",
                   "highpass=f=500,lowpass=f=6000,afade=t=in:d=0.2,afade=t=out:st=0.2:d=0.25,volume=0.28"),
        "pop": ("sine=frequency=880:duration=0.09", "afade=t=out:st=0:d=0.09,volume=0.22"),
        "click": ("sine=frequency=1600:duration=0.05", "afade=t=out:st=0:d=0.05,volume=0.2"),
        "thump": ("sine=frequency=95:duration=0.3", "afade=t=out:st=0:d=0.3,volume=0.8"),
    }
    for name, (src, af) in lav.items():
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", src, "-af", af, str(WORK / f"{name}.wav")], check=True)


def main():
    text = " ".join(s for s, _, _ in SCENES)
    dur, words = say(text, WORK / "voz.mp3", rate="+8%")

    # Split the timed words back into scenes and find the moments the animation keys on.
    scenes, i = [], 0
    for s, size, em in SCENES:
        n = len(s.split())
        scenes.append({"words": words[i:i + n], "size": size, "em": em})
        i += n
    for k, s in enumerate(scenes):
        s["start"] = 0 if k == 0 else round(s["words"][0][1] - .15, 3)
    for k, s in enumerate(scenes):
        s["end"] = scenes[k + 1]["start"] if k + 1 < len(scenes) else dur + HOLD
    total = dur + HOLD

    def at(scene, token):
        return next(w[1] for w in scenes[scene]["words"] if w[0] == token)

    ev = {
        "excel": at(0, "Excel,"), "email": at(0, "email,"), "caderno": at(0, "caderno."),
        "s2": scenes[1]["start"], "perde": at(1, "Perde-se"), "tempo": at(1, "tempo"),
        "junta": at(2, "junta"), "lugar": at(3, "lugar."),
        "mod": [at(3, "Clientes,"), at(3, "encomendas,"), at(3, "stock"), at(3, "faturação,")],
        "s5": scenes[4]["start"], "site": at(4, "hivecode.pt/business."),
    }

    blocks = "".join(
        f'<div class="txt" style="font-size:{s["size"]}px">'
        + "".join(f'<span class="w{" em" if w in s["em"] else ""}" data-s="{st:.3f}">{w}</span>' for w, st, _ in s["words"])
        + "</div>"
        for s in scenes
    )
    timeline = {"ev": ev, "scenes": [{"start": s["start"], "end": s["end"]} for s in scenes]}
    html = f"""<!doctype html><html lang="pt"><head><meta charset="utf-8">
<style>@import url('https://fonts.googleapis.com/css2?family=Geologica:wght@300;400;500;600;700&display=block');
{BASE_CSS}{CSS}</style></head><body>
<span class="glow" style="width:720px;height:720px;left:-220px;top:-160px;background:#4877FE"></span>
<span class="glow" style="width:680px;height:680px;right:-260px;bottom:260px;background:#D752FE"></span>
<div class="top"><span class="brand"><img src="{ASSETS}/logo_side.png" alt="">HiveCode</span><span>Business</span></div>
{blocks}{ART}
<script>{SEEK_JS.replace("__T__", json.dumps(timeline, ensure_ascii=False))}</script>
</body></html>"""
    page = HERE / "reel.html"
    page.write_text(html, encoding="utf-8")

    subprocess.run(["node", str(ROOT / "tools" / "reel.mjs"), str(page), str(WORK / "frames"), f"{total:.3f}", str(FPS)], check=True)

    sfx()
    hits = [("whoosh", s["start"] - .12) for s in scenes[1:]]
    hits += [("pop", ev[k]) for k in ("excel", "email", "caderno", "perde", "tempo")]
    hits += [("thump", ev["junta"] + .55)] + [("click", m) for m in ev["mod"]]
    hits += [("pop", ev["s5"] + .15), ("pop", ev["site"])]
    inputs, chains = ["-i", str(WORK / "voz.mp3")], ["[1:a]adelay=0:all=1[v0]"]
    for n, (name, when) in enumerate(hits, 2):
        inputs += ["-i", str(WORK / f"{name}.wav")]
        chains.append(f"[{n}:a]adelay={max(0, int(when * 1000))}:all=1[v{n - 1}]")
    mix = ";".join(chains) + ";" + "".join(f"[v{n}]" for n in range(len(hits) + 1)) + f"amix=inputs={len(hits) + 1}:normalize=0[a]"
    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", str(WORK / "frames" / "%05d.jpg"), *inputs,
        "-filter_complex", mix, "-map", "0:v", "-map", "[a]",
        "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS),
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-t", f"{total:.3f}", "-movflags", "+faststart",
        str(HERE / "reel.mp4"),
    ], check=True)
    print(f"reel.mp4 {total:.1f}s")


if __name__ == "__main__":
    main()
