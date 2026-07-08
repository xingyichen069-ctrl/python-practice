"""
This script is for Batch Rename: certain kinds of images in relevant folders
Sort by modification time (oldest to newest)
"""

import os

folder = "test_images"

# 1. 获取所有图片文件
files = [f for f in os.listdir(folder) if f.endswith((".jpg", ".png"))]

if not files:
    print("⚠️ 没有找到 .jpg 或 .png 文件")
    exit()

# 2. 按修改时间排序（从旧到新）
files.sort(key=lambda f: os.path.getmtime(os.path.join(folder, f)))

# 3. 开始重命名
jpg_count = 1
png_count = 1

print(f"📁 找到 {len(files)} 个文件，按修改时间排序...\n")

for f in files:
    oldpath = os.path.join(folder, f)
    
    if f.endswith(".jpg"):
        newname = f"IMG_JPG_{jpg_count:03d}.jpg"
        jpg_count += 1
    elif f.endswith(".png"):
        newname = f"IMG_PNG_{png_count:03d}.png"
        png_count += 1
    else:
        continue
    
    newpath = os.path.join(folder, newname)
    os.rename(oldpath, newpath)
    print(f"✅ {f} → {newname}")

print(f"\n🎉 重命名完成！共处理 {jpg_count+png_count-2} 个文件")

#知识点1：列表生成式
#知识点2：如何获得文件：相对路径计入文件名，同级文件夹直接使用，若脚本和图片同级则使用 "."，若上级则使用如 "../想要的文件夹名"
#知识点3：os.listdir(folder)获取folder中文件
#知识点4：通过f.endswith获得后缀 ；可以用（）元组而不是or进行多类型选择；也可以通过 files = [f for f in os.listdir(folder) if (f.endswith(ext) for ext in extensions)]
#知识点5：os.path.join(folder,newname)将文件名和目录拼接(加\),而os.rename在不使用cd到对应目录运行的话确实需要完整路径

#功能新增：根据最后修改时间从旧到新修改文件；进行修改计数；JPG\PNG 分开编号
#知识点6：os.path.getmtime(os.path.join(folder, f)) 完整路径（目录+文件名）
