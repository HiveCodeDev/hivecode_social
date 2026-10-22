"""Reel "Feriado. A loja fecha, o site não." (websites/online shops), paper theme, 1080x1920.

python posts/2026-11-01-feriado/reel/build.py
A calendar page for 1 November, the shop sign flipping to "Fechado", then a phone whose site
stays open while orders, contact requests and bookings drop in as notifications.
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
    ("Hoje é feriado.", 120, {"feriado."}),
    ("A loja está fechada.", 104, {"fechada."}),
    ("Mas o site continua aberto.", 104, {"aberto."}),
    ("Recebe encomendas,", 100, {"encomendas,"}),
    ("pedidos de contacto", 100, {"contacto"}),
    ("e marcações para amanhã.", 100, {"marcações"}),
    ("Quando voltar, está tudo à sua espera.", 92, {"tudo"}),
    ("Sites e lojas online em hivecode.pt.", 84, {"hivecode.pt."}),
]

CSS = """
.cal{left:340px;top:880px;width:400px;height:440px;border-radius:30px;background:#fff;color:#121125;overflow:hidden;opacity:0;text-align:center;box-shadow:0 40px 80px -36px rgba(18,17,37,.45)}
.cal .ctop{height:110px;background:#265ADF;color:#fff;font-size:40px;font-weight:700;display:grid;place-items:center}
.cal b{display:block;font-size:200px;font-weight:800;line-height:1.05;margin-top:10px}
.cal span{font-size:38px;font-weight:600;color:#8a8499}
#door{left:290px;top:860px;width:500px;height:620px;border-radius:24px 24px 0 0;background:#121125;opacity:0;display:flex;justify-content:center;padding-top:150px}
#sign{width:330px;height:150px;border-radius:18px;background:#fff;display:grid;place-items:center;font-size:56px;font-weight:800;color:#e5484d;transform-origin:50% 0}
#knob{position:absolute;right:50px;top:330px;width:30px;height:30px;border-radius:50%;background:#FFD84D}
.ph{left:340px;top:820px;width:400px;height:780px;border-radius:56px;background:#121125;padding:14px;opacity:0;box-shadow:0 40px 90px -36px rgba(18,17,37,.55)}
.ph .scr{height:100%;border-radius:44px;background:#fff;overflow:hidden;color:#121125}
.ph .hero{height:280px;background:linear-gradient(160deg,#f2c27b,#c9772f);display:grid;place-items:center;font-size:120px}
.ph .in{padding:26px 24px;display:flex;flex-direction:column;gap:16px}
.ph b{font-size:34px;font-weight:700}
.open{align-self:flex-start;padding:10px 18px;border-radius:999px;background:#dff5e8;color:#127a43;font-size:24px;font-weight:600}
.btn{padding:20px;border-radius:16px;background:#265ADF;color:#fff;font-size:26px;font-weight:600;text-align:center}
.nt{left:150px;width:780px;display:flex;align-items:center;gap:24px;padding:26px 30px;border-radius:28px;background:rgba(255,255,255,.96);color:#121125;opacity:0;box-shadow:0 30px 60px -26px rgba(18,17,37,.5)}
.nt i{width:76px;height:76px;border-radius:20px;display:grid;place-items:center;font-style:normal;font-size:40px;flex:none}
.nt small{display:block;font-size:24px;color:#8a8499}.nt span{font-size:34px;font-weight:600}
#count{left:88px;right:88px;top:1000px;text-align:center;opacity:0}
#count b{display:block;font-size:240px;font-weight:800;letter-spacing:-.05em;line-height:1;color:#265ADF}
#count span{font-size:44px;font-weight:500;color:#4a4560}
#logo{left:440px;top:930px;width:200px;height:200px;opacity:0}
#cta{left:88px;right:88px;top:1220px;display:flex;justify-content:center;opacity:0}
#cta span{padding:32px 54px;border-radius:999px;background:#265ADF;color:#fff;font-size:44px;font-weight:600;box-shadow:0 30px 70px -24px rgba(38,90,223,.7)}
"""

NOTES = [
    ("n0", "🛒", "#ffe9cf", "Nova encomenda", "2 bolos e 6 pães · levantar amanhã", 1060),
    ("n1", "✉️", "#e3ebff", "Pedido de contacto", "Encomenda para um evento", 1250),
    ("n2", "📅", "#dff5e8", "Nova marcação", "Segunda-feira · 9h30", 1440),
]

ART = f"""
<div class="cal" id="cal"><div class="ctop">Novembro</div><b>1</b><span>Feriado</span></div>
<div id="door"><div id="sign">Aberto</div><span id="knob"></span></div>
<div class="ph" id="ph"><div class="scr"><div class="hero">🥐</div><div class="in">
<b>Padaria do Bairro</b><span class="open">Online · sempre aberto</span><span class="btn">Encomendar</span></div></div></div>
{''.join(f'<div class="nt" id="{i}" style="top:{y}px"><i style="background:{bg}">{e}</i><div><small>{h}</small><span>{t}</span></div></div>' for i, e, bg, h, t, y in NOTES)}
<div id="count"><b>3</b><span>novos pedidos</span></div>
<img id="logo" src="{ASSETS}/logo_mark.svg" alt="">
<div id="cta"><span>hivecode.pt</span></div>
"""

ART_JS = r"""
function art(t, E) {
  stage($('#cal'), t, .15, E.s2);
  // The shop door: the sign flips from "Aberto" to "Fechado".
  stage($('#door'), t, E.s2 + .1, E.s3);
  const f = ease((t - E.fech) / .5), sg = $('#sign');
  sg.style.transform = `rotateX(${180 * f}deg)`;
  sg.textContent = f < .5 ? 'Aberto' : 'Fechado';
  sg.style.color = f < .5 ? '#127a43' : '#e5484d';
  if (f >= .5) sg.style.transform += ' scaleY(-1)';
  // The phone stays open; it slides up to make room for the notifications.
  const v = stage($('#ph'), t, E.s3 + .1, E.s7);
  $('#ph').style.transform += ` translateY(${-260 * ease((t - E.s4 + .3) / .5)}px) scale(${1 - .2 * ease((t - E.s4 + .3) / .5)})`;
  // Notifications drop in one by one.
  [['#n0', E.enc], ['#n1', E.cont], ['#n2', E.marc]].forEach(([s, a]) => {
    const k = back((t - a) / .45), o = ease((t - E.s7) / .3);
    $(s).style.opacity = cl((t - a) / .1) * (1 - o);
    $(s).style.transform = `translateY(${-80 * (1 - k)}px) translateX(${-160 * o}px)`;
  });
  // Back at work: everything waiting.
  stage($('#count'), t, E.s7 + .2, E.s8);
  // Close.
  const lg = back((t - E.s8 - .1) / .5);
  $('#logo').style.opacity = cl((t - E.s8 - .1) / .1);
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
    ev = {"s2": st[1], "fech": at(1, "fechada."), "s3": st[2], "s4": st[3], "enc": at(3, "encomendas,"),
          "cont": at(4, "contacto"), "marc": at(5, "marcações"), "s7": st[6], "s8": st[7], "site": at(7, "hivecode.pt.")}
    page = HERE / "reel.html"
    page.write_text(reelkit.page(scenes, ev, ART, CSS, ART_JS, theme="paper"), encoding="utf-8")
    hits = [("pop", .15)] + [("whoosh", s - .1) for s in (ev["s2"], ev["s3"], ev["s7"])]
    hits += [("click", ev["fech"]), ("pop", ev["enc"]), ("pop", ev["cont"]), ("pop", ev["marc"])]
    hits += [("thump", ev["s7"] + .2), ("pop", ev["s8"] + .15), ("pop", ev["site"])]
    reelkit.render(page, WORK, total, WORK / "voz.mp3", hits, HERE / "reel.mp4")
    reelkit.cover(HERE / "reel.mp4", 1.0, HERE / "cover.jpg")
    print(f"reel.mp4 {total:.1f}s")


if __name__ == "__main__":
    main()
