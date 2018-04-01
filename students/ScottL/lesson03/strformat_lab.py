#!/usr/bin/env python3
# Scott Luse, String Lab, Feb 05, 2018


# Task One, format a tuple
def format_task_one(a_tuple):
    # ( 2, 123.4567, 10000, 12345.67)
    # format result as 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    # Hint: You can pass in a tuple of values to a function with a *
    return "file_{:03d} :   {:.2f}, {:.2e}, {:.3g}".format(*a_tuple)

def test_format_task_one():
    string = "file_002 :   123.46, 1.00e+04, 1.23e+04"
    assert format_task_one((2, 123.4567, 10000, 12345.67)) == string


# Task Two, alternative method to Task one, note f-string
def format_task_two(a_tuple):
    file_number = "{:03d}".format(a_tuple[0])
    num_float = "{:.2f}".format(a_tuple[1])
    sci_note_1 = "{:.2e}".format(a_tuple[2])
    sci_note_2 = "{:.3g}".format(a_tuple[3])
    return f"file_{file_number} :   {num_float}, {sci_note_1}, {sci_note_2}"

def test_format_task_two():
    string = "file_002 :   123.46, 1.00e+04, 1.23e+04"
    assert format_task_two((2, 123.4567, 10000, 12345.67)) == string

# Task Three
def format_task_three(a_tuple):
    # Rewrite 'the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)'
    # to take an arbitrary number of values.
    length = len(a_tuple)
    form_string = "the {} numbers are: " + ", ".join(["{:d}"] * length)
    return form_string.format(length, *a_tuple)

# Task Four
def format_task_four(a_tuple):
    # Given a 5 element tuple ( 4, 30, 2017, 2, 27)
    # use string formatting to print '02 27 2017 04 30'
    # Hint: use index numbers to specify positions.
    new_tuple = a_tuple[3:] + a_tuple[2:3] + a_tuple[0:2]
    return "{:02} {:02} {} {:02} {:02}".format(*new_tuple)

# Task Five
def format_task_five(a_tuple):
    # Given the following four element list: ['oranges', 1.3, 'lemons', 1.1]
    # Write an f-string that will display: The weight of an orange is 1.3 and the weight of a lemon is 1.1
    fruit1 = a_tuple[0]
    fruit1_mass = a_tuple[1]
    fruit2 = a_tuple[2]
    fruit2_mass = a_tuple[3]
    return f"The weight of an {fruit1} is {fruit1_mass} and the weight of a {fruit2} is {fruit2_mass}"

# Task Six
def format_task_six():
    # Write some Python code to print a table of several rows, each with a name, an age and a cost.
    # Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.
    a_tuples = (('First', '30', '$99.01'), ('Third', '27', '$288.09'), ('Fourth', '88', '$1288.09'))
    for group in a_tuples:
        print('{:20}{:10}{:>10}'.format(*group))

if __name__ == '__main__':
    test_format_task_one()
    print(format_task_one((2, 123.4567, 10000, 12345.67)))
    test_format_task_two()
    print(format_task_two((2, 123.4567, 10000, 12345.67)))

    print(format_task_three((1, 2, 3, 4, 5, 6)))
    print(format_task_four((4, 30, 2017, 2, 27)))
    print(format_task_five(('orange', 1.3, 'lemon', 2.1)))

    format_task_six()


