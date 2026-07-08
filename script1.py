"""
This script is for Batch Rename: certain kinds of images in relevant folders
"""

import os

folder = "test_images"
files = [f for f in os.listdir(folder) if (f.endswith(".jpg") or f.endswith(".png"))]
prefix = "IMG"

i = 1
for f in files:
    oldname = f  
    if f.endswith(".jpg"):
        newname = f"IMG_JPG_{i}.jpg"
        os.rename(os.path.join(folder, oldname), os.path.join(folder, newname))
        print(f"**已将{oldname}命名为{newname}**")
        i += 1
    elif f.endswith(".png"): 
        newname = f"IMG_PNG_{i}.png"
        os.rename(os.path.join(folder, oldname), os.path.join(folder, newname))
        print(f"**已将{oldname}命名为{newname}**")
        i += 1

print("已全部完成")

#知识点1：列表生成式
#知识点2：如何获得文件：相对路径计入文件名，同级文件夹直接使用，若脚本和图片同级则使用 "."，若上级则使用如 "../想要的文件夹名"
#知识点3：os.listdir(folder)获取folder中文件
#知识点4：通过f.endswith获得后缀 ；可以用（）元组而不是or进行多类型选择；也可以通过 files = [f for f in os.listdir(folder) if (f.endswith(ext) for ext in extensions)]
#知识点5：os.path.join(folder,newname)将文件名和目录拼接(加\),而os.rename在不使用cd到对应目录运行的话确实需要完整路径