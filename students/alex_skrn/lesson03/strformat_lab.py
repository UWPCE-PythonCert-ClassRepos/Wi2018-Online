#!/usr/bin/env python3

"""Lesson03 - Assignment 2 - String formatting."""


# Task 1
def task_one_style_formatter(a_tuple):
    """Return the task-one-style formatted string."""
    # Eg. (2, 123.4567, 10000, 12345.67) -->
    # 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    return "file_{:03d} :   {:.2f}, {:.2e}, {:.3g}".format(*a_tuple)


# Task 2
def task_one_style_formatter2(a_tuple):
    """Alternative implementation to Task 1."""
    file_num = "{:03d}".format(a_tuple[0])
    a_float = "{:.2f}".format(a_tuple[1])
    sci_not1 = "{:.2e}".format(a_tuple[2])
    sci_not2 = "{:.3g}".format(a_tuple[3])
    return f"file_{file_num} :   {a_float}, {sci_not1}, {sci_not2}"


# Task 3
def task_three_style_formatter(a_tuple):
    """Return a str like, eg., 'the 3 numbers are: 1, 2, 3'."""
    length = len(a_tuple)
    form_string = "the {} numbers are: " + ", ".join(["{:d}"] * length)
    return form_string.format(length, *a_tuple)


# Task 4
def change_positions(a_tuple):
    """Change positions in a 5 element tuple."""
    # Eg., (4, 30, 2017, 2, 27) --> '02 27 2017 04 30'
    reorder_tuple = a_tuple[3:] + a_tuple[2:3] + a_tuple[0:2]

    return "{:02} {:02} {} {:02} {:02}".format(*reorder_tuple)


# Task 5 - f-strings
def f_formatter1(a_list):
    """Return a str formatted in the prescribed way."""
    # Eg., ['oranges', 1.3, 'lemons', 1.1] -->
    # The weight of an orange is 1.3 and the weight of a lemon is 1.1
    fruit1, weight1 = a_list[0], a_list[1]
    fruit2, weight2 = a_list[2], a_list[3]

    f_string = (f"The weight of an {fruit1[:-1]} is {weight1} "
                f"and the weight of a {fruit2[:-1]} is {weight2}"
                )

    return f_string


def f_formatter2(a_list):
    """Return a str formatted in the prescribed way."""
    # Eg., ['oranges', 1.3, 'lemons', 1.1] -->
    # The weight of an ORANGE is 1.56 and the weight of a LEMON is 1.32
    fruit1, weight1 = a_list[0], a_list[1]
    fruit2, weight2 = a_list[2], a_list[3]

    f_string = (f"The weight of an {fruit1[:-1].upper()} "
                f"is {weight1 * 1.2} "
                f"and the weight of a {fruit2[:-1].upper()} "
                f"is {weight2 * 1.2}"
                )

    return f_string


# Task 6
def display_col():
    """Display data in columns as required."""
    title_line = ("Name", "Age", "Cost")
    title_form = "{:<15}{:^10}{:^15}"

    data = (("Ford", "25", "$75125.99"),
            ("Hudson", "2", "$195"),
            ("Flint", "139.5", "$200099.5")
            )
    data_form = "{:<15}{:>10}{:>15}"

    print(title_form.format(*title_line))
    for item in data:
        print(data_form.format(*item))


def display_col2(a_tuple):
    """Print a_tuple of 10 consecutive numbers in columns 5 char wide."""
    print(''.join(["{:<5d}"] * 10).format(*a_tuple))


# TESTING SECTION
def test_task_one_style_formatter():
    """Test the named function."""
    string = "file_002 :   123.46, 1.00e+04, 1.23e+04"
    assert task_one_style_formatter((2, 123.4567, 10000, 12345.67)) == string


def test_task_one_style_formatter2():
    """Test the named function."""
    string = "file_002 :   123.46, 1.00e+04, 1.23e+04"
    assert task_one_style_formatter2((2, 123.4567, 10000, 12345.67)) == string


def test_task_three_style_formatter():
    """Test the named function."""
    res1 = "the 3 numbers are: 2, 3, 5"
    res2 = "the 5 numbers are: 2, 3, 5, 7, 9"
    assert task_three_style_formatter((2, 3, 5)) == res1
    assert task_three_style_formatter((2, 3, 5, 7, 9)) == res2


def test_change_positions():
    """Test the named function."""
    assert change_positions((4, 30, 2017, 2, 27)) == "02 27 2017 04 30"


def test_f_formatter1():
    """Test the named function."""
    output = "The weight of an orange is 1.3 and the weight of a lemon is 1.1"
    assert f_formatter1(["oranges", 1.3, "lemons", 1.1]) == output


def test_f_formatter2():
    """Test the named function."""
    res = "The weight of an ORANGE is 1.56 and the weight of a LEMON is 1.32"
    assert f_formatter2(["oranges", 1.3, "lemons", 1.1]) == res


def run_tests():
    """Run all tests."""
    test_task_one_style_formatter()
    test_task_one_style_formatter2()
    test_task_three_style_formatter()
    test_f_formatter1()
    test_f_formatter2()
    test_change_positions()
    test_f_formatter1()
    test_f_formatter2()


if __name__ == '__main__':
    run_tests()
    print(task_one_style_formatter((2, 123.4567, 10000, 12345.67)))
    print(task_one_style_formatter2((2, 123.4567, 10000, 12345.67)))
    print()
    print(task_three_style_formatter((2, 3, 5, 7, 9)))
    print(task_three_style_formatter((2, 3, 5, 7, 9, 10)))
    print()
    print(change_positions((4, 30, 2017, 2, 27)))
    print(change_positions((12, 3, 2018, 10, 1)))
    print()
    print(f_formatter1(["oranges", 1.3, "lemons", 1.1]))
    print(f_formatter2(["oranges", 1.3, "lemons", 1.1]))
    print()
    display_col()
    print()
    display_col2(tuple(range(10)))
