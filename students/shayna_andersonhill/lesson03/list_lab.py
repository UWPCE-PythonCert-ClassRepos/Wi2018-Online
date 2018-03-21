#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
#Shayna Anderson-Hill
#Goal: Learn the basic ins and outs of Python lists.
#03-03-2018

#Series 1
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)

response = input("Please user, give me a fruit > ")
fruits.append(response)
print(fruits)

response = input("Please user, give me a number > ")
print(response, fruits[(int(response)-1)])

fruits = ['Bananas'] + fruits
print(fruits)

fruits.insert(0, 'Mangoes')
print(fruits)

for fruit in fruits:
    if fruit[0]=='P':
        print(fruit)

#Series 2
print(fruits)
fruits.pop()
print(fruits)
response = input("Please user, give me a fruit to delete > ")
fruits.remove(response)
print(fruits)

#Series 3
response_list = []
for i in fruits:
    response = input('Do you like {}? '.format(i.lower()))
    while response != 'yes' and response != 'no':
        response = input('Only "yes" or "no" answers please. Trying again... Do you like {}? '.format(i.lower()))
    response_list.append(response)

fruit_dislikes = []
for index, i in enumerate(response_list):
    if i == 'no':
        fruit_dislikes.append(fruits[index])

for i in fruit_dislikes:
    fruits.remove(i)
print(fruits)

#Series 4
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
fruits2 = fruits[:]

for index, fruit in enumerate(fruits2):
    fruits2[index] = fruit[::-1]

fruits.pop()
print(fruits)
print(fruits2)









