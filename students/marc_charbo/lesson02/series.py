#!/usr/bin/env python3

import sys

def fibonacci(n=5):
    """Return the nth value in the fibonacci series"""
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

def lucas(n=5):
    """Return the nth value in the lucas series"""
    if (n==0):
        return 2
    elif (n==1):
        return 1
    else:
        return lucas(n-2) + lucas(n-1)

def sum_series(n,return_value_1=0,return_value_2=1):
    """Return the nth value in the fibonacci  or lucas series
    default value for both series is 5.
    return_value_1 and return_value_2 indicates which series to run.
    return values 0 and 1 will run fibonacci and 2 and 1 will run lucas.
    """
    if (n==0):
        return return_value_1
    elif (n==1):
        return return_value_2
    else:
        return sum_series(n-2,return_value_1,return_value_2) + sum_series(n-1,return_value_1,return_value_2)

def main(argv=None):
    """Four assert statement test the 3 functions above
    first assert makes sure fibonacci function returns 5 using n=5 default value
    second assert makes sure lucas function returns 11 using n=5 default value
    third assert makes sure sum_series function returns 5 using n=4, 0&1 for fibonacci
    fourth assert makes sure sum_series function returns 11 using n=4, 2&1 for lucas
    """
    print (argv)
    assert fibonacci()==5,"error with fibonacci function"
    assert lucas()==11,"error with lucas function"
    assert sum_series(4,0,1)==3,"error with sum_series for fibonacci arguments"
    assert sum_series(4,2,1)==7,"error with sum_series for lucas arguments"


if __name__ == "__main__":
    main()