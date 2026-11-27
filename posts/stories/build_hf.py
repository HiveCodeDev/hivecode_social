"""HyperFrames versions of the animated stories (no voice): hook title, art, arrow to the profile, logo outro.

python posts/stories/build_hf.py [name ...]   -> posts/stories/<name>/story-hf.mp4
Each entry: theme, title lines [(text, size, {em}, start, end)], arrow (label, at, css), html/css/js (GSAP on `tl`),
hits [(sound, s)]. Body length BODY, then a 1.6 s outro (blur, logo, hivecode.pt).
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import hfkit  # noqa: E402

BODY, OUTRO = 6.5, 1.6
TOTAL = BODY + OUTRO
Y, K = "#FFD400", "#0A0A0A"

STORIES = {
    # 25/11 "saiu hoje": the crossed-out price has rules (carousel). A price tag swings on its string,
    # the old price gets struck through, then a red "?" stamp lands.
    "2026-11-25-saiu": dict(
        theme="canvas", title=[("O preço riscado tem regras.", 130, {"regras."}, 0, BODY)],
        arrow=("Veja as regras no perfil", 3.6, "background:#9B3CF0;color:#fff"),
        css="""#tg{position:absolute;left:190px;top:900px;width:700px;padding:60px 60px 56px 110px;border-radius:28px 60px 60px 28px;background:#fff;
 border:6px solid #121125;box-shadow:0 40px 80px -30px rgba(18,17,37,.45);white-space:nowrap;transform-origin:0 50%}
#tg:before{content:"";position:absolute;left:40px;top:50%;width:34px;height:34px;margin-top:-17px;border-radius:50%;border:6px solid #121125;background:#F4F2FA}
#str{position:absolute;left:-40px;top:50%;width:200px;height:6px;margin-top:-3px;background:#121125;transform-origin:100% 50%;transform:translateX(-100%) rotate(-20deg)}
#old{position:relative;display:inline-block;font-size:70px;color:#8a879c}
#cut{position:absolute;left:-6px;right:-6px;top:50%;height:8px;margin-top:-4px;background:#D7263D;border-radius:4px;transform-origin:0 50%}
#new{display:block;margin-top:10px;font-size:150px;font-weight:800;line-height:1;color:#121125;letter-spacing:-.03em}
#q{position:absolute;left:770px;top:840px;width:140px;height:140px;border-radius:50%;background:#D7263D;color:#fff;display:grid;place-items:center;font-size:96px;font-weight:800}
#qr{position:absolute;left:770px;top:840px;width:140px;height:140px;border-radius:50%;border:6px solid #D7263D}""",
        html='<div id="tg"><span id="str"></span><span id="old">50,00 €<i id="cut"></i></span><span id="new">36,00 €</span></div><span id="qr"></span><span id="q">?</span>',
        js="""tl.fromTo("#tg", { rotate: -28, opacity: 0, y: -200 }, { rotate: 0, opacity: 1, y: 0, duration: 1.1, ease: "elastic.out(1, .45)" }, .25);
tl.fromTo("#cut", { scaleX: 0 }, { scaleX: 1, duration: .3, ease: "power3.inOut" }, 1.0);
tl.fromTo("#new", { scale: 1.3, color: "#D7263D" }, { scale: 1, color: "#121125", duration: .5, ease: "back.out(2)" }, 1.25);
tl.fromTo("#q", { scale: 3, opacity: 0, rotate: -40 }, { scale: 1, opacity: 1, rotate: 12, duration: .25, ease: "power4.in" }, 1.6);
tl.fromTo("#qr", { scale: 1, opacity: .9 }, { scale: 2.4, opacity: 0, duration: .6, ease: "power2.out" }, 1.85);
tl.fromTo("#tg", { x: 0 }, { x: 8, duration: .05, yoyo: true, repeat: 3, ease: "none", immediateRender: false }, 1.85);""",
        hits=[("whoosh", .25), ("click", 1.0), ("pop", 1.25), ("thump", 1.85), ("pop", 3.6)]),

    # 26/11 "amanhã": a yellow box drops, shakes, and its lid blows off with light rays.
    "2026-11-26-amanha": dict(
        theme="blackfriday", title=[("Amanhã: Black Friday na HiveCode.", 124, {"Black", "Friday"}, 0, BODY)],
        arrow=("Siga o perfil", 3.8, f"background:{Y};color:{K}"),
        css=f"""#rays{{position:absolute;left:40px;top:700px;width:1000px;height:1000px;border-radius:50%;
 background:repeating-conic-gradient(rgba(255,212,0,.32) 0 8deg,transparent 8deg 22deg);-webkit-mask-image:radial-gradient(circle,#000 20%,transparent 68%)}}
#bx{{position:absolute;left:290px;top:980px;width:500px;height:460px;border-radius:40px;background:{Y};display:grid;place-items:center;
 font-family:'Archivo Black',sans-serif;font-size:280px;color:{K};line-height:1;transform-origin:50% 100%}}
#bx:before{{content:"";position:absolute;left:220px;top:0;width:60px;height:100%;background:{K};opacity:.85}}
#bx span{{position:relative}}
#lid{{position:absolute;left:260px;top:910px;width:560px;height:110px;border-radius:30px;background:#fff}}
#lid:before{{content:"";position:absolute;left:250px;top:0;width:60px;height:100%;background:{K};opacity:.85}}""",
        html='<span id="rays"></span><div id="bx"><span id="qm">?</span></div><div id="lid"></div>',
        js="""tl.fromTo(["#bx", "#lid"], { y: -900 }, { y: 0, duration: .6, ease: "bounce.out" }, .2);
tl.fromTo("#bx", { scaleY: 1 }, { scaleY: .9, duration: .08, yoyo: true, repeat: 1 }, .55);
tl.fromTo(["#bx", "#lid"], { rotate: 0 }, { rotate: 5, duration: .07, yoyo: true, repeat: 11, ease: "none", immediateRender: false }, 1.5);
tl.fromTo("#lid", { y: 0, rotate: 0, x: 0 }, { y: -520, x: 260, rotate: 70, opacity: 0, duration: .6, ease: "power2.out", immediateRender: false }, 2.5);
tl.fromTo("#rays", { scale: .3, opacity: 0, rotate: 0 }, { scale: 1, opacity: 1, rotate: 40, duration: 1.2, ease: "power2.out" }, 2.5);
tl.fromTo("#rays", { rotate: 40 }, { rotate: 120, duration: 4, ease: "none", immediateRender: false }, 3.7);
tl.fromTo("#qm", { scale: 1 }, { scale: 1.25, duration: .25, yoyo: true, repeat: 1, ease: "power2.out" }, 2.55);""",
        hits=[("whoosh", .2), ("thump", .6), ("click", 1.55), ("click", 1.85), ("click", 2.15), ("rise", 2.45), ("pop", 3.8)]),

    # 27/11 "saiu hoje": a site window builds; a -20% stamp slams with a flash and a shake.
    "2026-11-27-saiu": dict(
        theme="natalnoite", title=[("Saiu hoje: mega campanha Black Friday + Natal.", 112, {"mega", "campanha"}, 0, BODY)],
        arrow=("Acompanhe o perfil", 3.6, "background:#F2C14E;color:#0E1A33"),
        css="""#shk{position:absolute;inset:0}
.tg{position:absolute;top:1000px;padding:34px 44px;border-radius:26px;font-family:'Archivo Black',sans-serif;font-size:66px;line-height:1;box-shadow:0 40px 90px -30px rgba(0,0,0,.7)}
#tb{left:110px;background:#0A0A0A;color:#F2C14E;border:8px solid #F2C14E}
#tn{right:110px;background:#C41E3A;color:#fff;border:8px solid #fff}
#pl{position:absolute;left:0;right:0;top:1040px;text-align:center;font-size:140px;font-weight:900;color:#F2C14E}
#mc{position:absolute;left:220px;top:1300px;width:640px;padding:24px 0;border:10px solid #F2C14E;border-radius:24px;background:#0E1A33;color:#F2C14E;
 text-align:center;font-family:'Archivo Black',sans-serif;font-size:66px}""",
        html='<div id="shk"><div class="tg" id="tb">BLACK<br>FRIDAY</div><div class="tg" id="tn">NATAL<br>🎄</div><div id="pl">+</div><div id="mc">MEGA CAMPANHA</div></div>',
        js="""tl.fromTo("#tb", { x: -700, rotate: -12 }, { x: 0, rotate: -4, duration: .45, ease: "expo.out" }, .2);
tl.fromTo("#tn", { x: 700, rotate: 12 }, { x: 0, rotate: 4, duration: .45, ease: "expo.out" }, .45);
tl.fromTo("#pl", { scale: 0 }, { scale: 1, duration: .35, ease: "back.out(3)" }, .8);
tl.fromTo("#mc", { scale: 2.6, rotate: -14, opacity: 0 }, { scale: 1, rotate: -5, opacity: 1, duration: .3, ease: "power4.in" }, 1.2);
tl.fromTo("#shk", { x: 0, y: 0 }, { x: 14, y: -10, duration: .05, yoyo: true, repeat: 5, ease: "none" }, 1.5);""",
        hits=[("whoosh", .2), ("whoosh", .45), ("pop", .8), ("thump", 1.5), ("pop", 3.6)]),

    # 28/11 (the 20% offer was cancelled): campaign, send us a message. A chat thread fills in, the reply
    # bubble pops, then a gold "ENVIE-NOS MENSAGEM" button lands.
    "2026-11-28-oferta": dict(
        theme="natal", title=[("Mega campanha: fale connosco.", 120, {"fale", "connosco."}, 0, BODY)],
        arrow=("Envie mensagem pelo perfil", 3.8, "background:#C41E3A;color:#fff"),
        css="""#ph{position:absolute;left:190px;top:900px;width:700px;height:600px;border-radius:50px;background:#fff;box-shadow:0 50px 120px -40px rgba(60,30,20,.45);overflow:hidden}
#ph .hd{display:flex;align-items:center;gap:22px;padding:26px 34px;background:#0F3A2C;color:#fff;font-size:40px;font-weight:800}
#ph .hd img{width:70px;height:70px;border-radius:50%;background:#fff;padding:12px;box-sizing:border-box}
.bb{position:absolute;padding:24px 34px;border-radius:36px;font-size:44px;font-weight:700;line-height:1.15}
#b1{left:34px;top:160px;background:#eef0f3;color:#1d1d1d;border-bottom-left-radius:8px}
#b2{right:34px;top:280px;background:#C41E3A;color:#fff;border-bottom-right-radius:8px}
#dots{position:absolute;left:34px;top:480px;padding:22px 30px;border-radius:30px;background:#eef0f3;display:flex;gap:12px}
#dots i{width:18px;height:18px;border-radius:50%;background:#8a8f99}""",
        html='<div id="ph"><div class="hd"><img src="assets/logo_mark.svg" alt="">HiveCode</div>'
             '<div class="bb" id="b1">Olá! Quero saber mais 👋</div><div class="bb" id="b2">Claro! Conte-nos o seu projeto.</div>'
             '<div id="dots"><i></i><i></i><i></i></div></div>',
        js="""tl.fromTo("#ph", { y: 400, opacity: 0, rotate: 5 }, { y: 0, opacity: 1, rotate: 0, duration: .6, ease: "back.out(1.5)" }, .2);
tl.fromTo("#b1", { scale: 0, transformOrigin: "0 100%" }, { scale: 1, duration: .4, ease: "back.out(2.4)" }, .9);
tl.fromTo("#b2", { scale: 0, transformOrigin: "100% 100%" }, { scale: 1, duration: .4, ease: "back.out(2.4)" }, 1.8);
tl.fromTo("#dots", { opacity: 0 }, { opacity: 1, duration: .2 }, 2.6);
tl.fromTo("#dots i", { y: 0 }, { y: -12, duration: .25, stagger: .1, yoyo: true, repeat: 7, ease: "sine.inOut" }, 2.6);""",
        hits=[("whoosh", .2), ("pop", .9), ("pop", 1.8), ("click", 2.6), ("pop", 3.8)]),

    # 29/11 (the 20% offer was cancelled): the campaign keeps going. A Follow button flips to "A seguir",
    # a bell rings for notifications, gold "BLACK FRIDAY + NATAL" ribbon.
    "2026-11-29-ultimo": dict(
        theme="natalverde", title=[("A mega campanha continua.", 124, {"continua."}, 0, BODY)],
        arrow=("Siga o perfil", 3.8, "background:#E8B84A;color:#0F3A2C"),
        css="""#fb{position:absolute;left:240px;top:930px;width:600px;height:150px;border-radius:40px;overflow:hidden;font-size:62px;font-weight:800}
#fb span{position:absolute;inset:0;display:grid;place-items:center}
#f1{background:#265ADF;color:#fff}#f2{background:#F5EEDD;color:#0F3A2C}
#bell{position:absolute;left:470px;top:1120px;font-size:140px;transform-origin:50% 10%}
#rib{position:absolute;left:150px;right:150px;top:1340px;padding:26px 0;border-radius:20px;background:#E8B84A;color:#0F3A2C;text-align:center;
 font-family:'Archivo Black',sans-serif;font-size:52px}""",
        html='<div id="fb"><span id="f1">Seguir</span><span id="f2">A seguir ✓</span></div><span id="bell">🔔</span><div id="rib">BLACK FRIDAY + NATAL</div>',
        js="""tl.fromTo("#fb", { scale: 0, opacity: 0 }, { scale: 1, opacity: 1, duration: .45, ease: "back.out(2)" }, .2);
tl.fromTo("#fb", { scale: 1 }, { scale: .9, duration: .1, yoyo: true, repeat: 1, ease: "power2.out", immediateRender: false }, 1.0);
tl.fromTo("#f2", { y: 150 }, { y: 0, duration: .3, ease: "power3.out" }, 1.1);
tl.fromTo("#bell", { scale: 0 }, { scale: 1, duration: .4, ease: "back.out(2.5)" }, 1.6);
tl.fromTo("#bell", { rotate: -18 }, { rotate: 18, duration: .08, yoyo: true, repeat: 9, ease: "sine.inOut", immediateRender: false }, 2.0);
tl.fromTo("#rib", { scaleX: 0 }, { scaleX: 1, duration: .5, ease: "expo.out" }, 2.6);""",
        hits=[("pop", .2), ("click", 1.0), ("pop", 1.6), ("click", 2.0), ("click", 2.3), ("whoosh", 2.6), ("pop", 3.8)]),

    # 30/11: November page flips over to December 1, snow falling.
    "2026-11-30-amanha": dict(
        theme="natal", title=[("Dezembro começa amanhã.", 140, {"Dezembro"}, 0, BODY)],
        arrow=("Siga o perfil", 3.8, "background:#C41E3A;color:#fff"),
        css="""#pg{position:absolute;left:290px;top:930px;width:500px;height:560px;border-radius:36px;background:#fff;text-align:center;
 box-shadow:0 50px 100px -40px rgba(15,59,44,.5);perspective:1400px}
#pg .m{height:120px;display:grid;place-items:center;font-size:48px;font-weight:800;letter-spacing:.1em;color:#fff;border-radius:36px 36px 0 0}
#pg .d{font-size:300px;font-weight:800;line-height:1.3;color:#0F3B2C}
#a,#b{position:absolute;inset:0;border-radius:36px;background:#fff;overflow:hidden;backface-visibility:hidden}
#a{transform-origin:50% 0}#a .m{background:#6f8a7d}#b .m{background:#C41E3A}""",
        html='<div id="pg"><div id="b"><div class="m">DEZEMBRO</div><div class="d">1</div></div><div id="a"><div class="m">NOVEMBRO</div><div class="d">30</div></div></div>',
        js="""tl.fromTo("#pg", { y: 300, opacity: 0 }, { y: 0, opacity: 1, duration: .6, ease: "back.out(1.6)" }, .2);
tl.fromTo("#a", { rotateX: 0 }, { rotateX: -2, duration: .08, yoyo: true, repeat: 5, ease: "none" }, 1.1);
tl.fromTo("#a", { rotateX: 0, opacity: 1 }, { rotateX: 110, opacity: 0, duration: .8, ease: "power2.in", immediateRender: false }, 1.6);
tl.fromTo("#b .d", { scale: .6 }, { scale: 1, duration: .5, ease: "back.out(3)" }, 2.3);""",
        hits=[("whoosh", .2), ("click", 1.1), ("click", 1.35), ("whoosh", 1.6), ("pop", 2.3), ("pop", 3.8)]),

    # 1/12 "saiu hoje": an advent door "1" opens onto the four dates of the reel.
    "2026-12-01-saiu": dict(
        theme="natal", title=[("Abriu dezembro.", 170, {"dezembro."}, 0, 2.7), ("4 datas que contam.", 140, {"4", "datas"}, 2.7, BODY)],
        arrow=("Veja o reel no perfil", 4.4, "background:#C41E3A;color:#fff"),
        css="""#fr{position:absolute;left:190px;top:880px;width:700px;height:760px;border-radius:40px;background:#0F3B2C;padding:26px;
 box-shadow:0 60px 120px -40px rgba(15,59,44,.6);perspective:1600px}
#in{position:absolute;inset:26px;border-radius:24px;background:#F5EEE2;display:grid;grid-template-columns:1fr 1fr;gap:26px;padding:40px}
.tg{border-radius:24px;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff}
.tg b{font-size:130px;font-weight:800;line-height:1}.tg small{margin-top:8px;font-size:30px;font-weight:700;letter-spacing:.06em}
#dr{position:absolute;inset:26px;border-radius:24px;background:#C41E3A;transform-origin:0 50%;display:grid;place-items:center;backface-visibility:hidden;
 background-image:radial-gradient(circle at 50% 50%,rgba(255,255,255,.12) 0 220px,transparent 221px);border:10px solid #F2B233}
#dr b{font-family:'Playfair Display',serif;font-style:italic;font-weight:700;font-size:400px;color:#F2B233;line-height:1}
#dr i{position:absolute;right:40px;top:50%;width:34px;height:34px;margin-top:-17px;border-radius:50%;background:#F2B233}
#glw{position:absolute;inset:26px;border-radius:24px;background:radial-gradient(circle,rgba(242,178,51,.9),transparent 70%)}""",
        html='<div id="fr"><div id="in">' + "".join(f'<div class="tg" id="g{i}" style="background:{c}"><b>{d}</b><small>{s}</small></div>' for i, (d, s, c) in enumerate(
            [("8", "FERIADO", "#C41E3A"), ("24", "HORÁRIO", "#0F3B2C"), ("26", "TROCAS", "#0F3B2C"), ("31", "HORÁRIO", "#C41E3A")]))
            + '</div><span id="glw"></span><div id="dr"><b>1</b><i></i></div></div>',
        js="""tl.fromTo("#fr", { scale: .6, opacity: 0 }, { scale: 1, opacity: 1, duration: .55, ease: "back.out(1.8)" }, .2);
tl.fromTo("#dr", { rotateY: 0 }, { rotateY: -4, duration: .07, yoyo: true, repeat: 7, ease: "none" }, 1.2);
tl.fromTo("#dr", { rotateY: 0 }, { rotateY: -115, duration: .9, ease: "power3.inOut", immediateRender: false }, 1.8);
tl.fromTo("#glw", { opacity: 0 }, { opacity: 1, duration: .3, yoyo: true, repeat: 1 }, 2.0);
tl.fromTo(".tg", { scale: 0, rotate: -12 }, { scale: 1, rotate: 0, duration: .45, stagger: .3, ease: "back.out(2.4)" }, 2.4);""",
        hits=[("pop", .2), ("click", 1.3), ("click", 1.6), ("whoosh", 1.8)] + [("pop", 2.4 + .3 * i) for i in range(4)] + [("pop", 4.4)]),

    # 3/12 "saiu hoje": a gold knife line wipes the pencil sketch into the bakery site and back, then settles on the site.
    "2026-12-03-saiu": dict(
        theme="natalnoite", title=[("Do esboço ao site.", 150, {"site."}, 0, BODY)],
        arrow=("Veja o reel no perfil", 3.8, "background:#F2C14E;color:#0E1A33"),
        css="""#ba{position:absolute;left:170px;top:960px;width:740px;height:520px;border-radius:26px;overflow:hidden;box-shadow:0 60px 120px -40px rgba(242,193,78,.35)}
#sk2{position:absolute;inset:0;background:#FBF8F1;background-image:linear-gradient(#e7e1d3 2px,transparent 2px);background-size:100% 46px}
#sk2 svg{position:absolute;inset:0}#sk2 path{fill:none;stroke:#3b3b46;stroke-width:5;stroke-linecap:round}
#st2{position:absolute;inset:0;background:#fff}
#st2 .h{position:absolute;left:30px;right:30px;top:90px;height:210px;border-radius:18px;background:linear-gradient(160deg,#f6c98a,#d98b4a 55%,#8a4b2a)}
#st2 .n{position:absolute;left:34px;top:30px;font-size:30px;font-weight:800;color:#3d2a1e}
#st2 .t{position:absolute;left:30px;top:336px;font-size:34px;font-weight:800;color:#3d2a1e}
#st2 .b{position:absolute;left:30px;top:400px;width:200px;height:70px;border-radius:14px;background:#3d2a1e;color:#fff;display:grid;place-items:center;font-size:26px;font-weight:700}
#st2 .c{position:absolute;left:440px;top:340px;width:266px;height:140px;border-radius:16px;background:linear-gradient(150deg,#f3d9a4,#d9a05a)}
#kn{position:absolute;left:170px;top:960px;width:8px;height:520px;margin-left:-4px;background:#F2C14E;box-shadow:0 0 30px rgba(242,193,78,.8)}""",
        html='<div id="ba"><div id="sk2"><svg viewBox="0 0 740 520">' + "".join(f'<path d="{d}" pathLength="1"/>' for d in [
            "M34,40 Q370,30 706,44", "M30,90 L708,92 L704,300 L32,296 Z", "M40,100 L696,290 M696,100 L40,290", "M30,340 Q200,336 380,344",
            "M30,400 L230,402 L228,470 L32,468 Z", "M440,340 L706,342 L704,480 L442,478 Z"])
            + '</svg></div><div id="st2"><span class="n">Padaria do Largo</span><span class="h"></span><span class="t">Feito aqui, desde 1987</span>'
            '<span class="b">Encomendar</span><span class="c"></span></div></div><span id="kn"></span>',
        js="""tl.fromTo("#ba", { scale: .6, opacity: 0 }, { scale: 1, opacity: 1, duration: .5, ease: "back.out(1.8)" }, .2);
tl.fromTo("#sk2 path", { strokeDasharray: 1, strokeDashoffset: 1 }, { strokeDashoffset: 0, duration: .3, stagger: .1, ease: "power2.out" }, .3);
const W = { w: 0 };
const paint = () => { document.querySelector("#st2").style.clipPath = `inset(0 ${100 * (1 - W.w)}% 0 0)`;
  const k = document.querySelector("#kn"); k.style.transform = `translateX(${740 * W.w}px)`; k.style.opacity = W.w > .01 && W.w < .99 ? 1 : 0; };
tl.fromTo(W, { w: 0 }, { w: 1, duration: 1.2, ease: "power2.inOut", onUpdate: paint }, 1.0);
tl.fromTo(W, { w: 1 }, { w: .6, duration: .5, ease: "power2.inOut", onUpdate: paint, immediateRender: false }, 2.4);
tl.fromTo(W, { w: .6 }, { w: 1, duration: .5, ease: "power2.inOut", onUpdate: paint, immediateRender: false }, 3.1);""",
        hits=[("pop", .2), ("click", .3), ("click", .5), ("click", .7), ("whoosh", 1.0), ("whoosh", 2.4), ("pop", 3.8)]),

    # 4/12: a red gift box with "?" bounces and shakes; question for the profile.
    "2026-12-04-pergunta": dict(
        theme="neve", title=[("O que oferecer a quem tem tudo?", 124, {"tudo?"}, 0, BODY)],
        arrow=("Siga o perfil", 3.8, "background:#10233F;color:#fff"),
        css="""#bx{position:absolute;left:290px;top:1000px;width:500px;height:440px;border-radius:40px;background:#C41E3A;display:grid;place-items:center;
 font-size:260px;font-weight:800;color:#fff;line-height:1;transform-origin:50% 100%}
#bx:before{content:"";position:absolute;left:220px;top:0;width:60px;height:100%;background:#FFD84D}
#bx span{position:relative}
#lid{position:absolute;left:260px;top:920px;width:560px;height:120px;border-radius:30px;background:#a3172f;transform-origin:50% 100%}
#lid:before{content:"";position:absolute;left:250px;top:0;width:60px;height:100%;background:#FFD84D}
#bow{position:absolute;left:470px;top:850px;width:140px;height:90px}""",
        html='<div id="bx"><span id="qm">?</span></div><div id="lid"></div><svg id="bow" viewBox="0 0 140 90"><ellipse cx="38" cy="45" rx="36" ry="24" fill="#FFD84D"/>'
             '<ellipse cx="102" cy="45" rx="36" ry="24" fill="#FFD84D"/><circle cx="70" cy="50" r="16" fill="#e8b52f"/></svg>',
        js="""tl.fromTo(["#bx", "#lid", "#bow"], { y: -900 }, { y: 0, duration: .65, stagger: .04, ease: "bounce.out" }, .2);
tl.fromTo(["#bx", "#lid", "#bow"], { rotate: 0 }, { rotate: 5, duration: .07, yoyo: true, repeat: 13, ease: "none", immediateRender: false }, 1.3);
tl.fromTo("#lid", { y: 0 }, { y: -30, duration: .12, yoyo: true, repeat: 3, ease: "power2.out", immediateRender: false }, 2.4);
tl.fromTo("#qm", { scale: 1, rotate: 0 }, { scale: 1.2, rotate: 10, duration: .3, yoyo: true, repeat: 3, ease: "sine.inOut" }, 2.5);""",
        hits=[("whoosh", .2), ("thump", .65), ("click", 1.35), ("click", 1.7), ("click", 2.05), ("pop", 2.5), ("pop", 3.8)]),

    # 5/12 "saiu hoje": a red voucher swings in on a ribbon and a shine sweeps across it.
    "2026-12-05-saiu": dict(
        theme="neve", title=[("Vales-oferta no seu site.", 140, {"Vales-oferta"}, 0, BODY)],
        arrow=("Veja o reel no perfil", 3.8, "background:#10233F;color:#fff"),
        css="""#vc{position:absolute;left:190px;top:1000px;width:700px;height:420px;border-radius:40px;background:#C41E3A;color:#fff;padding:54px 60px;
 box-shadow:0 50px 100px -30px rgba(16,35,63,.45);overflow:hidden;transform-origin:50% -200px}
#vc small{display:block;font-size:32px;font-weight:700;letter-spacing:.14em;opacity:.8}
#vc strong{display:block;margin-top:24px;font-size:84px;font-weight:800;line-height:1}
#vc b{position:absolute;left:60px;bottom:50px;font-size:70px;font-weight:800;color:#FFD84D}
#rb{position:absolute;right:120px;top:0;width:70px;height:100%;background:#FFD84D}
#sh{position:absolute;top:0;left:0;width:160px;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.4),transparent)}""",
        html='<div id="vc"><span id="rb"></span><small>VALE-OFERTA</small><strong>Jantar<br>para dois</strong><b>50 €</b><span id="sh"></span></div>',
        js="""tl.fromTo("#vc", { rotate: -40, opacity: 0, y: -300 }, { rotate: -4, opacity: 1, y: 0, duration: 1.2, ease: "elastic.out(1, .4)" }, .2);
tl.fromTo("#sh", { x: -200, skewX: -20 }, { x: 900, skewX: -20, duration: .8, ease: "power2.inOut" }, 1.4);
tl.fromTo("#sh", { x: -200 }, { x: 900, duration: .8, ease: "power2.inOut", immediateRender: false }, 3.0);
tl.fromTo("#vc b", { scale: 1 }, { scale: 1.2, duration: .2, yoyo: true, repeat: 1, ease: "power2.out" }, 1.8);""",
        hits=[("whoosh", .2), ("whoosh", 1.4), ("pop", 1.8), ("pop", 3.8)]),

    # 6/12: countdown 30 -> 19 days to Christmas, digits flipping, then a gold burst.
    "2026-12-06-natal": dict(
        theme="natal", title=[("Natal", 190, {"Natal"}, 0, BODY)],
        arrow=("Siga o perfil", 3.8, "background:#C41E3A;color:#fff"),
        css="""#fal{position:absolute;left:0;right:0;top:940px;text-align:center;font-size:64px;font-weight:700;color:#0F3B2C}
#ctr{position:absolute;left:0;right:0;top:1020px;text-align:center;font-size:460px;font-weight:900;color:#C41E3A;letter-spacing:-.06em;line-height:1;font-variant-numeric:tabular-nums}
#dias{position:absolute;left:0;right:0;top:1500px;text-align:center;font-size:90px;font-weight:800;color:#0F3B2C;letter-spacing:.06em}
#burst{position:absolute;left:240px;top:960px;width:600px;height:600px;border-radius:50%;background:repeating-conic-gradient(rgba(242,178,51,.35) 0 10deg,transparent 10deg 24deg);
 -webkit-mask-image:radial-gradient(circle,#000 25%,transparent 70%)}""",
        html='<span id="burst"></span><div id="fal">Faltam</div><div id="ctr">30</div><div id="dias">DIAS</div>',
        js="""const C = { v: 30 };
tl.fromTo(C, { v: 30 }, { v: 19, duration: 2.3, ease: "power2.in", onUpdate: () => { document.querySelector("#ctr").textContent = Math.round(C.v); } }, .1);
tl.fromTo("#ctr", { scale: 1 }, { scale: 1.15, duration: .15, yoyo: true, repeat: 1, ease: "power2.out" }, 2.4);
tl.fromTo("#burst", { scale: .2, opacity: 0, rotate: 0 }, { scale: 1, opacity: 1, rotate: 60, duration: 1, ease: "power2.out" }, 2.4);
tl.fromTo("#burst", { rotate: 60 }, { rotate: 160, duration: 4, ease: "none", immediateRender: false }, 3.4);
tl.fromTo("#dias", { y: 40, opacity: 0 }, { y: 0, opacity: 1, duration: .4, ease: "back.out(2.4)" }, 2.5);""",
        hits=[("click", .1 + 2.3 / 11 * i) for i in range(11)] + [("thump", 2.4), ("pop", 2.5), ("pop", 3.8)]),

    # 8/12 "saiu hoje": the five-item checklist, each box ticked with a pop.
    "2026-12-08-saiu": dict(
        theme="natalnoite", title=[("5 coisas antes do Natal.", 140, {"Natal."}, 0, BODY)],
        arrow=("Veja o reel no perfil", 3.8, "background:#F2C14E;color:#0E1A33"),
        css="""#cl{position:absolute;left:190px;top:940px;width:700px;padding:20px 44px;border-radius:36px;background:#F6F1E7;box-shadow:0 60px 120px -40px rgba(0,0,0,.6)}
.ci{display:flex;justify-content:space-between;align-items:center;height:96px;border-bottom:3px dashed #d9d2c2;font-size:44px;font-weight:700;color:#0E1A33}
.ci:last-child{border-bottom:0}.ci i{width:60px;height:60px;border-radius:16px;border:6px solid #0E1A33;position:relative}
.ci b{position:absolute;inset:-6px;border-radius:16px;background:#F2C14E;display:grid;place-items:center;font-size:40px;font-weight:900}""",
        html='<div id="cl">' + "".join(f'<div class="ci">{n}<i><b id="k{i}">✓</b></i></div>' for i, n in enumerate(
            ["Horário de Natal", "Prazo de entrega", "Vales-oferta", "Destaque de Natal", "Contacto rápido"])) + '</div>',
        js="""tl.fromTo("#cl", { y: 400, opacity: 0, rotate: 3 }, { y: 0, opacity: 1, rotate: 0, duration: .6, ease: "back.out(1.6)" }, .2);
tl.fromTo(".ci b", { scale: 0, rotate: -30 }, { scale: 1, rotate: 0, duration: .35, stagger: .45, ease: "back.out(3)" }, .8);
tl.fromTo(".ci", { x: 0 }, { x: 10, duration: .08, stagger: .45, yoyo: true, repeat: 1 }, .8);""",
        hits=[("whoosh", .2)] + [("click", .8 + .45 * i) for i in range(5)] + [("pop", 3.8)]),

    # 10/12 "saiu hoje": the orders counter races to 47 and a "Tudo faturado ✓" stamp lands.
    "2026-12-10-saiu": dict(
        theme="natal", title=[("Dezembro, num só lugar.", 140, {"só", "lugar."}, 0, BODY)],
        arrow=("Veja o reel no perfil", 3.8, "background:#0F3B2C;color:#fff"),
        css="""#cn{position:absolute;left:240px;top:960px;width:600px;padding:40px 0 46px;border-radius:40px;background:#0F3B2C;color:#fff;text-align:center;box-shadow:0 50px 100px -40px rgba(15,59,44,.5)}
#cn small{display:block;font-size:30px;font-weight:700;letter-spacing:.16em;opacity:.75}
#cn b{display:block;font-size:200px;line-height:1;margin-top:10px;font-variant-numeric:tabular-nums}
#ok{position:absolute;left:300px;top:1400px;padding:22px 40px;border-radius:20px;border:8px solid #0F7B4F;background:#fff;color:#0F7B4F;font-size:54px;font-weight:900;white-space:nowrap}""",
        html='<div id="cn"><small>ENCOMENDAS HOJE</small><b id="nm">12</b></div><span id="ok">Tudo faturado ✓</span>',
        js="""tl.fromTo("#cn", { scale: .5, opacity: 0 }, { scale: 1, opacity: 1, duration: .5, ease: "back.out(2)" }, .2);
const N = { v: 12 };
tl.fromTo(N, { v: 12 }, { v: 47, duration: 1.8, ease: "power2.in", onUpdate: () => { document.querySelector("#nm").textContent = Math.round(N.v); } }, .3);
tl.fromTo("#ok", { scale: 2.2, rotate: -20, opacity: 0 }, { scale: 1, rotate: -6, opacity: 1, duration: .25, ease: "power4.in" }, 2.1);
tl.fromTo("#cn", { y: 0 }, { y: 10, duration: .06, yoyo: true, repeat: 3, immediateRender: false }, 2.35);""",
        hits=[("pop", .2)] + [("click", .3 + .15 * i) for i in range(12)] + [("thump", 2.35), ("pop", 3.8)]),

    # 12/12 "saiu hoje": antes (paper notes) wipes into depois (the florist site).
    "2026-12-12-saiu": dict(
        theme="natalverde", title=[("Antes e depois.", 160, {"depois."}, 0, BODY)],
        arrow=("Veja o reel no perfil", 3.8, "background:#E8B84A;color:#0F3A2C"),
        css="""#ab{position:absolute;left:190px;top:940px;width:700px;height:560px;border-radius:36px;overflow:hidden;box-shadow:0 60px 120px -40px rgba(0,0,0,.6)}
#ab>div{position:absolute;inset:0}
#sd{background:#fff}#sd .h{padding:26px 32px;background:#0F3A2C;color:#fff;font-size:34px;font-weight:800}
#sd .p{display:flex;gap:26px;align-items:center;margin:34px 32px;padding:24px;border-radius:24px;background:#f4f1e8;color:#0F3A2C;font-size:40px;font-weight:800}
#sd .p i{font-style:normal;font-size:100px}#sd .p em{display:block;font-style:normal;color:#C41E3A}
#pa{background:repeating-linear-gradient(#FBF6EA 0 58px,#e5dcc6 58px 60px);font-family:'Playfair Display',serif;font-style:italic;color:#3b3226;font-size:50px;line-height:60px;padding:110px 46px 0}
#kn{position:absolute;top:940px;left:190px;width:8px;height:560px;margin-left:-4px;background:#E8B84A;z-index:3;box-shadow:0 0 30px rgba(232,184,74,.8)}""",
        html='<div id="ab"><div id="sd"><div class="h">Flores da Ribeira</div><div class="p"><i>🌲</i><span>Coroa de Natal<em>35 €</em></span></div>'
             '<div class="p"><i>💐</i><span>Arranjo de mesa<em>25 €</em></span></div></div>'
             '<div id="pa">Sra. Rosa: coroa, sexta?<br>Arranjo mesa, 25 € ??<br><s>ligar ao Sr. Paulo</s></div></div><span id="kn"></span>',
        js="""tl.fromTo("#ab", { scale: .6, opacity: 0 }, { scale: 1, opacity: 1, duration: .5, ease: "back.out(1.8)" }, .2);
const W = { w: 100 };
const paint = () => { document.querySelector("#pa").style.clipPath = `inset(0 ${100 - W.w}% 0 0)`;
  const k = document.querySelector("#kn"); k.style.transform = `translateX(${7 * W.w}px)`; k.style.opacity = W.w > 1 && W.w < 99 ? 1 : 0; };
tl.fromTo(W, { w: 100 }, { w: 0, duration: 1.4, ease: "power2.inOut", onUpdate: paint }, 1.0);
tl.fromTo("#sd .p", { scale: .85 }, { scale: 1, duration: .35, stagger: .12, ease: "back.out(2.4)" }, 2.3);""",
        hits=[("pop", .2), ("whoosh", 1.0), ("pop", 2.3), ("pop", 2.42), ("pop", 3.8)]),
}


def main(names):
    for name in names or STORIES:
        s = STORIES[name]
        hfkit.build(f"story-{name}", HERE / name / "hf", theme=s["theme"], total=TOTAL, html=s["html"], css=s["css"], js=s["js"],
                    title=s["title"], arrow=s["arrow"], outro=BODY, hits=s["hits"] + [("whoosh", BODY)], out_mp4=HERE / name / "story-hf.mp4")


if __name__ == "__main__":
    main(sys.argv[1:])
