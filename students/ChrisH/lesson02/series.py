# -----------------------------------------------------------
# series.py
#  Compute the Fibonacci and Lucas series.
# -----------------------------------------------------------


def fibonacci(n):
    """
    Computes the nth value in the Fibonacci series.
    :param n: n is the desired nth value in the series
    :return: Returns the nth value in the Fibonacci series
    """
    # Lower bounds check
    if n <= 0:
        return None

    # Exit statements from recursion
    if n == 1:
        return 0
    if n == 2:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """
    Computes the nth value in the Lucas series.
    :param n: n is the desired nth value
    :return: return nth value in Lucas series
    """
    # Lower bounds check
    if n <= 0:
        return None

    # Exit statements from recursion
    if n == 1:
        return 2
    if n == 2:
        return 1

    return lucas(n-1) + lucas(n-2)


def sum_series(n, start1=0, start2=1):
    """
    Generalized function to compute the sum of the two previous values in a series.
    Defaults to the Fibonacci series sum.
    :param n: the desired nth value in the series
    :param start1: value for first number in the series (Fib = 0, Lucas = 2)
    :param start2: value for second number in the series (Fib = 1, Lucas = 1)
    :return: nth value in the series based on start numbers
    """
    # Lower bounds check
    if n <= 0:
        return None

    # Exit statements from recursion
    if n == 1:
        return start1
    if n == 2:
        return start2

    # Note: have to provide start1, start2 on the recursive call, otherwise, the Lucas series
    #  will become the Fibonacci in the recursion due to default parameter values
    return sum_series(n-1, start1, start2) + sum_series(n-2, start1, start2)


def main():
    """
    Test functions using asserts.
    :return: None
    """
    # Test data format:
    #   List containing a List for each function to be tested.
    #   Each function test data set has:
    #       test function name to be called as the first element,
    #       followed by data tuples (desired_n_value, expected_result)
    test_data = [
        [fibonacci, (-15, None), (1, 0), (9, 21), (10, 34), (16, 610), (20, 4181), (30, 514229), ],
        [lucas, (-15, None), (1, 2), (2, 1), (3, 3), (4, 4), (5, 7), (6, 11), (7, 18), (30, 1149851), ],
    ]

    print("Assert tests:")
    for test in test_data:
        series_fn = test[0]
        for n, result in test[1:]:
            print(series_fn.__name__, 'given', n, 'expected result', result)
            assert series_fn(n) == result

    print("\nGeneralized function Assert tests:")
    for test in test_data:
        series_name = test[0].__name__
        for n, result in test[1:]:
            print(series_name, 'given', n, 'expected result', result)
            if series_name == 'lucas':
                assert sum_series(n, 2, 1) == result
            else:
                assert sum_series(n) == result      # Use default parameter values for Fibonacci


if __name__ == "__main__":
    main()
