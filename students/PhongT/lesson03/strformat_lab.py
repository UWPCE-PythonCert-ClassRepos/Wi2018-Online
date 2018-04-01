"""
Lesson 03
String Formatting Lab Exercise
"""


# Task One
def format_tuple(in_tuple):
    """
    Format string that will take the following four element tuple:
    ( 2, 123.4567, 10000, 12345.67)
    and produce:
    'file_002 :   123.46, 1.00e+04, 1.23e+04'

    :param in_tuple: input tuple
    :return:
    """
    return 'file_{:0>3d} :   {:.2f}, {:.2e}, {:.2e}'.format(in_tuple[0], in_tuple[1], in_tuple[2], in_tuple[3])


# Dynamically Building up Format Strings
def formatter(in_tuple):
    """
    Dynamically build up the format string to accommodate the length of the tuple.
    Example:
        formatter((2,3,5))
        'the 3 numbers are: 2, 3, 5'

        formatter((2,3,5,7,9))
        'the 5 numbers are: 2, 3, 5, 7, 9'
    :param in_tuple:
    :return:
    """
    length = len(in_tuple)
    form_string = ("the {} numbers are: " + ", ".join(["{}"]*length)).format(length, *in_tuple)
    return form_string.format(in_tuple)


def f_string_format(in_list):
    """
    use f-strings
    Example: input list = ['oranges', 1.3, 'lemons', 1.1]
    Will return The weight of an orange is 1.3 and the weight of a lemon is 1.1
    Also change the f-string so that it displays the names of the fruit in upper case, and the weight 20% higher
    """
    f_string = f'The weight of an: {in_list[0][:-1].upper()} is {in_list[1]*1.2} and ' \
               f'the weight of a {in_list[2][:-1].upper()} is {in_list[3]*1.2}'
    return f_string


if __name__ == "__main__":
    a_tuple = (2, 123.4567, 10000, 12345.67)
    print(format_tuple(a_tuple))
    assert format_tuple(a_tuple) == 'file_002 :   123.46, 1.00e+04, 1.23e+04'

    print(formatter((2, 3, 5)))
    assert formatter((2, 3, 5)) == 'the 3 numbers are: 2, 3, 5'

    print(formatter((2, 3, 5, 7, 9)))
    assert formatter((2, 3, 5, 7, 9)) == 'the 5 numbers are: 2, 3, 5, 7, 9'

    a_list = ['oranges', 1.3, 'lemons', 1.1]
    print(f_string_format(a_list))
    assert f_string_format(a_list) == 'The weight of an: ORANGE is 1.56 and the weight of a LEMON is 1.32'


