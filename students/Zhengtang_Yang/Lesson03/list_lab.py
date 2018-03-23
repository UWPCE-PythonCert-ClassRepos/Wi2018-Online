def series_one()
	fruit = ['Apples','Pears','Oranges','Peaches']
	print(fruit)
	response = input("Add another fruit\n")
	fruit.append(response)
	print(fruit)
	return fruit

def series_two(fruit):
	print(fruit)
	fruit0 = fruit[:-1]
	while True:
		print(fruit0)
		response = input("delete a fruit\n")
		if response in fruit0:
			fruit0.remove(response)
			print(fruit0)
			break

def series_three(fruit):
	fruit0, i = fruit[:], 0
	while i < len(fruit):
		response = input("Do you like %s\n" % fruit[i]) 
		if response == "no":
			fruit0.remove(fruit[i])
		elif response == "yes":
			i += 1
		else:
			print("Please answer yes or no")
		print(fruit0)


def series_four(fruit):
	fruit0 = fruit[:]
	fruit0.reverse()
	print(fruit0)
	fruit.pop()
	print(fruit)

