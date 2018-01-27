# print 1 to 100, multiples of 3 prints Fizz, multiples of 5 print Buzz, both multiples print FizzBuzz
	
count3 = 0									# count every 3 steps 
count5 = 0									# count every 5 steps

for index in range(1,100+1):
	text = index							# text variable by default is the index

	count3 += 1								# count starts at 0, then increments until it hits a divide by 3
	count5 += 1								# ^ same but for divide by 5

	div3 = count3 is 3						# division check for 3 - boolean
	div5 = count5 is 5						# division check for 5 - boolean
	
	if div3 is True:
		text = "Fizz"
		count3 = 0
	if div5 is True:
		text = "Buzz"
		count5 = 0
	if div3 is True and div5 is True:
		text = "FizzBuzz"
		count3 = 0
		count5 = 0
	print(text)

