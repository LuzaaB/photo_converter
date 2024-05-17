from heic2png import HEIC2PNG
import os
# import glob
from pathlib import Path

parent_path = Path(__file__).parent.parent.resolve()
print(parent_path)

heic_path = parent_path / "heic_images"
image_path = parent_path / "png_images"

dir_list = os.listdir(heic_path)
# print("Files and directories in '", path, "' :")
# print(dir_list)
for each in dir_list: # os.listdir() can also be used
    print("each ", each)
    if each.endswith(".heic") or each.endswith(".HEIC"):
        print(each)
        img = HEIC2PNG(heic_path / each, quality=70)
        img.save(f"{image_path}/{each[:-4]}.png")




# files = [f for f in pathlib.Path().iterdir() if f.is_file()]
# print(files)

# file = [f for f in pathlib.Path().glob("/photo_converter/*.png")]
# print(file)

# print(glob.glob("/photo_converter/*.png"))

# files = [f for f in os.listdir() if os.path.isdir(f)]
# print(files)