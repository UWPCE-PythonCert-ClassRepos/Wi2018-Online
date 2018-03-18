#!/usr/bin/env python3
"""Lesson 3 task 3 string formatting re-write"""


def number_Formatter(in_tuple):
    out_list = []
    for number in in_tuple:
        out_list.append('${:,.2f}'.format(number))  # format numbers to dollar format and add to the list
    return (out_list)


my_tuple = (1, 2, 3)
dollars = (number_Formatter(my_tuple))
dollar_string = ", ".join(str(x) for x in dollars)  # create a string because it looks better when printing
print(f'The amounts are {dollar_string}')
