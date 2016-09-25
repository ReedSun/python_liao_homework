# -*- coding: utf-8 -*-

#杨辉三角
#把杨辉三角的每一行看做一个list，试写一个generator，不断输出下一行的list：
def triangles():
    n=[1]
    while True:
        yield n
        n.append(0)
        n=[n[x]+n[x-1] for x in range(len(n))]
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break