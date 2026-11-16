"""Carrossel "A fatura em PDF vai deixar de contar?" (Business, receipt theme, 6 slides).

python posts/2026-11-19-fatura-pdf/build.py && node tools/render.mjs posts/2026-11-19-fatura-pdf/slides
Facts (2026-11-16): a PDF sent by email counts as an e-invoice until 31/12/2026; the law set the end
for 1/1/2027; the 2027 State Budget proposal extends it to 31/12/2027 (Vendus, Checkmate).
"""
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from build_week import page  # noqa: E402

HERE = Path(__file__).resolve().parent

CSS = """
.count{position:absolute;top:96px;right:88px;font-size:24px;color:var(--muted);letter-spacing:.1em}
h1{font-size:80px;line-height:1.04}
h1 em{color:#D7263D;font-style:normal}
.k{font-size:30px;font-weight:700;letter-spacing:.12em;color:#D7263D}
.p{margin-top:28px;font-size:36px;line-height:1.4;color:var(--soft);max-width:880px}
.doc{margin-top:56px;width:520px;border:3px solid #111;border-radius:6px;background:#fff;padding:30px 34px;font-size:26px;position:relative}
.doc b{display:block;font-size:34px;margin-bottom:14px}
.doc i{display:block;height:14px;background:#e4e2dc;border-radius:7px;margin:12px 0}
.stamp{position:absolute;right:-40px;top:40px;transform:rotate(12deg);padding:12px 22px;border:5px solid;border-radius:10px;font-size:34px;font-weight:700;background:#fff}
.ok{color:#1f8a4c;border-color:#1f8a4c}.bad{color:#D7263D;border-color:#D7263D}
.tl{margin-top:60px;display:flex;flex-direction:column;gap:26px}
.tl div{display:flex;gap:28px;align-items:center;font-size:34px}
.tl b{flex:none;width:250px;padding:16px 0;text-align:center;border:3px solid #111;border-radius:8px;font-size:30px}
.tl .on b{background:#111;color:#fff}
.cta{margin-top:50px;align-self:flex-start;padding:26px 40px;border-radius:8px;background:#111;color:#fff;font-size:36px;font-weight:700}
"""


def doc(stamp, cls):
    return f'<div class="doc"><b>FATURA 2026/041</b>fatura.pdf<i></i><i style="width:70%"></i><i style="width:85%"></i><span class="stamp {cls}">{stamp}</span></div>'


SLIDES = [
    f'<span class="k">FATURAÇÃO</span><h1 style="font-size:104px;margin-top:24px">A fatura em PDF vai deixar de <em>contar</em>?</h1>{doc("?", "bad")}<p class="p">Deslize →</p>',
    f'<span class="k">HOJE</span><h1 style="margin-top:24px">Um PDF enviado por email vale como <em>fatura eletrónica</em>.</h1>{doc("VÁLIDA", "ok")}',
    '<span class="k">A LEI</span><h1 style="margin-top:24px">A lei marcava o fim desta regra para <em>1 de janeiro de 2027</em>.</h1>'
    '<div class="tl"><div><b>até 31/12/2026</b>PDF vale como fatura eletrónica</div><div class="on"><b>1/1/2027</b>data prevista na lei</div></div>',
    '<span class="k">A PROPOSTA</span><h1 style="margin-top:24px">O Orçamento do Estado para 2027 prolonga-a até <em>31 de dezembro de 2027</em>.</h1>'
    '<p class="p">Atenção: ainda é uma proposta. Só fica decidido com a aprovação do Orçamento.</p>',
    '<span class="k">O QUE FAZER JÁ</span><h1 style="margin-top:24px">Prepare a faturação <em>com tempo</em>.</h1>'
    '<p class="p">Use um programa de faturação que emita no formato certo, sem esperar pelo último mês.</p>',
    '<span class="k">HIVECODE BUSINESS</span><h1 style="font-size:92px;margin-top:24px">O nosso <em>programa de faturação</em>.</h1>'
    '<p class="p">Faturas, clientes e encomendas no mesmo sistema, feito à medida da sua empresa.</p><span class="cta">hivecode.pt/business</span>',
]

if __name__ == "__main__":
    shutil.rmtree(HERE / "slides", ignore_errors=True)
    for n, body in enumerate(SLIDES, 1):
        d = HERE / "slides" / f"{n:02d}"
        d.mkdir(parents=True)
        (d / "post.html").write_text(page(f'<span class="count">{n}/{len(SLIDES)}</span>' + body, CSS, theme="receipt"), encoding="utf-8")
    print("ok")
