"""Fibonacci, Lucas and general series functions."""


def fibonacci(n):
    """Return the nth term in the fibonacci series starting with 0 and 1."""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)


assert fibonacci(1) == 0, 'failed, expected 0'
assert fibonacci(2) == 1, 'failed, expected 1'
assert fibonacci(3) == 1, 'failed, expected 1'
assert fibonacci(4) == 2, 'failed, expected 2'
assert fibonacci(5) == 3, 'failed, expected 3'
assert fibonacci(6) == 5, 'failed, expected 5'
assert fibonacci(7) == 8, 'failed, expected 8'
assert fibonacci(8) == 13, 'failed, expected 13'


def lucas(n):
    """Return the nth term in the lucas series starting with 2 and 1."""
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n-2) + lucas(n-1)


assert lucas(1) == 2, 'failed, expected 2'
assert lucas(2) == 1, 'failed, expected 1'
assert lucas(3) == 3, 'failed, expected 3'
assert lucas(4) == 4, 'failed, expected 4'
assert lucas(5) == 7, 'failed, expected 7'
assert lucas(6) == 11, 'failed, expected 11'
assert lucas(7) == 18, 'failed, expected 18'
assert lucas(8) == 29, 'failed, expected 29'


def sum_series(n, first=0, second=1):
    """Return the nth term in a user-defined series."""
    if n == 1:
        return first
    elif n == 2:
        return second
    else:
        return sum_series(n-2, first, second) + sum_series(n-1, first, second)


# Test sum_series() with default values for optional parameters
assert sum_series(1) == 0, 'failed, expected 0'
assert sum_series(2) == 1, 'failed, expected 1'
assert sum_series(3) == 1, 'failed, expected 1'
assert sum_series(4) == 2, 'failed, expected 2'
assert sum_series(5) == 3, 'failed, expected 3'
assert sum_series(6) == 5, 'failed, expected 5'
assert sum_series(7) == 8, 'failed, expected 8'
assert sum_series(8) == 13, 'failed, expected 13'


# Test sum_series() with values 2 and 1 for optional parameters
assert sum_series(1, 2, 1) == 2, 'failed, expected 2'
assert sum_series(2, 2, 1) == 1, 'failed, expected 1'
assert sum_series(3, 2, 1) == 3, 'failed, expected 3'
assert sum_series(4, 2, 1) == 4, 'failed, expected 4'
assert sum_series(5, 2, 1) == 7, 'failed, expected 7'
assert sum_series(6, 2, 1) == 11, 'failed, expected 11'
assert sum_series(7, 2, 1) == 18, 'failed, expected 18'
assert sum_series(8, 2, 1) == 29, 'failed, expected 29'
