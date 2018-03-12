#!/usr/bin/env python3
"""modify the fruit list"""
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






