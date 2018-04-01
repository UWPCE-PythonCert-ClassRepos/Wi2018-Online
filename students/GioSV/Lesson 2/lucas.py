print("Please, call the function using lucas(n), where n is the n'ieth number of the Fibonacci series")
def lucas(n):
    if n == 0:
        return(2)
    elif n==1:
        return(1)
    return lucas(n-2) + lucas(n-1)
