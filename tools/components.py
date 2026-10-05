"""Shared slide pieces for carousels (used by posts/*/build.py)."""
import math
from pathlib import Path

from build_week import ASSETS, page

CAROUSEL_CSS = """
.count{position:absolute;top:96px;right:88px;font-size:24px;color:var(--muted);letter-spacing:.1em}
.cta{margin-top:56px;align-self:flex-start;padding:28px 46px;border-radius:999px;background:#265ADF;font-size:36px;font-weight:600}
.art{margin-top:52px;border-radius:24px;overflow:hidden;border:1px solid rgba(255,255,255,.14);box-shadow:0 40px 90px -30px rgba(72,119,254,.55)}
.art img{display:block;width:100%}
.note{margin-top:40px;font-size:34px;line-height:1.4;color:var(--soft);font-weight:300;max-width:880px}
.diagram{position:relative;width:904px;height:660px;margin-top:34px}
.diagram svg{position:absolute;inset:0;width:100%;height:100%}
.core{position:absolute;left:452px;top:330px;transform:translate(-50%,-50%);width:300px;height:180px;border-radius:30px;
display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;
background:linear-gradient(160deg,#2a1f5c,#1a1538);border:2px solid rgba(215,82,254,.65);
box-shadow:0 0 0 10px rgba(215,82,254,.08),0 0 90px rgba(215,82,254,.45)}
.core img{width:70px;height:70px}.core b{font-size:36px;font-weight:600}
.node{position:absolute;transform:translate(-50%,-50%);display:flex;align-items:center;gap:14px;white-space:nowrap;
padding:20px 28px;border-radius:20px;background:#191433;border:1px solid rgba(255,255,255,.16);font-size:32px;font-weight:500;
box-shadow:0 18px 40px -18px rgba(0,0,0,.7)}
.node i{width:14px;height:14px;border-radius:50%}
"""


def diagram(modules, center="O seu sistema"):
    """Hub-and-spoke system diagram: six modules around the centre."""
    cx, cy, rx, ry = 452, 330, 345, 282
    colors = ["pink", "blue"]
    lines, pills = [], []
    for i, name in enumerate(modules):
        a = math.radians(-90 + 360 / len(modules) * i)
        x, y = cx + rx * math.cos(a), cy + ry * math.sin(a)
        mx, my = cx + (x - cx) * 0.55, cy + (y - cy) * 0.55
        c = colors[i % 2]
        lines.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}"/>')
        lines.append(f'<circle cx="{mx:.0f}" cy="{my:.0f}" r="6" fill="var(--{c})" stroke="none"/>')
        pills.append(f'<span class="node" style="left:{x:.0f}px;top:{y:.0f}px"><i style="background:var(--{c})"></i>{name}</span>')
    return (
        '<div class="diagram"><svg viewBox="0 0 904 660"><defs><linearGradient id="ln" gradientUnits="userSpaceOnUse" '
        'x1="0" y1="0" x2="904" y2="660"><stop offset="0" stop-color="#EF5AFE"/><stop offset="1" stop-color="#4877FE"/>'
        '</linearGradient></defs><g stroke="url(#ln)" stroke-width="3" stroke-linecap="round" opacity=".75">'
        + "".join(lines)
        + f'</g></svg><span class="core"><img src="{ASSETS}/logo_side.png" alt=""><b>{center}</b></span>'
        + "".join(pills)
        + "</div>"
    )


def write_slides(here, slides, css=""):
    """Writes slides/NN/post.html with the n/total counter."""
    total = len(slides)
    for n, body in enumerate(slides, 1):
        d = Path(here) / "slides" / f"{n:02d}"
        d.mkdir(parents=True, exist_ok=True)
        counter = f'<span class="count">{n}/{total}</span>'
        (d / "post.html").write_text(page(counter + body, CAROUSEL_CSS + css), encoding="utf-8")
