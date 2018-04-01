#!/usr/bin/env python3

# Name error - Calls a variable that doesn't exist
def error_name():
    print(test_name_error)

error_name()

# TypeError
def error_type():
    a = 5
    b = "some string"
    return a + b


error_type()


# SyntaxError - left off colon
def error_syntax()
    print("error")


error_syntax()

# AttributeError
def error_attr(a, b):
    import collections
    test = collections.noWayThisExists(a, b)
    return test


error_attr(5, 8)

import collections

my_tuple = collections.namedtuple("MyTuple", 'food price')
