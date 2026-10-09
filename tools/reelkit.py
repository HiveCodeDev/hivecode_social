"""Shared pieces for voiced reels (1080x1920): one voice take, words that pop as they are said,
frame-by-frame render and the final mix with small synthesized sound effects.

A reel script defines SCENES = [(text, font_size, {emphasised tokens}), ...], its own art HTML/CSS
and an art JS function `art(t, E)`; build(...) does the rest. See posts/2026-10-13-*/reel/build.py.
"""
import json
import subprocess
from pathlib import Path

from build_week import ASSETS, BASE_CSS
from voice import say

ROOT = Path(__file__).resolve().parent.parent
FPS = 30

CSS = """
html,body{width:1080px;height:1920px}
.top{position:absolute;left:88px;right:88px;top:150px;display:flex;justify-content:space-between;align-items:center;font-size:28px;color:var(--muted);z-index:5}
.txt{position:absolute;left:88px;width:904px;top:300px;font-weight:600;line-height:1.08;letter-spacing:-.025em;z-index:4}
.txt .w{display:inline-block;opacity:0;margin-right:.24em}
.txt .w.em{color:var(--violet)}
#art{position:absolute;inset:0;transform-origin:540px 1140px}
#art>*{position:absolute}
"""

# Helpers and the text track; the reel's own art(t, E) runs after it every frame.
JS = r"""
const T = __T__, E = T.ev;
const cl = x => Math.min(Math.max(x, 0), 1);
const ease = x => 1 - Math.pow(1 - cl(x), 3);
const back = x => { x = cl(x); const c = 1.9; return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); };
const $ = s => document.querySelector(s);
const $$ = s => [...document.querySelectorAll(s)];
const blocks = $$('.txt'), glows = $$('.glow');
// Shows an element from `a` (pops in) until `b` (slides out left); returns visibility 0..1.
function stage(el, t, a, b, dist = 60) {
  const k = back((t - a) / .5), o = ease((t - b) / .3);
  el.style.opacity = cl((t - a) / .12) * (1 - o);
  el.style.transform = `translate(${-160 * o}px,${dist * (1 - k)}px) scale(${.92 + .08 * k})`;
  return cl((t - a) / .12) * (1 - o);
}
function pop(el, t, a, base = '') {
  const k = back((t - a) / .45);
  el.style.opacity = cl((t - a) / .1);
  el.style.transform = `${base} scale(${k})`;
}
__ART__
window.seek = t => {
  glows[0].style.transform = `translate(${40 * Math.sin(t * .5)}px,${30 * Math.cos(t * .4)}px)`;
  glows[1].style.transform = `translate(${-50 * Math.sin(t * .35)}px,${40 * Math.cos(t * .45)}px)`;
  T.scenes.forEach((s, i) => {
    const b = blocks[i], last = i === T.scenes.length - 1, out = last ? 0 : ease((t - s.end) / .25);
    b.style.display = t >= s.start && (t < s.end + .25 || last) ? 'block' : 'none';
    b.style.opacity = 1 - out;
    b.style.transform = `translateY(${-70 * out}px)`;
    b.querySelectorAll('.w').forEach(w => {
      const k = back((t - +w.dataset.s + .08) / .32);
      w.style.opacity = cl((t - +w.dataset.s + .08) / .1);
      w.style.transform = `translateY(${34 * (1 - k)}px) scale(${.88 + .12 * k})`;
    });
  });
  $('#art').style.transform = `scale(${1.02 + .02 * Math.sin(t * .6)})`;
  art(t, E);
};
seek(0);
"""


def voice(scenes_spec, mp3, rate="+8%", hold=1.4):
    """Says all scene texts in one take; returns (total seconds, scenes with words/start/end)."""
    text = " ".join(s for s, _, _ in scenes_spec)
    dur, words = say(text, mp3, rate=rate)
    scenes, i = [], 0
    for s, size, em in scenes_spec:
        n = len(s.split())
        scenes.append({"words": words[i:i + n], "size": size, "em": em})
        i += n
    for k, s in enumerate(scenes):
        s["start"] = 0 if k == 0 else round(s["words"][0][1] - .15, 3)
    for k, s in enumerate(scenes):
        s["end"] = scenes[k + 1]["start"] if k + 1 < len(scenes) else dur + hold
    return dur + hold, scenes


def at(scenes, scene, token):
    """Time the voice starts saying `token` in scene number `scene`."""
    return next(w[1] for w in scenes[scene]["words"] if w[0] == token)


def page(scenes, ev, art_html, art_css, art_js, corner="hivecode.pt"):
    blocks = "".join(
        f'<div class="txt" style="font-size:{s["size"]}px">'
        + "".join(f'<span class="w{" em" if w in s["em"] else ""}" data-s="{st:.3f}">{w}</span>' for w, st, _ in s["words"])
        + "</div>"
        for s in scenes
    )
    timeline = {"ev": ev, "scenes": [{"start": s["start"], "end": s["end"]} for s in scenes]}
    js = JS.replace("__T__", json.dumps(timeline, ensure_ascii=False)).replace("__ART__", art_js)
    return f"""<!doctype html><html lang="pt"><head><meta charset="utf-8">
<style>@import url('https://fonts.googleapis.com/css2?family=Geologica:wght@300;400;500;600;700&display=block');
{BASE_CSS}{CSS}{art_css}</style></head><body>
<span class="glow" style="width:720px;height:720px;left:-220px;top:-160px;background:#4877FE"></span>
<span class="glow" style="width:680px;height:680px;right:-260px;bottom:260px;background:#D752FE"></span>
<div class="top"><span class="brand"><img src="{ASSETS}/logo_side.png" alt="">HiveCode</span><span>{corner}</span></div>
{blocks}<div id="art">{art_html}</div>
<script>{js}</script>
</body></html>"""


SFX = {
    "whoosh": ("anoisesrc=color=pink:duration=0.45:amplitude=0.5",
               "highpass=f=500,lowpass=f=6000,afade=t=in:d=0.2,afade=t=out:st=0.2:d=0.25,volume=0.28"),
    "pop": ("sine=frequency=880:duration=0.09", "afade=t=out:st=0:d=0.09,volume=0.22"),
    "click": ("sine=frequency=1600:duration=0.05", "afade=t=out:st=0:d=0.05,volume=0.2"),
    "thump": ("sine=frequency=95:duration=0.3", "afade=t=out:st=0:d=0.3,volume=0.8"),
    "error": ("sine=frequency=190:duration=0.16", "afade=t=out:st=0.04:d=0.12,volume=0.45"),
    "rise": ("anoisesrc=color=pink:duration=0.9:amplitude=0.5",
             "highpass=f=300,lowpass=f=3000,afade=t=in:d=0.7,afade=t=out:st=0.7:d=0.2,volume=0.3"),
}


def render(page_path, work, total, voice_mp3, hits, out_mp4):
    """Frames from the page, then voice + sound effects (name, seconds) mixed into the mp4."""
    work = Path(work)
    subprocess.run(["node", str(ROOT / "tools" / "reel.mjs"), str(page_path), str(work / "frames"), f"{total:.3f}", str(FPS)], check=True)
    for name, (src, af) in SFX.items():
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", src, "-af", af, str(work / f"{name}.wav")], check=True)
    inputs, chains = ["-i", str(voice_mp3)], ["[1:a]adelay=0:all=1[v0]"]
    for n, (name, when) in enumerate(hits, 2):
        inputs += ["-i", str(work / f"{name}.wav")]
        chains.append(f"[{n}:a]adelay={max(0, int(when * 1000))}:all=1[v{n - 1}]")
    mix = ";".join(chains) + ";" + "".join(f"[v{n}]" for n in range(len(hits) + 1)) + f"amix=inputs={len(hits) + 1}:normalize=0[a]"
    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", str(work / "frames" / "%05d.jpg"), *inputs,
        "-filter_complex", mix, "-map", "0:v", "-map", "[a]",
        "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS),
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-t", f"{total:.3f}", "-movflags", "+faststart",
        str(out_mp4),
    ], check=True)


def cover(mp4, seconds, out_jpg):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(seconds), "-i", str(mp4), "-frames:v", "1", "-q:v", "2", str(out_jpg)], check=True)
