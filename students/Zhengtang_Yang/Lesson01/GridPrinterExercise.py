print('+ - - - - + - - - - +')
print('|         |         |')
print('|         |         |')
print('|         |         |')
print('|         |         |')
print('+ - - - - + - - - - +')
print('|         |         |')
print('|         |         |')
print('|         |         |')
print('|         |         |')
print('+ - - - - + - - - - +')

def print_grid(n):
	a1 = '+ '+'- '*((n-1)//2)+'+ '+'- '*((n-1)//2)+'+ '+'\n'
	a2 = '| '+'  '*((n-1)//2)+'| '+'  '*((n-1)//2)+'| '+'\n'
	a3 = a1+a2*((n-1)//2)+a1+a2*((n-1)//2)+a1
	print(a3)

print('print_grid(3)')
print_grid(3)

print('print_grid(11)')
print_grid(11)

print('print_grid(15)')
print_grid(15)

print('print_grid2(n,m)')
def print_grid2(n,m):
	a1 = '+' + (' -'*m + ' +')*n+'\n'
	a2 = '|' + ('  '*m + ' |')*n+'\n'
	a3 = a1+(a2*m+a1)*3
	print(a3)

print('print_grid2(3,4)')
print_grid2(3,4)
print('print_grid2(5,3)')
print_grid2(5,3) 
