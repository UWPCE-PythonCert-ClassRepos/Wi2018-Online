#----------------------------------------#
# Title: Working with Fibonnacci and Lucas series
# Written by Sam Cooper
#----------------------------------------#


def fibonnacci(n):
	"""-Calculate the Fibonnacci series for a number of interest
	-A Fibonnacci series is created by the following formula: fib(n) = fib(n-2) + fib(n-1)
	-A Fibonnacci series will always start with the numbers 0 and 1
	:param n: n i sthe desired nth value in the series
	:return: Returns the nth value in the Fibonnaci series"""
	if n == 0:
		return n
	elif n == 1:
		return n
	else:
		return (n - 2) + (n - 1)

def lucas(n):
	"""-Calculate the Lucas series for a number of interest
	-A Lucas series is created by the following formula: lucas(n) = lucas(n-2) + lucas(n-1)
	-The key difference between Fibonnaci and Lucas series' is that Lucas starts with 2 and 1
	:param n: n i sthe desired nth value in the series
	:return: Returns the nth value in the Fibonnaci series"""

	if n == 0:
		return 2
	elif n == 1: 
		return 1
	else:
		return (n - 2) + (n - 1)


def sum_series(n, param1 = 0, param2 = 1):
	if n == 0:
		return param1
	elif n == 1: 
		return param2
	else: 
		return (n-2, param1, param2) + (n-1, param1, param2)


def main():
	print("\tCalculate the Fibonnacci Series")
	print("---------------------------------------------------\n")
	fibonnacci_list = []
	fib_range = int(input('Enter a number and you will see the respective Fibonnacci series: '))
	while fib_range < 0:
		print("You've entered invalid input, please provide a positive integer")
		fib_range = int(input('Enter a number and you will see the respective Fibonnacci series: '))
	for num in range(fib_range):
		fibonnacci_list.append(str(fibonnacci(num)))
	print(', '.join(fibonnacci_list))
	print("\n" * 3)


	print("\tCalculate the Lucas Series")
	print("----------------------------------------------\n")
	lucas_list = []
	lucas_range = int(input('Enter a number and you will see the respective Lucas series: '))
	while lucas_range < 0:
		print("You've entered invalid input, please provide a positive integer")
		lucas_range = int(input('Enter a number and you will see the respective Lucas series: '))
	for num in range(lucas_range):
		lucas_list.append(str(lucas(num)))
	print(', '.join(lucas_list))
	print("\n" * 3)

	print("\tSum series assertion testing")
	print("----------------------------------------------\n")
	print("Assertion Testing Part One: Testing for Fibonnaci")
	fibonnaci_test = []
	fib_range_test = int(input(" Enter a number and you will see the respective Fibonnacci series: "))
	while fib_range_test < 0:
		print("You've entered invalid input, please provide a positive integer")
		fib_range_test = int(input(" Enter a number and you will see the respective Fibonnacci series: "))
	for num in range(fib_range_test):
		fibonnaci_test.append(str(sum_series(num, param1 = 0, param2 = 1)))
	print(', '.join(fibonnaci_test))
	print("\n" * 3)

	print("Assertion Testing Part Two: Testing for Lucas")
	lucas_test = []
	lucas_range_test = int(input(" Enter a number and you will see the respective Fibonnacci series: "))
	while lucas_range_test < 0:
		print("You've entered invalid input, please provide a positive integer")
		lucas_range_test = int(input(" Enter a number and you will see the respective Fibonnacci series: "))
	for num in range(lucas_range_test):
		lucas_test.append(str(sum_series(num, param1 = 2, param2 = 1)))
	print(', '.join(lucas_test))

if __name__ == '__main__':
	main()