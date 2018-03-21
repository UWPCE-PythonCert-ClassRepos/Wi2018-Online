#!/usr/bin/env python3

#Series1
def series_1():
	print ("Series1")
	fruitslist = ["Apples","Pears","Oranges","Peaches"]

	while (True):	
		response = input("Enter a fruit to add to the list of Fruits > ")
		if not(response == None and response == ''):
			fruitslist.append(response)
			break
		else: 
			print ("Enter valid non-empty fruit name")
	print ("Series1 fruits list" + str(fruitslist))

	print (fruitslist)
	while (True):	
		response = input("Enter a number or index for the fruit to find in the Fruits list > ")
		if (response != None and response != '' and response.lstrip('+-').isdigit() and int(response) >=1 and int(response) <= len(fruitslist)):
 			index = int(response)
 			fruit = fruitslist[index-1]
 			print ("The fruit with index {} is {}".format(str(index),fruit))
 			break
		else:
			print ("Enter a valid integer >= 1 and <= {} (the number of fruits)".format(str(len(fruitslist))))

	# adding Grapes to the beginning of the list using +
	fruitslist = ["Grapes"] + fruitslist

	# adding Strawberries to the beginning of the list using insert 
	fruitslist.insert(0,"Strawberries")
	print("Fruits list after adding fruits to the beginning of the list : {}".format(str(fruitslist)))

	print ("Printing fruits in the List which begin with a P or p")
	for fruit in fruitslist:
		if fruit[:1].lower() == 'p': #check the first letter in the fruit string
			print (fruit)
	print ("Series 1 complete")
	return fruitslist

#Series2
def series_2(fruits):
	print ("Series2")
	tmpfruits = list(fruits)
	print ("Fruits in Series2: " + str(tmpfruits))

	del tmpfruits[len(tmpfruits)-1]

	print ("Fruits List after deletion of last item: "+ str(tmpfruits))

	tmpfruits = tmpfruits * 2
	print ("Fruits List after doubling the fruits: " + str(tmpfruits))

	while (True):
		response = input("Enter a fruit to delete > ")
		if not((response == None) and (response =='')) and (response in tmpfruits):
			for item in tmpfruits:
				#delete every occurence of the item 
				if item == response:
					tmpfruits.remove(response) #removes one of more occurences of the fruit
			break
		else:
			print (response + " is not in Fruits. Please enter another Fruit to delete:")
	print ("Fruits List after deleting a fruit" + str(tmpfruits))
	print ("Series 2 complete")

#Series3 - use the original fruits
def series_3(fruits):
	tmpfruits = list(fruits) #make a copy
	fruitsToDelete = []
	print ("Series3")
	print ("Fruits List is Series 3: " + str(tmpfruits))
	for fruit in tmpfruits:
		message = "Do you like {0}? Enter Yes or No > ".format(fruit.lower())
		response = input(message)
		if response.lower() == "no":
			fruitsToDelete.append(fruit)
	for fr in fruitsToDelete:
		tmpfruits.remove(fr)
	print("Fruits is Fruits List after deletion: " + str(tmpfruits))
	print ("Series 3 complete")


#Series4
def series_4(fruitsSeries1):
	print ("Series4")
	fruits = list(fruitsSeries1)
	print ("Fruits List is Series 4: " + str(fruits))
	for i,fruit in enumerate(fruits):
		fruit = fruit[-1::-1] #reverse string
		fruits[i] = fruit #update the list item with the reversed value
	print ("Fruits list with each fruit letters reversed: " +  str(fruits))
	#del (fruitsSeries1[len(fruitsSeries1)-1])
	fruitsSeries1.pop()
	print("Original fruits list with last item deleted: " + str(fruitsSeries1))
	print ("Series 4 complete")


if __name__ == "__main__":
	fruitsFromSeries1 = series_1()
	series_2(fruitsFromSeries1)
	series_3(fruitsFromSeries1)
	series_4(fruitsFromSeries1)

