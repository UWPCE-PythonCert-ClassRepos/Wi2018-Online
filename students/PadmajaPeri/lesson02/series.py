#!/usr/bin/env python

"""
This program returns the nth term in fibonacci or lucas series given n as the
input argument
"""


def fibonacci(n):
    """
    This function computes the nth term in the fibonacci series. It takes n as
    the input argument and returns its value. If n is negative it returns
    None. The series starts at 0th term. The first 2 numbers in the sequence are
    0 and 1.
    :param n: the number of the term in the sequence to return
    :return: the value of the nth term
    """
    if n <= 0:
        return 0
    return sum_series(n, 0, 1)


def lucas(n):
    """
    This function computes the nth term in the lucas series. It takes n as
    the input argument and returns its value. If n is negative it returns
    None. The series starts at 0th term. The first 2 numbers in the sequence are
    1 and 2.
    :param n: the number of the term in the sequence to return
    :return: the value of the nth term
    """
    if n <= 0:
        return 0
    return sum_series(n, 2, 1)


def sum_series(n, first_term, second_term):
    """
    This function holds the common logic to compute the nth term in the Fibonacci/
    Lucas series.Both of them are based on the formula, f(n) = f(n - 1) + f(n - 2)
    :param n: nth term whose value is to be computed
    :param first_term: The first value in the sequence
    :param second_term: The second value in the sequence
    :return:
    """
    if n == 1:
        return first_term
    elif n == 2:
        return second_term
    else:
        return sum_series(n - 1, first_term, second_term) + sum_series(n - 2,
                                                    first_term, second_term)


if __name__ == '__main__':
    """
    Test the values in fibonacci series
    """
    assert fibonacci(0) == 0   # Test with 0
    assert fibonacci(1) == 0   # First Term
    assert fibonacci(-1) == 0  # Negative Term
    assert fibonacci(8) == 13
    assert fibonacci(5) == 3

    assert lucas(0) == 0   # Test with 0
    assert lucas(1) == 2   # First Term
    assert lucas(2) == 1
    assert lucas(-10) == 0 # Negative term
    assert lucas(5) == 7
