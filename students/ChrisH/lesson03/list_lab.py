#!/usr/bin/env python3
# -----------------------------------------------------------
# list_lab.py
#  demonstrates basic Python lists
# -----------------------------------------------------------

# Series 1
print('*** Series 1')
basket = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(basket)
response = input("Please type the name of another fruit > ")
basket.append(response)
print(basket)
while True:
    response = int(input("Please type a number to display the corresponding fruit (0 to quit) > "))
    if response == 0:
        break
    elif 0 < response <= len(basket):
        print(f"Index {response}: {basket[response - 1]}")
    else:
        print(f"No fruit at index {response}.")

basket = ['Tangerine'] + basket
print(basket)
basket.insert(0, 'Kiwi')
print(basket)
for fruit in basket:
    if fruit[0] == 'P':
        print(fruit, " ", end="")
print('')

# Series 2
print('\n*** Series 2')
print(basket)
basket.pop()
while True:
    print(basket)
    response = input("Enter a fruit from the list to delete (q to quit) > ")
    if response == 'q':
        break
    elif response in basket:
        basket.remove(response)
    else:
        print("Did not find {:s}.".format(response))

basket *= 2
print('Doubled the list.')
while True:
    print(basket)
    response = input("Delete another fruit (q to quit) > ")
    if response == 'q':
        break
    elif response in basket:
        while response in basket:
            basket.remove(response)
    else:
        print("Fruit not found. Please try again.")

# Series 3
print('\n*** Series 3')
basket = ['Apples', 'Pears', 'Oranges', 'Peaches']

for fruit in basket[:]:     # make a copy of the list to iterate here, as it gets modified
    while True:
        response = input('Do you like {}?'.format(fruit.lower()))
        if response == 'no':
            while fruit in basket:
                basket.remove(fruit)
        elif response != 'yes':
            print("Please answer with either 'yes' or 'no'.")
            continue
        break
print(basket)

# Series 4
print('\n*** Series 4')
basket = ['Apples', 'Pears', 'Oranges', 'Peaches']
basket2 = basket[:]
# print(basket2)
for i in range(len(basket2)):
    basket2[i] = (basket2[i])[::-1]
# print(basket2)
basket2.pop()
print("Original:{}".format(basket))
print("Copy: {}".format(basket2))

