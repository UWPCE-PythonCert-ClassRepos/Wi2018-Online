# Lesson 04 - Dictionary and Set Lab
# =================================================================

print("\n============ Dictionaries 1 ============")
dict1 = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
print(dict1)
# remove last
dict1.popitem()
print(dict1)
dict1["fruit"] = "Mango"
dict1.keys()
dict1.values()
print("Is ""cake"" a key of dict1? ", "cake" in dict1.keys())
print("Is ""Mango"" a value of dict1? ", "Mango" in dict1.values())

print("\n============ Dictionaries 2 ============")
dict2 = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
print("Original dict2: ", dict2)
# loop through dict2 with "key" = each key per loop
for key in dict2.keys():
    dict2[key] = dict2[key].lower().count('t')
print("Dict2 with values = # of ""t""s", dict2)

print("\n============ Sets 1 ============")
s1 = set(range(1, 20 + 1))
s2 = s1.copy()
s3 = s1.copy()
s4 = s1.copy()
# loop through s1 starting from 1 to last
for index in range(1, len(s1) + 1):
    if index % 2 == 0:
        s2.remove(index)
    if index % 3 == 0:
        s3.remove(index)
    if index % 4 == 0:
        s4.remove(index)
print("s1: ", s1, "\ns2: ", s2, "\ns3: ", s3, "\ns4: ", s4)
print("Is s3 a subset of s2? ", s2.issubset(s3))
print("Is s4 a subset of s2? ", s2.issubset(s4))

print("\n============ Sets 2 ============")
# DOES NOT WORK: set1 = (set(list("Python"))).add("i") not sure why? 
set1 = set(list("Python"))
set1.add("i")
set2 = frozenset(tuple(list("marathon")))
print("Set1: ", set1, "\nSet2: ", set2)
print("Union of set1 & set2 is: ", set1.union(set2))
print("Intersection of set1 & set2 is: ", set1.intersection(set2))

print("\n============ File Lab ============")
# print full path of all files in cd
import os

list_of_files = os.listdir()
for n in range(len(list_of_files)):
    print("{}".format(os.path.abspath(list_of_files[n])))

# copy a file from source to destination (dont read content), binary ie. jpeg
with open("pic.jpg", "rb") as f1:
    with open("pic2.jpg", "wb") as f2:
        while True:
            # read 1 byte at a time, read(1) always steps 1 head each time it's called
            char = f1.read(1)
            # if the end of the file has been reached f1.read() will return ""
            if char:
                f2.write(char)
            else:
                break
        f1.close()
        f2.close()
