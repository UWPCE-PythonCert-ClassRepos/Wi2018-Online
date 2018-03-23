#!/usr/bin/env python

def fibonacci(n):
    """
    The function fibonacci returns the nth term of the Fibonacci sequence. The first two elements of 
    the fibonacci sequence are initialized with values of 0 and 1. Then, subsequent values are created by
    adding the previous two values of the sequence. The third element is equal to the sum of the 1st
    and 2nd elements (i.e., 0 + 1 = 1), the fourth element is the sum of the 2nd and 3rd elements, 
    and so on and so forth. As you can see, the sequence is constructed recursively. 
    """
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        results = []
        results.append(0)
        results.append(1)
        for i in range(2, n+1):
            new_value = fibonacci(i - 2) + fibonacci(i - 1)
            results.append(new_value)
        return results[n]

print('The result of fibonacci(10) is ' + str(fibonacci(10)))

def lucas(n):
    """
    The function lucas returns the nth term of the Lucas sequence. The Lucas sequence is identical to the 
    Fibonacci sequence, except that its first two elements are 2 and 1, rather than 0 and 1. 
    """
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        results = []
        results.append(2)
        results.append(1)
        for i in range(2, n+1):
            new_value = lucas(i-2) + lucas(i - 1)
            results.append(new_value)
        return results[n]

print('The result of lucas(10) is ' + str(lucas(10)))

def sum_series(n, elem1 = 0, elem2 = 1):
    """
    The function sum_series generalizes the fibonacci and lucas functions into one function 
    that takes 3 arguments. The first is a required parameter, n, that specifies the index 
    number of the number that you want to return. The second and third parameters are optional, and they
    default to the first two elements of the Fibonacci sequence. If these elements are unchanged
    when the function is called, it will default to the Fibonacci sequence. If you call it with
    the parameters of 2 and 1, it will return the nth Lucas number. If other values are used, it will
    return different series. 
    """
    if n == 1:
        return elem1
    elif n == 2:
        return elem2
    else:
        results = []
        results.append(elem1)
        results.append(elem2)
        for i in range(2, n+1):
            new_value = sum_series(i - 2, elem1, elem2) + sum_series(i - 1, elem1, elem2)
            results.append(new_value)
        return results[n]

print('The 10th element of the Fibonacci sequence is ' + str(sum_series(10)))
print('The 10th element of the Lucas sequence is ' + str(sum_series(10, 2, 1)))


# check that 1st and 2nd results of the fibonacci sequence are 0 and 1
assert fibonacci(1) == 0
assert fibonacci(2) == 1

# check that 5th element of the fibonacci sequence is 3
assert fibonacci(5) == 3

# check that 1st and 2nd results of the lucas sequence are 2 and 1
assert lucas(1) == 2
assert lucas(2) == 1

# check that the 7th element of the lucas sequence is 18
assert lucas(7) == 18

# check that the 5th sum_series element with default values is 3
assert sum_series(5) == 3

# check that the 7th element of sum_series with initial values of 2 and 1 is 18
# this is the lucas series, which is why it is equivalent to the above assertion that
# lucas(7) == 18. 
assert sum_series(7, elem1 = 2, elem2 = 1) == 18





