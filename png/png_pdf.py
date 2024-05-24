from pathlib import Path
import img2pdf

parent_path = Path(__file__).parent.parent.resolve()

png_path = parent_path / "png_images"
pdf_path = parent_path / "pdf_images"

for each in png_path.iterdir():
    file_name = Path(each).name
    if file_name.endswith(".png") or file_name.endswith(".PNG"):
        pdf_name = pdf_path / f"{file_name[:-4]}.pdf"
        with open(pdf_name, "wb") as f:
            f.write(img2pdf.convert(each))