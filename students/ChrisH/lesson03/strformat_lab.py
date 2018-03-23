#!/usr/bin/env python3
# -----------------------------------------------------------
# strformat_lab.py
#  demonstrates basic Python string formatting
# -----------------------------------------------------------

# Task One
data = (2, 123.4567, 10000, 12345.67)
print("file_{:03d} :{:9.2f}, {:.2e}, {:.2e}".format(data[0], data[1], data[2], data[3]))

# Task Two
print("file_{:03d} :{:9.2f}, {:.2e}, {:.2e}".format(*data))
print(f"file_{data[0]:03d} :{data[1]:9.2f}, {data[2]:.2e}, {data[3]:.2e}")


# Task Three


def formatter(in_tuple):
    """
    Dynamically format a tuple of numbers with a format string.
    :param in_tuple: tuple of any length, containing numbers
    :return: formatted string of output text
    """
    in_tuple_length = len(in_tuple)
    form_string = "the {} numbers are: ".format(in_tuple_length)
    form_string += ', '.join(['{:d}'] * in_tuple_length)

    return form_string.format(*in_tuple)


print(formatter((2, 3, 5, 7, 9)))
print(formatter((2, 3, 5)))

# Task Four
data = (4, 30, 2017, 2, 27)
# Output should be: '02 27 2017 04 30'
print("{:02d} {:02d} {:d} {:02d} {:02d}".format(data[3], data[4], data[2], data[0], data[1]))
print("{3:02d} {4:02d} {2:d} {0:02d} {1:02d}".format(*data))

# Task Five
data = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {data[0][:-1]} is {data[1]} and the weight of a {data[2][:-1]} is {data[3]}")
print(f"The weight of an {(data[0][:-1]).upper()} is {data[1] * 1.2} \
and the weight of a {(data[2][:-1]).upper()} is {data[3] * 1.2}")

# Task Six
people = [('Bill', 10, '$10439.99'), ('Elizabeth', 35, '$75000.01'), ('Norman', 70, '$15.95'), ('Alice', 3, '$425.55')]
print("{:<12} {:>3} {:>11}".format('Name', 'Age', 'Cost'))
for person in people:
    print("{:<12} {:>3} {:>11}".format(*person))

data_num = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(("{:5}"*len(data_num)).format(*data_num))

