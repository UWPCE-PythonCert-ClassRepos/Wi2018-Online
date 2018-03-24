#!/usr/bin/env python3
"""
String Formatting Lab Exercises
__author__ == "Padmaja Peri"
"""


def task_one(*args):
    """ Function that formats 4 element tuple"""
    return "file_{:0>3d}  :{:.2f},{:.2e},{:.3g}".format(*args)


def task_two(a, b, c, d):
    """ Alternate way to accomplish the task_one output """
    return f"file_{a:0>3d}  :{b:.2f}," \
           f"{c:.2e},{d:.3g}"


def formatter(input_tuple):
    """ Helper Function to build dynamic formatting strings """
    len_tuple = len(input_tuple)
    format_string = ",". join(["{}"] * len_tuple).format(*input_tuple)
    return ("There are {} items, and they are:" + format_string).\
        format(len_tuple, *input_tuple)


def task_three(input_tuple):
    """ Function to build dynamic formatting strings """
    return formatter(input_tuple)


def task_four(input_tuple):
    """
    Function to print using positional args
    Ex: Input is - ( 4, 30, 2017, 2, 27)
    Output will be of form - '02 27 2017 04 30'
    """
    return "{3} {4} {2} {0} {1}".format(input_tuple[0],
                                        input_tuple[1],
                                        input_tuple[2],
                                        input_tuple[3],
                                        input_tuple[4])


def task_five(input_list):
    """
    Function that uses f-strings to format a 4 element list
    The list is ['oranges', 1.3, 'lemons', 1.1]
    """
    formatted_str = f'The weight of an {input_list[0][:-1].upper()} is ' \
                    f'{input_list[1] * 1.2}' \
                    f' and the weight of a {input_list[2][:-1].upper()} is ' \
                    f'{input_list[3] * 1.2}'
    return formatted_str


if __name__ == '__main__':
    print(task_one(2, 123.4567, 10000, 12345.67))
    print(task_two(2, 123.4567, 10000, 12345.67))
    input_tuple = (4, 30, 2017, 2, 27, 200, 300, 800)
    print(task_three(input_tuple))
    print(task_four([4, 30, 2017, 2, 27]))
    print(task_five(['oranges', 1.3, 'lemons', 1.1]))


