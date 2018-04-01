#!/usr/bin/env python

"""
This program prints the numbers from 1 to 100 inclusive. If the number is
multiple of both 3 and 5, it prints FizzBuzz
If it is a multiple of 3, it prints Fizz
If it is a multiple of 5, it prints Buzz
Otherwise, it prints the number.
"""


def fizz_buzz_func(start, end):
    # Loop till end + 1 so that end is included.
    for num in range(start, end+1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


if __name__ == '__main__':
    fizz_buzz_func(1, 100)
