# string formatting task 3
from __future__ import print_function


def stringformat(x):
    lst = x
    print(" the numbers are :" '{},{},{}'.format(*lst))


def stringformat1(x1):
    lst1 = x1
    l = len(lst1)
    x = '{},' * l
    b = x.format(*lst1)
    c = "the "'{}'.format(l)
    print(c, end='')
    print(" numbers in the list : ", end='')
    print(b)


lst1 = (1, 2, 4, 5, 6, 7, 8, 9, 10)
x = (1, 2, 4, 5, 6, 7, 8, 9, 10)
stringformat(x)
stringformat1(x)
