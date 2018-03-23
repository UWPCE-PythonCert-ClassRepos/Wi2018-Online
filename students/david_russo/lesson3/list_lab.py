#!/usr/bin/env python

# Series 1

# Initial list of fruits
fruits = ["Apples", "Pears", "Oranges", "Peaches"]

# print list of fruits
print(fruits)

# prompt user for new fruit and append it to the fruits list
fruits.append(input("Enter a new fruit > "))

# print the modified fruits list
print(fruits)

# print the index and the corresponding fruit at the user supplied index
fruit_index = int(input("Enter a number between 1 and 5 > "))
print(fruit_index, fruits[fruit_index - 1])

# Add another fruit to the beginning of the list and print it
fruits = ["Cherry"] + fruits
print(fruits)

# Add another fruit to the beginning of the list with .insert() and print it
fruits.insert(0, "Pineapple")
print(fruits)

for fruit in fruits:	
	if fruit[0] == 'P':
		print(fruit)

# Series 2

# make a copy of the fruits list
fruits2 = fruits[:]

# display the list
print(fruits2)

# remove the last fruit from the list 
del fruits2[-1]

# display the list
print(fruits2)

# Promp the user for a fruit to delete, find it, and delete it
fruit_to_remove = input("Enter a fruit to delete > ")
fruits2.remove(fruit_to_remove)

# print the list
print(fruits2)

# Series 3

# copy the list from series 1
fruits3 = fruits[:]

# initialize container for removal fruits
fruits_to_remove = []

# iterate through each fruit and ask the user if they like it. If no, store it for later removal.
for fruit in fruits3:
	response = input("Do you like {}? ".format(fruit).lower())
	while(response not in ("yes", "no")):
		response = input("Do you like {}? Please make sure your answer is 'yes' or 'no'. ".format(fruit.lower()))
	if response == "no":
		fruits_to_remove.append(fruit)

# remove the fruits that the user didn't like
for fruit in fruits_to_remove:
	fruits3.remove(fruit)

# print the remaining fruits (the fruits that the user does like)
print(fruits3)

# series 4

# make a copy of the list and reverse the letters in each fruit in the copy
fruits_copy = fruits[:]
for i, fruit in enumerate(fruits_copy):
	fruits_copy[i] = fruit[::-1]

# delete the last item from the original list
fruits.pop()

# display the original list and the copy
print(fruits)
print(fruits_copy)





