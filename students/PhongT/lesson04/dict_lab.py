"""
Lesson04 Activities
Activity 1: Dictionary and Set Lab
"""

# Dictionaries 1 ---
dict1 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(dict1)
del dict1['cake']
dict1['fruit'] = 'Mango'
print(dict1)

# display the dictionary keys.
print(dict1.keys())

# display the dictionary values.
print(dict1.values())
for key, value in dict1.items():
    print(key, ': ', value)

# Display whether or not “cake” is a key in the dictionary (False)
print('cake' in dict1.keys())

# Display whether or not “Mango” is a value in the dictionary (True)
print('Mango' in dict1.values())

# Dictionaries 2 ---
# Make a dictionary using the same keys but with the number of ‘t’s in each value as the value
dict2 = {}
for key, value in dict1.items():
    dict2[key] = value.count('t')
print(dict1)
print(dict2)

# Sets 1 ---
# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.
s2 = set()
s3 = set()
s4 = set()
for i in range(21):
    if (i % 2) == 0:
        s2.add(i)
    if (i % 3) == 0:
        s3.add(i)
    if (i % 4) == 0:
        s4.add(i)
print(s2)
print(s3)
print(s4)

# Display if s3 is a subset of s2 (False)
print(s3.issubset(s2))

# Display if s4 is a subset of s2 (True).
print(s4.issubset(s2))

# Sets 2 ---
# Create a set with the letters in ‘Python’ and add ‘i’ to the set.
a_set = set('Python')
a_set.add('i')
print(a_set)

frozen_set = frozenset('marathon')
print(frozen_set)

# Display the union and intersection of the two sets.
print(a_set.union(frozen_set))
print(a_set.intersection(frozen_set))