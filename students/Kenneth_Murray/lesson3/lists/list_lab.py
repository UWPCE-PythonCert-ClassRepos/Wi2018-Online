#!/usr/bin/env python3
"""modify the fruit list - Series1"""
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
l = len(fruit_list)
print(fruit_list)	#display the original list

response = input("Please name another fruit > ")	#get response from user to modify the list
fruit_list.append(response)	#update the list
print(response +" has been added to the fruit list")
print(fruit_list)	#display the updated list

response = input("Please choose a fruit using the number that corresponds to its position in the list > ")
fruit_index = int(response) - 1
print(fruit_list[fruit_index])	#display the selected fruit

response = input("Please name another fruit to add to the list > ")	#get response from user to modify the list
fruit_list = ",".join(str(x) for x in fruit_list)	#create a CSV string from the list
response1 = response + ","	#add a comma to the response
fruit_list = response1 + str(fruit_list)	#add the new fruit to the front of the string
fruit_list=fruit_list.split(",")	#create a list from the string using the comma to seperate items
print(response +" has been added to the fruit list")
print(fruit_list)	#display the updated list

response = input("Please name another fruit to add to the list > ")	#get response from user to modify the list
fruit_list.insert(0,response)
print(response +" has been added to the fruit list")
print(fruit_list)	#display the updated list

print("These fruits all start with the letter P")
for fruit in fruit_list:
    if (fruit[0]).upper() == "P":
        print(fruit)

"""Fruit List Series Two"""
print(fruit_list)
print("Removing " + fruit_list[-1] + " from the list")
fruit_list.remove(fruit_list[-1])
print(fruit_list)

response = input("Please name a fruit to remove from the list > ")	#get response from user to modify the list
print(response + " has been removed from the list")
for fruit in fruit_list:
    if fruit.casefold() == response.casefold(): #compare regaurdless of case
        fruit_list.remove(fruit)
print(fruit_list)

"""Fruit List Series Three"""

for fruit in fruit_list:
#    fruit_list.remove(fruit)
#    fruit_list.append(fruit.lower())
#    fruit = fruit.lower()
    response = input("Do you like " + fruit + "? Please answer YES or NO > ")	#get response from user to modify the list
    response = response.lower()
    print(response)
    print(type(response))
    while response == "yes" or "no":
        if response == "no":
            fruit_list.remove(fruit)
            print(fruit + " has been removed from the list")
        else:
            print("I like " + fruit + " too.")
    else:
         response = input("Please answer YES or NO > ")	#get response from user to modify the list
print("Here is a list of your favorite fruits.")
print(fruit_list)


















