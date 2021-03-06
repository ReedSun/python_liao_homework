# -*- coding: utf-8 -*-

#对函数fact(n)编写doctest并执行
def fact(n):
    '''


    >>> fact(0)
    Traceback (most recent call last):
      ...
    ValueError
    >>> fact(1)
    1
    >>> fact(2)
    2
    >>> fact(3)
    6
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()