print("If the fibonacci series is required, please type fib(n), where n is the n'ieth number of the Fibonacci series\n\n")
def fib(n):
    """
    Presents to the user the n'ieth number in the
    Fibonacci series, where 'n' is a number input
    by the user.
    """
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)


print("If the lucas series is required, please type lucas(n), where n is the n'ieth number of the Lucas series\n\n")
def lucas(n):
    """
    Presents to the user the n'ieth number in the
    Lucas series, where 'n' is a number input
    by the user.
    """
    if n == 0:
        return(2)
    elif n==1:
        return(1)
    return lucas(n-2) + lucas(n-1)


o=0
p=1
print("Finally, if a more general sum series is required, please type sum_series(n,o,p), where n is the n'ieth number of the sum series. Default values for 'o' and 'p' are 0 and 1, respectively.\n\n")
def sum_series(n,o,p):
    """
    Presents to the user the n'ieth number in the
    Sum series, where 'n' is a number input
    by the user. The 'o' and 'p' optional values
    are, by default, 0 and 1. If left this way, the
    sum series will return the result of the n'ieth 
    number in the Fibonacci series. If changed, it
    will return other series. 
    """
    if n == 0:
        return(o)
    elif n==1:
        return(p)
    return sum_series(n-2,o,p) + sum_series(n-1,o,p)

def main():
    assert fib(30) == 832040
    assert fib(2) == 1
    assert fib(4) == 3
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(4) == 7
    assert sum_series(3,0,1) == 2
    assert sum_series(8,2,1) == 47
    assert sum_series(5,3,7) == 44
    assert sum_series(7,4,3) == 71
    assert sum_series(4,2,1) == 7
    print("Tests concluded. Everything in order.\n")

if __name__ == '__main__':
    main()