# -*- coding: utf-8 -*-

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
from functools import reduce

def str2float(s):

    left,right=s.split(".")
    L1=reduce(fn,map(char2num,left))
    L2=(reduce(fn,map(char2num,right))/10**(len(right)))
    return L1+L2
def fn(x, y):
    return x * 10 + y
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print('str2float(\'123.456\') =', str2float('123.456'))