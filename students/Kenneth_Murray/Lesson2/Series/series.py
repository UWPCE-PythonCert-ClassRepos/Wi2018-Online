def fibonacci(n):
	"""prints the Nth fibbonachi number in the series"""
	a, b = 0, 1 #first two numbers in the series
	c = 0	#the value to be printed
	i = 3	#the iteration in the loop begins with 3 because 1 and 2 are outside the loop
	while i <= n and n > 2: #itereate if the n value is higher than 2
		c = a + b
		a, b = b, a + b
		if i == n:
			return c
		i = i + 1	#add 1 and return to beginning of while loop
	if n == 1:
		c = a
		return c
	if n == 2:
		c = b
		return c
			
def lucas(n):
	"""prints the Nth lucas number in the series"""
	a, b = 2, 1	#first two numbers in the series
	c = 0	#the value to be printed
	i = 3	#the iteration in the loop begins with 3 because 1 and 2 are outside the loop
	while i <= n and n > 2:	#itereate if the n value is higher than 2
		c = a + b
		a, b = b, a + b
		if i == n:
			return c
		i = i + 1	#add 1 and return to beginning of while loop
	if n == 1:
		c = a
		return c
	if n == 2:
		c = b
		return c

def sum_series(n,a=0,b=1):
	"""Prints the nth number in a series defined by a and b"""
	c = 0	#the value to be printed
	i = 3	#the iteration in the loop begins with 3 because 1 and 2 are outside the loop
	while i <= n and n > 2:	#itereate if the n value is higher than 2
		c = a + b
		a, b = b, a + b
		if i == n:
			return c
		i = i + 1	#add 1 and return to beginning of while loop
	if n == 1:
		c = a
		return c
	if n == 2:
		c = b
		return c
		
"""test the series code"""
if __name__ == "__main__":
	print("Running tests on the series functions")
	assert fibonacci(1) == 0
	assert fibonacci(2) == 1
	assert fibonacci(5) == 3
	print("fibonacci tests are complete")
	assert lucas(1) == 2
	assert lucas(2) == 1
	assert lucas(5) == 7
	print("lucas tests are complete")
	assert sum_series(1) == 0
	assert sum_series(2) == 1
	assert sum_series(5) == 3
	assert sum_series(1,2,1) == 2
	assert sum_series(5,2,1) == 7
	print("the sum_series tests are comlete")
	print("this concludes all testing")
	
		

		

		
		