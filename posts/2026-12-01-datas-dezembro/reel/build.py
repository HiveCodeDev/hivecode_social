"""Reel "Dezembro: as datas que contam" (natal theme, 1080x1920).

python posts/2026-12-01-datas-dezembro/reel/build.py
A December 2026 calendar card: day 8 gets a red holiday ring, a parcel chip for Christmas orders,
24 and 31 fill green (special hours), 26 gets an exchange ring; then a search card shows the shop
open with its Christmas hours; logo and CTA. Snow dots drift all along.
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
    ("Dezembro começou.", 150, {"Dezembro"}),
    ("Dia 8 é feriado: há quem procure se está aberto.", 90, {"feriado:"}),
    ("As encomendas de Natal têm de seguir a tempo.", 90, {"Natal"}),
    ("Nos dias 24 e 31, os horários mudam.", 96, {"horários"}),
    ("E a partir de 26, começam as trocas.", 96, {"trocas."}),
    ("Os clientes procuram primeiro online. Tenha tudo à vista no site e no Google.", 84, {"online."}),
    ("Boas festas, da HiveCode.", 120, {"festas,"}),
]

RED, GREEN = "#C41E3A", "#0F3B2C"
CSS = f"""
#cal{{left:120px;right:120px;top:740px;border-radius:34px;background:#fff;overflow:hidden;opacity:0;box-shadow:0 50px 100px -40px rgba(15,59,44,.45)}}
#cal .hd{{height:110px;background:{RED};color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 44px;font-size:46px;font-weight:800;letter-spacing:.08em}}
#cal .hd small{{font-size:34px;font-weight:600;opacity:.8}}
#cal .wd,#cal .gr{{display:grid;grid-template-columns:repeat(7,1fr);padding:0 22px}}
#cal .wd span{{height:64px;display:grid;place-items:center;font-size:26px;font-weight:700;color:#6f8a7d}}
#cal .gr{{padding-bottom:22px}}
#cal .gr span{{position:relative;height:104px;display:grid;place-items:center;font-size:40px;font-weight:600;color:{GREEN};border-radius:50%}}
#cal .gr span i{{position:absolute;inset:8px 14px;border-radius:24px;border:6px solid transparent}}
#cal .gr span b{{position:relative}}
#chip{{left:0;right:0;top:1560px;display:flex;justify-content:center}}
#chip span{{position:absolute;padding:24px 42px;border-radius:999px;font-size:46px;font-weight:700;white-space:nowrap;opacity:0}}
#srch{{left:120px;right:120px;top:800px;border-radius:34px;background:#fff;padding:40px 44px;opacity:0;box-shadow:0 50px 100px -40px rgba(15,59,44,.45)}}
#srch .q{{padding:24px 32px;border-radius:999px;background:#F5EEE2;font-size:38px;color:#2f5646}}
#srch .r{{margin-top:34px;padding:34px;border-radius:24px;border:4px solid #e9e1d2}}
#srch .r h3{{margin:0;font-size:46px;color:{GREEN}}}
#srch .r p{{margin:14px 0 0;font-size:34px;color:#2f5646}}
#srch .r .ok{{display:inline-block;margin-top:22px;padding:14px 26px;border-radius:14px;background:{GREEN};color:#fff;font-size:32px;font-weight:700;opacity:0}}
#srch .r .hr{{margin-top:18px;font-size:32px;font-weight:700;color:{RED};opacity:0}}
.sn{{width:14px;height:14px;border-radius:50%;background:rgba(196,30,58,.25)}}
#logo{{left:440px;top:930px;width:200px;height:200px;opacity:0}}
#cta{{left:88px;right:88px;top:1220px;display:flex;justify-content:center;opacity:0}}
#cta span{{padding:32px 56px;border-radius:999px;background:{RED};color:#fff;font-size:50px;font-weight:700}}
"""

DAYS = [""] + [str(d) for d in range(1, 32)]  # 1 Dec 2026 is a Tuesday; weeks start on Monday
ART = ('<div id="cal"><div class="hd">DEZEMBRO<small>2026</small></div><div class="wd">'
       + "".join(f"<span>{d}</span>" for d in "STQQSSD") + '</div><div class="gr">'
       + "".join(f'<span id="d{d}"><i></i><b>{d}</b></span>' if d else "<span></span>" for d in DAYS) + "</div></div>"
       + '<div id="chip">'
       + f'<span id="c0" style="background:{RED};color:#fff">8 · Feriado</span>'
       + f'<span id="c1" style="background:{GREEN};color:#fff">📦 Encomendas de Natal</span>'
       + f'<span id="c2" style="background:{GREEN};color:#fff">24 e 31 · Horário especial</span>'
       + f'<span id="c3" style="background:#fff;color:{GREEN};border:5px solid {GREEN}">26 · Trocas</span></div>'
       + '<div id="srch"><div class="q">🔍 loja aberta perto de mim</div><div class="r"><h3>A Sua Loja</h3>'
       + '<p>Rua do Comércio, 12 · ★ 4,8</p><div class="ok" id="ok">Aberto agora</div><div class="hr" id="hr">Horário de Natal: 9h–20h</div></div></div>'
       + "".join(f'<span class="sn" id="s{i}"></span>' for i in range(14))
       + f'<img id="logo" src="{ASSETS}/logo_mark.svg" alt=""><div id="cta"><span>hivecode.pt</span></div>')

ART_JS = r"""
function art(t, E) {
  const k = cl(t / .01);
  stage($('#cal'), t, .35, E.s6 - .1);
  // day 8: red ring; Christmas day: red star; 24 and 31: green fill; 26: green ring
  const ring = (d, a, col, fill) => { const el = $('#d' + d), on = t > a, i = el.querySelector('i');
    i.style.borderColor = on ? col : 'transparent'; i.style.background = on && fill ? col : 'transparent';
    el.querySelector('b').style.color = on && fill ? '#fff' : ''; i.style.transform = `scale(${on ? back((t - a) / .4) : 0})`; };
  ring(8, E.fer, '#C41E3A', false);
  ring(25, E.nat, '#C41E3A', true);
  ring(24, E.h24, '#0F3B2C', true); ring(31, E.h31, '#0F3B2C', true);
  ring(26, E.tro, '#0F3B2C', false);
  const chips = [[E.fer, E.s3], [E.s3, E.s4], [E.s4, E.s5], [E.tro, E.s6 - .1]];
  chips.forEach(([a, b], i) => stage($('#c' + i), t, a, b - .05, 40));
  stage($('#srch'), t, E.s6, E.s7 - .1);
  pop($('#ok'), t, E.onl); $('#hr').style.opacity = cl((t - E.vis) / .2);
  for (let i = 0; i < 14; i++) { const s = $('#s' + i), x = (i * 137) % 1040 + 20, sp = 60 + (i * 37) % 70;
    s.style.transform = `translate(${x + 30 * Math.sin(t + i)}px,${((t * sp + i * 160) % 2000) - 60}px)`; }
  const lg = back((t - E.s7 - .1) / .5);
  $('#logo').style.opacity = cl((t - E.s7 - .1) / .1);
  $('#logo').style.transform = `rotate(${-120 * (1 - lg)}deg) scale(${lg})`;
  const ct = back((t - E.s7 - .5) / .45);
  $('#cta').style.opacity = cl((t - E.s7 - .5) / .1);
  $('#cta').style.transform = `scale(${ct})`;
}
"""


def main():
    total, scenes = reelkit.voice(SCENES, WORK / "voz.mp3")
    at = lambda s, w: reelkit.at(scenes, s, w)  # noqa: E731
    st = [s["start"] for s in scenes]
    ev = {"fer": at(1, "feriado:"), "nat": at(2, "Natal"), "h24": at(3, "24"), "h31": at(3, "31,"), "tro": at(4, "26,"),
          "onl": at(5, "online."), "vis": at(5, "vista"), "s3": st[2], "s4": st[3], "s5": st[4], "s6": st[5], "s7": st[6]}
    page = HERE / "reel.html"
    page.write_text(reelkit.page(scenes, ev, ART, CSS, ART_JS, theme="natal"), encoding="utf-8")
    hits = [("pop", .35), ("thump", ev["fer"]), ("pop", ev["nat"]), ("click", ev["h24"]), ("click", ev["h31"]),
            ("pop", ev["tro"]), ("whoosh", ev["s6"]), ("pop", ev["onl"]), ("pop", ev["s7"] + .1), ("pop", ev["s7"] + .5)]
    reelkit.render(page, WORK, total, WORK / "voz.mp3", hits, HERE / "reel.mp4")
    reelkit.cover(HERE / "reel.mp4", ev["tro"] + .8, HERE / "cover.jpg")
    print(f"reel.mp4 {total:.1f}s")


if __name__ == "__main__":
    main()
