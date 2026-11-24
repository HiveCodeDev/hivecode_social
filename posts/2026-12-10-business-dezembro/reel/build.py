"""Reel Business "Dezembro: mais encomendas, menos tempo" (natal theme, 1080x1920).

python posts/2026-12-10-business-dezembro/reel/build.py
Hook: an "orders today" counter races up while order notifications pile in; then email, a stock
notebook and a separate invoicing app scatter and shake; they fly into one HiveCode Business
dashboard (in / missing / invoiced tiles light up as said); a January page gets "Fecho do ano ✓".
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
    ("Dezembro: mais encomendas, mais faturas e menos tempo.", 96, {"Dezembro:"}),
    ("Encomendas no email, stock num caderno, faturas noutro programa.", 88, {"email,", "caderno,", "programa."}),
    ("Com o HiveCode Business, fica tudo num só lugar.", 96, {"só", "lugar."}),
    ("Vê o que entrou, o que falta e o que já foi faturado.", 92, {"entrou,", "falta", "faturado."}),
    ("E em janeiro, o fecho do ano já está feito.", 96, {"feito."}),
    ("Fale connosco em hivecode.pt.", 110, {"hivecode.pt."}),
]

INK, RED, GREEN = "#0F3B2C", "#C41E3A", "#0F7B4F"
CSS = f"""
#cnt{{left:240px;top:830px;width:600px;padding:34px 0 40px;border-radius:36px;background:{INK};color:#fff;text-align:center;opacity:0}}
#cnt small{{display:block;font-size:28px;font-weight:700;letter-spacing:.16em;opacity:.75}}
#cnt b{{display:block;font-size:170px;line-height:1;margin-top:10px}}
.nt{{left:160px;top:1180px;width:760px;padding:26px 34px;border-radius:26px;background:#fff;font-size:34px;font-weight:600;color:{INK};opacity:0;
 box-shadow:0 30px 60px -25px rgba(15,59,44,.45);display:flex;justify-content:space-between}}
.nt i{{font-style:normal;color:{RED};font-weight:800}}
.wd{{width:520px;border-radius:28px;background:#fff;overflow:hidden;opacity:0;box-shadow:0 40px 80px -30px rgba(15,59,44,.5)}}
.wd .h{{padding:20px 28px;font-size:28px;font-weight:800;color:#fff}}
.wd .b{{padding:24px 28px 30px;font-size:32px;line-height:1.5;color:{INK}}}
#w0{{left:90px;top:830px}}#w0 .h{{background:#2C6FD1}}
#w1{{left:470px;top:1060px}}#w1 .h{{background:#8a6a3c}}
#w1 .b{{background:repeating-linear-gradient(#fffdf6 0 46px,#e6dcc4 46px 48px);font-family:'Instrument Serif',serif;font-style:italic;font-size:40px}}
#w2{{left:150px;top:1300px}}#w2 .h{{background:#6c4bb5}}
#db{{left:88px;right:88px;top:830px;border-radius:36px;background:#fff;overflow:hidden;opacity:0;box-shadow:0 60px 120px -40px rgba(15,59,44,.5)}}
#db .h{{display:flex;align-items:center;gap:18px;padding:26px 34px;background:{INK};color:#fff;font-size:32px;font-weight:700}}
#db .h img{{width:46px;height:46px;filter:brightness(0) invert(1)}}
#db .tl{{display:flex;gap:20px;padding:30px 30px 10px}}
#db .tl div{{flex:1;padding:24px 0;border-radius:24px;background:#f3efe6;text-align:center;font-size:28px;font-weight:700;color:#5d7569;transition:none}}
#db .tl b{{display:block;font-size:84px;line-height:1.05;color:{INK}}}
#db .ls{{padding:10px 30px 30px}}
#db .ls p{{display:flex;justify-content:space-between;margin:16px 0 0;padding:20px 24px;border-radius:18px;background:#faf8f3;font-size:30px;color:{INK}}}
#db .ls p span{{padding:4px 18px;border-radius:999px;font-size:24px;font-weight:800;color:#fff}}
#jan{{left:340px;top:870px;width:400px;border-radius:30px;background:#fff;overflow:hidden;text-align:center;opacity:0;box-shadow:0 50px 100px -40px rgba(15,59,44,.5)}}
#jan .m{{padding:22px 0;background:{RED};color:#fff;font-size:40px;font-weight:800;letter-spacing:.1em}}
#jan .d{{padding:30px 0 40px;font-size:200px;font-weight:800;line-height:1;color:{INK}}}
#stamp{{left:250px;top:1330px;padding:24px 40px;border-radius:20px;border:8px solid {GREEN};color:{GREEN};font-size:56px;font-weight:900;opacity:0;white-space:nowrap;background:#fff}}
#logo{{left:440px;top:900px;width:200px;height:200px;opacity:0}}
#cta{{left:88px;right:88px;top:1190px;display:flex;justify-content:center;opacity:0}}
#cta span{{padding:32px 56px;border-radius:999px;background:{INK};color:#fff;font-size:50px;font-weight:700}}
"""

NOTES = [("Nova encomenda #1047", "agora"), ("Nova encomenda #1046", "1 min"), ("Nova encomenda #1045", "2 min")]
ART = ('<div id="cnt"><small>ENCOMENDAS HOJE</small><b id="num">12</b></div>'
       + "".join(f'<div class="nt" id="n{i}"><span>✉ {a}</span><i>{b}</i></div>' for i, (a, b) in enumerate(NOTES))
       + '<div class="wd" id="w0"><div class="h">Email · 23 por ler</div><div class="b">Encomenda Sra. Rosa<br>RE: RE: encomenda?</div></div>'
       + '<div class="wd" id="w1"><div class="h">Stock · caderno</div><div class="b">Papel de embrulho: 3?<br>Velas: <s>12</s> 4</div></div>'
       + '<div class="wd" id="w2"><div class="h">Faturas · outro programa</div><div class="b">Fatura 2026/318<br>Por emitir: 9</div></div>'
       + f'<div id="db"><div class="h"><img src="{ASSETS}/logo_mark.svg" alt="">HiveCode Business · dezembro</div>'
       + '<div class="tl"><div id="t0"><b>48</b>Entrou</div><div id="t1"><b>7</b>Falta</div><div id="t2"><b>41</b>Faturado</div></div>'
       + f'<div class="ls"><p>#1047 · Cabaz de Natal<span style="background:#F2B233">Em preparação</span></p>'
       + f'<p>#1046 · Vale-oferta 50 €<span style="background:{GREEN}">Faturada</span></p>'
       + f'<p>#1045 · Bolo-rei grande<span style="background:{GREEN}">Faturada</span></p></div></div>'
       + '<div id="jan"><div class="m">JANEIRO</div><div class="d">2</div></div><span id="stamp">Fecho do ano ✓</span>'
       + f'<img id="logo" src="{ASSETS}/logo_mark.svg" alt=""><div id="cta"><span>hivecode.pt</span></div>')

ART_JS = r"""
function art(t, E) {
  // 1. counter races, notifications pile up
  stage($('#cnt'), t, .1, E.s1 - .05);
  $('#num').textContent = Math.round(12 + 35 * ease(t / (E.s1 - .3)));
  [.5, 1.0, 1.5].forEach((a, i) => {
    const el = $('#n' + (2 - i)), k = back((t - a) / .4), o = ease((t - E.s1) / .3);
    el.style.opacity = cl((t - a) / .1) * (1 - o);
    el.style.transform = `translate(${-200 * o}px,${(2 - i) * 130 - 40 * (1 - k)}px) rotate(${(i - 1) * 2}deg)`;
  });
  // 2. three scattered tools, shaking, then sucked into the dashboard
  const into = ease((t - E.s2) / .5);
  [[E.mail, -5], [E.cad, 4], [E.prog, -3]].forEach(([a, r], i) => {
    const el = $('#w' + i), k = back((t - a) / .45), sh = t > a + .4 && t < E.s2 ? Math.sin(t * 30 + i) * 1.5 : 0;
    el.style.opacity = cl((t - a) / .1) * (1 - into);
    el.style.transform = `translate(${(270 - [350, 730, 410][i]) * into}px,${(1100 - [900, 1130, 1370][i]) * into}px) rotate(${r * k + sh}deg) scale(${(.8 + .2 * k) * (1 - .6 * into)})`;
  });
  // 3. dashboard, tiles light up
  stage($('#db'), t, E.s2 + .35, E.s4 - .05);
  [E.en, E.fa, E.ft].forEach((a, i) => {
    const el = $('#t' + i), on = t > a;
    el.style.background = on ? ['#0F7B4F', '#C41E3A', '#0F3B2C'][i] : '#f3efe6';
    el.style.color = on ? '#fff' : '#5d7569';
    el.querySelector('b').style.color = on ? '#fff' : '#0F3B2C';
    el.style.transform = `scale(${1 + .08 * Math.sin(Math.PI * cl((t - a) / .4))})`;
  });
  // 4. January, stamp
  stage($('#jan'), t, E.s4, E.s5 - .1);
  const sk = cl((t - E.feito) / .25);
  $('#stamp').style.opacity = sk * (1 - ease((t - E.s5 + .1) / .3));
  $('#stamp').style.transform = `rotate(-8deg) scale(${2 - sk})`;
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
    ev = {"s1": st[1], "mail": at(1, "email,"), "cad": at(1, "caderno,"), "prog": at(1, "programa."), "s2": st[2],
          "en": at(3, "entrou,"), "fa": at(3, "falta"), "ft": at(3, "faturado."), "s4": st[4], "feito": at(4, "feito."),
          "s5": st[5], "site": at(5, "hivecode.pt.")}
    page = HERE / "reel.html"
    page.write_text(reelkit.page(scenes, ev, ART, CSS, ART_JS, theme="natal"), encoding="utf-8")
    hits = [("pop", .1), ("pop", .5), ("pop", 1.0), ("pop", 1.5), ("whoosh", ev["s1"]), ("error", ev["mail"]),
            ("error", ev["cad"]), ("error", ev["prog"]), ("rise", ev["s2"]), ("pop", ev["s2"] + .35),
            ("click", ev["en"]), ("click", ev["fa"]), ("click", ev["ft"]), ("pop", ev["s4"]), ("thump", ev["feito"]),
            ("pop", ev["s5"] + .1), ("pop", ev["site"])]
    reelkit.render(page, WORK, total, WORK / "voz.mp3", hits, HERE / "reel.mp4")
    reelkit.cover(HERE / "reel.mp4", ev["s4"] - .3, HERE / "cover.jpg")
    print(f"reel.mp4 {total:.1f}s")


if __name__ == "__main__":
    main()
