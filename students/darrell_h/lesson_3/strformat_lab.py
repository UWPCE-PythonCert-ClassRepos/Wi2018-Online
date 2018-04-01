#!/usr/local/bin/python3


my_tuple = (2, 123.4567, 10000, 12345.67)  # immutable


def task_1():
    print('Task 1::: file_{:02d}:'.format(my_tuple[0]),
          '{:.2f},'.format(my_tuple[1]),  # ugly...
          '{:.2e},'.format(my_tuple[2]),
          '{:.2e}'.format(my_tuple[3]))


def task_2():
    print('Task 2::: file_{:02d}: {:.2f}, {:.2e}, {:.2e}'.format(*my_tuple))


def task_3(t):
    str = 'Task 3::: the {:d} numbers are: '
    for i in range(len(t)):
        str += '{} '
    #  format takes 2 inputs.  the lenght of the tuple and the tuple items
    print(str.format(len(t), *t))


def task_4(t):
    print('Task 4::: {:02d}'.format(t[3]),
          '{}'.format(t[4]),
          '{}'.format(t[2]),
          '{:02d}'.format(t[0]),
          '{}'.format(t[1]))


def task_5(l):
    print(f"The weight of an {l[0][:-1]} is {l[1]} and the weight of a {l[2][:-1]} is {l[3]}")


def task_6():
    pass


task_1()
task_2()
task_3((1, 2, 3, 4, 5, 6))
task_4((4, 30, 2017, 2, 27))
task_5(['oranges', 1.3, 'lemons', 1.1])
