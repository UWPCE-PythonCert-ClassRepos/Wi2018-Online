def delete(x):
    fruits.pop(x)


def printlist():
    l = length()
    for i in range(0, l):
        print("{0}.{1}".format(i, fruits[i]))


def length():
    n = len(fruits)
    return n


fruits = ["Apples", "Pears", "Oranges", "Peaches", "Mango", "banannas", "Necter", "Plums"]
printlist()
k = length()
print("the number of fruits in the list:{0}".format(k))
print("what fruit do you want to delete")
delete(2)
printlist()
k = length()
print("the number of fruits in the list:{0}".format(k))

reverse = []
fruits = ["Apples", "Pears", "Oranges", "Peaches", "Mango", "banannas", "Necter"]
for i in fruits:
    y = i[::-1]
    reverse.append(y)
    print(y)
print("the original list of the fruits")
for i in reverse:
    y = i[::-1]
    print(y)
