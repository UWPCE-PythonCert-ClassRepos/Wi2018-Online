# Task One
def str_format(stuff):
    ''' Task One:::   Intro to String Formatting '''
    print("Task One: Intro to String Formatting")
    print("file_{:03d} :{:10.2f}, {:.2e}, {:.2e}".format(stuff[0], stuff[1], stuff[2], stuff[3]))


# Task Two
def str_format_alt(stuff):
    ''' Task Two:::   Alternate Way for String Formatting '''
    print('\n' + "Task Two: Alternate Way for String Formatting")
    print("file_{:03d} :{:10.2f}, {:.2e}, {:.2e}".format(*stuff))


# Task Three
def formatter(in_tuple):
    ''' Task Three:::   Dynamically Building up Format Strings '''
    print('\n' + "Task Three:")
    form_string = 'the {:d} numbers are:  '
    for i in range(len(in_tuple)):
        form_string += '{} '
        return print(form_string.format(len(in_tuple), *in_tuple))


# Task Four
def str_format_fun(tup):
    '''Task Four:::   Fun with Formatting '''
    print('\n' + "Task Four: Fun with Formatting")
    print('{:02d} '.format(tup[3]),
          '{:d} '.format(tup[4]),
          '{:d} '.format(tup[2]),
          '{:02d} '.format(tup[0]),
          '{:d} '.format(tup[1]))


# Task Five
def f_string(fruity):
    '''Task Five:::   f-strings '''
    print('\n' + "Task Four: Fun with Formatting")
    print(f"The weight of an {fruity[0][:-1]} is {fruity[1]} "
          f"and the weight of a {fruity[2][:-1]} is {fruity[3]}")


def f_string_part2(fruity):
    '''Task Five:::   f-strings - Part 2 '''
    print('\n' + "Task Five: f-strings - Part 2")
    print(f"The weight of an {fruity[0][:-1].upper()} is {fruity[1] * 1.2} "
          f"and the weight of a {fruity[2][:-1].upper()} is {fruity[3] * 1.2}")


# Task Six
def str_table(data):
    ''' Task Six:::   Making a Table '''
    print('\n' + "Task Six::   Making a Table")
    print("{:12} {:8} {:}".format('Name', 'Age', 'Cost'))
    for i in data:
        print("{:12} {:<8} {:}".format(*i))


def str_columns(numbers):
    ''' Task Six:::   Making Columns '''
    print('\n' + "Task Six::   Making a Table")
    print(("{:5}"*len(numbers)).format(*numbers))


# Adding the Data
stuff = (2, 123.4567, 10000, 12345.67)
tup = (4, 30, 2017, 2, 27)
fruity = ['oranges', 1.3, 'lemons', 1.1]
data = [('Mandy', 22, '$130,014.57'), ('John', 29, '$99,400.00'), ('Nathan', 33, '$53,000.00'), ('Bret', 65, '$13.75')]
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


# Running the Functions
str_format(stuff)
str_format_alt(stuff)
formatter((2, 3, 5))
formatter((2, 3, 5, 7, 9))
str_format_fun(tup)
f_string(fruity)
f_string_part2(fruity)
str_table(data)
str_columns(numbers)

