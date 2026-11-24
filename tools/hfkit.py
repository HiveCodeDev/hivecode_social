"""HyperFrames kit: reels and stories as HyperFrames projects (1080x1920), rendered by the HyperFrames CLI.

build(name, out_dir, theme=..., total=..., html=..., css=..., js=..., ...) writes <out_dir>/index.html plus
assets (logo, mixed audio), checks it and renders <out_mp4>. The video's own `js` adds GSAP tweens to `tl`
(always fromTo, times in seconds) and can read `E` (the events dict passed in `ev`).

Reels:   scenes=reelkit.voice(...)[1]  -> captions of <=3 words with a gold sweep on the spoken word, brand header.
Stories: title=[(text, size, {em words}, start, end)] -> big words popping in; arrow=(label, at, css) points at
         the profile picture; outro=at -> blur + logo + hivecode.pt from `at` to the end.
Themes come from tools/themes.py (colours, textures, Christmas scenery); Christmas themes also get falling snow.
"""
import json
import shutil
import subprocess
from pathlib import Path

import reelkit
import themes

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "tools" / "hf_template"   # hyperframes.json, meta.json, package.json, compositions/snow.html
CLI = Path.home() / ".claude/plugins/cache/hyperframes/hyperframes/0.9.91/skills/hyperframes/scripts/plugin-cli.mjs"
SERIF_THEMES = {"paper", "natal", "natalverde"}


def mix(work, total, voice, hits, out_audio, music=None, music_vol=.2):
    """Voice (or silence) + synthesized sound effects (name, seconds) + optional looped music -> one AAC file."""
    work = Path(work)
    work.mkdir(parents=True, exist_ok=True)
    for name, (src, af) in reelkit.SFX.items():
        subprocess.run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", "-f", "lavfi", "-i", src, "-af", af, str(work / f"{name}.wav")], check=True)
    if voice:
        inputs = ["-i", str(voice)]
    else:
        inputs = ["-f", "lavfi", "-t", f"{total:.3f}", "-i", "anullsrc=r=48000:cl=stereo"]
    chains = ["[0:a]adelay=0:all=1[v0]"]
    for n, (name, when) in enumerate(hits, 1):
        inputs += ["-i", str(work / f"{name}.wav")]
        chains.append(f"[{n}:a]adelay={max(0, int(when * 1000))}:all=1[v{n}]")
    tracks = len(hits) + 1
    if music:
        inputs += ["-stream_loop", "-1", "-i", str(music)]
        chains.append(f"[{tracks}:a]atrim=0:{total:.3f},afade=t=in:d=0.8,afade=t=out:st={max(0, total - 1.5):.3f}:d=1.5,volume={music_vol}[v{tracks}]")
        tracks += 1
    graph = ";".join(chains) + ";" + "".join(f"[v{n}]" for n in range(tracks)) + f"amix=inputs={tracks}:normalize=0,apad,atrim=0:{total:.3f}[a]"
    subprocess.run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", *inputs, "-filter_complex", graph, "-map", "[a]",
                    "-c:a", "aac", "-ac", "2", "-ar", "48000", "-b:a", "192k", str(out_audio)], check=True)


def _theme_css(name):
    t = themes.THEMES[name]
    # Instrument Serif is not bundled with HyperFrames; Playfair Display is
    css = themes.css(name).replace("body{", "#root{").replace("body,", "#root,").replace("'Instrument Serif'", "'Playfair Display'")
    css += f"#root{{color:{t['ink']}}}\n"
    serif = "font-family:'Playfair Display',serif;font-style:italic;font-weight:700;letter-spacing:-.01em"
    if name in SERIF_THEMES:
        css += f".cw.em b,.tw.em{{{serif}}}\n"
    if name in ("forest", "receipt"):
        css += "#root{font-family:'IBM Plex Mono',monospace}\n"
    return css


KIT_CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:var(--ground)}
#root{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:Outfit,sans-serif}
#root>.a{position:absolute}
#brand{position:absolute;left:120px;top:300px;display:flex;align-items:center;gap:14px;font-size:30px;font-weight:700;opacity:.85;z-index:5}
#brand img{width:40px;height:40px}
.cg{position:absolute;left:130px;right:130px;top:1070px;display:flex;flex-wrap:wrap;justify-content:center;gap:4px 10px;z-index:20}
.cw{position:relative;display:inline-block;padding:4px 14px 8px;font-size:70px;font-weight:800;letter-spacing:-.02em;line-height:1.05}
.cw b{position:relative;z-index:1;font-weight:inherit}
.cb{position:absolute;inset:0;border-radius:14px;transform-origin:0 50%;opacity:0}
.tl{position:absolute;left:110px;right:110px;display:flex;flex-wrap:wrap;gap:0 .24em;font-weight:800;line-height:1;letter-spacing:-.03em;z-index:20}
.tw{display:inline-block}
#arrow{position:absolute;left:70px;top:150px;display:flex;align-items:center;gap:20px;padding:20px 30px 20px 22px;border-radius:999px;font-size:38px;font-weight:800;z-index:60}
#arrow svg{width:56px;height:56px}
#outro{position:absolute;inset:0;z-index:50;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:40px;color:#fff;background:rgba(18,17,37,.72)}
#outro img{width:300px;height:300px}
#outro b{font-size:76px;font-weight:700;letter-spacing:-.01em}
"""


def _captions(scenes, ink, accent, ground):
    groups = []
    for si, sc in enumerate(scenes):
        ws, nxt_scene = sc["words"], (scenes[si + 1]["start"] if si + 1 < len(scenes) else sc["end"])
        for i in range(0, len(ws), 3):
            chunk = ws[i:i + 3]
            nxt = ws[i + 3][1] if i + 3 < len(ws) else nxt_scene
            groups.append((chunk, sc["em"], max(0, chunk[0][1] - .05), min(chunk[-1][2] + .45, nxt - .04)))
    groups[0] = (groups[0][0], groups[0][1], 0, groups[0][3])
    html = "".join(
        f'<div class="cg clip" id="cg{g}" data-start="{a:.3f}" data-duration="{b - a:.3f}" data-track-index="20">'
        + "".join(f'<span class="cw{" em" if w in em else ""}" data-ws="{s:.3f}" data-we="{e:.3f}"><i class="cb"></i><b>{w}</b></span>'
                  for w, s, e in chunk) + "</div>"
        for g, (chunk, em, a, b) in enumerate(groups))
    js = f"""document.querySelectorAll(".cg").forEach(g => {{
  const g0 = +g.dataset.start;
  tl.fromTo(g, {{ y: 24, opacity: 0 }}, {{ y: 0, opacity: 1, duration: .14, ease: "power2.out" }}, g0);
  g.querySelectorAll(".cw").forEach(w => {{
    const ws = +w.dataset.ws, we = Math.max(+w.dataset.we, ws + .14), bg = w.querySelector(".cb"), tx = w.querySelector("b"), rest = w.classList.contains("em") ? "{accent}" : "{ink}";
    tl.fromTo(w, {{ scale: .85 }}, {{ scale: 1, duration: .18, ease: "back.out(3)", immediateRender: false }}, ws - .04);
    tl.fromTo(bg, {{ scaleX: 0, opacity: 0 }}, {{ scaleX: 1, opacity: 1, duration: .12, ease: "power2.out", immediateRender: false }}, ws);
    tl.fromTo(tx, {{ color: rest }}, {{ color: "{ground}", duration: .08, immediateRender: false }}, ws);
    tl.fromTo(bg, {{ opacity: 1 }}, {{ opacity: 0, duration: .1, immediateRender: false }}, we);
    tl.fromTo(tx, {{ color: "{ground}" }}, {{ color: rest, duration: .1, immediateRender: false }}, we);
  }});
}});"""
    css = f".cw{{color:{ink}}}.cw.em b{{color:{accent}}}.cb{{background:{accent}}}"
    return html, js, css


def _title(lines, accent):
    html, js = "", ""
    for n, (text, size, em, a, b, *top) in enumerate(lines):
        y = top[0] if top else 430
        html += (f'<div class="tl clip" id="tl{n}" data-start="{a}" data-duration="{b - a:.3f}" data-track-index="{21 + n}" style="top:{y}px;font-size:{size}px">'
                 + "".join(f'<span class="tw{" em" if w in em else ""}">{w}</span>' for w in text.split()) + "</div>")
        js += f'tl.fromTo("#tl{n} .tw", {{ y: 60, opacity: 0, scale: .8 }}, {{ y: 0, opacity: 1, scale: 1, duration: .4, stagger: .12, ease: "back.out(2.2)" }}, {a + .2});\n'
    return html, js, f".tw.em{{color:{accent}}}"


ARROW_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M17 17 7 7M16 7H7v9"/></svg>'


def build(name, out_dir, *, theme, total, html, css="", js="", ev=None, scenes=None, title=None, arrow=None, outro=None,
          voice=None, hits=(), music=None, music_vol=.2, out_mp4, cover=None, snow=None):
    out_dir = Path(out_dir)
    if not (out_dir / "hyperframes.json").exists():
        shutil.copytree(TEMPLATE, out_dir, dirs_exist_ok=True)
    (out_dir / "assets").mkdir(exist_ok=True)
    for logo in ("logo_mark.svg", "logo_mark_white.svg"):
        shutil.copy(ROOT / "assets" / logo, out_dir / "assets" / logo)
    t = themes.THEMES[theme]
    mix(ROOT / "reels" / f"hf-{name}", total, voice, list(hits), out_dir / "assets" / "audio.m4a", music, music_vol)

    extra_html, extra_js, extra_css = "", "", ""
    if scenes:
        h, j, c = _captions(scenes, t["ink"], t["accent"], t["bg"])
        extra_html += h + f'<div id="brand" class="brand"><img src="assets/logo_mark.svg" alt="">HiveCode</div>'
        extra_js += j
        extra_css += c
    if title:
        h, j, c = _title(title, t["accent"])
        extra_html, extra_js, extra_css = extra_html + h, extra_js + j, extra_css + c
    if arrow:
        label, at, acss = arrow
        extra_html += f'<div id="arrow" style="{acss}">{ARROW_SVG}{label}</div>'
        extra_js += (f'tl.fromTo("#arrow", {{ opacity: 0, scale: .3 }}, {{ opacity: 1, scale: 1, duration: .45, ease: "back.out(2.5)" }}, {at});\n'
                     f'tl.fromTo("#arrow", {{ x: 0, y: 0 }}, {{ x: -14, y: -14, duration: .26, ease: "sine.inOut", yoyo: true, repeat: {int((total - at) / .52)} }}, {at + .5});\n')
    if outro is not None:
        extra_html += (f'<div id="outro" class="clip" data-start="{outro}" data-duration="{total - outro:.3f}" data-track-index="30">'
                       f'<img id="olg" src="assets/logo_mark_white.svg" alt=""><b id="ourl">hivecode.pt</b></div>')
        extra_js += (f'tl.fromTo("#outro", {{ opacity: 0, backdropFilter: "blur(0px)" }}, {{ opacity: 1, backdropFilter: "blur(28px)", duration: .4, ease: "power2.out" }}, {outro});\n'
                     f'tl.fromTo("#olg", {{ scale: 0, rotate: -90 }}, {{ scale: 1, rotate: 0, duration: .5, ease: "back.out(2)" }}, {outro + .15});\n'
                     f'tl.fromTo("#ourl", {{ opacity: 0, y: 30 }}, {{ opacity: 1, y: 0, duration: .35, ease: "power2.out" }}, {outro + .4});\n')
    snow = theme in themes.XMAS if snow is None else snow
    snow_html = (f'<div id="snowfx" data-composition-id="snow" data-composition-src="compositions/snow.html" data-start="0" '
                 f'data-duration="{total:.3f}" data-width="1080" data-height="1920" data-track-index="1" data-track-kind="graphics"></div>') if snow else ""

    page = f"""<!doctype html>
<html lang="pt">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=1080, height=1920"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
<style>
:root{{--ground:{t['bg']};--ink:{t['ink']};--accent:{t['accent']}}}
{KIT_CSS}
{_theme_css(theme)}
{extra_css}
{css}
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{total:.3f}" data-width="1080" data-height="1920">
{snow_html}
{html}
{extra_html}
<audio id="audio" class="clip" src="assets/audio.m4a" data-start="0" data-duration="{total:.3f}" data-track-index="40" data-volume="1"></audio>
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
const E = {json.dumps(ev or {})};
{js}
{extra_js}
window.__timelines["main"] = tl;
tl.seek(0);
</script>
</body>
</html>
"""
    (out_dir / "index.html").write_text(page, encoding="utf-8")
    check = subprocess.run(["node", str(CLI), "check", "--json", "--safe-zone", "reels"], cwd=out_dir, capture_output=True, text=True, encoding="utf-8")
    errors = check.stdout.count('"severity": "error"')
    print(f"{name}: check {'ok' if errors == 0 else f'{errors} errors'}")
    subprocess.run(["node", str(CLI), "render", "--output", str(Path(out_mp4).resolve())], cwd=out_dir, check=True, capture_output=True)
    if cover is not None:
        reelkit.cover(out_mp4, cover, Path(out_mp4).with_name("cover-hf.jpg"))
    print(f"{name}: {out_mp4}")
