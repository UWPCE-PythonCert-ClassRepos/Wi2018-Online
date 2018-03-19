# Series 1
print("Series 1" + '\n' + '\n')

fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)

# Ask for a new fruit, add it to the list, and display
response = input("Please add another fruit to the list >  ")
fruit.append(response)
print(fruit)

# Ask for a number to display a particular element of the list
response = input("Please enter a number to view an element in the list >  ")
print(fruit[int(response)])

# Add a new element to the beginning of the list using "+"
fruit = ["Mangos"] + fruit
print(fruit)

# Add a new element to the beginning of the list using ".insert"
fruit.insert(0, "Lemons")
print(fruit)

# Display all the fruits that begin with “P”, using a for loop.
for i in fruit:
    if i.startswith("P") is True:
        print(i)


# Series 2
print('\n' + '\n' + "Series 2" + '\n' + '\n')

# Display the list.
print(fruit)

# Remove the last fruit from the list.
fruit.pop()

# Display the list.
print(fruit)

# Ask the user for a fruit to delete, find it and delete it.
response = input("Please identify a fruit to delete:  ")
while True:
    response = input("Please enter a fruit to delete, (q to quit) >  ")
    if response == "q":
        break
    elif response in fruit:
        fruit.remove(response)
        print(fruit)
    else:
        print("Did not find {:s}.".format(response))

# (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
fruit *= 2
while True:
    response = input("Please enter another fruit to delete, (q to quit) >  ")
    if response == "q":
        break
    elif response in fruit:
        while response in fruit:
            fruit.remove(response)
            print(fruit)
    else:
        print("Did not find {:s}.".format(response))


# Series 3
print('\n' + '\n' + "Series 3" + '\n' + '\n')

fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)

#   Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list
for i in fruit:
    while True:
        response = input("Do you like {}?   ".format(i.lower()))
        # For each “no”, delete that fruit from the list.
        if response == 'no':
            while i in fruit:
                fruit.remove(i)
        # For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values
        elif response != 'yes':
            print("Please answer with 'yes' or 'no'.")
            continue
        break

# Display the list.
print(fruit)


# Series 4
print('\n' + '\n' + "Series 4" + '\n' + '\n')

fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)

# Make a copy of the list and reverse the letters in each fruit in the copy.
fruit2 = fruit[:]
for i in range(len(fruit2)):
    fruit2[i] = (fruit2[i])[::-1]

# Delete the last item of the original list. Display the original list and the copy.
fruit.pop()
print(fruit)
print(fruit2)

