from pathlib import Path
import img2pdf

parent_path = Path(__file__).parent.parent.resolve()

jpg_path = parent_path / "jpg_images"
pdf_path = parent_path / "pdf_images"

for each in jpg_path.iterdir():
    file_name = Path(each).name
    # pdf_name = file_name[:-4]
    pdf_name = pdf_path / f"{file_name[:-4]}.pdf"
    with open(pdf_name, "wb") as f :
        f.write(img2pdf.convert(each))
        