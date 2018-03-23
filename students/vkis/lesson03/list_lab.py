select = input("\nEnter which Series (1,2,3,4) to run: ")
while select != "1" and select != "2" and select != "3" and select != "4":		# is there away to run a variable check against a list of conditions without repeating like this?
	select = input("Incorrect selection enter Series: 1,2,3, or 4 to run: ")

# Series 1
if select == "1":
	print()
	mylist = ["Apples","Pears","Oranges","Peaches"]
	print("[OUT]: mylist = ", mylist)
	print()
	newfruit= input("[OUT]: Input another fruit, \n[IN]: newfruit <<< ")
	mylist.append(newfruit)
	print()
	print("[OUT]: mylist = ", mylist)
	print()
	fruit_id = input("[OUT]: Enter which fruit to display in the series \n[IN]: fruit_id <<< ")
	print("[OUT]: Fruit ID = ", fruit_id, " -->", mylist[int(fruit_id)-1])
	print()
	mylist = ["Watermellon"] + mylist
	print("[OUT]: mylist = ", mylist)
	mylist.insert(0,"Kiwi")
	print("[OUT]: mylist = ", mylist)
	for index in range(len(mylist)):
		chars_of_fruit = list(mylist[index])
		if chars_of_fruit[0] == "P" or chars_of_fruit[0] == "p":
			print("[OUT]: Fruits that start with P: ",mylist[index])



# Series 2
if select == "2":
	mylist = ["Apples","Pears","Oranges","Peaches"]
	print("[OUT]: mylist = ", mylist)
	mylist = mylist[:-1]
	print("[OUT]: mylist = ", mylist)
	del_fruit = input("[OUT]: Enter which fruit to delete \n[IN] del_fruit: ")
	test = False
	while test == False:
		try:
			mylist.remove(del_fruit)
		except ValueError:
			del_fruit = input("[OUT]: Fruit entered is not in the list. Enter which fruit to delete \n[IN] del_fruit: ")
		else:
			test = True
	print("[OUT]: mylist = ", mylist)



# Series 3
if select == "3":
	mylist = ["Apples","Pears","Oranges","Peaches"]
	print(mylist)
	newlist = []
	for index in range(int(len(mylist))):
		like = input(f"[OUT]: Do you like {mylist[index].lower()} \n[IN] Yes/No: ")
		like = like.lower()
		while like != "yes" and like != "no":
			like = input("[OUT]: Incorrect answer. \n[IN] Enter Yes/No: ")
			like = like.lower()
		if like == "yes":
			newlist = newlist + [mylist[index]]		# dummy variable created since mylist's index keeps changing within the for loop
	else:
		mylist = newlist			# overwrite to mylist, prevents code from writing more unnecessary variables 
	print(mylist)



# Series 4
if select == "4":
	mylist = ["Apples","Pears","Oranges","Peaches"]
	newlist = mylist[::-1]
	print("Original list: ", mylist)
	print("Reverse list: ", newlist)
