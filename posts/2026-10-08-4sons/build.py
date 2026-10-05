import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from cases import build

# Slide 3 drawn from scratch in the client's own type (Syne) and blue (#2B35A8):
# the three services stacked, over a sound waveform. No screenshot.
bars = "".join(
    f'<i style="height:{20 + 70 * abs(math.sin(i * 0.55)) * (0.6 + 0.4 * math.sin(i * 0.17)):.0f}%"></i>' for i in range(46)
)
DETAIL = f"""<div class="pillars">
<div class="wave">{bars}</div>
<span>SOM</span><span>LUZ</span><span>EVENTOS</span>
<small>Do palco ao corporativo.</small>
</div>"""

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&display=block');
.pillars{position:relative;margin-top:60px;padding:56px 54px 50px;border-radius:30px;background:#080808;
border:1px solid rgba(255,255,255,.12);overflow:hidden;box-shadow:0 50px 100px -40px rgba(43,53,168,.7)}
.pillars span{position:relative;display:block;font-family:'Syne',sans-serif;font-weight:800;font-size:96px;line-height:1.05;
letter-spacing:.02em;color:#f4f4f6}
.pillars span:nth-of-type(2){color:#5b66e0}
.pillars small{position:relative;display:block;margin-top:26px;font-size:30px;color:#9a9ab0;letter-spacing:.04em}
.wave{position:absolute;left:0;right:0;bottom:0;height:62%;display:flex;align-items:flex-end;gap:7px;padding:0 28px;opacity:.55}
.wave i{flex:1;border-radius:6px 6px 0 0;background:linear-gradient(#2B35A8,rgba(43,53,168,.15))}
"""

build(
    Path(__file__).resolve().parent,
    title="Novo site para a <em>4Sons</em>, empresa audiovisual.",
    desktop="4sons-home.png",
    mobile="4sons-mobile.png",
    phone_title="Pensado para o <em>telemóvel</em>.",
    phone_note="O pedido de orçamento está sempre à mão, em qualquer ecrã.",
)
print("ok")
