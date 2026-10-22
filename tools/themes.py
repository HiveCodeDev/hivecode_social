"""Visual families beyond the night base, so the profile grid alternates light and dark.

Each theme overrides the base colour variables; build_week.page(..., theme=) and
reelkit.page(..., theme=) drop the hex grid and glows when a theme is given.
  paper   cream, dark ink, serif italic emphasis (editorial)
  blue    full HiveCode blue, white type, yellow emphasis, white logo
  spooky  near-black with pumpkin orange (Halloween)
  canvas  light grey design-tool canvas with a dot grid, violet selection accent
"""

THEMES = {
    "paper": dict(bg="#F6F1E7", ink="#121125", soft="#4a4560", muted="#8a8499", accent="#265ADF", logo=""),
    "blue": dict(bg="#265ADF", ink="#ffffff", soft="#dbe5ff", muted="#b7c8ff", accent="#FFD84D",
                 logo="filter:brightness(0) invert(1)"),
    "spooky": dict(bg="#0B0B0B", ink="#F6F1E7", soft="#bdb6a8", muted="#7d776c", accent="#FF8A1F", logo=""),
    "canvas": dict(bg="#ECECF1", ink="#121125", soft="#4a4560", muted="#8a8499", accent="#9B3CF0", logo=""),
}

SERIF = "@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&display=block');"


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
    return out
