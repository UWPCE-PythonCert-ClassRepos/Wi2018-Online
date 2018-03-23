#!/usr/bin/env python

# establish the starting tuple
starting_tuple = (2, 123.4567, 10000, 12345.67)

# Task 1
def task1(st):
	print("file_{:03d}: {:05.2f}, {:.2E}, {:.2E}".format(*st))

task1(starting_tuple)

# Task 2: Alternative format
def task2(st):
	print("file_{file_number}: {val1}, {val2}, {val3}".format(file_number = "{:03d}".format(st[0]), val1 = "{:05.2f}".format(st[1]), val2 = "{:.2E}".format(st[2]), val3 = "{:.2E}".format(st[3])))

task2(starting_tuple)

# Task 3
def task3(st):
	# create the initial string, which contains the length of the sequence 
	initial_string = "the {:d} numbers are: ".format(len(st))
	string_to_format = []
	# build the list of elements that need to be formatted 
	for __ in range(len(st)):
		string_to_format.append("{:d}")
	# join the strings in a comma separated fashion
	formatted_string = ', '.join(string_to_format).format(*st)
	# print results
	print(initial_string + formatted_string)

task3((1, 2, 3))
task3((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# Task 4
def task4():
	task4_tuple = (4, 30, 2017, 2, 27)
	print("{:02d} {:d} {:d} {:02d} {:d}".format(task4_tuple[3], task4_tuple[4], task4_tuple[2], task4_tuple[0], task4_tuple[1]))

task4()

# Task 5
def task5():
	input_list = ['oranges', 1.3, 'lemons', 1.1]
	print(f'The weight of an {input_list[0][:-1]} is {input_list[1]} and the weight of an {input_list[2][:-1]} is {input_list[3]}')
	print(f'The weight of an {input_list[0][:-1].upper()} is {input_list[1]*1.2} and the weight of an {input_list[2][:-1].upper()} is {input_list[3]*1.2}')

task5()

# Task 6
def task6(ten_digit_tuple):
	print('{:20s}{:<10d}${:<8.2f}'.format('Walter White', 55, 15000000))
	print('{:20s}{:<10d}${:<8.2f}'.format('John Snow', 28, 500))
	print('{:20s}{:<10d}${:<8.2f}'.format('Ray Donovan', 43, 25000))
	formats = "{:<5d}"*10
	print(formats.format(*ten_digit_tuple))
task6((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
