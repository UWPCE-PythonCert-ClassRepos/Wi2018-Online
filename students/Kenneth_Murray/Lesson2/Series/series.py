def fibonacci(n):
	"""prints the Nth fibbonachi number in the series"""
	a, b = 0, 1 #first two numbers in the series
	c = 0	#the value to be printed
	i = 3	#the iteration in the loop begins with 3 because 1 and 2 are outside the loop
	while i <= n and n > 2: #itereate if the n value is higher than 2
		c = a + b
		a, b = b, a + b
		if i == n:
			print(c)
		i = i + 1	#add 1 and return to beginning of while loop
	if n == 1:
		c = a
		print(c)
	if n == 2:
		c = b
		print(c)
			
def lucas(n):
	"""prints the Nth lucas number in the series"""
	a, b = 2, 1	#first two numbers in the series
	c = 0	#the value to be printed
	i = 3	#the iteration in the loop begins with 3 because 1 and 2 are outside the loop
	while i <= n and n > 2:	#itereate if the n value is higher than 2
		c = a + b
		a, b = b, a + b
		if i == n:
			print(c)
		i = i + 1	#add 1 and return to beginning of while loop
	if n == 1:
		c = a
		print(c)
	if n == 2:
		c = b
		print(c)

def sum_series(n,a=0,b=1):
	"""Prints the nth number in a series defined by a and b"""
	c = 0	#the value to be printed
	i = 3	#the iteration in the loop begins with 3 because 1 and 2 are outside the loop
	while i <= n and n > 2:	#itereate if the n value is higher than 2
		c = a + b
		a, b = b, a + b
		if i == n:
			print(c)
		i = i + 1	#add 1 and return to beginning of while loop
	if n == 1:
		c = a
		print(c)
	if n == 2:
		c = b
		print(c)
		

		

		
		