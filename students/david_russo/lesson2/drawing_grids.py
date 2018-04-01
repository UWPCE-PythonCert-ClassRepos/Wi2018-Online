#!/usr/bin/env python

# This script draws grids in an increasingly general and abstract manner 

# Part 1
def print_fixed_grid():
	plus = '+ '
	minus = '- ' 
	# define distinct strings
	full_line = '+ ' * 1 + '- ' * 4 + '+ ' + '- ' * 4 + '+'
	sparse_line = '| ' + '  ' * 4 + '| ' + '  ' * 4 + '|'

	# print(full_line)
	print(full_line)
	for i in range(1, 5):
		print(sparse_line)
	print(full_line)
	for i in range(1, 5):
		print(sparse_line)
	print(full_line)

print_fixed_grid()

# Part 2
# Make it a function
def print_grid(n):
	dash_segment_length = int((n - 1)/2)
	full_line = '+ ' * 1 + '- ' * dash_segment_length + '+ ' * 1 + '- ' * dash_segment_length + '+'
	sparse_line = '| ' + '  ' * dash_segment_length + '| ' + '  ' * dash_segment_length  + '|' 

	print(full_line)
	for i in range(dash_segment_length):
		print(sparse_line)
	print(full_line)
	for i in range(dash_segment_length):
		print(sparse_line)
	print(full_line)

print_grid(3)
print_grid(15)

# Part 3
# Make it a function with two parameters
#def print_grid2(n, size):
def print_grid2(n, size):

	# initialize the line segments
	dash_segment = ' ' + '- ' * size + '+'
	pipe_segment = ' ' + '  ' * size + '|'

	# initialize and grow the full line segments
	full_line = '+'
	for i in range(1, n+1):
		full_line += dash_segment

	# initialize and grow the sparse segments 
	sparse_line = '|'
	for i in range(1, n+1):
		sparse_line += pipe_segment

	# grow the square grid
	print(full_line)
	for i in range(1, n*(size + 1)):
		if i % (size+1) == 0:
			print(full_line)
		else:
			print(sparse_line)
	print(full_line)

print_grid2(5, 3)
print_grid2(3, 4)









