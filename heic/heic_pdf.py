import img2pdf
from pathlib import Path
import os

parent_path = Path(__file__).parent.parent.resolve()
print(parent_path)

heic_path = parent_path / "heic_images"
print(heic_path)
pdf_path = parent_path / "pdf_images"
print(pdf_path)

dir_list = os.listdir(heic_path)
print(dir_list)

for each in dir_list:
    print("each",each)
    if each.endswith("heic") or each.endswith(".HEIC"):
        with open(heic_path, "wb") as f:
                f.write(img2pdf.convert(each))