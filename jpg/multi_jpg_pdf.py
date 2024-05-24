from pathlib import Path
import img2pdf

parent_path = Path(__file__).parent.parent.resolve()

jpg_path = parent_path / "multi_jpg"
pdf_path = parent_path / "pdf_multi_images"

file_name = pdf_path / "name.pdf"
with open(file_name, "wb") as f :
    f.write(
        img2pdf.convert(
            [
                each for each in jpg_path.iterdir() if str(each).endswith(".jpg")
            ],
            rotation = img2pdf.Rotation.ifvalid
        )
    )
    
    #  img2pdf.convert([each for each in jpg_path.iterdir() if str(each).endswith(".jpg")] ,
    #                     rotation = img2pdf.Rotation.ifvalid)