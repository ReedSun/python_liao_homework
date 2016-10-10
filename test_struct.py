# 检查文件是否是位图文件（*.bmp），如果是，输出图片大小和颜色数。
import struct
print("这个程序用来检查一个文件是否是一个位图文件")
file = input("请输入你要检查的文件路径")
with open(file, "rb") as f:
    result = f.read(30)

feature = struct.unpack("<ccIIIIIIHH", result)

if feature[0:2] == (b"B", b"M"):
    print("这是一个位图文件")
    print("他的图片大小为%s" % feature[2])
    print("他的颜色数为%s" % feature[-1])
else:
    print("这不是一个位图文件")
print("结束")
