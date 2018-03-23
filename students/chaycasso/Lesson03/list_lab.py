#!/usr/bin/env python3
#
# Learning About Lists
# Chay Casso, 2/4/2018

# Series 1
# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
print("Series 1")
print("--------")

fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]

# Display the list (plain old print() is fine…).
print(fruit_list)

# Ask the user for another fruit and add it to the end of the list.
additional_fruit = input("Please enter another fruit for the list. ")
fruit_list.append(additional_fruit.title())

# Display the list.
print(fruit_list)

# Ask the user for a number and display the number back to the user and the fruit corresponding to that number
# (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
number = int(input("Please select a fruit number from 1 to {:d}. ".format(len(fruit_list))))
print("{:d} {}".format(number,fruit_list[number-1]))

# Add another fruit to the beginning of the list using “+” and display the list.
print("Adding Limes to the beginning of the list.")
fruit_list = ["Limes"] + fruit_list
print(fruit_list)

# Add another fruit to the beginning of the list using insert() and display the list.
print("Adding Apricots to the beginning of the list.")
fruit_list.insert(0, "Apricots")
print(fruit_list)
print()
# Display all the fruits that begin with “P”, using a for loop.
print("All fruits beginning with P:")
for fruit in fruit_list:
    if fruit[:1] == "P": print(fruit)

# Series 2
# Using the list created in series 1 above:

# Display the list.
print("\nSeries 2")
print("--------")
fruit_list2 = fruit_list[:]
print(fruit_list2)

# Remove the last fruit from the list.
print("Removing the last fruit.")
del fruit_list2[-1:]

# Display the list.
print(fruit_list2)

# Ask the user for a fruit to delete, find it and delete it.
# (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
fruit_list2 = fruit_list2 * 2
fruit = ""
while fruit not in fruit_list2:
    fruit = input("Please enter a fruit to remove. ").title()
    if fruit not in fruit_list2: print("Fruit not found.")
while fruit in fruit_list2:
    fruit_list2.remove(fruit)
print("Resultant list is:", fruit_list2)

# Series 3
print("\nSeries 3")
print("--------")
# Again, using the list from series 1:
fruit_list3 = fruit_list[:]
print(fruit_list3)
# Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit
# all lowercase).
# For each “no”, delete that fruit from the list.
# For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is
# good here)
fruit = ""

# Need to make a copy of fruit_list3 here.
for fruit in fruit_list3[:]:
    answer = ""
    while answer not in ["yes","no"]:
        answer = input("Do you like {}? ".format(fruit.lower())).lower()
        if answer not in ["yes","no"]: print("Please answer yes or no.")
    if answer == "no":
        print("Removing {}.".format(fruit))
        fruit_list3.remove(fruit)
# Display the list.
print("Resultant list is:", fruit_list3)

print("\nSeries 4")
print("--------")
# Once more, using the list from series 1:
fruit_list4 = fruit_list[:]
# print(fruit_list4)

# Make a copy of the list and reverse the letters in each fruit in the copy.
for i in range(len(fruit_list4)):
    fruit_list4[i]=fruit_list4[i][::-1]

# Delete the last item of the original list. Display the original list and the copy.
del fruit_list[-1:]
print("Original list: ", fruit_list)
print("Copy list: ", fruit_list4)