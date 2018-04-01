#!/usr/bin/env python3

# UW Python 210A - Lesson02


def fibonacci(n):
    """Return the nth value in a fibonacci sequence."""
    if n < 0:
        return None
    elif n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """This function will return a related series of integers that start
    with the values 2 and 1 rather than 0 and 1."""
    if n <= 0:
        print("The use of zero is not a valid input.")
    elif n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, opt1=0, opt2=1):
    """This function will return the sum of either a
    Fibonacci or Lucas series dependingon the inputs.
    """

    if n <= 0:
        print("The use of zero is not a valid input.")
    elif n == 1:
        return opt1
    elif n == 2:
        return opt2
    else:
        return sum_series(n - 1, opt1, opt2) + sum_series(n - 2, opt1, opt2)


def test_fib():
    """Test the Fibonacci series function."""
    print("Testing for assertion errors...")
    assert (fibonacci(0) == 0)
    assert (fibonacci(1) == 1)
    assert (fibonacci(2) == 1)
    assert (fibonacci(3) == 2)
    assert (fibonacci(4) == 3)
    print("No assertion errors found running the test on Fibonacci series function.")


def test_lucas():
    """Test the Fibonacci series function."""
    assert (lucas(1) == 2)
    assert (lucas(2) == 1)
    assert (lucas(3) == 3)
    assert (lucas(4) == 4)
    assert (lucas(5) == 7)
    print("No assertion errors found running the test on Lucas series function.")

def test_sum_series():
    """Testing out the sum_series function on both Fibonacci and Lucas"""
    # Testing the sum_series function on Fibonacci Series
    assert (sum_series(1, 0, 1) == 0)
    assert (sum_series(2, 0, 1) == 1)
    assert (sum_series(3, 0, 1) == 1)
    assert (sum_series(4, 0, 1) == 2)
    assert (sum_series(5, 0, 1) == 3)

    # Testing the sum_series function on Lucas Series
    assert (sum_series(1, 2, 1) == 2)
    assert (sum_series(2, 2, 1) == 1)
    assert (sum_series(3, 2, 1) == 3)
    assert (sum_series(4, 2, 1) == 4)
    assert (sum_series(5, 2, 1) == 7)

    print("No assertion errors found running the test on sum series function.")

test_fib()
test_lucas()
test_sum_series()
