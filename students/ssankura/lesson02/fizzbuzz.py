#Lesson2 - FizzBuzz Assignment

#Print all numbers from 1 to 100
#Print FizzBuzz instead of the number if it is divisible by 15
#Print Fizz instead of the number if it is divisible by 3
#Print Buzz instead of the number if it is divisible by 5
def fizzbuzz():
	startnum = 1
	endnum = 100
	for i in range(startnum,endnum+1):
		if i % 15 == 0:
			print ("FizzBuzz")
		elif i % 3 == 0:
			print ("Fizz")
		elif i % 5 == 0:
			print ("Buzz")
		else:
			print (i)

#code to run FizzBuzz
if __name__ == "__main__":
	fizzbuzz()
