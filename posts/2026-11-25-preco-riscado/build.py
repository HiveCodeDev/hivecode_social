"""Carrossel "Black Friday: o preço riscado tem regras" (canvas theme, 6 slides).

python posts/2026-11-25-preco-riscado/build.py && node tools/render.mjs posts/2026-11-25-preco-riscado/slides
Facts (Decreto-Lei 109-G/2021, changing DL 70/2007): the "preço mais baixo anteriormente praticado" is the
lowest price in the 30 consecutive days before the reduction; labels must show the new price and that
previous price (percentage optional); the announcement must state the start date and duration.
"""
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from build_week import page  # noqa: E402

HERE = Path(__file__).resolve().parent

CSS = """
.count{position:absolute;top:96px;right:88px;font-size:24px;color:var(--muted);letter-spacing:.1em}
h1{font-size:82px;line-height:1.04}
h1 em{color:#9B3CF0;font-style:normal}
.k{font-size:30px;font-weight:700;letter-spacing:.12em;color:#9B3CF0}
.p{margin-top:28px;font-size:36px;line-height:1.4;color:var(--soft);max-width:880px}
.tags{margin-top:60px;display:flex;gap:40px;align-items:flex-start}
.tag{position:relative;width:420px;white-space:nowrap;padding:44px 40px 40px 70px;border-radius:18px 40px 40px 18px;background:#fff;border:4px solid #121125;box-shadow:0 30px 60px -30px rgba(18,17,37,.45)}
.tag:before{content:"";position:absolute;left:26px;top:50%;width:22px;height:22px;margin-top:-11px;border-radius:50%;border:4px solid #121125;background:#F4F2FA}
.tag s{display:block;font-size:44px;color:#8a879c;text-decoration-thickness:5px}
.tag b{display:block;margin-top:6px;font-size:84px;line-height:1;color:#121125;letter-spacing:-.03em}
.tag i{display:inline-block;margin-top:18px;padding:8px 18px;border-radius:999px;background:#9B3CF0;color:#fff;font-style:normal;font-size:30px;font-weight:700}
.mark{position:absolute;right:-26px;top:-30px;width:84px;height:84px;border-radius:50%;display:grid;place-items:center;font-size:52px;font-weight:800;color:#fff}
.ok{background:#1f8a4c}.bad{background:#D7263D}
.cap{margin-top:22px;font-size:28px;color:var(--soft);text-align:center}
.tl{margin-top:70px;display:flex;flex-direction:column;gap:30px}
.tl div{display:flex;gap:34px;align-items:center;font-size:44px;font-weight:600}
.tl b{flex:none;width:360px;padding:22px 0;text-align:center;border:3px solid #121125;border-radius:12px;font-size:36px;background:#fff;white-space:nowrap}
.tl .on b{background:#121125;color:#fff}
.list{margin-top:50px;display:flex;flex-direction:column;gap:24px}
.list div{display:flex;gap:26px;align-items:center;padding:28px 34px;border-radius:18px;background:#fff;border:3px solid #121125;font-size:38px;font-weight:600}
.list span{flex:none;width:60px;height:60px;border-radius:50%;background:#9B3CF0;color:#fff;display:grid;place-items:center;font-size:34px;font-weight:800}
.law{margin-top:40px;font-size:26px;color:var(--muted)}
.cta{margin-top:50px;align-self:flex-start;padding:26px 40px;border-radius:999px;background:#121125;color:#fff;font-size:36px;font-weight:700}
"""


def tag(old, new, pct="", mark="", cls=""):
    m = f'<span class="mark {cls}">{mark}</span>' if mark else ""
    p = f"<i>{pct}</i>" if pct else ""
    return f'<div class="tag">{m}<s>{old}</s><b>{new}</b>{p}</div>'


SLIDES = [
    '<span class="k">BLACK FRIDAY</span><h1 style="font-size:110px;margin-top:24px">O preço riscado tem <em>regras</em>.</h1>'
    f'<div class="tags" style="zoom:1.35;margin-top:50px">{tag("50,00 €", "36,00 €", "−?%")}</div><p class="p">Deslize →</p>',
    '<span class="k">A REGRA</span><h1 style="margin-top:24px">O preço riscado tem de ser o <em>mais baixo dos últimos 30 dias</em>.</h1>'
    '<p class="p">Não o preço de etiqueta, nem o de há três meses: o mais baixo a que o produto foi vendido nos 30 dias antes do desconto.</p>',
    '<span class="k">UM EXEMPLO</span><h1 style="font-size:70px;margin-top:24px">Um produto que mudou de preço em novembro.</h1>'
    '<div class="tl"><div><b>até 31/10</b>50,00 €</div><div><b>a partir de 10/11</b>45,00 €</div><div class="on"><b>27/11</b>Black Friday: 36,00 €</div></div>',
    '<span class="k">CERTO OU ERRADO?</span><h1 style="font-size:70px;margin-top:24px">O riscado é o <em>45&nbsp;€</em>, não o 50&nbsp;€.</h1>'
    f'<div class="tags"><div>{tag("50,00 €", "36,00 €", "−28%", "✕", "bad")}<p class="cap">Errado</p></div>'
    f'<div>{tag("45,00 €", "36,00 €", "−20%", "✓", "ok")}<p class="cap">Certo</p></div></div>',
    '<span class="k">O QUE O ANÚNCIO DEVE MOSTRAR</span><h1 style="font-size:70px;margin-top:24px">Quatro informações, bem visíveis.</h1>'
    '<div class="list"><div><span>1</span>O preço novo</div><div><span>2</span>O preço anterior (o dos 30 dias)</div>'
    '<div><span>3</span>A data de início</div><div><span>4</span>Quanto tempo dura</div></div>'
    '<p class="law">A percentagem é opcional. Decreto-Lei n.º 109-G/2021.</p>',
    '<span class="k">HIVECODE</span><h1 style="font-size:104px;margin-top:24px">Boas <em>vendas</em>!</h1>'
    '<p class="p">Descontos claros dão confiança a quem compra, na loja e no site.</p><span class="cta">hivecode.pt</span>',
]

if __name__ == "__main__":
    shutil.rmtree(HERE / "slides", ignore_errors=True)
    for n, body in enumerate(SLIDES, 1):
        d = HERE / "slides" / f"{n:02d}"
        d.mkdir(parents=True)
        (d / "post.html").write_text(page(f'<span class="count">{n}/{len(SLIDES)}</span>' + body, CSS, theme="canvas"), encoding="utf-8")
    print("ok")
