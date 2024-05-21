from heic2png import HEIC2PNG
from pathlib import Path

parent_path = Path(__file__).parent.parent.resolve()
print(parent_path)

heic_path = parent_path / "heic_images"
image_path = parent_path / "png_images"

# dir_list = os.listdir(heic_path)
# # print("Files and directories in '", path, "' :")
# # print(dir_list)
for each in heic_path.iterdir():
    file_name = Path(each).name
    if file_name.endswith(".heic") or file_name.endswith(".HEIC"):
        img = HEIC2PNG(each, quality=70)
        img.save(f"{image_path}/{file_name[:-4]}.png")