"""Square icons for the LinkedIn credibility highlights (python linkedin/destaques/build.py).

White line icons on the brand gradient (no emoji: their orange clashes with the brand).
"""
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ICONS = {
    # gift
    "1-mockup": '<rect x="3" y="8" width="18" height="4" rx="1"/><path d="M5 12v8h14v-8M12 8v12M12 8S10 3 7.5 4.5 9 8 12 8zM12 8s2-5 4.5-3.5S15 8 12 8z"/>',
    # receipt
    "2-faturacao": '<path d="M6 3h12v18l-2-1.5-2 1.5-2-1.5-2 1.5-2-1.5L6 21z"/><path d="M9 8h6M9 12h6M9 16h4"/>',
    # browser window
    "3-projetos": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M7 6.5h.01M10 6.5h.01M7 13h6M7 16h10"/>',
    # bolt
    "4-resposta": '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
}
PAGE = """<!doctype html><html><head><meta charset="utf-8"><style>
*{{margin:0}}html,body{{width:400px;height:400px;overflow:hidden}}
body{{display:grid;place-items:center;background:linear-gradient(135deg,#D752FE,#4877FE)}}</style></head><body>
<svg viewBox="0 0 24 24" width="230" height="230" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{icon}</svg>
</body></html>"""
for name, icon in ICONS.items():
    html = HERE / f"{name}.html"
    html.write_text(PAGE.format(icon=icon), encoding="utf-8")
    subprocess.run(["node", str(ROOT / "tools/render_one.mjs"), str(html), str(HERE / f"{name}.jpg"), "400", "400"], check=True)
print("ok")
