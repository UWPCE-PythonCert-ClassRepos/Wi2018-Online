# function that draws a static 2x2 grid
# function name is gird()

# individual graphic elements
plus = "+ "
minus = "- "
vertical = "| "
space = "  "

# full grid
def grid(row, col, size):
	# box structure
	top = plus + minus * size
	side = vertical + minus * size
	
	for index in range(row):				#print bunch of rows
		print(top * col + plus)				#print top grid that has # of columns + ending |			
		for index in range(size):			#print a bunch of sides based on grid size
			print(side * col + vertical)	#print side grid that has # of columns
	print(top * col + plus)					#print bottom close-out

##############################################################
# Run as a program

# preface
print()
print("Create a grid of any # of rows, columns, and size.")
print()
row = int(input("--> Enter # of rows = "))
col = int(input("--> Enter # of columns = "))
size = int(input("--> Enter grid size = "))
print("Note the grid creator can also be recalled by the function by grid(row, col, size)")
print()

grid(row,col,size)
