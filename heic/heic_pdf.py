import img2pdf
from pathlib import Path
# from heic2png import HEIC2PNG

parent_path = Path(__file__).parent.parent.resolve()
print(parent_path)

heic_path = parent_path / "heic_images"
print(heic_path)
pdf_path = parent_path / "pdf_images"
print(pdf_path)

for each in heic_path.iterdir():
    file_name = Path(each).name
    if file_name.endswith(".heic") or file_name.endswith(".HEIC"):
        # img = HEIC2PNG(each, quality=70)
        pdf_name = pdf_path / f"{file_name[:-5]}.pdf"
        with open(pdf_name, "wb") as f:
                f.write(img2pdf.convert(each))