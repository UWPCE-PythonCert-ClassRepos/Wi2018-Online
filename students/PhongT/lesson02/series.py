"""
Lesson 02
Fibonacci Series Exercise
"""


def fibonacci(n):
    """The Fibonacci Series"""
    if n <= 0:
        print("Invalid input: n must be >= 0")
        raise ValueError
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """The Lucas Number"""
    if n <= 0:
        print("Invalid input: n must be >= 0")
        raise ValueError
    elif n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)



def sum_series(n, element_0 = 0, element_1 = 1):
    """
    :param n: nth number
    :param element_0/element_1: value of zeroth, and 1st number in the series
        If element_0=0, element_1=1 then it is fibonacci.
        Otherwise element_0=2, element_1=1 then it is lucas
    :return: nth value in the series
    """
    # check if valid input for element_0 and element_1: either 0/1, or 2/1
    if not (element_0==0 and element_1==1 or element_0==2 and element_1==1):
        print("Invalid element_0/element_1 arguments")
        raise ValueError

    if n <= 0:
        print("Invalid input n: n must be > 0")
        raise ValueError
    elif n == 1:
        return element_0
    elif n == 2:
        return element_1
    else:
        return sum_series(n - 1, element_0, element_1) + sum_series(n - 2, element_0, element_1)


def test_fibonacci():
    """ test fibonacci series """
    assert (fibonacci(1) == 0)
    assert (fibonacci(2) == 1)
    assert (fibonacci(3) == 1)
    assert (fibonacci(4) == 2)
    assert (fibonacci(5) == 3)
    assert (fibonacci(6) == 5)

def test_lucas():
    """ test lucas series """
    assert (lucas(1) == 2)
    assert (lucas(2) == 1)
    assert (lucas(3) == 3)
    assert (lucas(4) == 4)
    assert (lucas(5) == 7)
    assert (lucas(6) == 11)

def test_sum_series():
    # test fibonacci
    assert (sum_series(1, 0, 1) == 0)
    assert (sum_series(2,     ) == 1) # test optional params with default values
    assert (sum_series(3, 0, 1) == 1)
    assert (sum_series(4, 0, 1) == 2)
    assert (sum_series(5, 0, 1) == 3)
    assert (sum_series(6, 0, 1) == 5)

    # test lucas
    assert (sum_series(1, 2, 1) == 2)
    assert (sum_series(2, 2, 1) == 1)
    assert (sum_series(3, 2, 1) == 3)
    assert (sum_series(4, 2, 1) == 4)
    assert (sum_series(5, 2, 1) == 7)
    assert (sum_series(6, 2, 1) == 11)


if __name__ == "__main__":
    # testing
    test_fibonacci()
    test_lucas()
    test_sum_series()
