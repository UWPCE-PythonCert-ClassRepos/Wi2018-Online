def fizzbuzz(a):
	if ((a%3==0) and (a%5==0)):	
		print('FizzBuzz')
	elif a%5==0:
		print('Buzz')
	elif a%3==0:
		print('Fizz')
	else:
		print(a)

for i in range(1,100):
	fizzbuzz(i)

