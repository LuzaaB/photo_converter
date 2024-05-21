from PIL import Image
from pillow_heif import register_heif_opener
from pathlib import Path
# import os

register_heif_opener()

parent_path = Path(__file__).parent.parent.resolve()
print(parent_path)

heic_path = parent_path / "heic_images"
image_path = parent_path / "jpg_images"

# dir_list = os.listdir(heic_path)
# print("Directory List : ", dir_list)

for each in heic_path.iterdir():
    file_name = Path(each).name
    if file_name.endswith(".heic") or file_name.endswith(".HEIC"):
        img = Image.open(each)
        img.convert('RGB').save(f"{image_path}/{file_name[:-5]}.jpg")