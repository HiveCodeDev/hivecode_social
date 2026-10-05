"""Ana Carolina Pereira: same format as the 4Sons case (approved by the owner).

Three slides: laptop cover, phone, HiveCode close. Shows the start of the
clinic's home page, as on the live site (the owner asked for that part).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from cases import build

build(
    Path(__file__).resolve().parent,
    title="Novo site para a clínica <em>Ana Carolina Pereira</em>.",
    desktop="acp-home.png",
    mobile="acp-mobile.png",
    phone_title="Pensado para o <em>telemóvel</em>.",
    phone_note="Um site sereno e claro, com a marcação de consultas sempre à mão.",
)
print("ok")
