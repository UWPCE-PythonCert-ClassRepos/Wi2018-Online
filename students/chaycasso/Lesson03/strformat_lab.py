#!/usr/bin/env python3
#
# String Format Lab
# Chay Casso, 2/6/2018

# Task One
# Write a format string that will take the following four element tuple:
# ( 2, 123.4567, 10000, 12345.67)
# and produce:
# 'file_002 :   123.46, 1.00e+04, 1.23e+04'

initial_tuple = (2, 123.4567, 10000, 12345.67)
resultant_string = "file_{:0>3d} : {:.2f}, {:.2e}, {:.2e}".format(*initial_tuple)
print(resultant_string)

# Task Two
# Using your results from Task One, repeat the exercise, but this time using an alternate type of format string
resultant_string2 = f"file_{initial_tuple[0]:0>3d} : {initial_tuple[1]:.2f}, {initial_tuple[2]:.2e}, " \
                    f"{initial_tuple[3]:.2e}"
print(resultant_string2)

# Task Three
# Dynamically Building up Format Strings

# Rewrite:
# "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
# to take an arbitrary number of values.


def formatter(in_tuple):
    length = len(in_tuple)
    form_string = f"the {length} numbers are: "
    for i in range(length):
        form_string = "".join([form_string, "{:d}, "])
    form_string = form_string[:-2]  # Truncating the last comma-space in the string.
    return form_string.format(*in_tuple)


print(formatter((2,3,5)))
print(formatter((2,3,5,7,9)))

# Task Four
# Given a 5 element tuple:
# ( 4, 30, 2017, 2, 27)
# use string formating to print:
# '02 27 2017 04 30'

initial_tuple = (4, 30, 2017, 2, 27)
resultant_string3 = "'{:0>2d} {:0>2d} {:0>4d} {:0>2d} {:0>2d}'".format(initial_tuple[3],initial_tuple[4],
                                                                       initial_tuple[2],initial_tuple[0],
                                                                       initial_tuple[1])
print(resultant_string3)

# Task Five
# Here’s a task for you: Given the following four element list:
# ['oranges', 1.3, 'lemons', 1.1]
initial_list = ['oranges', 1.3, 'lemons', 1.1]

# Write an f-string that will display:
# The weight of an orange is 1.3 and the weight of a lemon is 1.1

resultant_string4 = (f"The weight of an {initial_list[0][:-1]} is {initial_list[1]} and the weight of "
                     f"a {initial_list[2][:-1]} is {initial_list[3]}.")
print(resultant_string4)

# Now see if you can change the f-string so that it displays the names of the fruit in upper case, and the weight
# 20% higher (that is 1.2 times higher).

resultant_string5 = (f"The weight of an {initial_list[0][:-1].upper()} is {initial_list[1] * 1.2} and the weight of "
                     f"a {initial_list[2][:-1].upper()} is {initial_list[3] * 1.2}.")
print(resultant_string5)

# Task Six
# Write some Python code to print a table of several rows, each with a name, an age and a cost. Make sure some of the
# costs are in the hundreds and thousands to test your alignment specifiers.
initial_table = ([["Port", "25", "20.00"],["Stout","100","120.50"],
                  ["Bordeaux", "43", "1250.25"],["Pinot Noir", "61", "512.80"]])
table_width_x, table_width_y, table_width_z = [0, 0, 0]

# Running through all data points to see what the maximum width needs to be for a given column.
for row in initial_table:
    if table_width_x < len(row[0]): table_width_x = len(row[0])
    if table_width_y < len(row[1]): table_width_y = len(row[1])
    if table_width_z < len(row[2]): table_width_z = len(row[2])

for row in initial_table:
    print("{:>{width}} | {:^{width2}} | ${:<{width3}}".format(row[0], row[1], row[2],
                                                             width=table_width_x, width2=table_width_y,
                                                             width3=table_width_z))

# And for an extra task, given a tuple with 10 consecutive numbers, can you work how to quickly print the tuple in
# columns that are 5 charaters wide? It’s easily done on one short line!

tuple = (1, 10, 100, 1000, 10000, 2, 20, 200, 2000, 20000)
# I can't figure this one out because I don't know how to unpack the tuple here. Best guess is:
# print("{:>5}"*10.format(tuple)
