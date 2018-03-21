def length(x):
    l = len(x)
    print("the number of fruits in the list :{}".format(l))


def printlist():
    for x in fruits:
        print(x)


def appendfun(x):
    fruits.append(x)


def insertfun(x, y):
    fruits.insert(x, y)


fruits = ["Apples", "Pears", "Oranges", "Peaches"]
length(fruits)
printlist()

appendfun("Bananas")
print("new fruit appended at the end of the list")
length(fruits)
printlist()

insertfun(0, "Grapes")
length(fruits)
printlist()

print("the fruits starts with letter P")

pfruits = []
for i in fruits:
    if (i[0] == 'P'):
        pfruits.append(i)
for x in pfruits:
    print(x)
