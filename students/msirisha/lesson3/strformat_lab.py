def task_one(input_tuple):
    print("file_{:0>3d}, {:.2f}, {:.2e}, {:.2e}".format(input_tuple[0], input_tuple[1], input_tuple[2], input_tuple[3]))

def task_two(input_tuple):
    print("file_{:0>3d}, {:.2f}, {:.2e}, {:.2e}".format(*input_tuple))

def formatter(input_tuple):
    format_string = "The {} numbers are: ".format(len(input_tuple))
    format_string += ", ".join(["{:d}"] * len(input_tuple))
    print(format_string.format(*input_tuple))

def task_three(input_tuple):
    formatter(input_tuple)

def task_four(t):
    print("{:02d} {:02d} {:d} {:02d} {:02d}".format(t[3], t[4], t[2], t[0], t[1]))
    print("{3:02d} {4:02d} {2:d} {0:02d} {1:02d}".format(*t))

def task_five(list):
    print(f"The weight of an {list[0][:-1]} is {list[1]} and the weight of a {list[2][:-1]} is {list[3]}")
    print(f"The weight of an {list[0][:-1].upper()} is {list[1] * 1.2} and the weight of a {list[2][:-1].upper()} is {list[3] * 1.2}")

def task_six(input_tuple):
    print('{:10}{:3}{:>10}'.format('Name', 'Age', 'Cost'))
    for person in input_tuple:
        print('{:10}{:3}{:>10}'.format(*person))


if __name__ == "__main__":
    input_tuple = (2, 123.4567, 10000, 12345.67)
    print("== task1 output ==")
    task_one(input_tuple)
    print("== task2 output ==")
    task_two(input_tuple)
    print("== task3 output ==")
    task_three((1,2,3))
    print("== task3 output ==")
    task_three((1,2,3,4,5))
    print("== task4 output ==")
    task_four(( 4, 30, 2017, 2, 27))
    list = ['oranges', 1.3, 'lemons', 1.1]
    print("== task5 output ==")
    task_five(list)
    input_tuple = [('sirisha', 20, '$20543.67'), ('sai', 20, '$4345.567'), ('ani', 5, '34.67'), ('test_name', 10, '3456.234')]
    print("== task6 output ==")
    task_six(input_tuple)
