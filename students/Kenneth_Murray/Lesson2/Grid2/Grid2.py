def grid2(x,y):
#This will create a grid with x number of rows and columns
#and y number of spaces in each cell
#The minimum value is 1
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
	qs=y
	#total spaces
	ts=x*y+x+1
	
	#check to see if x is an odd integer greagter than or equall to 5
	if x or y >=1 and type(x) and type(y)==int:
		#i is the line counter
        i=0
		c=0
		while i<ts:
			if i==0 or i==c or i==ts-1:
				print((s+h*qs)*x+s)
				i=i+1
				c=c+y+1
			else:
				print((v+sp*qs)*x+v)
				i=i+1
	else:
		return "please enter an odd integer greater than 1"		
	