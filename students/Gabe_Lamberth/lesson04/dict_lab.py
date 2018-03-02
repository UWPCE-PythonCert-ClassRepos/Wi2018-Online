#!/usr/bin/env python3

# Activity 1
print("{:-^70s}".format("Dictionary Activities"), end='\n')

tst_dict = {'name': 'Chris', 'city':'Seattle', 'cake':'Chocolate'}
print(f'Here are the Keys & Values in the dictonary: \n{tst_dict}\n')
# remove cake entry
tst_dict.pop("cake")

print(f'Here are the values after removing the "cake" key: \n{tst_dict}\n')
tst_dict["fruit"] = "Mango"
print(f'Here are the values after adding "fruit":"Mango "\n {tst_dict}\n')
print(f'Here are the dictionary "keys": \n{tst_dict.keys()}\n')
print(f'Here are the dictionary "values": \n{tst_dict.values()}\n')

print("The dictionary has cake as a key?", bool(tst_dict.get('cake', 0)))
print("Is Mango a value?", 'Mango' in tst_dict.values())
print()
new_dict = {}
for k in tst_dict:
    new_dict[k] = (tst_dict[k].lower()).count('t')
print("Count of 't's in the New dictionary Key:value pairs :\n", new_dict)

print("{:-^70s}".format("Sets Activities"), end='\n')
# Sets 1
print()
# Create sets with numbers 0 - 20 that are divisible by 2,3,4 using range function
s2 = set(range(0, 21, 2))
s3 = set(range(0, 21, 3))
s4 = set(range(0, 21, 4))

print("Values in Set s2:", s2)
print("Values in Set s3:", s3)
print("Values in Set s4:", s4)
print("Is s3 a subset of s2?", s3.issubset(s2))
print("Is s4 a subset of s2?", s4.issubset(s2))

# Sets 2
set_python = set('Python')
set_python.add('i')
"""
Sets are mutable and unordered collections of unique
and immutable objects.
"""
print("Values in Set Python:", set_python)
# create an immutable set
set_marathon = frozenset('marathon')
print("Values in Frozenset marathon:", set_marathon)
print("Union:", set_python.union(set_marathon))
print("Intersection:", set_python.intersection(set_marathon))




