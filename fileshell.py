import os
from os import path
import shutil
from zipfile import ZipFile
if path.exists("sample2.txt"):
#     src = path.realpath("sample1.txt")
#     dst = src + ".bak"
#     shutil.copy(src, dst)
# os.rename("sample1.txt", "sample2.txt")
    root_dir, tail = path.split(path.realpath("sample2.txt"))
    print(root_dir)
    print(tail)
    shutil.make_archive("archive", "zip", root_dir)
    with ZipFile("archive.zip", "w") as zip:
        zip.write("sample2.txt")
        zip.write("sample.txt")
        zip.write("sample1.txt.bak")
else:
    print("The file does not exist")
