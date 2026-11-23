"""Visual families beyond the night base, so the profile grid alternates light and dark.

Each theme overrides the base colour variables; build_week.page(..., theme=) and
reelkit.page(..., theme=) drop the hex grid and glows when a theme is given.
  paper   cream, dark ink, serif italic emphasis (editorial)
  blue    full HiveCode blue, white type, yellow emphasis, white logo
  spooky  near-black with pumpkin orange (Halloween)
  canvas  light grey design-tool canvas with a dot grid, violet selection accent
  receipt till-receipt white, monospace type, black ink with red emphasis
  screen  desktop-screen grey with a menu bar, system-blue accent (scenes happen in windows)
  lilac   lavender, deep-violet ink and emphasis
  terracotta warm orange poster, dark-brown ink, cream emphasis (user disliked the orange, 2026-10-27)
  forest  deep green, cream ink, mustard emphasis, monospace (pairs with receipt-style cards)
  kraft   brown paper-bag, dark-brown ink, wine emphasis (autumn, São Martinho)
  blackfriday  black with signal yellow, white type (Black Friday)
  blackmonth   the light twin: signal-yellow ground, black type, emphasis as black highlight
  natal   warm cream with falling-snow dots, pine-green ink, Christmas-red serif emphasis (December)
"""

THEMES = {
    "paper": dict(bg="#F6F1E7", ink="#121125", soft="#4a4560", muted="#8a8499", accent="#265ADF", logo=""),
    "blue": dict(bg="#265ADF", ink="#ffffff", soft="#dbe5ff", muted="#b7c8ff", accent="#FFD84D",
                 logo="filter:brightness(0) invert(1)"),
    "spooky": dict(bg="#0B0B0B", ink="#F6F1E7", soft="#bdb6a8", muted="#7d776c", accent="#FF8A1F", logo=""),
    "canvas": dict(bg="#ECECF1", ink="#121125", soft="#4a4560", muted="#8a8499", accent="#9B3CF0", logo=""),
    "receipt": dict(bg="#FBFAF6", ink="#111111", soft="#444444", muted="#888888", accent="#D7263D", logo=""),
    "screen": dict(bg="#E6E8EE", ink="#16181D", soft="#4b505c", muted="#8a8f9c", accent="#0A84FF", logo=""),
    "halloween": dict(bg="#120B1F", ink="#F1ECFF", soft="#c5b8e6", muted="#8a7bb0", accent="#9BFF5B", logo=""),
    "lilac": dict(bg="#B8A4F4", ink="#1A1033", soft="#35265e", muted="#4d3b85", accent="#3A12A8", logo=""),
    "terracotta": dict(bg="#E2603A", ink="#23130D", soft="#4a2418", muted="#7a3a24", accent="#FFF1DC", logo=""),
    "forest": dict(bg="#0F3D2E", ink="#F3EFE6", soft="#b9cfc3", muted="#7fa393", accent="#F4C542",
                   logo="filter:brightness(0) invert(1)"),
    "kraft": dict(bg="#D8C3A0", ink="#2B1B12", soft="#4d3526", muted="#7a5c45", accent="#8E1F35", logo=""),
    "blackfriday": dict(bg="#0A0A0A", ink="#FFFFFF", soft="#d6d6d6", muted="#8f8f8f", accent="#FFD400",
                        logo="filter:brightness(0) invert(1)"),
    "blackmonth": dict(bg="#FFD400", ink="#0A0A0A", soft="#2a2a2a", muted="#5c4f00", accent="#0A0A0A",
                       logo="filter:brightness(0)"),
    "natal": dict(bg="#F5EEE2", ink="#0F3B2C", soft="#2f5646", muted="#6f8a7d", accent="#C41E3A", logo=""),
    "natalnoite": dict(bg="#0E1A33", ink="#F6F1E7", soft="#c9d3e6", muted="#8f9bb8", accent="#F2C14E",
                       logo="filter:brightness(0) invert(1)"),
    "neve": dict(bg="#E8F0F6", ink="#10233F", soft="#33476a", muted="#6c7f9c", accent="#C41E3A", logo=""),
}

# Christmas scenery drawn behind everything: a garland of bulbs along the top, snowflakes, a row of
# pines on a snowy ground at the bottom (content stays above y=1700).
XMAS = {
    "natal": dict(flake="rgba(15,59,44,.11)", wire="#0F3B2C", bulbs=["#C41E3A", "#F2B233", "#0F7B4F", "#2C6FD1"],
                  tree="#0F3B2C", cap="#ffffff", ground="#ffffff"),
    "natalnoite": dict(flake="rgba(255,255,255,.2)", wire="#3a4a70", bulbs=["#F2C14E", "#ff5a6e", "#7ee0a0", "#F2C14E"],
                       tree="#1d5c46", cap="#E9EEF6", ground="#E9EEF6"),
    "neve": dict(flake="rgba(16,35,63,.13)", wire="#10233F", bulbs=["#C41E3A", "#F2B233", "#1E5A45", "#C41E3A"],
                 tree="#1E5A45", cap="#ffffff", ground="#ffffff"),
}


def _svg(body, w, h):
    from urllib.parse import quote
    return f"url(\"data:image/svg+xml,{quote(f'<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 {w} {h}\" width=\"{w}\" height=\"{h}\">{body}</svg>')}\")"


def _xmas_css(x):
    import math
    flake = lambda cx, cy, r: "".join(  # noqa: E731
        f'<line x1="{cx}" y1="{cy}" x2="{cx + r * math.cos(a):.1f}" y2="{cy + r * math.sin(a):.1f}"/>' for a in [k * math.pi / 3 for k in range(6)])
    flakes = _svg(f'<g stroke="{x["flake"]}" stroke-width="4" stroke-linecap="round">'
                  + flake(50, 60, 18) + flake(170, 150, 12) + flake(110, 240, 22) + flake(250, 50, 9) + flake(230, 260, 14) + "</g>", 300, 300)
    bulbs = ""
    for n, bx in enumerate(range(45, 1080, 90)):
        u = (bx % 270) / 270
        by = 20 + 140 * u * (1 - u)
        bulbs += (f'<rect x="{bx - 6}" y="{by - 2}" width="12" height="12" rx="2" fill="{x["wire"]}"/>'
                  f'<ellipse cx="{bx}" cy="{by + 24}" rx="11" ry="17" fill="{x["bulbs"][n % len(x["bulbs"])]}"/>')
    garland = _svg(f'<path d="M0,20 Q135,90 270,20 T540,20 T810,20 T1080,20" fill="none" stroke="{x["wire"]}" stroke-width="4"/>{bulbs}', 1080, 110)
    trees = ""
    for tx, th in [(40, 150), (150, 200), (250, 130), (840, 140), (950, 210), (1050, 150)]:
        base, w = 200, th * .62
        for k in range(3):  # three tiers
            top, bot, half = base - th + k * th * .26, base - th + k * th * .26 + th * .48, w / 2 * (.6 + .2 * k)
            trees += f'<polygon points="{tx},{top:.0f} {tx + half:.0f},{bot:.0f} {tx - half:.0f},{bot:.0f}" fill="{x["tree"]}"/>'
        trees += f'<polygon points="{tx},{base - th} {tx + w * .13:.0f},{base - th + th * .1:.0f} {tx - w * .13:.0f},{base - th + th * .1:.0f}" fill="{x["cap"]}"/>'
    ground = f'<path d="M0,195 Q270,170 540,192 T1080,188 V240 H0Z" fill="{x["ground"]}"/>'
    scene = _svg(trees + ground, 1080, 240)
    return (f"body{{background-image:{garland},{scene},{flakes};background-repeat:no-repeat,no-repeat,repeat;"
            "background-size:1080px 110px,1080px 240px,300px 300px;background-position:0 0,0 1680px,0 0}\n")

SERIF = "@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=IBM+Plex+Mono:wght@400;500;700&display=block');"


def css(name):
    t = THEMES[name]
    out = f"""
:root{{--night:{t['bg']};--deep:{t['bg']};--ink:{t['ink']};--soft:{t['soft']};--muted:{t['muted']};
--violet:{t['accent']};--pink:{t['accent']};--blue:{t['accent']}}}
body{{background:{t['bg']};color:{t['ink']}}}
.brand{{color:{t['ink']}}}.brand img{{{t['logo']}}}
.glow,.hex{{display:none}}
"""
    if name == "paper":
        out += "h1 em,.txt .w.em{font-family:'Instrument Serif',serif;font-style:italic;font-weight:400;letter-spacing:0}\n"
    if name == "canvas":
        out += "body{background-image:radial-gradient(#c4c3d0 2px,transparent 2px);background-size:36px 36px}\n"
    if name == "forest":
        out += "body,.txt{font-family:'IBM Plex Mono',monospace}.txt{letter-spacing:-.04em}.top{border-bottom:3px dashed #F3EFE6;padding-bottom:22px}\n"
    if name == "receipt":
        out += ("body,.txt{font-family:'IBM Plex Mono',monospace}.txt{letter-spacing:-.04em}"
                ".top{border-bottom:3px dashed #111;padding-bottom:22px}\n")
    if name == "kraft":
        out += "body{background-image:radial-gradient(rgba(43,27,18,.07) 1.5px,transparent 1.5px);background-size:9px 9px}\n"
    if name == "blackfriday":
        out += "h1 em,.txt .w.em{color:#FFD400}\n"
    if name == "blackmonth":
        out += "h1 em,.txt .w.em{color:#FFD400;background:#0A0A0A;box-shadow:0 0 0 .1em #0A0A0A;border-radius:.06em}\n"
    if name == "natal":
        out += ("h1 em,.txt .w.em{font-family:'Instrument Serif',serif;font-style:italic;font-weight:400;letter-spacing:0}\n")
    if name in XMAS:
        out += _xmas_css(XMAS[name])
    if name == "screen":
        out += ("body{background:linear-gradient(180deg,#F2F3F6,#DADDE5)}"
                ".top{top:0;left:0;right:0;height:64px;padding:0 40px;background:rgba(255,255,255,.75);font-size:24px}"
                ".top .brand{font-size:24px}.top .brand img{width:34px;height:34px}\n")
    return out
