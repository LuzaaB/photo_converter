from PIL import Image
from pillow_heif import register_heif_opener
from pathlib import Path
import os

register_heif_opener()

parent_path = Path(__file__).parent.parent.resolve()
print(parent_path)

heic_path = parent_path / "heic_images"
image_path = parent_path / "jpg_images"

dir_list = os.listdir(heic_path)
print("Directory List : ", dir_list)

for each in dir_list:
    if each.endswith(".heic") or each.endswith(".HEIC"):
        img = Image.open(heic_path/each)
        img.convert('RGB').save(f"{image_path}/{each[:-5]}.jpg")

# # Open HEIF or HEIC file
# image = Image.open('example.heic')

# # Convert to JPEG
# image.convert('RGB').save('example.jpg')