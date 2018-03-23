#!/usr/bin/env python

# Daniel Grubbs
# Date: 1/31/2018


def f_tuple(t):
    """Setup the format for printing the tuple."""
    print("file_{:03}: {:.2f} {:.2e} {:.3e}".format(t[0], t[1], t[2], t[3]))


f_tuple((2, 123.4567, 10000, 12345.67))


t = (1, 2, 3, 4, 5)
print('The three numbers: {} {} {}'.format(*t))


def formatter(nums):
    """Dynamioc strings with variable lengths."""
    form_string = ''
    for num in nums:
        form_string = form_string + '{:d} '
    temp = form_string.split()
    space = ', '
    form_string = space.join(temp)
    form_string = 'The ' + str(len(nums)) + ' numbers are: ' + form_string
    return form_string.format(*nums)


print(formatter((4, 6, 8, 10, 12)))


# Task 4
task4_tup = (4, 30, 2017, 2, 27)
print('{} {} {} {} {}'.format(*task4_tup))
print('{3:02d} {1} {2} {0:02d} {4}'.format(4, 30, 2017, 2, 27))

# Task 5
task5_list =['orange', 1.3, 'lemon', 1.1]
print('The weight of an {} is {} and the weight of a {} is {}'.format(*task5_list))


# Task 6
print('{:20}{:10}{:20}{:8}'.format('First', '$99.01', 'Second', '$88.09'))