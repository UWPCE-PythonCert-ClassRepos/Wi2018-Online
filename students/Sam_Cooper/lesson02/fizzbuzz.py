"""Write a program that prints the numbers 1 to 100 inclusive. 
Multiples of three, print "Fizz" instead of the number. 
Multiples of five, print "Buzz" instead of the number.
Multiples of both three and five, print "FizzBuzz"""

def fizz_buzz():
	for num in range(1, 101):
		if num % 3 == 0 and num % 5 == 0:
			print("FizzBuzz")
		elif num % 3 == 0:
			print("Fizz")
		elif num % 5 == 0:
			print("Buzz")
		else:
			print(num)

def main():
	fizz_buzz()
	
if __name__ == '__main__':
	main()


