py#!/usr/local/bin/python3

#if __name__ == '__main__':

# Fininacci Series
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fib(n-1) + fib(n-2)

#for n in range (1, 20):
#    print (n, fib(n))

#Lucas series
def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n > 1:
        print('Test')
        return lucas(n-1) + lucas(n-2)

#GenSeries
def genseries(n, x=1, y=0):
    if n==0:
        return x
    elif n==1:
        return y
    elif n > 1:
        return genseries(n-1, x, y) + genseries(n-2, x, y)
