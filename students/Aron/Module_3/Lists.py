# Lists

#Series 1
# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”
fruit=["Apples", "Pears", "Oranges", "Peaches"]

# Display the list (plain old print() is fine…)
print(fruit)

#Ask the user for another fruit and add it to the end of the list
response = input("What fruit should we add: ")
fruit.append(response)

# Display the list
print(fruit)

# Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
response_number = input("What number of the index should we grab?: ")
fruit[(n-1):n]
#fruit.pop(n-1)

# Add another fruit to the beginning of the list using “+” and display the list
fruit2 = ["Lemon"] + fruit
print(fruit2)

# Add another fruit to the beginning of the list using insert() and display the list
fruit.insert(0,"Lime")
print(fruit)

#Display all the fruits that begin with “P”, using a for loop
for list in fruit:
    if "P" in list:
        print(list)

#Series 2
# Display the list
print(fruit)

#Remove the last fruit from the list
fruit.pop(-1)

#Display the list
print(fruit)

#Ask the user for a fruit to delete, find it and delete it.
#(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
rmfruit = input("What fruit should we remove: ")


#Series3
#Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
for fruit in fruits:
    result = input("Do you like {:s}?".format(fruit.lower()))
    if result == 'n':
        fruits.remove(fruit)
    else:
        result = input("Do you like {:s}?".format(fruit.lower()))
        if result == 'y'
        print fruits

for i in range(len(fruits) -1, -1, -10:
#For each “no”, delete that fruit from the list.

#For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
new_fruit=fruit[:]
for item in fruit:
    while True:
        result = input('Do you like {:s}(y/n)?'.format(item))
        if result == 'y':
            print('great')
            break
        elif result == 'n':
            print('Deleting {:s}'.format(item))
            new_fruit.remove(item)
            break
print(new_fruit)


#Display the list.

#Series4
#Make a copy of the list and reverse the letters in each fruit in the copy.

#Delete the last item of the original list. Display the original list and the copy.
