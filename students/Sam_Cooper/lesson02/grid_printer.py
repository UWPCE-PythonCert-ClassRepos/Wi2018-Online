plus = '+'
minus = '-'
pipe = '|'

def print_grid(width):
	box_size = width // 2
	horizontal_row = (plus + (minus * box_size) + plus + (minus * box_size) + plus)
	vertical_row = (pipe + (" " * box_size) + pipe + (" " * box_size) + pipe) 

	print(horizontal_row)

	for row in range(2):
		for row in range(box_size):
			print(vertical_row)
		print(horizontal_row)

def print_grid2(box_count, box_size):
	horizontal_row = plus + ((minus * box_size + plus) * box_count)
	vertical_row = pipe + ((" " * box_size + pipe) * box_count)

	#create the grid
	print(horizontal_row)
	for row in range(box_count): #outer loop
		for row in range(box_size): #inner loop
			print(vertical_row)
		print(horizontal_row)


def main():
	print("Part 1: Printing a 4x4 grid" + '\n')
	part1_test_data = 8
	print_grid(part1_test_data)

	print('\n' + "Part 2: Printing a custom grid")
	custom_grid = int(input('Enter a grid size you would like to create: '))
	print_grid(custom_grid)

	print('\n' + "Part 3: Print a custom number of boxes and the size of each box")
	box_count = int(input('Enter the number of boxes you would like to see in a row: '))
	box_size = int(input('Input the desired size of the box: '))
	print_grid2(box_count, box_size)

if __name__ == '__main__':
	main()



