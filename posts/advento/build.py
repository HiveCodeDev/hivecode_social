"""Advent calendar stories, 1-24 December at 17:30 (natal theme, 1080x1920, ~10 s + outro).

python posts/advento/build.py [day ...]
The whole calendar, a HiveCode Christmas tree of 24 hexagon doors (shuffled, earlier days open, logo as the star) appears; the camera
zooms into today's door, which shakes and swings open; the screen dims and a card with the day's
curiosity pops; "Amanhã às 17h30: porta N+1". Reuses the story builder (arrow + logo outro).
"""
import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "posts" / "stories"))
import build_anim  # noqa: E402

FACTS = {
    1: "O primeiro calendário do advento impresso surgiu na Alemanha, no início do século XX.",
    2: "O primeiro spam foi enviado em 1978, para cerca de 400 pessoas, a anunciar computadores.",
    3: "O primeiro SMS da história foi enviado a 3 de dezembro de 1992 e dizia “Merry Christmas”.",
    4: "A Nintendo foi fundada em 1889 e fazia cartas de jogar.",
    5: "O primeiro artigo vendido no eBay foi um ponteiro laser avariado, por 14,83 dólares.",
    6: "O nome Google vem de “googol”: um 1 seguido de 100 zeros.",
    7: "A primeira mensagem da internet, em 1969, foi “LO”: o sistema foi abaixo a meio de “LOGIN”.",
    8: "A palavra “robô” vem de uma peça de teatro checa de 1920 e significa “trabalho forçado”.",
    9: "O primeiro rato de computador era uma caixa de madeira e foi apresentado a 9 de dezembro de 1968.",
    10: "Quase toda a internet entre continentes passa por cabos no fundo do mar, que já foram mordidos por tubarões.",
    11: "O QR code foi inventado em 1994 para seguir peças de automóveis numa fábrica japonesa.",
    12: "O Bluetooth tem o nome de um rei viking, Harald “Dente Azul”, e o logótipo junta as iniciais dele em runas.",
    13: "A primeira fotografia publicada na web foi de uma banda formada por funcionárias do CERN.",
    14: "O Pai Natal tem código postal no Canadá, H0H 0H0, e as cartas recebem resposta.",
    15: "Um carregador de telemóvel atual tem mais capacidade de cálculo do que o computador que levou o homem à Lua.",
    16: "“Jingle Bells” foi a primeira música tocada no espaço, a 16 de dezembro de 1965.",
    17: "O primeiro telemóvel pesava quase 1 kg: dava 30 minutos de conversa e precisava de 10 horas para carregar.",
    18: "O primeiro “bug” registado num computador foi uma traça verdadeira, presa lá dentro em 1947.",
    19: "Hedy Lamarr, atriz de Hollywood, coinventou a técnica que está na base do Wi-Fi e do Bluetooth.",
    20: "O primeiro site do mundo ficou online a 20 de dezembro de 1990 e ainda funciona: info.cern.ch",
    21: "Todos os dias são enviados mais de 300 mil milhões de emails.",
    22: "O som de arranque do Windows 95 foi composto por Brian Eno… num Mac.",
    23: "O primeiro vírus de PC, em 1986, tinha lá dentro a morada e o telefone dos dois irmãos que o criaram.",
    24: "O NORAD segue o Pai Natal desde 1955, por causa de um número de telefone mal impresso num anúncio.",
}

ORDER = list(range(1, 25))
random.Random(2026).shuffle(ORDER)  # doors are scattered, like a real advent calendar
# HiveCode tree: hexagons (the brand mark) in a honeycomb triangle of rows 1..6 (21 doors),
# then a trunk of 1 and a stand of 2 (24 doors). The logo sits on top as the star.
W = 130                      # hexagon width (pointy top)
H = W * 1.1547               # hexagon height
STEP = H * .75               # vertical distance between honeycomb rows
TOP = 760                    # centre of the first row
ROWS = [1, 2, 3, 4, 5, 6, 1, 2]
SLOTS = [(540 + (i - (n - 1) / 2) * W, TOP + r * STEP, r) for r, n in enumerate(ROWS) for i in range(n)]
GREENS = ["#0F7B4F", "#0F3B2C", "#1d5c46"]
ORN = {2: "#C41E3A", 4: "#F2B233", 7: "#C41E3A", 11: "#F2B233", 13: "#C41E3A", 17: "#F2B233", 19: "#C41E3A"}  # baubles
HEX = "polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%)"

CSS = f"""
#cam{{left:0;top:0;width:1080px;height:1920px;transform-origin:0 0}}
#tree{{position:absolute;inset:0}}
#tstar{{position:absolute;left:475px;top:{TOP - H / 2 - 145:.0f}px;width:130px;height:130px;filter:drop-shadow(0 0 30px rgba(242,178,51,.9))}}
.dc{{position:absolute;width:{W - 10}px;height:{H - 10:.0f}px;margin:{-(H - 10) / 2:.0f}px 0 0 {-(W - 10) / 2:.0f}px;perspective:900px}}
.in{{position:absolute;inset:0;clip-path:{HEX};background:#0F3B2C;box-shadow:inset 0 0 0 6px #F2B233;display:grid;place-items:center;font-size:62px;color:#F2B233}}
.lf{{position:absolute;inset:0;clip-path:{HEX};transform-origin:0 50%;display:grid;place-items:center;font-size:56px;font-weight:800;backface-visibility:hidden}}
#dim{{inset:0;background:#F5EEE2;opacity:0}}
#card{{left:90px;right:90px;top:720px;padding:60px 60px 70px;border-radius:40px;background:#fff;border:8px solid #C41E3A;opacity:0;
 box-shadow:0 60px 120px -40px rgba(15,59,44,.5)}}
#card small{{display:block;font-size:30px;font-weight:800;letter-spacing:.14em;color:#C41E3A}}
#card p{{margin:24px 0 0;font-size:62px;font-weight:700;line-height:1.15;color:#0F3B2C;letter-spacing:-.01em}}
#next{{left:0;right:0;top:1500px;display:flex;justify-content:center;opacity:0}}
#next span{{padding:24px 42px;border-radius:999px;background:#0F3B2C;color:#fff;font-size:42px;font-weight:700}}
"""


def door_xy(n):
    x, y, _ = SLOTS[ORDER.index(n)]
    return x, y


def story(day):
    cells = ""
    for i, n in enumerate(ORDER):
        x, y, r = SLOTS[i]
        col = "#6b4226" if r >= 6 else ORN.get(i, GREENS[i % 3])
        ink = "#0F3B2C" if col == "#F2B233" else "#fff"
        opened = "transform:rotateY(-108deg)" if n < day else ""
        star = "<span id=star style=display:inline-block>★</span>" if n == day else "★" if n < day else ""
        cells += (f'<div class="dc" style="left:{x:.0f}px;top:{y:.0f}px"><div class="in">{star}</div>'
                  f'<div class="lf" id="{"today" if n == day else f"d{n}"}" style="background:{col};color:{ink};{opened}">{n}</div></div>')
    cx, cy = door_xy(day)
    nxt = f"Amanhã às 17h30: porta {day + 1}" if day < 24 else "Boas festas! 🎄"
    html = (f'<div id="cam"><div id="tree"><img id="tstar" src="{(ROOT / "assets" / "logo_mark.svg").as_uri()}" alt="">{cells}</div></div>'
            f'<span id="dim"></span><div id="card"><small>PORTA {day} · SABIA QUE…</small><p>{FACTS[day]}</p></div>'
            f'<div id="next"><span>{nxt}</span></div>')
    js = f"""pop($('#tree'), t, .2);
$('#tstar').style.transform = `rotate(${{8 * Math.sin(t * 1.5)}}deg) scale(${{1 + .06 * Math.sin(t * 3)}})`;
const k = ease((t - 1.6) / 1.4), s = 1 + 2.8 * k, fx = 540 + ({cx} - 540) * k, fy = 960 + ({cy} - 960) * k;
$('#cam').style.transform = `translate(${{540 - fx * s}}px,${{1000 - fy * s}}px) scale(${{s}})`;
const sh = t > 3.0 && t < 3.5 ? Math.sin((t - 3.0) * 50) * 4 : 0, o = ease((t - 3.5) / .7);
$('#today').style.transform = `rotateY(${{sh - 108 * o}}deg)`;
$('#star').style.transform = `scale(${{back((t - 3.9) / .5)}}) rotate(${{40 * Math.sin(t * 2)}}deg)`; $('#star').style.textShadow = '0 0 30px rgba(242,178,51,.9)';
$('#dim').style.opacity = .82 * ease((t - 5.0) / .4);
pop($('#card'), t, 5.2);
pop($('#next'), t, 8.0);"""
    return dict(theme="natal", total=11.0, arrow="Siga o perfil", arrow_at=8.6, arrow_css="background:#C41E3A;color:#fff",
                lines=[(f"Dezembro, dia {day}.", 120, {"Dezembro,"}, 0, 1.6, .3), (f"Porta {day}", 130, {str(day)}, 5.1, 11.0, 5.2)],
                css=CSS, html=html, js=js,
                hits=[("pop", .2), ("whoosh", 1.6), ("click", 3.05), ("click", 3.3), ("whoosh", 3.5), ("pop", 3.9), ("pop", 5.2), ("pop", 8.0), ("pop", 8.6)])


if __name__ == "__main__":
    build_anim.reelkit.SFX.update(build_anim.SPOOKY)
    days = [int(d) for d in sys.argv[1:]] or sorted(FACTS)
    for d in days:
        build_anim.build(f"advento-{d:02d}", story(d))
