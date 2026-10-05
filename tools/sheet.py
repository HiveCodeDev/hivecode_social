"""Contact sheet of a carousel's slides: python tools/sheet.py posts/<folder>"""
import glob
import sys
from pathlib import Path

from PIL import Image

folder = Path(sys.argv[1])
files = sorted(glob.glob(str(folder / "slides" / "*" / "post.jpg")))
w, h = 300, 375
cols = min(len(files), 4)
rows = (len(files) + cols - 1) // cols
sheet = Image.new("RGB", (cols * (w + 8) + 8, rows * (h + 8) + 8), (240, 240, 245))
for i, f in enumerate(files):
    sheet.paste(Image.open(f).resize((w, h)), (8 + (i % cols) * (w + 8), 8 + (i // cols) * (h + 8)))
sheet.save(folder / "carousel.jpg", quality=88)
print(folder / "carousel.jpg")
