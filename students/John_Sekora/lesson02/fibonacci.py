# 0, 1, 1, 2, 3, 5, 8, 13, ...
def fibonacci(n):
    '''The Fibonacci Series'''
    if n <= 0:
        print("ERROR: Fibonacci Series input requires a number greater than zero")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)


print(fibonacci(7))


# 2, 1, 3, 4, 7, 11, 18, 29, ...
def lucas(n):
    '''The Lucas Numbers'''
    if n <= 0:
        print("ERROR: Lucas Number input requires a number greater than zero")
    elif n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n-2) + lucas(n-1)


print(lucas(7))


def sum_series(n, first=0, second=1):
    """Fibonacci & Lucas"""
    if n == 1:
        return first
    elif n == 2:
        return second
    else:
        return sum_series(n - 2, first, second) + sum_series(n - 1, first, second)


# Testing fibonacci
assert fibonacci(1) == 0, "Fibonacci Error: The expected value is 0"
assert fibonacci(2) == 1, "Fibonacci Error: The expected value is 1"
assert fibonacci(3) == 1, "Fibonacci Error: The expected value is 1"
assert fibonacci(4) == 2, "Fibonacci Error: The expected value is 2"
assert fibonacci(5) == 3, "Fibonacci Error: The expected value is 3"
assert fibonacci(6) == 5, "Fibonacci Error: The expected value is 5"
assert fibonacci(7) == 8, "Fibonacci Error: The expected value is 8"


# Testing lucas
assert lucas(1) == 2, "Lucas Error: The expected value is 2"
assert lucas(2) == 1, "Lucas Error: The expected value is 1"
assert lucas(3) == 3, "Lucas Error: The expected value is 3"
assert lucas(4) == 4, "Lucas Error: The expected value is 4"
assert lucas(5) == 7, "Lucas Error: The expected value is 7"
assert lucas(6) == 11, "Lucas Error: The expected value is 11"
assert lucas(7) == 18, "Lucas Error: The expected value is 18"


# Testing Sum Series (default parameters)
assert sum_series(1) == 0, "Sum Series Error: The expected value is 0"
assert sum_series(2) == 1, "Sum Series Error: The expected value is 1"
assert sum_series(3) == 1, "Sum Series Error: The expected value is 1"
assert sum_series(4) == 2, "Sum Series Error: The expected value is 2"
assert sum_series(5) == 3, "Sum Series Error: The expected value is 3"
assert sum_series(6) == 5, "Sum Series Error: The expected value is 5"
assert sum_series(7) == 8, "Sum Series Error: The expected value is 8"


# Testing Sum Series (2 and 1 as inputs)
assert sum_series(1, 2, 1) == 2, "Sum Series Error: The expected value is 2"
assert sum_series(2, 2, 1) == 1, "Sum Series Error: The expected value is 1"
assert sum_series(3, 2, 1) == 3, "Sum Series Error: The expected value is 3"
assert sum_series(4, 2, 1) == 4, "Sum Series Error: The expected value is 4"
assert sum_series(5, 2, 1) == 7, "Sum Series Error: The expected value is 7"
assert sum_series(6, 2, 1) == 11, "Sum Series Error: The expected value is 11"
assert sum_series(7, 2, 1) == 18, "Sum Series Error: The expected value is 18"


