from pathlib import Path
from PIL import Image

parent_path = Path(__file__).parent.parent.resolve()
print(parent_path)

jpg_path = parent_path / "jpg_images"
print(jpg_path)
png_path = parent_path / "png_images"
print(png_path)

for each in jpg_path.iterdir():
    print(each)
    file_name = Path(each).name
    print(file_name)
    if file_name.endswith(".jpg") or file_name.endswith(".JPG"):
        img = Image.open(each)
        img.save(f"{png_path}/{file_name[:-4]}.png")