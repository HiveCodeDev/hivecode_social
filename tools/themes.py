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
"""

THEMES = {
    "paper": dict(bg="#F6F1E7", ink="#121125", soft="#4a4560", muted="#8a8499", accent="#265ADF", logo=""),
    "blue": dict(bg="#265ADF", ink="#ffffff", soft="#dbe5ff", muted="#b7c8ff", accent="#FFD84D",
                 logo="filter:brightness(0) invert(1)"),
    "spooky": dict(bg="#0B0B0B", ink="#F6F1E7", soft="#bdb6a8", muted="#7d776c", accent="#FF8A1F", logo=""),
    "canvas": dict(bg="#ECECF1", ink="#121125", soft="#4a4560", muted="#8a8499", accent="#9B3CF0", logo=""),
    "receipt": dict(bg="#FBFAF6", ink="#111111", soft="#444444", muted="#888888", accent="#D7263D", logo=""),
    "screen": dict(bg="#E6E8EE", ink="#16181D", soft="#4b505c", muted="#8a8f9c", accent="#0A84FF", logo=""),
    "lilac": dict(bg="#B8A4F4", ink="#1A1033", soft="#35265e", muted="#4d3b85", accent="#3A12A8", logo=""),
    "terracotta": dict(bg="#E2603A", ink="#23130D", soft="#4a2418", muted="#7a3a24", accent="#FFF1DC", logo=""),
    "forest": dict(bg="#0F3D2E", ink="#F3EFE6", soft="#b9cfc3", muted="#7fa393", accent="#F4C542",
                   logo="filter:brightness(0) invert(1)"),
}

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
    if name == "screen":
        out += ("body{background:linear-gradient(180deg,#F2F3F6,#DADDE5)}"
                ".top{top:0;left:0;right:0;height:64px;padding:0 40px;background:rgba(255,255,255,.75);font-size:24px}"
                ".top .brand{font-size:24px}.top .brand img{width:34px;height:34px}\n")
    return out
