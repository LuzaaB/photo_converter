from heic2png import HEIC2PNG
import os
# import glob
# import pathlib

path = "E://Python//photo_converter"
dir_list = os.listdir(path)
# print("Files and directories in '", path, "' :")
# print(dir_list)
for each in dir_list: # os.listdir() can also be used
    if each.endswith(".heic") or each.endswith(".HEIC"):
        print(each)
        img = HEIC2PNG(each, quality=70)
        img.save()




# files = [f for f in pathlib.Path().iterdir() if f.is_file()]
# print(files)

# file = [f for f in pathlib.Path().glob("/photo_converter/*.png")]
# print(file)

# print(glob.glob("/photo_converter/*.png"))

# files = [f for f in os.listdir() if os.path.isdir(f)]
# print(files)