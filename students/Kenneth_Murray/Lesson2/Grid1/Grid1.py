def grid1(x):
#This will create a grid with 4 equal quadrants
#The input must be an odd number 
#the input is equall to the vertical or horizontal lines that make up the grid
#The minimum value is 5
#The input must be an integer

#assign variables to the print characters
	#horizontal 
	h="-"
	#vertical
	v="|"
	#separator
	s="+"
	#space
	sp=" "
	#quadrant spaces
	qs=int((x-3)/2)
	#check to see if x is an odd integer greagter than or equall to 5
	if x>=5 and type(x)==int and not x%2==0:
		#i is the line counter
        i=0
		while i<x:
			if i==0 or i==(x-1)/2 or i==x-1:
				print(s+h*qs+s+h*qs+s)
				i=i+1
			else:
				print(v+sp*qs+v+sp*qs+v)
				i=i+1
	else:
		return "please enter an odd integer greater than 5"		
	