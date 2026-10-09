"""Reel "Do pedido à fatura, sem copiar dados" (HiveCode Business), 1080x1920, ~35 s.

python posts/2026-10-17-do-pedido-a-fatura/reel/build.py
Act 1: manual copying from email to Excel, then the three errors it causes.
Act 2: one order flows through a custom system on its words (order, stock, invoice, email).
Act 3: the three benefits, then the close. Voice at normal speed (the owner found +8% too fast).
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
    ("Quanto tempo perde a passar encomendas do email para o Excel?", 84, {"tempo"}),
    ("Copiar dados à mão dá origem a erros: stock errado, faturas atrasadas e clientes à espera.", 72, {"erros:"}),
    ("Com um sistema à medida, tudo acontece sozinho.", 92, {"sozinho."}),
    ("O cliente encomenda no seu site e o pedido entra logo no sistema.", 80, {"sistema."}),
    ("O stock atualiza-se e a fatura é emitida no nosso programa de faturação.", 76, {"fatura"}),
    ("E o cliente recebe a confirmação por email.", 88, {"confirmação"}),
    ("Menos tarefas repetidas, menos erros e mais tempo para o seu negócio.", 80, {"mais", "tempo"}),
    ("Saiba mais em hivecode.pt/business.", 76, {"hivecode.pt/business."}),
]

CSS = """
.card{border-radius:26px;background:#1b1638;border:1px solid rgba(255,255,255,.16);box-shadow:0 40px 80px -30px rgba(0,0,0,.8);overflow:hidden;opacity:0}
.card .hd{height:56px;display:flex;align-items:center;gap:12px;padding:0 22px;font-size:24px;font-weight:500;color:var(--soft);border-bottom:1px solid rgba(255,255,255,.1)}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;padding:20px 22px}
.grid i{height:26px;border-radius:6px;background:rgba(255,255,255,.08)}
.grid i.h{background:rgba(47,191,113,.45)}
.row{display:flex;align-items:center;gap:14px;padding:16px 22px;border-bottom:1px solid rgba(255,255,255,.06);font-size:24px}
.row b{width:16px;height:16px;border-radius:50%;background:var(--blue);flex:none}
.bar{display:block;height:16px;border-radius:8px;background:rgba(255,255,255,.14)}
.chip{display:flex;align-items:center;gap:16px;padding:20px 30px;border-radius:999px;background:#1b1638;border:1px solid rgba(255,255,255,.16);font-size:34px;font-weight:600;opacity:0;white-space:nowrap}
.chip.bad{border-color:rgba(255,77,109,.6)}
.chip.bad i{width:40px;height:40px;border-radius:50%;background:#ff4d6d;display:grid;place-items:center;font-size:26px;font-weight:700}
.chip.good i{width:44px;height:44px;border-radius:50%;background:#2fbf71;display:grid;place-items:center}
.clock{width:150px;height:150px;border-radius:50%;border:8px solid #f3f1fb;background:#1b1638;opacity:0}
.clock i{position:absolute;left:50%;bottom:50%;width:8px;margin-left:-4px;border-radius:4px;background:#f3f1fb;transform-origin:50% 100%}
.dot{width:64px;height:40px;border-radius:10px;background:linear-gradient(90deg,var(--pink),var(--blue));opacity:0}
.oc,.env,.dot{left:0;top:0}
#db{z-index:2}.inv{z-index:1}
.flash{inset:0;background:#fff;opacity:0;z-index:9}
.ph{width:270px;height:530px;border-radius:46px;background:#0d0b1c;border:2px solid rgba(255,255,255,.22);padding:12px;opacity:0;box-shadow:0 40px 90px -30px rgba(215,82,254,.6)}
.ph .scr{position:relative;height:100%;border-radius:34px;background:#1b1638;padding:24px 18px;display:flex;flex-direction:column;gap:14px;overflow:hidden}
.prod{height:170px;border-radius:18px;background:linear-gradient(150deg,rgba(239,90,254,.55),rgba(72,119,254,.55))}
.buy{margin-top:auto;padding:18px 0;border-radius:999px;background:#265ADF;text-align:center;font-size:26px;font-weight:700}
.ripple{position:absolute;left:50%;bottom:44px;width:120px;height:120px;margin-left:-60px;border-radius:50%;border:3px solid rgba(255,255,255,.7);opacity:0}
.note{position:absolute;left:10px;right:10px;top:12px;padding:14px 16px;border-radius:18px;background:#f3f1fb;color:#121125;font-size:20px;font-weight:600;display:flex;gap:10px;align-items:center;opacity:0}
.note i{width:28px;height:28px;border-radius:50%;background:#2fbf71;display:grid;place-items:center;flex:none}
#db{left:420px;top:860px;width:572px;height:430px;border-radius:30px;background:#18132f;border:1px solid rgba(215,82,254,.5);opacity:0;padding:26px 28px;display:flex;flex-direction:column;gap:20px}
#db .ttl{display:flex;align-items:center;gap:14px;font-size:30px;font-weight:600}
#db .ttl img{width:44px;height:44px}
#db .tiles{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.tile{border-radius:20px;background:#1f1940;border:2px solid rgba(255,255,255,.08);padding:20px 22px;display:flex;flex-direction:column;gap:8px}
.tile span{font-size:24px;color:var(--soft)}
.tile b{font-size:60px;font-weight:700;letter-spacing:-.02em}
.oc{width:250px;padding:16px 20px;border-radius:18px;background:#265ADF;font-size:22px;font-weight:600;opacity:0;box-shadow:0 20px 40px -10px rgba(72,119,254,.8)}
.oc small{display:block;font-weight:400;opacity:.85;margin-top:4px}
.inv{left:520px;top:1180px;width:300px;height:330px;border-radius:12px;background:#f3f1fb;color:#121125;padding:24px;opacity:0;box-shadow:0 30px 60px -20px rgba(0,0,0,.8)}
.inv h4{font-size:26px;margin-bottom:16px}
.inv .bar{background:#d6d2ea;margin-bottom:12px}
.inv .ok{position:absolute;right:-22px;bottom:-22px;width:76px;height:76px;border-radius:50%;background:#2fbf71;display:grid;place-items:center;opacity:0}
.env{width:110px;height:76px;border-radius:10px;background:#f3f1fb;opacity:0}
.env:before{content:"";position:absolute;left:0;right:0;top:0;height:50%;border-left:55px solid transparent;border-right:55px solid transparent;border-top:38px solid #c9c3e6}
.node{padding:20px 28px;border-radius:20px;background:#191433;border:1px solid rgba(255,255,255,.18);font-size:30px;font-weight:600;opacity:0;white-space:nowrap}
.hubc{left:440px;top:1060px;width:200px;height:200px;border-radius:40px;background:linear-gradient(160deg,#2a1f5c,#1a1538);border:2px solid rgba(215,82,254,.65);
display:grid;place-items:center;opacity:0;box-shadow:0 0 80px rgba(215,82,254,.45)}
.hubc img{width:100px;height:100px}
#lines{left:0;top:0;width:1080px;height:1920px;opacity:0}
#logo{left:440px;top:930px;width:200px;height:200px;opacity:0}
#cta{left:88px;right:88px;top:1220px;display:flex;justify-content:center;opacity:0}
#cta span{padding:32px 54px;border-radius:999px;background:#265ADF;font-size:44px;font-weight:600;box-shadow:0 30px 70px -20px rgba(72,119,254,.8)}
"""

CHECK = '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>'
NODES = [("Loja online", 170, 930), ("Faturação", 910, 930), ("Email", 170, 1390), ("Stock", 910, 1390)]  # centre points

ART = f"""
<div class="card" id="em" style="left:100px;top:860px;width:400px;height:270px"><div class="hd">Caixa de entrada</div>
<div class="row"><b></b>Nova encomenda · Ana S.</div><div class="row"><b></b>Nova encomenda · Rui M.</div><div class="row"><b style="background:var(--muted)"></b><span class="bar" style="width:60%"></span></div></div>
<div class="card" id="xl" style="left:580px;top:900px;width:400px;height:290px"><div class="hd"><i style="width:18px;height:18px;border-radius:4px;background:#2fbf71"></i>encomendas.xlsx</div>
<div class="grid">{"".join(f'<i class="{"h" if n < 4 else ""}"></i>' for n in range(20))}</div></div>
<span class="dot" id="dot"></span>
<div class="clock" id="ck" style="left:110px;top:1190px"><i id="hh" style="height:40px"></i><i id="mh" style="height:56px;width:6px;margin-left:-3px"></i></div>
<div class="chip bad" id="a1" style="left:330px;top:1220px"><i>!</i>Stock errado</div>
<div class="chip bad" id="a2" style="left:330px;top:1310px"><i>!</i>Fatura atrasada</div>
<div class="chip bad" id="a3" style="left:330px;top:1400px"><i>!</i>Cliente à espera</div>
<div class="flash" id="flash"></div>

<div class="ph" id="ph" style="left:100px;top:860px"><div class="scr">
<div class="note" id="nt"><i>{CHECK.format(s=18)}</i>Encomenda confirmada</div>
<div class="prod"></div><span class="bar" style="height:24px;width:80%;background:rgba(255,255,255,.3)"></span><span class="bar" style="width:55%"></span>
<span style="font-size:30px;font-weight:700">24,90 €</span>
<div class="buy" id="buy">Encomendar</div><span class="ripple" id="rp"></span></div></div>
<div id="db"><div class="ttl"><img src="{ASSETS}/logo_side.png" alt="">Painel da empresa</div>
<div class="tiles"><div class="tile" id="tE"><span>Encomendas</span><b id="vE">36</b></div><div class="tile" id="tS"><span>Stock</span><b id="vS">120</b></div></div>
<span class="bar" style="width:90%"></span><span class="bar" style="width:70%"></span></div>
<div class="oc" id="oc">Pedido nº 215<small>Ana S. · 24,90 €</small></div>
<div class="inv" id="inv"><h4 style="display:flex;align-items:center;gap:10px"><img src="{ASSETS}/logo_side.png" style="width:30px;height:30px" alt="">Fatura 2026/215</h4><span class="bar" style="width:80%"></span><span class="bar" style="width:60%"></span><span class="bar" style="width:70%"></span>
<span class="bar" style="width:40%;margin-top:30px;background:#121125"></span><span class="ok" id="invok">{CHECK.format(s=40)}</span></div>
<span class="env" id="env"></span>

<div class="chip good" id="b1" style="left:150px;top:900px"><i>{CHECK.format(s=26)}</i>Menos tarefas repetidas</div>
<div class="chip good" id="b2" style="left:150px;top:1040px"><i>{CHECK.format(s=26)}</i>Menos erros</div>
<div class="chip good" id="b3" style="left:150px;top:1180px"><i>{CHECK.format(s=26)}</i>Mais tempo para o negócio</div>


<img id="logo" src="{ASSETS}/logo_side.png" alt="">
<div id="cta"><span>hivecode.pt/business</span></div>
"""

ART_JS = r"""
const lerp = (a, b, k) => a + (b - a) * k;
function art(t, E) {
  // Act 1: the manual mess, shaking while the errors are named, pulled away on the glitch.
  const pull = ease((t - E.s3) / .45), shake = cl((t - E.s2) / .3) * (1 - pull);
  [['#em', .2], ['#xl', E.excel], ['#ck', .7]].forEach(([s, a], j) => {
    const el = $(s), k = back((t - a) / .45);
    el.style.opacity = cl((t - a) / .1) * (1 - pull);
    el.style.transform = `translate(${6 * shake * Math.sin(t * 40 + j)}px,${-200 * pull}px) rotate(${(j - 1) * 3 + 2 * Math.sin(t * 2 + j)}deg) scale(${k * (1 - .4 * pull)})`;
  });
  $('#hh').style.transform = `rotate(${t * 240}deg)`; $('#mh').style.transform = `rotate(${t * 1400}deg)`;
  const cp = ((t - E.excel - .2) % 1.2 + 1.2) % 1.2 / 1.2, dot = $('#dot');
  dot.style.opacity = t > E.excel + .2 ? (1 - pull) * Math.sin(Math.PI * cp) : 0;
  dot.style.transform = `translate(${lerp(320, 700, ease(cp))}px,${lerp(990, 1040, cp) - 120 * Math.sin(Math.PI * cp)}px)`;
  [['#a1', E.stock], ['#a2', E.faturas], ['#a3', E.clientes]].forEach(([s, a]) => {
    pop($(s), t, a, `translateX(${8 * shake * Math.sin(t * 37)}px)`);
    $(s).style.opacity = cl((t - a) / .1) * (1 - pull);
  });
  $('#flash').style.opacity = .5 * Math.max(0, 1 - Math.abs(t - E.s3 - .35) / .12);

  // Act 2: one order through the system.
  const on = t > E.s3 + .35, off = ease((t - E.s9) / .35);
  ['#ph', '#db'].forEach((s, j) => {
    const el = $(s), k = back((t - E.s3 - .4 - .12 * j) / .55);
    el.style.opacity = on ? cl((t - E.s3 - .4 - .12 * j) / .12) * (1 - off) : 0;
    el.style.transform = `translateY(${80 * (1 - k) - 100 * off + 8 * Math.sin(t * 1.4 + j)}px) scale(${.9 + .1 * k})`;
  });
  const press = Math.max(0, 1 - Math.abs(t - E.pedido - .25) / .15);
  $('#buy').style.transform = `scale(${1 - .07 * press})`;
  const rp = cl((t - E.pedido - .2) / .6);
  $('#rp').style.opacity = t > E.pedido + .2 ? .8 * (1 - rp) : 0;
  $('#rp').style.transform = `scale(${.4 + 1.4 * rp})`;
  // The order card flies from the phone into the dashboard.
  const fly = ease((t - E.entra) / .75), oc = $('#oc');
  oc.style.opacity = t > E.entra - .05 ? cl((t - E.entra + .05) / .1) * (1 - cl((t - E.entra - .8) / .2)) : 0;
  oc.style.transform = `translate(${lerp(110, 600, fly)}px,${lerp(1240, 1000, fly) - 160 * Math.sin(Math.PI * fly)}px) scale(${1 - .3 * fly})`;
  const bump = (el, a) => { const p = Math.max(0, 1 - Math.abs(t - a - .15) / .25);
    el.style.borderColor = `rgba(215,82,254,${.08 + .8 * p})`; el.style.transform = `scale(${1 + .06 * p})`; };
  $('#vE').textContent = t > E.entra + .75 ? 37 : 36; bump($('#tE'), E.entra + .75);
  $('#vS').textContent = t > E.atual + .1 ? 119 : 120; bump($('#tS'), E.atual + .1);
  // Invoice slides out, then gets its check.
  const iv = back((t - E.fatura) / .6), inv = $('#inv');
  inv.style.opacity = t > E.fatura ? cl((t - E.fatura) / .12) * (1 - off) : 0;
  inv.style.transform = `translateY(${-240 * (1 - iv) - 100 * off}px) rotate(${-4 * iv}deg)`;
  pop($('#invok'), t, E.fatura + .6);
  // Confirmation email flies back to the client's phone.
  const ef = ease((t - E.confirm) / .8), env = $('#env');
  env.style.opacity = t > E.confirm ? cl((t - E.confirm) / .1) * (1 - cl((t - E.confirm - .75) / .15)) : 0;
  env.style.transform = `translate(${lerp(650, 180, ef)}px,${lerp(1000, 900, ef) - 200 * Math.sin(Math.PI * ef)}px) rotate(${-15 * Math.sin(Math.PI * ef)}deg)`;
  const nk = back((t - E.confirm - .8) / .45), nt = $('#nt');
  nt.style.opacity = cl((t - E.confirm - .8) / .1);
  nt.style.transform = `translateY(${-70 * (1 - nk)}px)`;

  // Act 3: benefits on their words, then the tools around the hub.
  [['#b1', E.tarefas], ['#b2', E.erros2], ['#b3', E.tempo2]].forEach(([s, a]) => {
    const el = $(s), k = back((t - a) / .45);
    el.style.opacity = cl((t - a) / .1) * (1 - ease((t - E.s11) / .3));
    el.style.transform = `translateX(${140 * (1 - k)}px) scale(${.9 + .1 * k})`;
  });
  // Close.
  const lg = back((t - E.s11 - .1) / .5);
  $('#logo').style.opacity = cl((t - E.s11 - .1) / .1);
  $('#logo').style.transform = `rotate(${-120 * (1 - lg)}deg) scale(${lg})`;
  const ct = back((t - E.site) / .45);
  $('#cta').style.opacity = cl((t - E.site) / .1);
  $('#cta').style.transform = `scale(${ct * (1 + .03 * Math.sin((t - E.site) * 5) * cl(t - E.site - .5))})`;
}
"""


def main():
    total, scenes = reelkit.voice(SCENES, WORK / "voz.mp3", rate="+0%")
    at = lambda s, w: reelkit.at(scenes, s, w)  # noqa: E731
    st = [s["start"] for s in scenes]
    ev = {
        "excel": at(0, "Excel?"), "s2": st[1], "stock": at(1, "stock"), "faturas": at(1, "faturas"), "clientes": at(1, "clientes"),
        "s3": st[2], "pedido": at(3, "encomenda"), "entra": at(3, "entra"), "atual": at(4, "atualiza-se"),
        "fatura": at(4, "fatura"), "confirm": at(5, "confirmação"), "s9": st[6],
        "tarefas": at(6, "tarefas"), "erros2": at(6, "erros"), "tempo2": at(6, "tempo"),
        "s11": st[7], "site": at(7, "hivecode.pt/business."),
    }
    page = HERE / "reel.html"
    page.write_text(reelkit.page(scenes, ev, ART, CSS, ART_JS, corner="Business"), encoding="utf-8")
    hits = [("pop", .2), ("pop", ev["excel"])] + [("error", ev[k]) for k in ("stock", "faturas", "clientes")]
    hits += [("rise", ev["s3"] - .5), ("thump", ev["s3"] + .4), ("click", ev["pedido"] + .25), ("whoosh", ev["entra"]),
             ("pop", ev["entra"] + .75), ("click", ev["atual"] + .1), ("whoosh", ev["fatura"]), ("pop", ev["fatura"] + .6),
             ("whoosh", ev["confirm"]), ("pop", ev["confirm"] + .8)]
    hits += [("pop", ev[k]) for k in ("tarefas", "erros2", "tempo2")]
    hits += [("whoosh", ev["s11"] - .1)]
    hits += [("pop", ev["s11"] + .15), ("pop", ev["site"])]
    reelkit.render(page, WORK, total, WORK / "voz.mp3", hits, HERE / "reel.mp4")
    reelkit.cover(HERE / "reel.mp4", ev["clientes"] + .5, HERE / "cover.jpg")
    print(f"reel.mp4 {total:.1f}s")


if __name__ == "__main__":
    main()
