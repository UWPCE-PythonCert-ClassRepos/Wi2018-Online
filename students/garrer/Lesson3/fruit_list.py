fruit_list=['Apples', 'Pears', 'Oranges', 'Peaches']
#print(fruit_list)
fruit_list.append(input('Enter the fruit you want to add to the list:'))
print(fruit_list)
q=int(input("Enter an of the fruit to be displayed in the list:"))
print(fruit_list[q+1])
fruit_list+=['Guava']
fruit_list.insert(len(fruit_list),'Kiwi')
print(fruit_list)