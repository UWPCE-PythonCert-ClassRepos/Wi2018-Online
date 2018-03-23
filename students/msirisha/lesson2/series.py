# =============================== #
# Fibonacci series, Lucas numbers
# =============================== #

def fib(n):
    """
    prints the nth value fibonacci series
    :param n: n is the desired value in the series
    :return: returns the nth value in the fibonacci series
    """
    if n <= 0 :
        return None
    # conditions for recursive function to exit.
    elif n == 1:
       return 0
    elif n == 2:
        return 1

    return fib(n-2) + fib(n-1)

def lucas(n):
    """
    computes the nth value in lucas series.
    :param n: n is the desired value in the series
    :return: returns the nth value in lucas series
    """

    if n <= 0:
        return None
    # exit statements for recursive function
    elif n == 1:
        return 2
    elif n == 2:
        return 1

    return lucas(n-2) + lucas(n-1)

def sum_series(n, first=0, second=1):
    """ sum_series is unique function to print fibonacci series and lucas series based on
        given optional input values.
        :param n: desired n value in series
        :first : optional value, by defaul first number of fibonacci series
        :second : optional value, by default second number of fibonacci series
    """
    if n <= 0 :
        return None
    elif n == 1:
        return first
    elif n == 2:
        return second

    return sum_series(n-2, first, second) + sum_series(n-1, first, second)

def test_series():
    """ Test functions for asserts
        test_data contains lists of list. Each list item has function name as a first list element and a tuple of number n vs desired nth value in series
    Fibonacci - 0 1 1 2 3 5 8 13 21 34 55
    Lucas -   2 1 3 4 7 11 18 29 47 76 123
    """
    test_data = [
                [fib, (-1, None), (0, None), (1, 0), (2,1), (3, 1), (4,2), (5,3), (6,5), (7,8),(8,13),(9,21),(10,34), (11,55)],
                [lucas, (-1, None), (0, None), (1,2), (2,1), (3,3), (4, 4), (5, 7), (6,11), (7,18), (8, 29), (9, 47), (10, 76), (11, 123)]
                ]

    for item in test_data:
        func = item[0]
        for n, result in item[1:]:
            if func.__name__ == "fib":
                print("Running test with {} function, given value {}, expected  result {}".format(func.__name__, n , result))
                assert fib(n) == result
                print("Running test for fibonacci series with sum_series function, given value {}, expected  result {}\n".format(n, result))
                assert sum_series(n) == result
            elif func.__name__ == "lucas":
                print("Running test with {} function, given value {}, expected  result {}".format(func.__name__, n , result))
                assert lucas(n) == result
                print("Running test for lucas series with sum_series function, given value {}, expected  result {}\n".format(n, result))
                assert sum_series(n, 2, 1) == result

if __name__ == "__main__":
    test_series()