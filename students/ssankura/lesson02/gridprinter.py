#Lesson 02 - assignment to print grid

#print_grid 
#Input params - two integers - m,n
#m represents the number of rows in the grid
#n represents the number of columns in the grid and the number of dashes in each grid
#Output - prints a grid with the specified format

def print_grid(m,n):
	plus = "+ "
	dash = "- "
	verticalBar = "| "
	space = "  "
	plusDashLine = ""
	verticalBarSpaceLine = ""
	#prepare the plus and dash line with the correct number of plus-es and dash-es
	#prepare the vertical bar and space line with the correct number of vertical bars and spaces to align with the plus dash line
	for i in range(0,n):
		plusDashLine = plusDashLine + plus +  dash*(n)
		verticalBarSpaceLine = verticalBarSpaceLine + verticalBar + space*(n)
	plusDashLine = plusDashLine + plus #ending plus
	verticalBarSpaceLine = verticalBarSpaceLine + verticalBar #ending vertical bar
	
	#print the grid - print the grid lines - m*n number of times
	#Repeat the following for "m" times
		#print entire row - first the plus dash line and then multiple vertical bar space lines
	#finally print the last plus dash line
	for i in range(0,m):
		print (plusDashLine)
		for j in range(0,n):
			print (verticalBarSpaceLine)
	print (plusDashLine) #print the last Dash Line

if __name__ == "__main__":
	#testing the print grid functionality
	print_grid(3,4)
	print_grid(5,3)
	print_grid(5,4)

