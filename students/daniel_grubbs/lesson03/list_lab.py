#!/usr/bin/env python3

# Daniel Grubbs
# 1/31/2018
# Goal: Learn the basic ins and outs of Python lists

# Section 1
fruits = ['Apples', 'Pears', 'Organges', 'Peaches']
print(fruits)

# append a fruit
response = input('Enter another fruit > ')
fruits.append(response)
print(fruits)

number = int(input('Enter a number > '))

print(fruits[number - 1])

fruits += ['Grapes']
print(fruits)

fruits.insert(3, 'Plums')
print((fruits))

# Section 2
print(fruits)
fruits.pop()
print(fruits)
delete_fruit = int(input('Enter a fruit to delete >'))
fruits.pop(delete_fruit)

# Section 3
print(fruits)

for fruit in fruits:
    while True:
        like = input('Do you like {}? '.format(fruit)).lower()
        if like == 'no':
            fruits.remove(fruit)
            break
        elif like == 'yes':
            break
        else:
            print("Please enter 'yes' or 'no' ")

# Section 4
new_fruits = fruits[:]
for i in range(len(new_fruits)):
    new_fruits[i] = new_fruits[i][::-1]

del new_fruits[-1]
print(new_fruits)

print("Original list: " + str(fruits))
print("Copied list: " + str(new_fruits))
