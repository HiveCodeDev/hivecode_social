"""Reel "Uma noite assombrada no seu site" (Halloween, websites), halloween theme, 1080x1920.

python posts/2026-10-31-noite-assombrada/reel/build.py
Midnight: the shop is closed, the site starts to haunt its visitors (503, a contact that
vanishes, "não seguro"); they drift off as ghosts. Moon, bats, fog and lightning; Halloween
sound effects and a soft music-box loop over a low drone, all synthesised here.
"""
import math
import struct
import sys
import wave
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import reelkit  # noqa: E402
from build_week import ASSETS  # noqa: E402

WORK = ROOT / "reels" / HERE.parent.name
WORK.mkdir(parents=True, exist_ok=True)

SCENES = [
    ("Meia-noite. A sua loja está fechada.", 96, {"Meia-noite."}),
    ("Mas no site, algo estranho acontece.", 92, {"estranho"}),
    ("Um cliente tenta encomendar… e a página não abre.", 84, {"não", "abre."}),
    ("Outro procura o seu contacto… e ele desaparece.", 84, {"desaparece."}),
    ("Um terceiro vê o aviso: não seguro.", 88, {"não", "seguro."}),
    ("Não são fantasmas. São clientes que perde.", 88, {"clientes"}),
    ("Neste Halloween, assuste a concorrência, não os clientes.", 80, {"concorrência,"}),
    ("hivecode.pt.", 110, {"hivecode.pt."}),
]

GHOST = ('<svg viewBox="0 0 80 90" width="{w}" height="{h}"><path d="M8 88V38a32 32 0 0 1 64 0v50l-10.6-9-10.7 9-10.7-9-10.7 9-10.6-9z" '
         'fill="#EDE7FF" opacity=".92"/><ellipse cx="28" cy="38" rx="6" ry="9" fill="#120B1F"/><ellipse cx="52" cy="38" rx="6" ry="9" fill="#120B1F"/>'
         '<ellipse cx="40" cy="60" rx="7" ry="9" fill="#120B1F"/></svg>')
BAT = ('<svg viewBox="0 0 100 40" width="{w}" height="{h}"><path d="M50 14c-3-6-7-6-8 0-6-8-18-10-30-6 8 2 12 8 12 16 4-4 10-4 14 0 2-4 6-6 '
       '12-4 6-2 10 0 12 4 4-4 10-4 14 0 0-8 4-14 12-16-12-4-24-2-30 6-1-6-5-6-8 0z" fill="#05020b"/></svg>')

CSS = """
#moon{left:770px;top:660px;width:230px;height:230px;border-radius:50%;background:radial-gradient(circle at 40% 40%,#fffbe6,#f3e9b8 60%,#d8c98a);box-shadow:0 0 120px 40px rgba(243,233,184,.25)}
.fog{width:1400px;height:300px;border-radius:50%;background:radial-gradient(ellipse,rgba(200,190,255,.22),transparent 70%);filter:blur(20px)}
.bat{z-index:3}
#flash{inset:0;background:#e9e3ff;opacity:0;z-index:8}
#shop{left:190px;top:1000px;width:700px;height:520px;background:#0a0614;border:3px solid #2a1f45;border-radius:14px 14px 0 0;opacity:0}
#shop .win{position:absolute;left:60px;top:150px;width:300px;height:230px;background:#1a1230;border:3px solid #2a1f45}
#shop .door{position:absolute;right:70px;bottom:0;width:200px;height:340px;background:#1a1230;border:3px solid #2a1f45}
#sign{position:absolute;left:24px;top:60px;padding:8px 14px;background:#e5484d;color:#fff;font-size:28px;font-weight:800;transform:rotate(-6deg)}
#clock{left:60px;top:880px;font-size:72px;font-weight:800;color:#9BFF5B;text-shadow:0 0 30px rgba(155,255,91,.6);opacity:0;font-variant-numeric:tabular-nums}
#br{left:120px;top:960px;width:840px;height:560px;border-radius:24px;background:#1b1230;border:2px solid rgba(155,255,91,.45);overflow:hidden;opacity:0;box-shadow:0 0 80px -10px rgba(155,255,91,.35)}
#br .bar{height:60px;background:#140c26;display:flex;align-items:center;gap:12px;padding:0 22px;font-size:24px;color:#8a7bb0}
#br .bar b{width:14px;height:14px;border-radius:50%;background:#3a2c5e}
#warn{display:none;color:#ff4d6d;font-weight:700}
.pane{position:absolute;left:0;right:0;top:60px;bottom:0;display:grid;place-items:center;opacity:0}
#e503{font-size:220px;font-weight:800;color:#9BFF5B;text-shadow:0 0 40px rgba(155,255,91,.7)}
#ct{padding:30px 44px;border-radius:20px;background:#2a1f45;font-size:48px;font-weight:700}
#ns{display:flex;align-items:center;gap:26px;padding:30px 40px;border-radius:20px;background:rgba(229,72,77,.15);border:2px solid #ff4d6d;color:#ffb3c0;font-size:46px;font-weight:700}
.gh{z-index:4;opacity:0}
#pump{left:390px;top:960px;font-size:300px;opacity:0;filter:drop-shadow(0 0 60px rgba(255,140,40,.6))}
#logo{left:440px;top:980px;width:200px;height:200px;opacity:0}
#cta{left:88px;right:88px;top:1260px;display:flex;justify-content:center;opacity:0}
#cta span{padding:32px 56px;border-radius:999px;background:#9BFF5B;color:#120B1F;font-size:48px;font-weight:800;box-shadow:0 0 70px -10px rgba(155,255,91,.8)}
"""

ART = f"""
<span id="moon"></span>
<span class="fog" id="f0" style="left:-200px;top:1500px"></span><span class="fog" id="f1" style="left:-100px;top:1650px"></span>
{''.join(f'<span class="bat" id="bat{i}">{BAT.format(w=w, h=w * .4)}</span>' for i, w in enumerate([150, 110, 90]))}
<div id="clock">00:00</div>
<div id="shop"><span class="win"></span><span class="door"><span id="sign">Fechado</span></span></div>
<div id="br"><div class="bar"><b></b><b></b><b></b><span id="warn">⚠ Não seguro</span><span style="margin-left:14px">o-seu-negocio.pt</span></div>
<div class="pane" id="p0"><span id="e503">503</span></div>
<div class="pane" id="p1"><span id="ct">📞 Contactos</span></div>
<div class="pane" id="p2"><span id="ns">⚠ Não seguro</span></div></div>
{''.join(f'<span class="gh" id="g{i}">{GHOST.format(w=w, h=w * 1.12)}</span>' for i, w in enumerate([220, 170, 140]))}
<span id="pump">🎃</span>
<img id="logo" src="{ASSETS}/logo_mark.svg" alt="">
<div id="cta"><span>hivecode.pt</span></div>
<span id="flash"></span>
"""

ART_JS = r"""
const flick = t => (Math.sin(t * 47) * Math.sin(t * 13) > .55 ? .55 : 1);
function art(t, E) {
  // Ambience: drifting fog, bats crossing, lightning flashes.
  $('#f0').style.transform = `translateX(${60 * Math.sin(t * .3)}px)`;
  $('#f1').style.transform = `translateX(${-80 * Math.sin(t * .25)}px)`;
  [[0, 0, 600, 1.0], [1, 4.5, 760, 1.3], [2, 9, 680, 1.1]].forEach(([i, d, y, sp]) => {
    const p = ((t - d) * .18 * sp) % 1.4 - .2, b = $('#bat' + i);
    b.style.transform = `translate(${-200 + p * 1400}px,${y + 40 * Math.sin((t - d) * 3)}px) scaleY(${.7 + .3 * Math.abs(Math.sin(t * 14 + i))})`;
    b.style.opacity = t > d ? 1 : 0;
  });
  $('#flash').style.opacity = E.light.reduce((m, l) => Math.max(m, .55 * Math.max(0, 1 - Math.abs(t - l) / .09), .3 * Math.max(0, 1 - Math.abs(t - l - .22) / .07)), 0);
  // Midnight: the clock and the closed shop.
  pop($('#clock'), t, .1); $('#clock').style.opacity = cl((t - .1) / .1) * (1 - ease((t - E.s2) / .3));
  $('#clock').textContent = t < .6 ? '23:59' : '00:00';
  stage($('#shop'), t, .4, E.s2);
  $('#sign').style.transform = `rotate(${-6 + 5 * Math.sin(t * 2.5)}deg)`;
  // The haunted site.
  const v = stage($('#br'), t, E.s2 + .2, E.s6);
  $('#br').style.opacity = v * (t < E.s3 ? flick(t) : 1);
  const show = (s, a, b) => { $(s).style.opacity = cl((t - a) / .2) * (1 - cl((t - b) / .2)); };
  show('#p0', E.nao1 - .1, E.s4); $('#e503').style.transform = `translate(${8 * Math.sin(t * 50)}px,${4 * Math.sin(t * 37)}px)`;
  $('#e503').style.opacity = flick(t + 1);
  show('#p1', E.s4 + .1, E.s5);
  const gone = ease((t - E.desap) / 1);
  $('#ct').style.opacity = 1 - gone; $('#ct').style.filter = `blur(${12 * gone}px)`; $('#ct').style.transform = `translateY(${-80 * gone}px) scale(${1 + .2 * gone})`;
  show('#p2', E.s5 + .1, E.s6);
  $('#warn').style.display = t > E.nao2 && t < E.s6 ? 'inline' : 'none';
  $('#ns').style.transform = `scale(${1 + .05 * Math.max(0, Math.sin(t * 7.5))})`;
  // The lost customers float off as ghosts.
  [[0, 280, 1080], [1, 600, 1180], [2, 160, 1300]].forEach(([i, x, y]) => {
    const a = E.s6 + .2 + .35 * i, k = ease((t - a) / .6), o = ease((t - E.s7) / .4), g = $('#g' + i);
    g.style.opacity = cl((t - a) / .3) * .9 * (1 - o);
    g.style.transform = `translate(${x + 30 * Math.sin(t * 2 + i)}px,${y - 60 * k - 140 * o + 20 * Math.sin(t * 3 + i)}px)`;
  });
  // Scare the competition: a pumpkin, then the close.
  pop($('#pump'), t, E.conc - .2); $('#pump').style.opacity = cl((t - E.conc + .2) / .1) * (1 - ease((t - E.s8) / .3));
  const lg = back((t - E.s8 - .05) / .5);
  $('#logo').style.opacity = cl((t - E.s8 - .05) / .1);
  $('#logo').style.transform = `rotate(${-120 * (1 - lg)}deg) scale(${lg})`;
  const ct = back((t - E.site) / .45);
  $('#cta').style.opacity = cl((t - E.site) / .1);
  $('#cta').style.transform = `scale(${ct * (1 + .03 * Math.sin((t - E.site) * 5) * cl(t - E.site - .5))})`;
}
"""

# Halloween sound effects, synthesised with ffmpeg like the base set.
SPOOKY = {
    "thunder": ("anoisesrc=color=brown:duration=2.6:amplitude=1", "lowpass=f=380,afade=t=in:d=0.03,afade=t=out:st=0.25:d=2.3,volume=2.2"),
    "wind": ("anoisesrc=color=pink:duration=3:amplitude=0.7", "bandpass=f=520:w=380,tremolo=f=0.7:d=0.8,afade=t=in:d=1,afade=t=out:st=1.8:d=1.2,volume=0.55"),
    "bell": ("aevalsrc=0.5*sin(2*PI*196*t)*exp(-1.6*t)+0.25*sin(2*PI*523*t)*exp(-2.4*t)+0.12*sin(2*PI*1180*t)*exp(-4*t):d=2.2", "volume=0.9"),
    "heart": ("aevalsrc=sin(2*PI*52*t)*exp(-16*t)+0.8*gte(t\\,0.24)*sin(2*PI*48*(t-0.24))*exp(-16*(t-0.24)):d=0.8", "lowpass=f=200,volume=2.4"),
    "ghost": ("aevalsrc=0.4*sin(2*PI*(520*t+90*sin(2*PI*1.3*t)))*sin(PI*t/1.6):d=1.6", "aecho=0.8:0.7:140:0.45,volume=0.45"),
}

SR = 22050


def music(seconds, out):
    """A slow A-minor music-box loop over a low tremolo drone."""
    notes = [69, 72, 76, 75, 76, 72, 69, 68, 69, 72, 76, 79, 77, 76, 72, 69]  # MIDI
    step = .55
    n = int(seconds * SR)
    buf = [0.0] * n
    for i in range(n):
        t = i / SR
        buf[i] = .09 * (math.sin(2 * math.pi * 55 * t) + .6 * math.sin(2 * math.pi * 82.6 * t)) * (.7 + .3 * math.sin(2 * math.pi * .25 * t))
    k = 0
    while k * step < seconds:
        f = 440 * 2 ** ((notes[k % len(notes)] - 69) / 12)
        start = int(k * step * SR)
        for j in range(min(int(1.4 * SR), n - start)):
            t = j / SR
            env = math.exp(-3.2 * t) * min(1, t / .004)
            buf[start + j] += .16 * env * (math.sin(2 * math.pi * f * t) + .35 * math.sin(2 * math.pi * 2 * f * t) + .12 * math.sin(2 * math.pi * 3.01 * f * t))
        k += 1
    with wave.open(str(out), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(b"".join(struct.pack("<h", int(max(-1, min(1, s)) * 30000)) for s in buf))
    return out


def main():
    total, scenes = reelkit.voice(SCENES, WORK / "voz.mp3", rate="-6%")
    at = lambda s, w: reelkit.at(scenes, s, w)  # noqa: E731
    st = [s["start"] for s in scenes]
    ev = {"s2": st[1], "s3": st[2], "s4": st[3], "nao1": at(2, "não"), "s5": st[4], "desap": at(3, "desaparece."),
          "nao2": at(4, "não"), "s6": st[5], "s7": st[6], "conc": at(6, "concorrência,"), "s8": st[7], "site": at(7, "hivecode.pt.")}
    ev["light"] = [.05, ev["s2"] + .1, ev["s6"] - .1]
    page = HERE / "reel.html"
    page.write_text(reelkit.page(scenes, ev, ART, CSS, ART_JS, theme="halloween"), encoding="utf-8")
    reelkit.SFX.update(SPOOKY)
    hits = [("bell", .05), ("bell", .55), ("thunder", .05), ("wind", ev["s2"] - .2), ("thunder", ev["s2"] + .1),
            ("error", ev["nao1"]), ("error", ev["nao1"] + .25), ("ghost", ev["desap"]),
            ("heart", ev["nao2"]), ("heart", ev["nao2"] + .8), ("heart", ev["nao2"] + 1.6),
            ("thunder", ev["s6"] - .1), ("ghost", ev["s6"] + .3), ("ghost", ev["s6"] + 1.0),
            ("pop", ev["conc"] - .2), ("pop", ev["s8"] + .05), ("pop", ev["site"])]
    bgm = music(total + .5, WORK / "music.wav")
    reelkit.render(page, WORK, total, WORK / "voz.mp3", hits, HERE / "reel.mp4", music=bgm, music_vol=.2)
    reelkit.cover(HERE / "reel.mp4", ev["s6"] + 1.4, HERE / "cover.jpg")
    print(f"reel.mp4 {total:.1f}s")


if __name__ == "__main__":
    main()
