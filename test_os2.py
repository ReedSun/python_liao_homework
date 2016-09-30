#！/usr/bin/env python
# -*- coding: utf-8 -*-

import os
keyword = input("请输入你要搜索的字符")
up = "."  # . 代表当前的路径，.. 代表当前路径的上一级路径。
result = []

def check(up,keyword):
    all = os.listdir(up)  #os.listdir(path)返回定目录下的所有文件名和目录名
    for x in all:         # all 是一个包含目录中所有文件和目录名的列表
        try:
            abs_x = os.path.join(up,x)   #os.path.join(path,name)连接path和name
            if os.path.isdir(abs_x):    #os.path.isdir()检验给出的目录是否是一个目录
                up = os.path.join(up,x)
                check(up,keyword)    #递归结构
            if os.path.isfile(abs_x):   #os.path.isfile()检验给出的目录是否是一个文件
                if keyword in x:
                    result.append(abs_x)
        except:
            continue   #跳出本次循环
            
check(up,keyword)
print("找到%d个文件" %len(result))
for r in result:
    print(r)
print("+++end+++")
os.system("pause")     #os.system的意思是执行系统中cmd的指令。cmd指令pause是指暂停，等待用户回车之后，执行下一条语句
                