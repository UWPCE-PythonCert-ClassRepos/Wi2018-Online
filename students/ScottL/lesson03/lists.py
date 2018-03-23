#!/usr/bin/env python3
# Scott Luse, List Lab, Feb 04, 2018

# SERIES-1

fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit_list)

'''starting with a set list of fruit, ask the user for another fruit and append'''
user_fruit = input("Enter the name of a new fruit (Avacado): ")
fruit_list.append(user_fruit)
print(fruit_list)

'''allow the user to select a fruit from the list using item number'''
user_item = int(input("Select a fruit item (1-5): "))
print(fruit_list[user_item-1:user_item])

my_fruit = ["Grapefruit"]
fruit_list = my_fruit + fruit_list
print(fruit_list)

fruit_list.insert(0, "Pineapple")
print(fruit_list)

for item in fruit_list:
    if item.lower().startswith('p'):
        print(item, end=' ')
        print(" ")


# SERIES-2
print('\n*** Series 2')
print(fruit_list)
fruit_list.pop()
print(fruit_list)

user_fruit = input("Enter a fruit name to delete:")
fruit_list.remove(user_fruit)
print(fruit_list)

# SERIES-3
print('\n*** Series 3')
new_fruit_bucket = []

for item in fruit_list:
    while(True):
        user_fruit = input("Do you like " + item + "?(yes/no):")
        if (user_fruit == "no"):
            print("bummer")
        elif (user_fruit == "yes"):
            print("yum")
            new_fruit_bucket.append(item)
        else:
            print("Please enter yes or no.")
            continue
        break

print(new_fruit_bucket)



# SERIES-4
print('\n*** Series 4')
new_fruit_reverse = fruit_list[:]

for index, item in enumerate(fruit_list):
    temp_string = item [::-1]
    new_fruit_reverse[index] = temp_string

fruit_list = fruit_list[:-1]
print(fruit_list)
print(new_fruit_reverse)
