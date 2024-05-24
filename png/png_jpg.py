from PIL import Image
from pathlib import Path

parent_path = Path(__file__).parent.parent.resolve()

png_path = parent_path / "png_images"
print(png_path)
jpg_path = parent_path / "jpg_images"
print(jpg_path)

for each in png_path.iterdir():
    file_name = Path(each).name
    print(each)
    if file_name.endswith("png") or file_name.endswith("PNG"):
        img = Image.open(each)  
        image = img.convert('RGB').save(f"{jpg_path}/{file_name[:-4]}.jpg")    