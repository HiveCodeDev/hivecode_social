"""Animated stories (6-7 s, no voice) built to send viewers to the profile: a giant hook, a
partial reveal (curiosity), and an arrow that points at the profile picture (top left of the
Instagram story UI) with "Toque no perfil".

python posts/stories/build_anim.py [name ...]     (needs the Halloween reel built: it makes the sounds)
"""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "posts" / "2026-10-31-noite-assombrada" / "reel"))
import reelkit  # noqa: E402
from build import BAT, GHOST, SPOOKY, music  # noqa: E402  (the Halloween reel)
from build_week import ASSETS  # noqa: E402

POSTS = ROOT / "posts"

BASE_CSS = """
.top{display:none}
.txt{top:430px;line-height:1}
#arrow{left:70px;top:150px;display:flex;align-items:center;gap:20px;padding:20px 30px 20px 22px;border-radius:999px;font-size:38px;font-weight:800;opacity:0;z-index:9}
#arrow svg{width:56px;height:56px}
.peek{border-radius:30px;overflow:hidden;box-shadow:0 50px 100px -30px rgba(0,0,0,.6)}
.peek img{display:block;width:100%}
"""
ARROW = '<div id="arrow"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17 17 7M8 7h9v9"/></svg>{label}</div>'
ARROW = ARROW.replace("M7 17 17 7M8 7h9v9", "M17 17 7 7M16 7H7v9")  # points up-left, at the profile picture
ARROW_JS = r"""
function arrowAt(t, a) {
  const el = $('#arrow'), k = back((t - a) / .45);
  el.style.opacity = cl((t - a) / .1);
  el.style.transform = `translate(${-14 * Math.max(0, Math.sin((t - a) * 6))}px,${-14 * Math.max(0, Math.sin((t - a) * 6))}px) scale(${k})`;
}
"""


def thumb(path):
    return Path(path).as_uri()


STORIES = {
    # 0. "Saiu hoje": before/after wipe between two slides of the bakery carousel.
    "2026-10-27-saiu": dict(theme="paper", total=6.5, arrow="Veja tudo no perfil", arrow_at=3.8, arrow_css="background:#121125;color:#F6F1E7",
        lines=[("Antes e depois.", 180, {"depois."}, 0, 6.5, .3)],
        css="""#ba{left:140px;top:860px;width:800px;height:1000px;border-radius:30px;overflow:hidden;box-shadow:0 50px 100px -30px rgba(18,17,37,.5)}
#ba img{position:absolute;left:0;top:0;width:800px}#after{clip-path:inset(0 0 0 100%)}
#knife{left:0;top:860px;width:8px;height:1000px;background:#265ADF;box-shadow:0 0 30px rgba(38,90,223,.7)}
.lbl{top:900px;padding:12px 26px;border-radius:999px;font-size:34px;font-weight:700;letter-spacing:.06em;text-transform:uppercase}""",
        html=f"""<div id="ba"><img src="{thumb(POSTS / '2026-10-27-padaria/slides/02/post.jpg')}"><img id="after" src="{thumb(POSTS / '2026-10-27-padaria/slides/03/post.jpg')}"></div>
<span id="knife"></span><span class="lbl" style="left:170px;background:#121125;color:#F6F1E7">Antes</span><span class="lbl" id="dl" style="right:170px;background:#265ADF;color:#fff">Depois</span>""",
        js="""const w = ease((t - 1.2) / 1.6) - .5 * ease((t - 3.4) / .8) + .5 * ease((t - 4.4) / .8);
$('#after').style.clipPath = `inset(0 0 0 ${100 * (1 - w)}%)`;
$('#knife').style.transform = `translateX(${140 + 800 * (1 - w)}px)`; $('#knife').style.opacity = w > .01 && w < .99 ? 1 : 0;
$('#dl').style.opacity = cl((w - .4) / .2);""",
        hits=[("pop", .3), ("whoosh", 1.2), ("pop", 3.8), ("whoosh", 4.4)]),
    # 1. Tip: a huge counter runs to 3 s while a loading bar crawls.
    "2026-10-28-dica": dict(theme="paper", total=6.5, arrow="Mais dicas no perfil", arrow_at=4.2, arrow_css="background:#121125;color:#F6F1E7",
        lines=[("3 segundos.", 190, {"segundos."}, 0, 2.6, .3), ("É o que um cliente espera pelo seu site.", 92, {"espera"}, 2.6, 6.5, 2.7)],
        css="""#ctr{left:0;right:0;top:820px;text-align:center;font-size:420px;font-weight:800;letter-spacing:-.06em;color:#e5484d;font-variant-numeric:tabular-nums}
#bar{left:140px;right:140px;top:1360px;height:40px;border-radius:20px;background:#e8e0cf;overflow:hidden}#bar i{display:block;height:100%;background:#e5484d;width:0}""",
        html='<div id="ctr">0,0</div><div id="bar"><i id="fill"></i></div>',
        js="""$('#ctr').textContent = (Math.min(3, t * 1.25)).toFixed(1).replace('.', ',') + (t > 2.4 ? ' s' : '');
$('#ctr').style.transform = `scale(${t > 2.4 && t < 2.7 ? 1.08 : 1})`;
$('#fill').style.width = `${Math.min(100, t * 16)}%`;
$('#ctr').style.opacity = 1 - ease((t - 2.6) / .3) * .85;""",
        hits=[("click", .4), ("click", 1.2), ("click", 2.0), ("thump", 2.4), ("pop", 4.2)]),
    # 2. "Saiu hoje": a price that spins like a slot machine and never settles.
    "2026-10-29-saiu": dict(theme="blue", total=6.5, arrow="A resposta está no perfil", arrow_at=3.6, arrow_css="background:#FFD84D;color:#121125",
        lines=[("Quanto custa um site?", 150, {"custa"}, 0, 6.5, .3)],
        css="""#tag{left:190px;top:960px;width:700px;height:420px;border-radius:40px;background:#fff;color:#265ADF;display:grid;place-items:center;font-size:220px;font-weight:800;letter-spacing:-.05em;box-shadow:0 50px 100px -30px rgba(10,20,80,.7)}
#tag:before{content:"";position:absolute;left:-60px;top:160px;width:110px;height:110px;border-radius:50%;background:#265ADF;border:18px solid #fff}
#new{left:640px;top:880px;padding:16px 30px;border-radius:14px;background:#FFD84D;color:#121125;font-size:40px;font-weight:800;transform:rotate(8deg)}""",
        html='<div id="tag"><span id="num">€ ???</span></div><span id="new">Novo reel</span>',
        js="""const n = Math.floor(t * 23) % 9;
$('#num').textContent = t < 3.4 ? '€ ' + String(170 + n * 431 % 3900) : '€ ???';
$('#tag').style.transform = `rotate(${-4 + 3 * Math.sin(t * 2)}deg) scale(${back((t - .2) / .5)})`;
pop($('#new'), t, 1.2, 'rotate(8deg)');""",
        hits=[("pop", .2)] + [("click", .3 + .15 * i) for i in range(20)] + [("thump", 3.4), ("pop", 3.6)]),
    # 3. Halloween eve: tombstones rise, the carousel peeks out blurred.
    "2026-10-30-halloween": dict(theme="halloween", total=7.0, arrow="Veja os 5 no perfil", arrow_at=4.4, arrow_css="background:#9BFF5B;color:#120B1F",
        lines=[("5 sustos 🎃", 190, {"sustos"}, 0, 3.0, .3), ("Quantos já lhe aconteceram?", 110, {"Quantos"}, 3.0, 7.0, 3.1)],
        css="""#moon{left:720px;top:700px;width:240px;height:240px;border-radius:50%;background:radial-gradient(circle at 40% 40%,#fffbe6,#f3e9b8 60%,#d8c98a);box-shadow:0 0 120px 40px rgba(243,233,184,.25)}
.tomb{bottom:240px;width:250px;border-radius:125px 125px 8px 8px;background:#1f1830;border:3px solid #3a2c5e;display:grid;place-items:center;text-align:center;font-size:30px;font-weight:700;color:#c5b8e6;padding-top:30px}
#flash{inset:0;background:#e9e3ff;opacity:0;z-index:8}
#pk{left:300px;top:930px;width:480px;transform:rotate(-5deg);filter:blur(10px);opacity:0}""",
        html=f"""<span id="moon"></span>{''.join(f'<span id="b{i}">{BAT.format(w=w, h=w * .4)}</span>' for i, w in enumerate([140, 100]))}
<div class="peek" id="pk"><img src="{thumb(POSTS / '2026-10-31-sustos/slides/01/post.jpg')}"></div>
<div class="tomb" id="t0" style="left:60px;height:330px">Site<br>em baixo</div><div class="tomb" id="t1" style="left:415px;height:420px">Domínio<br>expirado</div>
<div class="tomb" id="t2" style="right:60px;height:300px">Sem<br>backup</div><span id="flash"></span>""",
        js="""[0, 1, 2].forEach(i => { const k = back((t - .5 - .3 * i) / .6); $('#t' + i).style.transform = `translateY(${400 * (1 - k)}px)`; });
[[0, 0, 640], [1, 1, 780]].forEach(([i, d, y]) => { const p = ((t - d) * .25) % 1.4 - .2; $('#b' + i).style.transform = `translate(${-200 + p * 1400}px,${y + 40 * Math.sin(t * 3)}px) scaleY(${.7 + .3 * Math.abs(Math.sin(t * 14 + i))})`; });
$('#flash').style.opacity = Math.max(.55 * Math.max(0, 1 - Math.abs(t - .1) / .09), .45 * Math.max(0, 1 - Math.abs(t - 3.0) / .09));
const pk = $('#pk'); pk.style.opacity = cl((t - 3.2) / .4); pk.style.filter = `blur(${10 - 4 * cl((t - 3.2) / 1)}px)`;
pk.style.transform = `rotate(-5deg) translateY(${-260 * ease((t - 3.2) / .8)}px)`;""",
        hits=[("thunder", .05), ("thump", .5), ("thump", .8), ("thump", 1.1), ("wind", 1.5), ("thunder", 3.0), ("ghost", 3.3), ("pop", 4.4)], music=True),
    # 4. Halloween day: ghost, pumpkin, lightning.
    "2026-10-31-halloween": dict(theme="halloween", total=7.0, arrow="Reel novo no perfil", arrow_at=5.0, arrow_css="background:#9BFF5B;color:#120B1F",
        lines=[("Feliz Halloween 🎃", 160, {"Halloween"}, 0, 3.1, .3), ("Que o único susto seja o da concorrência.", 96, {"concorrência."}, 3.1, 7.0, 3.3)],
        css="""#moon{left:720px;top:760px;width:240px;height:240px;border-radius:50%;background:radial-gradient(circle at 40% 40%,#fffbe6,#f3e9b8 60%,#d8c98a);box-shadow:0 0 120px 40px rgba(243,233,184,.25)}
#gh{left:150px;top:1050px;opacity:0}#pump{left:560px;top:1100px;font-size:280px;opacity:0;filter:drop-shadow(0 0 60px rgba(255,140,40,.6))}
#flash{inset:0;background:#e9e3ff;opacity:0;z-index:8}""",
        html=f"""<span id="moon"></span>{''.join(f'<span id="b{i}">{BAT.format(w=w, h=w * .4)}</span>' for i, w in enumerate([150, 100, 80]))}
<span id="gh">{GHOST.format(w=280, h=314)}</span><span id="pump">🎃</span><span id="flash"></span>""",
        js="""[[0, 0, 660], [1, .8, 820], [2, 1.6, 740]].forEach(([i, d, y]) => { const p = ((t - d) * .27) % 1.4 - .2; $('#b' + i).style.transform = `translate(${-200 + p * 1400}px,${y + 40 * Math.sin((t - d) * 3)}px) scaleY(${.7 + .3 * Math.abs(Math.sin(t * 14 + i))})`; $('#b' + i).style.opacity = t > d ? 1 : 0; });
$('#flash').style.opacity = Math.max(.55 * Math.max(0, 1 - Math.abs(t - .1) / .09), .3 * Math.max(0, 1 - Math.abs(t - .32) / .07), .5 * Math.max(0, 1 - Math.abs(t - 3.1) / .09));
const g = $('#gh'); g.style.opacity = .9 * cl((t - .8) / .4); g.style.transform = `translate(${40 * Math.sin(t * 1.6)}px,${30 * Math.sin(t * 2.3)}px)`;
pop($('#pump'), t, 1.4);""",
        hits=[("thunder", .05), ("wind", .3), ("ghost", .9), ("pop", 1.4), ("thunder", 3.05), ("pop", 5.0)], music=True),
    # 5. Offer: a giant GRÁTIS stamp slams onto a mockup.
    "2026-11-02-oferta": dict(theme="lilac", total=6.5, arrow="Peça no perfil", arrow_at=3.8, arrow_css="background:#1A1033;color:#fff",
        lines=[("Mockup grátis.", 170, {"grátis."}, 0, 6.5, .3)],
        css="""#mk{left:110px;top:900px;width:860px;height:560px;border-radius:30px;background:#fff;overflow:hidden;box-shadow:0 50px 100px -30px rgba(26,16,51,.6)}
#mk .b{height:56px;background:#eee9ff}#mk .h{margin:30px;height:240px;border-radius:20px;background:#e8e3f7}#mk .l{margin:0 30px 20px;height:28px;border-radius:14px;background:#e8e3f7}
#stamp{left:250px;top:1020px;padding:30px 60px;border:14px solid #e5484d;border-radius:28px;color:#e5484d;font-size:150px;font-weight:900;letter-spacing:.02em;opacity:0;background:rgba(255,255,255,.85)}
#sub{left:0;right:0;top:1560px;text-align:center;font-size:48px;font-weight:700;opacity:0}""",
        html='<div id="mk"><div class="b"></div><div class="h" id="hh"></div><div class="l" id="l0" style="width:60%"></div><div class="l" id="l1" style="width:40%"></div></div><div id="stamp">GRÁTIS</div><div id="sub">+ orçamento sem compromisso</div>',
        js="""const c = t > 1.2;
$('#hh').style.background = c ? 'linear-gradient(150deg,#FFD84D,#ff9f43)' : '#e8e3f7';
$('#l0').style.background = $('#l1').style.background = c ? '#1A1033' : '#e8e3f7';
const k = cl((t - 2.0) / .18); $('#stamp').style.opacity = k;
$('#stamp').style.transform = `rotate(-12deg) scale(${3 - 2 * k})`;
$('#sub').style.opacity = cl((t - 2.8) / .3);""",
        hits=[("pop", .3), ("pop", 1.2), ("thump", 2.18), ("pop", 2.8), ("pop", 3.8)]),
    # 6. "Saiu hoje": the mockup reel's cover peeks out with a play button.
    "2026-11-03-saiu": dict(theme="canvas", total=6.0, arrow="Veja o reel no perfil", arrow_at=3.0, arrow_css="background:#9B3CF0;color:#fff",
        lines=[("Novo reel.", 190, {"reel."}, 0, 2.4, .3), ("Veja o seu site antes de o pagar.", 104, {"antes"}, 2.4, 6.0, 2.5)],
        css="""#pk{left:290px;top:880px;width:500px;outline:6px solid #9B3CF0;outline-offset:14px}
#play{left:460px;top:1240px;width:160px;height:160px;border-radius:50%;background:#9B3CF0;display:grid;place-items:center;box-shadow:0 30px 60px -20px rgba(155,60,240,.8)}""",
        html=f"""<div class="peek" id="pk"><img src="{thumb(POSTS / '2026-11-mockup-gratuito/reel/cover.jpg')}"></div>
<span id="play"><svg viewBox="0 0 24 24" width="70" height="70"><path d="M8 5v14l11-7z" fill="#fff"/></svg></span>""",
        js="""$('#pk').style.transform = `rotate(${3 * Math.sin(t * 1.5)}deg) scale(${back((t - .2) / .6)})`;
$('#play').style.transform = `scale(${back((t - .8) / .5) * (1 + .08 * Math.max(0, Math.sin(t * 6)))})`;""",
        hits=[("pop", .2), ("pop", .8), ("pop", 3.0)]),
    # 7. Week recap: three reel covers shuffle like cards.
    "2026-11-06-resumo": dict(theme="forest", total=7.0, arrow="Os 3 estão no perfil", arrow_at=4.2, arrow_css="background:#F4C542;color:#0F3D2E",
        lines=[("3 reels esta semana.", 150, {"3", "reels"}, 0, 7.0, .3)],
        css=".card{top:900px;width:380px;outline:5px solid #F3EFE6}",
        html="".join(f'<div class="peek card" id="c{i}" style="left:350px"><img src="{thumb(POSTS / p)}"></div>' for i, p in enumerate(
            ["2026-11-05-onde-esta-a-encomenda/reel/cover.jpg", "2026-11-04-quanto-tempo/reel/cover.jpg", "2026-11-mockup-gratuito/reel/cover.jpg"])),
        js="""[0, 1, 2].forEach(i => { const a = .5 + .5 * i, k = back((t - a) / .55), sp = ease((t - 2.4) / .6);
  const x = (i - 1) * 330 * sp, r = (i - 1) * 9 * sp + (1 - k) * 30;
  $('#c' + i).style.transform = `translate(${x}px,${(1 - k) * 600 + Math.abs(i - 1) * 40 * sp}px) rotate(${r}deg) scale(${.8 + .2 * k - .12 * sp})`;
  $('#c' + i).style.opacity = cl((t - a) / .1); $('#c' + i).style.zIndex = i === 1 ? 3 : 2; });""",
        hits=[("whoosh", .45), ("whoosh", .95), ("whoosh", 1.45), ("pop", 2.4), ("pop", 4.2)]),
    # 8. "Saiu hoje": a calendar flips through the days and lands on a question mark.
    "2026-11-04-saiu": dict(theme="lilac", total=6.5, arrow="A resposta está no perfil", arrow_at=3.6, arrow_css="background:#1A1033;color:#fff",
        lines=[("Quanto tempo demora um site?", 130, {"tempo"}, 0, 6.5, .3)],
        css="""#cal{left:230px;top:1010px;width:620px;height:660px;border-radius:40px;background:#fff;overflow:hidden;box-shadow:0 50px 100px -30px rgba(26,16,51,.6)}
#cal .b{height:130px;background:#3A12A8}
#cal .r{position:absolute;top:-30px;width:34px;height:100px;border-radius:17px;background:#1A1033;border:6px solid #fff}
#day{left:0;right:0;top:150px;text-align:center;color:#1A1033;font-size:380px;font-weight:800;letter-spacing:-.05em;font-variant-numeric:tabular-nums}""",
        html='<div id="cal"><div class="b"></div><span class="r" style="left:150px"></span><span class="r" style="right:150px"></span><div id="day">1</div></div>',
        js="""$('#day').textContent = t < 2.6 ? String(Math.floor(t * 12) % 30 + 1) : '?';
$('#day').style.color = t < 2.6 ? '#1A1033' : '#3A12A8';
$('#cal').style.transform = `rotate(${-3 + 2 * Math.sin(t * 2)}deg) scale(${back((t - .2) / .5) * (t > 2.6 && t < 2.8 ? 1.06 : 1)})`;""",
        hits=[("pop", .2)] + [("click", .4 + .18 * i) for i in range(12)] + [("thump", 2.6), ("pop", 3.6)]),
    # 9. "Saiu hoje": a timer reaches five minutes, gets struck out, and the order turns up at once.
    "2026-11-05-saiu": dict(theme="receipt", total=6.5, arrow="Veja como no perfil", arrow_at=4.0, arrow_css="background:#111;color:#fff",
        lines=[("5 minutos.", 190, {"minutos."}, 0, 2.8, .3), ("Ou 5 segundos.", 170, {"segundos."}, 2.8, 6.5, 2.9)],
        css="""#ctr{left:0;right:0;top:860px;text-align:center;font-size:290px;font-weight:700;letter-spacing:-.06em;color:#111;font-variant-numeric:tabular-nums}
#cut{left:120px;top:1010px;width:840px;height:22px;background:#D7263D;transform-origin:left center}
#ok{left:130px;right:130px;top:1240px;padding:48px 54px;border-radius:24px;background:#111;color:#FBFAF6;font-size:60px;font-weight:700;opacity:0}
#ok small{display:block;margin-top:14px;font-size:40px;font-weight:400;color:#bdbdbd}""",
        html='<div id="ctr">00:00</div><span id="cut"></span><div id="ok">✓ Encomenda encontrada<small>Cliente: Silva</small></div>',
        js="""const s = Math.min(300, Math.floor(t * 115));
$('#ctr').textContent = String(Math.floor(s / 60)).padStart(2, '0') + ':' + String(s % 60).padStart(2, '0');
$('#ctr').style.opacity = 1 - .75 * cl((t - 3.0) / .3);
$('#cut').style.transform = `rotate(-3deg) scaleX(${ease((t - 2.7) / .25)})`;
pop($('#ok'), t, 3.3);""",
        hits=[("click", .4 + .25 * i) for i in range(9)] + [("thump", 2.7), ("whoosh", 2.9), ("pop", 3.3), ("pop", 4.0)]),
    # 10. "Saiu hoje": a phone and a website collide, with VS between them.
    "2026-11-07-saiu": dict(theme="blue", total=6.5, arrow="A resposta está no perfil", arrow_at=3.6, arrow_css="background:#FFD84D;color:#121125",
        lines=[("Tenho Instagram. Preciso de um site?", 116, {"site?"}, 0, 6.5, .3)],
        css="""#ph{left:110px;top:960px;width:310px;height:580px;box-sizing:border-box;padding:60px 18px;border-radius:52px;background:#121125;border:10px solid #fff;display:grid;grid-template-columns:repeat(3,1fr);gap:8px;align-content:start}
#ph i{aspect-ratio:1;border-radius:8px;background:linear-gradient(135deg,#EF5AFE,#4877FE)}
#wn{left:500px;top:1040px;width:470px;height:410px;border-radius:24px;background:#fff;overflow:hidden;box-shadow:0 50px 100px -30px rgba(10,20,80,.7)}
#wn .b{height:50px;background:#dbe5ff}#wn .h{margin:26px;height:170px;border-radius:16px;background:#265ADF}#wn .l{margin:0 26px 16px;height:24px;border-radius:12px;background:#dbe5ff}
#vs{left:360px;top:1150px;width:200px;height:200px;border-radius:50%;background:#FFD84D;color:#121125;display:grid;place-items:center;font-size:92px;font-weight:800;opacity:0;z-index:3}""",
        html=f"""<div id="ph">{'<i></i>' * 9}</div><div id="wn"><div class="b"></div><div class="h"></div><div class="l" style="width:70%"></div><div class="l" style="width:45%"></div></div><div id="vs">VS</div>""",
        js="""const k = ease((t - .5) / .7), sh = t > 1.2 && t < 1.5 ? 10 * Math.sin(t * 90) : 0;
$('#ph').style.transform = `translate(${-620 * (1 - k) + sh}px,${sh / 2}px) rotate(-4deg)`;
$('#wn').style.transform = `translate(${620 * (1 - k) - sh}px,${-sh / 2}px) rotate(3deg)`;
pop($('#vs'), t, 1.25);""",
        hits=[("whoosh", .5), ("thump", 1.2), ("pop", 1.25), ("pop", 3.6)]),
    # 11. "Saiu hoje": five answers tick themselves and the score stays blurred.
    "2026-11-08-saiu": dict(theme="paper", total=7.0, arrow="Faça o teste no perfil", arrow_at=4.4, arrow_css="background:#121125;color:#F6F1E7",
        lines=[("Teste de 30 segundos.", 150, {"segundos."}, 0, 7.0, .3)],
        css="""#list{left:110px;right:110px;top:860px}
.q{display:flex;align-items:center;gap:30px;height:118px;border-bottom:3px solid #e0d8c6;font-size:46px;font-weight:600;color:#121125;opacity:0}
.q b{flex:none;width:68px;height:68px;box-sizing:border-box;border:6px solid #265ADF;border-radius:16px;display:grid;place-items:center;color:#fff;font-size:46px}
#res{left:110px;right:110px;top:1500px;padding:34px 40px;border-radius:24px;background:#121125;color:#F6F1E7;font-size:52px;font-weight:700;text-align:center;opacity:0}
#res span{display:inline-block;filter:blur(16px)}""",
        html='<div id="list">' + "".join(f'<div class="q" id="q{i}"><b id="k{i}">✓</b>{q}</div>' for i, q in enumerate(
            ["Abre em 3 segundos?", "Horário à vista?", "Lê-se sem zoom?", "Aparece no Google?", "Atualizado?"])) + '</div><div id="res">O seu resultado: <span>3 em 5</span></div>',
        js="""[0, 1, 2, 3, 4].forEach(i => { const a = .7 + .45 * i, on = t > a + .25;
  $('#q' + i).style.opacity = cl((t - a) / .2); $('#q' + i).style.transform = `translateX(${60 * (1 - ease((t - a) / .3))}px)`;
  $('#k' + i).style.background = on ? '#265ADF' : 'transparent'; });
pop($('#res'), t, 3.2);""",
        hits=[("pop", .95 + .45 * i) for i in range(5)] + [("thump", 3.2), ("pop", 4.4)]),
}


def build(name, s):
    work = ROOT / "reels" / f"story-{name}"
    work.mkdir(parents=True, exist_ok=True)
    scenes = [{"words": [(w, round(first + .26 * i, 3), 0) for i, w in enumerate(text.split())], "size": size, "em": em, "start": a, "end": b}
              for text, size, em, a, b, first in s["lines"]]
    art = s["html"] + ARROW.format(label=s["arrow"])
    js = ARROW_JS + "function art(t, E) {\n" + s["js"] + f"\narrowAt(t, {s['arrow_at']});\n}}"
    css = BASE_CSS + f"#arrow{{{s['arrow_css']}}}" + s["css"]
    page = HERE / name / "story.html"
    page.parent.mkdir(exist_ok=True)
    page.write_text(reelkit.page(scenes, {}, art, css, js, theme=s["theme"]), encoding="utf-8")
    silent = work / "silence.mp3"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono", "-t", str(s["total"]), str(silent)], check=True)
    bgm = music(s["total"] + .5, work / "music.wav") if s.get("music") else None
    reelkit.render(page, work, s["total"], silent, s["hits"], HERE / name / "story.mp4", music=bgm, music_vol=.3)
    print(name, "ok")


if __name__ == "__main__":
    reelkit.SFX.update(SPOOKY)
    for name in sys.argv[1:] or STORIES:
        build(name, STORIES[name])
