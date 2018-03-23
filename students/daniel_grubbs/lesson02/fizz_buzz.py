#!/usr/bin/env python3

# UW Python 210A - Lesson02


def print_fizz_buzz(n):
    """Write a program that prints the numbers from 1 to 100 inclusive.
    For multiples of 3 print 'Fizz'. For multiples of 5 print 'Buzz'.
    For numbers that are multiples of both 3 and 5 print 'FizzBuzz'."""
    for i in range(1, n + 1):
        seq = ""

        if i % 3 == 0:
            seq += 'Fizz'
        if i % 5 == 0:
            seq += 'Buzz'
        if seq == '':
            seq = i

        print(seq)


print_fizz_buzz(100)
