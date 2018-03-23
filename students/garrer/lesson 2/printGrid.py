def print_grid(x,y):
	for i in range(0,x):
		print(x*('+'+'-'*y)+'+')
		for i in range(0,y):
			print(x*('|'+' '*y)+'|')
	print(x*('+'+'-'*y)+'+')

print_grid(3,2)