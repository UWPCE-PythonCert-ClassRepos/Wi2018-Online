"""
Lesson02 - Assignment3 - Sum Series
NON RECURSIVE approach to compute Fibonacci and Lucas values
contains 3 methods: fibonacci, lucas and sum_series and global initialization
code which tests the methods in the "main" method
This code can compute the Fibonacci or Lucas value for any number from 0 to 10000 
Need to figure out a way - to dynamically allocate the size of the global lists 
"""

"""
Using global lists (capacity 10000) and initializing the values to -1
These lists will store the values of the Fibonacci and Lucas numbers resp.
If the value is -1, it implies that the value has not been computed for that index
ex: fib[5] contains the fibonacci number for number 5
ex: luc[5] contains the Lucas number for number 5
"""
fib = []
n = 100000
for i in range(0, n+1):
    fib.append(-1) # you push your element here, as of now I have push i

luc =[]
for i in range(0,n+1):
	luc.append(-1)


"""
fibonacci method - which returns the fibonacci number for the input number
starting values - populate the starting values in the list fib[0] and fib[1]
if the array value is not equal to fib[n] to -1, then return the value
Else, compute the value using the sum of the previous 2 values in the fib list (which are not -1)
"""
def fibonacci(n):
	fib[0] = 0
	fib[1] = 1
	if fib[n] != -1:
		return fib[n]
	#Compute fib[n]
	for i in range (2,n+1):
		if fib[i] == -1:
			fib[i] = fib[i-1] + fib[i-2]
	return (fib[i])

"""
lucas method - which returns the lucas number for the input number
starting values - populate the starting values in the list luc[0] and luc[1]
if the array value is not equal to luc[n] to -1, then return the value
Else, compute the value using the sum of the previous 2 values in the luc list (which are not -1)
"""
def lucas(n):
	luc[0] = 2
	luc[1] = 1
	if luc[n] != -1:
		return luc[n]
	#Compute luc[n]
	for i in range (2,n+1):
		if luc[i] == -1:
			luc[i] = luc[i-1] + luc[i-2]
	return (luc[i])
	
"""
sum_series methods- with 3 input params 
	n - value for which we need to compute fibonacci value or lucas value
	x - with a default value 0
	y - with a default value 1
if x and y have the default values, then return the Fibonacci number for the input value
if x and y have the values 2 and 1 respectively, then return the Lucas number for the input value
if x and y have any other value, then return -1
"""
def sum_series(n,x=0,y=1):
	if x == 0 and y == 1:
		return (fibonacci(n))
	elif x == 2 and y == 1:
		return (lucas(n))
	else: return -1

"""
testing code in main block
testing for fibonacci series without default values for x and y - with inputs - 0,1,4,10,20
testing for fibonacci series by providing default values for x and y - with inputs - 0,1,4,10,20
testing for lucas series by providing values of 2 and 1 x and y - with inputs - 0,1,4,10,20
testing to ensure that sum_series returns -1, in case x and y are any value other than 2 and 1 or 0 and 1 
"""
if __name__ == "__main__":
	print ("Running tests")

	assert(sum_series(0) == 0) #fibonacci series value for 0
	assert(sum_series(0,0,1) == 0) #fibonacci series value for 0
	assert(sum_series(0,2,1) == 2) #lucas series value for 0
	assert(sum_series(0,1,0) == -1) #not fibonacci or lucas series

	assert(sum_series(1) == 1) #fibonacci series value for 1
	assert(sum_series(1,0,1) == 1) #fibonacci series value for 1
	assert(sum_series(1,2,1) == 1) #lucas series value for 1
	assert(sum_series(1,1,2) == -1) #not fibonacci or lucas series

	assert(sum_series(4) == 3) #fibonacci series value for 4
	assert(sum_series(4,0,1) == 3) #fibonacci series value for 4
	assert(sum_series(4,2,1) == 7) #lucas series value for 4
	assert(sum_series(4,1,1) == -1) #not fibonacci or lucas series

	assert (sum_series(10) == 55) #fibonacci series value for 10
	assert (sum_series(10,0,1) == 55) #fibonacci series value for 10
	assert(sum_series(10,2,1) == 123) #lucas series value for 10
	assert(sum_series(10,2,2) == -1) #not fibonacci or lucas series

	assert (sum_series(20) == 6765) #fibonacci series value for 20
	assert (sum_series(20,0,1) == 6765) #fibonacci series value for 20
	assert(sum_series(20,2,1) == 15127) #lucas series value for 20
	assert(sum_series(20,1,3) == -1) #not fibonacci or lucas series

	assert (sum_series(100) == 354224848179261915075) #fibonacci series value for 20
	assert (sum_series(100,0,1) == 354224848179261915075) #fibonacci series value for 20
	assert(sum_series(100,2,1) == 792070839848372253127) #lucas series value for 20
	assert(sum_series(100,1,3) == -1) #not fibonacci or lucas series

	print ("Tests passed")
