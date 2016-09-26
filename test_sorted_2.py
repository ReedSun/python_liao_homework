# -*- coding: utf-8 -*-

# 再按成绩从高到低排序：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_score(t):
    return t[1]

L2 = sorted(L,key=by_score,reverse=True)
print(L2)