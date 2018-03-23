#! python3
#if __name__ == '__main__':
#if __name__=='__main__':
    #print('This is run by itself2')
#else:
    #print('Run as a module2')
# Fininacci Series
print(__name__)

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
def genseries(n, x=0, y=1):
    if n==0:
        return x
    elif n==1:
        return y
    elif n > 1:
        return genseries(n-1, x, y) + genseries(n-2, x, y)

if __name__=="__main__":
    print('This is run as module')
else:
    print('This is run as a script')

    
