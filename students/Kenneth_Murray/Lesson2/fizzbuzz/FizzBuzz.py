#KenMurray FizzBuzz assignment
#n is the total numbers to print like 100
def fizzBuzz(n):
#set counter to 0
i=0
	#itterate through n numbers
	while i<n:
		i=i+1
		#test to see if only divisible by 5
		if i % 5==0 and not i % 3==0:
			print("Buzz")
		#test to see if divisible by 3 only
		elif i % 3==0 and not i % 5==0:
			print("Fizz")
		#test to see if divisible by 5 and 3
		elif i % 5==0 and i % 3==0:
			print("FizzBuzz")
		else:
			print(i)