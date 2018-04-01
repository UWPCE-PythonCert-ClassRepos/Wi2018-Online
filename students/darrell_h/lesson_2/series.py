#!/usr/local/bin/python3
import sys


def fib(n, seq='initial'):
    """Recursive function returning Fibonacci seq or Lucas"""
    print(seq, n)
    # sys.exit()
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1, 'primary: ') + fib(n - 2, 'secondary: ')


def lucus(n):
    """Recursive function returning lucus seq"""
    print(n)
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucus(n - 1) + lucus(n - 2)


def calc(type, n):
    """Iterate a range of numbers adding the fib or lucus numbers to a str"""
    result = ''
    for i in range(n):
        if type == 'fib':
            result += str(fib(i)) + ','
        if type == 'lucus':
            result += str(lucus(i)) + ','
    return result


def generic(n, x=0, y=1):  # default fib
    # print(n,x,y)
    if n == 0:
        return x
    elif n == 1:
        return y
    else:
        return generic(n - 1, x, y) + generic(n - 2, x, y)


if __name__ == "__main__":
    print('fibonacci:::', calc('fib', 10))
    print('lucus:::::::', calc('lucus', 10))
