"""Reel "Quanto tempo demora a fazer um site?" (websites), lilac theme, 1080x1920.

python posts/2026-11-04-quanto-tempo/reel/build.py
Everything happens in one desktop window while a four-step track fills underneath: a
conversation, a free mockup taking shape, code being written, the site going live.
No deadlines are promised: "depende do projeto".
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
    ("Quanto tempo demora a fazer um site?", 104, {"tempo"}),
    ("Depende do projeto, mas o caminho é sempre o mesmo.", 84, {"caminho"}),
    ("Primeiro, uma conversa sobre o seu negócio.", 88, {"conversa"}),
    ("Depois, um mockup gratuito para ver como vai ficar.", 84, {"mockup", "gratuito"}),
    ("Aprovado o mockup, desenvolvemos o site.", 88, {"desenvolvemos"}),
    ("Por fim, testamos e pomos o site no ar.", 88, {"no", "ar."}),
    ("Peça um orçamento gratuito em hivecode.pt.", 84, {"gratuito", "hivecode.pt."}),
]
STEPS = ["Conversa", "Mockup", "Código", "No ar"]

CSS = """
#win{left:80px;top:780px;width:920px;height:760px;border-radius:22px;background:#fff;overflow:hidden;opacity:0;box-shadow:0 50px 100px -40px rgba(26,16,51,.6)}
#win .tb{height:58px;background:#F2F3F6;border-bottom:1px solid #E1E3E9;display:flex;align-items:center;gap:12px;padding:0 22px;font-size:22px;color:#8a8f9c}
#win .tb b{width:16px;height:16px;border-radius:50%}
.pane{position:absolute;left:0;right:0;top:58px;bottom:0;padding:40px;opacity:0}
#p0{display:grid;place-items:center;font-size:200px}
#p1{display:flex;align-items:center;justify-content:space-between;padding:40px 60px}
#p1 span{padding:22px 26px;border-radius:16px;background:#F2F3F6;font-size:28px;font-weight:600;opacity:0}
.bub{max-width:560px;padding:24px 30px;border-radius:24px;font-size:32px;margin-bottom:24px;opacity:0}
.bub.a{background:#5B2EE0;color:#fff;margin-left:auto;border-bottom-right-radius:6px}
.bub.b{background:#F2F3F6;color:#16181D;border-bottom-left-radius:6px}
.blk{position:absolute;border-radius:14px;background:#E6E8EE}
#tag{position:absolute;right:30px;top:30px;padding:12px 24px;border-radius:12px;background:#FFD84D;color:#16181D;font-size:28px;font-weight:800;transform:rotate(6deg);opacity:0}
#p4{background:#16181D;font-family:'IBM Plex Mono',monospace}
.cl{height:22px;border-radius:6px;margin-bottom:22px;transform-origin:left}
#p5 .url{display:flex;align-items:center;gap:14px;padding:18px 24px;border-radius:14px;background:#F2F3F6;font-size:30px;color:#4b505c}
#live{position:absolute;right:40px;bottom:40px;padding:22px 32px;border-radius:18px;background:#1f8a4c;color:#fff;font-size:34px;font-weight:700;opacity:0}
#track{left:120px;right:120px;top:1610px;height:120px;opacity:0}
#track .ln{position:absolute;left:30px;right:30px;top:28px;height:8px;border-radius:4px;background:rgba(26,16,51,.25)}
#fill{position:absolute;left:30px;top:28px;height:8px;border-radius:4px;background:#1A1033;width:0}
.st{position:absolute;top:0;width:64px;height:64px;margin-left:-32px;border-radius:50%;background:#B8A4F4;border:4px solid rgba(26,16,51,.35);display:grid;place-items:center;font-size:26px;font-weight:700;color:#35265e}
.st.on{background:#1A1033;border-color:#1A1033;color:#ffffff}
.st small{position:absolute;top:78px;white-space:nowrap;font-size:26px;font-weight:700;color:#1A1033}
#cur{left:0;top:0;width:44px;height:44px;opacity:0;z-index:5}
#logo{left:440px;top:930px;width:200px;height:200px;opacity:0}
#cta{left:88px;right:88px;top:1220px;display:flex;justify-content:center;opacity:0}
#cta span{padding:32px 56px;border-radius:999px;background:#1A1033;color:#ffffff;font-size:46px;font-weight:600;box-shadow:0 30px 70px -24px rgba(26,16,51,.7)}
"""

CODE = "".join(f'<div class="cl" style="width:{w}%;background:{c}"></div>' for w, c in
               [(40, "#c792ea"), (70, "#82aaff"), (55, "#c3e88d"), (80, "#82aaff"), (35, "#f78c6c"), (65, "#c3e88d"), (50, "#c792ea"), (75, "#82aaff")])
ART = f"""
<div id="win"><div class="tb"><b style="background:#ff5f57"></b><b style="background:#febc2e"></b><b style="background:#28c840"></b><span id="ttl" style="margin-left:18px">Novo projeto</span></div>
<div class="pane" id="p0">⏳</div>
<div class="pane" id="p1">{''.join(f'<span id="o{i}">{i + 1}. {s}</span>' for i, s in enumerate(STEPS))}</div>
<div class="pane" id="p2"><div class="bub a" id="m0">Fale-nos do seu negócio.</div><div class="bub b" id="m1">Temos uma loja e queremos vender online.</div><div class="bub a" id="m2">Perfeito. Vamos preparar uma proposta.</div></div>
<div class="pane" id="p3"><div class="blk" id="k0" style="left:40px;right:40px;top:40px;height:60px"></div><div class="blk" id="k1" style="left:40px;right:40px;top:130px;height:260px"></div>
<div class="blk" id="k2" style="left:40px;width:380px;top:420px;height:30px"></div><div class="blk" id="k3" style="left:40px;width:260px;top:470px;height:30px"></div>
<div class="blk" id="k4" style="left:40px;width:240px;top:540px;height:70px"></div><span id="tag">Gratuito</span></div>
<div class="pane" id="p4">{CODE}</div>
<div class="pane" id="p5"><div class="url">🔒 www.o-seu-negocio.pt</div><div style="margin-top:30px;height:300px;border-radius:18px;background:linear-gradient(150deg,#d9ccff,#5B2EE0)"></div>
<div style="margin-top:24px;height:28px;width:60%;border-radius:8px;background:#E6E8EE"></div><div id="live">● Online</div></div></div>
<div id="track"><span class="ln"></span><span id="fill"></span>{''.join(f'<span class="st" id="t{i}" style="left:{30 + i * (780 / 3):.0f}px">{i + 1}<small>{s}</small></span>' for i, s in enumerate(STEPS))}</div>
<svg id="cur" viewBox="0 0 24 24"><path d="M4 2l16 10-7 1.5L9.5 21z" fill="#16181D" stroke="#fff" stroke-width="1.5"/></svg>
<img id="logo" src="{ASSETS}/logo_mark.svg" alt="">
<div id="cta"><span>hivecode.pt</span></div>
"""

ART_JS = r"""
const show = (s, a, b) => { $(s).style.opacity = cl((t0 - a) / .25) * (1 - cl((t0 - b) / .25)); };
let t0 = 0;
function art(t, E) {
  t0 = t;
  stage($('#win'), t, .15, E.s7);
  $('#ttl').textContent = t < E.s3 ? 'Novo projeto' : t < E.s4 ? 'Conversa' : t < E.s5 ? 'Mockup' : t < E.s6 ? 'site.html' : 'www.o-seu-negocio.pt';
  show('#p0', 0, E.s2); $('#p0').style.transform = `rotate(${t < E.s2 ? 180 * ease((t % 1.5) / .6) : 0}deg)`;
  show('#p1', E.s2, E.s3); [0, 1, 2, 3].forEach(i => pop($('#o' + i), t, E.cam + .2 * i));
  show('#p2', E.s3, E.s4); [0, 1, 2].forEach(i => pop($('#m' + i), t, E.s3 + .3 + .7 * i));
  show('#p3', E.s4, E.s5);
  [0, 1, 2, 3, 4].forEach(i => { const k = $('#k' + i); pop(k, t, E.s4 + .3 + .25 * i); });
  const col = t > E.mock + .4;
  $('#k1').style.background = col ? 'linear-gradient(150deg,#d9ccff,#5B2EE0)' : '#E6E8EE';
  $('#k4').style.background = col ? '#16181D' : '#E6E8EE';
  pop($('#tag'), t, E.grat, 'rotate(6deg)');
  show('#p4', E.s5, E.s6); $$('.cl').forEach((c, i) => c.style.transform = `scaleX(${ease((t - E.dev - .15 * i) / .3)})`);
  show('#p5', E.s6, 99); pop($('#live'), t, E.ar);
  // The four-step track fills as each phase starts.
  stage($('#track'), t, E.s2 + .2, E.s7);
  const marks = [E.s3, E.s4, E.s5, E.s6];
  let f = 0;
  marks.forEach((m, i) => { const on = t > m; $('#t' + i).className = 'st' + (on ? ' on' : ''); if (on) f = i; });
  $('#fill').style.width = `${(t > E.s3 ? f / 3 + ease((t - marks[f]) / .5) * 0 : 0) * 780}px`;
  // A cursor that clicks each new step.
  const cur = $('#cur'), clicks = [[540, 1400, E.s3 - .4], [700, 1100, E.s4 - .4], [600, 1300, E.s5 - .4], [760, 1450, E.ar - .4]];
  cur.style.opacity = cl((t - E.s3 + 1) / .2) * (1 - cl((t - E.s7) / .2));
  let x = 900, y = 1700;
  clicks.forEach(([cx, cy, ct]) => { if (t > ct - .6) { const k = ease((t - ct + .6) / .6); x = x + (cx - x) * k; y = y + (cy - y) * k; } });
  cur.style.transform = `translate(${x}px,${y}px) scale(${clicks.some(([, , ct]) => Math.abs(t - ct) < .08) ? .8 : 1})`;
  // Close.
  const lg = back((t - E.s7 - .1) / .5);
  $('#logo').style.opacity = cl((t - E.s7 - .1) / .1);
  $('#logo').style.transform = `rotate(${-120 * (1 - lg)}deg) scale(${lg})`;
  const ct = back((t - E.site) / .45);
  $('#cta').style.opacity = cl((t - E.site) / .1);
  $('#cta').style.transform = `scale(${ct * (1 + .03 * Math.sin((t - E.site) * 5) * cl(t - E.site - .5))})`;
}
"""


def main():
    total, scenes = reelkit.voice(SCENES, WORK / "voz.mp3")
    at = lambda s, w: reelkit.at(scenes, s, w)  # noqa: E731
    st = [s["start"] for s in scenes]
    ev = {"s2": st[1], "cam": at(1, "caminho"), "s3": st[2], "s4": st[3], "mock": at(3, "mockup"), "grat": at(3, "gratuito"),
          "s5": st[4], "dev": at(4, "desenvolvemos"), "s6": st[5], "ar": at(5, "ar."), "s7": st[6], "site": at(6, "hivecode.pt.")}
    page = HERE / "reel.html"
    page.write_text(reelkit.page(scenes, ev, ART, CSS, ART_JS, theme="lilac"), encoding="utf-8")
    hits = [("pop", .15)] + [("pop", ev["cam"] + .2 * i) for i in range(4)]
    hits += [("click", s - .4) for s in (ev["s3"], ev["s4"], ev["s5"])] + [("click", ev["ar"] - .4)]
    hits += [("pop", ev["s3"] + .3 + .7 * i) for i in range(3)] + [("thump", ev["grat"]), ("pop", ev["ar"])]
    hits += [("pop", ev["s7"] + .15), ("pop", ev["site"])]
    reelkit.render(page, WORK, total, WORK / "voz.mp3", hits, HERE / "reel.mp4")
    reelkit.cover(HERE / "reel.mp4", ev["s4"] + 1.6, HERE / "cover.jpg")
    print(f"reel.mp4 {total:.1f}s")


if __name__ == "__main__":
    main()
