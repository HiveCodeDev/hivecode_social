"""Reel "Antes e depois: uma florista no Natal" (natalverde theme, 1080x1920; fictitious example).

python posts/2026-12-12-florista-natal/reel/build.py
Hook: one card with a wipe that swings between "ANTES" (paper order notes, ringing phone) and
"DEPOIS" (the shop site with wreaths and prices). Antes holds while the voice tells it, then the
wipe reveals Depois; a pickup-time sheet is filled and paid; late-night online orders drop in.
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
    ("Uma florista no Natal: antes e depois do site.", 96, {"antes", "depois"}),
    ("Antes, as encomendas chegavam por telefone e ficavam num papel.", 86, {"telefone", "papel."}),
    ("Depois, as coroas e os arranjos estão no site, com foto e preço.", 86, {"site,"}),
    ("O cliente escolhe a hora de recolha e paga online.", 92, {"hora", "online."}),
    ("E o Natal vende-se também a quem não passa à porta.", 92, {"porta."}),
    ("Fale connosco em hivecode.pt.", 110, {"hivecode.pt."}),
]

PINE, GOLD, RED, CREAM = "#0F3A2C", "#E8B84A", "#C41E3A", "#FBF6EA"
CSS = f"""
#card{{left:130px;top:830px;width:820px;height:780px;border-radius:40px;overflow:hidden;opacity:0;box-shadow:0 60px 120px -40px rgba(0,0,0,.6)}}
#card>div{{position:absolute;inset:0}}
#site{{background:#fff;z-index:1}}
#site .hd{{display:flex;justify-content:space-between;align-items:center;padding:28px 34px;background:{PINE};color:#fff;font-size:34px;font-weight:800}}
#site .hd span{{font-size:26px;font-weight:600;opacity:.8}}
#site .bn{{margin:24px 30px 0;padding:22px 28px;border-radius:22px;background:linear-gradient(120deg,{RED},#8f1228);color:#fff;font-size:34px;font-weight:800}}
#site .gr{{display:grid;grid-template-columns:1fr 1fr;gap:20px;padding:24px 30px}}
#site .pr{{border-radius:22px;background:#f4f1e8;padding:18px 20px 20px;color:{PINE}}}
#site .pr i{{display:grid;place-items:center;height:120px;border-radius:16px;background:#e3ecdf;font-style:normal;font-size:76px}}
#site .pr b{{display:block;margin-top:12px;font-size:28px;line-height:1.15}}
#site .pr em{{display:block;margin-top:6px;font-style:normal;font-size:30px;font-weight:800;color:{RED}}}
#paper{{background:repeating-linear-gradient({CREAM} 0 58px,#e5dcc6 58px 60px);font-family:'Instrument Serif',serif;font-style:italic;color:#3b3226;z-index:2}}
#paper p{{margin:0;padding:0 50px;font-size:52px;line-height:60px}}
#paper p:first-child{{padding-top:120px}}
#paper s{{text-decoration-thickness:4px}}
#ring{{position:absolute;right:46px;top:30px;font-size:80px;font-style:normal}}
.tag{{position:absolute;top:28px;padding:10px 24px;border-radius:999px;font-family:Geologica,sans-serif;font-style:normal;font-size:28px;font-weight:800;letter-spacing:.12em;z-index:3}}
#tA{{left:30px;background:#3b3226;color:{CREAM}}}
#tD{{right:30px;background:{GOLD};color:{PINE}}}
#line{{position:absolute;top:0;bottom:0;width:8px;margin-left:-4px;background:{GOLD};z-index:4}}
#slot{{left:170px;top:1290px;width:740px;padding:30px 34px 34px;border-radius:32px;background:#fff;opacity:0;box-shadow:0 40px 90px -30px rgba(0,0,0,.55);color:{PINE}}}
#slot small{{display:block;font-size:26px;font-weight:800;letter-spacing:.12em;color:#6b8a7c}}
#slot .ch{{display:flex;gap:16px;margin-top:18px}}
#slot .ch span{{flex:1;padding:16px 0;text-align:center;border-radius:16px;border:4px solid #dfe8e2;font-size:32px;font-weight:800}}
#pay{{margin-top:22px;height:96px;border-radius:20px;background:{PINE};color:#fff;display:grid;place-items:center;font-size:36px;font-weight:800}}
.or{{left:130px;width:820px;padding:28px 34px;border-radius:28px;background:#fff;color:{PINE};font-size:34px;font-weight:700;opacity:0;
 display:flex;gap:24px;align-items:center;box-shadow:0 30px 70px -30px rgba(0,0,0,.55)}}
.or i{{font-style:normal;flex:none;padding:10px 18px;border-radius:14px;background:{PINE};color:{GOLD};font-size:30px;font-weight:800}}
#moon{{left:800px;top:760px;font-size:110px;opacity:0}}
#logo{{left:440px;top:900px;width:200px;height:200px;opacity:0}}
#cta{{left:88px;right:88px;top:1190px;display:flex;justify-content:center;opacity:0}}
#cta span{{padding:32px 56px;border-radius:999px;background:{GOLD};color:{PINE};font-size:50px;font-weight:800}}
"""

PRODUCTS = [("🌲", "Coroa de Natal", "35 €"), ("💐", "Arranjo de mesa", "25 €"), ("🌺", "Bico-de-papagaio", "18 €"), ("🌿", "Ramo de inverno", "30 €")]
ORDERS = [("22:47", "Coroa de Natal"), ("23:15", "Arranjo de mesa"), ("07:02", "Ramo de inverno")]
ART = ('<div id="card"><div id="site"><div class="hd">Flores da Ribeira<span>Encomendas</span></div>'
       + '<div class="bn">🎄 Especial Natal</div><div class="gr">'
       + "".join(f'<div class="pr"><i>{e}</i><b>{n}</b><em>{p}</em></div>' for e, n, p in PRODUCTS)
       + '</div><span class="tag" id="tD">DEPOIS</span></div>'
       + '<div id="paper"><p>Sra. Rosa: coroa, sexta?</p><p>Arranjo mesa, 25 € ??</p><p><s>ligar ao Sr. Paulo</s></p>'
       + '<p>Ramo… vermelho ou branco?</p><p>Recolhe às 15h? 16h?</p><i id="ring">📞</i><span class="tag" id="tA">ANTES</span></div>'
       + '<span id="line"></span></div>'
       + '<div id="slot"><small>RECOLHA · SEXTA, 18 DE DEZEMBRO</small><div class="ch"><span>10h</span><span>12h</span><span id="h15">15h</span></div>'
       + '<div id="pay">Pagar 35 €</div></div>'
       + "".join(f'<div class="or" id="o{i}" style="top:{860 + i * 170}px"><i>{h}</i>Nova encomenda: {n}</div>' for i, (h, n) in enumerate(ORDERS))
       + '<span id="moon">🌙</span>'
       + f'<img id="logo" src="{ASSETS}/logo_mark.svg" alt=""><div id="cta"><span>hivecode.pt</span></div>')

ART_JS = r"""
function art(t, E) {
  stage($('#card'), t, .05, E.s4 - .05);
  // wipe: swings in the hook, full "antes" while it is told, opens to "depois"
  let w;
  if (t < E.s1) w = 50 + 42 * Math.sin((t - .2) * 3.2) * cl((t - .2) / .3);
  else if (t < E.s2) w = 50 + 50 * ease((t - E.s1) / .4);
  else w = 100 * (1 - ease((t - E.s2) / .7));
  $('#paper').style.clipPath = `inset(0 ${100 - w}% 0 0)`;
  $('#line').style.left = `${w}%`;
  $('#line').style.opacity = w > 1 && w < 99 ? 1 : 0;
  const rg = t > E.tel && t < E.s2 ? Math.sin(t * 40) * 14 : 0;
  $('#ring').style.transform = `rotate(${rg}deg)`;
  // pickup slot + payment
  stage($('#slot'), t, E.s3, E.s4 - .05);
  const on = t > E.hora;
  $('#h15').style.borderColor = on ? '#0F3A2C' : '#dfe8e2';
  $('#h15').style.background = on ? '#0F3A2C' : '#fff';
  $('#h15').style.color = on ? '#E8B84A' : '#0F3A2C';
  const paid = t > E.online;
  $('#pay').textContent = paid ? 'Pago ✓' : 'Pagar 35 €';
  $('#pay').style.background = paid ? '#C41E3A' : '#0F3A2C';
  // late-night orders
  [E.s4 + .2, E.s4 + .7, E.porta].forEach((a, i) => stage($('#o' + i), t, a, E.s5 - .05, 80));
  pop($('#moon'), t, E.s4 + .1);
  $('#moon').style.opacity = cl((t - E.s4 - .1) / .1) * (1 - ease((t - E.s5 + .05) / .3));
  const lg = back((t - E.s5 - .1) / .5);
  $('#logo').style.opacity = cl((t - E.s5 - .1) / .1);
  $('#logo').style.transform = `rotate(${-120 * (1 - lg)}deg) scale(${lg})`;
  const ct = back((t - E.site) / .45);
  $('#cta').style.opacity = cl((t - E.site) / .1);
  $('#cta').style.transform = `scale(${ct})`;
}
"""


def main():
    total, scenes = reelkit.voice(SCENES, WORK / "voz.mp3")
    at = lambda s, w: reelkit.at(scenes, s, w)  # noqa: E731
    st = [s["start"] for s in scenes]
    ev = {"s1": st[1], "tel": at(1, "telefone"), "s2": st[2], "s3": st[3], "hora": at(3, "hora"), "online": at(3, "online."),
          "s4": st[4], "porta": at(4, "porta."), "s5": st[5], "site": at(5, "hivecode.pt.")}
    page = HERE / "reel.html"
    page.write_text(reelkit.page(scenes, ev, ART, CSS, ART_JS, theme="natalverde"), encoding="utf-8")
    hits = [("pop", .05), ("whoosh", .4), ("whoosh", 1.4), ("click", ev["tel"]), ("click", ev["tel"] + .25),
            ("rise", ev["s2"]), ("pop", ev["s3"]), ("click", ev["hora"]), ("thump", ev["online"]),
            ("pop", ev["s4"] + .2), ("pop", ev["s4"] + .7), ("pop", ev["porta"]), ("pop", ev["s5"] + .1), ("pop", ev["site"])]
    reelkit.render(page, WORK, total, WORK / "voz.mp3", hits, HERE / "reel.mp4")
    reelkit.cover(HERE / "reel.mp4", ev["s3"] - .3, HERE / "cover.jpg")
    print(f"reel.mp4 {total:.1f}s")


if __name__ == "__main__":
    main()
