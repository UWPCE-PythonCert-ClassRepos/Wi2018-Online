#!/usr/bin/env python3

fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]

print("== Series1 ==")
print("Original fruit list is {}".format(fruit_list))
response = input("Please enter name of another fruit\n")
fruit_list.append(response)

while True:
    response = int(input("please enter the number to display corresponding fruit (0 to quit)\n"))
    if response == 0:
        break
    elif 0 < response <= len(fruit_list):
        print(f"Index {response}: {fruit_list[response-1]}")
    else:
        print(f"No fruit at Index {response}")
print("Adding another fruit {} to fruit list {} using + operator ".format("Bananas", fruit_list))
fruit_list = ["Bananas"] + fruit_list
print("Adding another fruit {} to fruit list {} using insert method ".format("Papayas", fruit_list))
fruit_list.insert(0, "Papayas")
print("Printing final list {}".format(fruit_list))
for fruit in fruit_list:
    if fruit.startswith("P"):
        print(fruit, " ", end="")

print("\n=== Series2 ===")
print(fruit_list)
fruit_list.pop()
print(fruit_list)
while True:
    print(fruit_list)
    response = input("enter fruit to delete (q to quit)>")
    if response == 'q':
        break
    elif response in fruit_list:
        fruit_list.remove(response)
    else:
        print("Did not find {:s} in {}".format(response, fruit_list))

fruit_list *= 2
while True:
    print(fruit_list)
    response = input("enter fruit to delete (q to quit)>")
    if response == 'q':
        break
    elif response in fruit_list:
        while response in fruit_list:
            fruit_list.remove(response)
    else:
        print("Did not find {:s} in {}".format(response, fruit_list))

print("=== Series3 ===")
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
for fruit in fruit_list[:]:
    while True:
        response=input("Do you like {:s}".format(fruit.lower()))
        if response == "no":
            fruit_list.remove(fruit)
        elif response != "yes":
            print("Please enter yes or no")
            continue
        break
print(fruit_list)

print("=== Series 4 ===")
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
fruit_list_copy = fruit_list[:]
for index in range(len(fruit_list_copy)):
    fruit_list_copy[index] = fruit_list_copy[index][::-1]

fruit_list.pop()
print(f"Original: {fruit_list}")
print(f"Copy: {fruit_list_copy}")







