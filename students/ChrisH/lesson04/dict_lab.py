#!/usr/bin/env python3
# -----------------------------------------------------------
# dict_lab.py
#  demonstrates basic Python dictionaries
# -----------------------------------------------------------


def dictionaries():
    # Dictionaries 1
    data = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
    print("Dictionary:", data)
    print("Deleting cake.")
    del data['cake']
    print("Dictionary:", data)
    print("Adding fruit.")
    data['fruit'] = 'Mango'
    print("Dictionary:", data)
    print("Keys:", ", ".join([x for x in data.keys()]))
    print("Values:", ", ".join([x for x in data.values()]))
    print("Is cake a key?", bool(data.get('cake', 0)))
    print("Is Mango a value?", 'Mango' in data.values())

    # Dictionaries 2
    new_data = {}
    for k in data:
        new_data[k] = (data[k].lower()).count('t')
    print("New dictionary, same keys, value is count of 't's in the old dictionary value:\n", new_data)


def sets():
    # Sets 1
    s2 = set(range(0, 21, 2))
    s3 = set(range(0, 21, 3))
    s4 = set(range(0, 21, 4))
    print("Set s2:", s2)
    print("Set s3:", s3)
    print("Set s4:", s4)
    print("Is s3 a subset of s2?", s3.issubset(s2))  # equiv. s3 <= s2
    print("Is s4 a subset of s2?", s4.issubset(s2))  # equiv. s4 <= s2

    # Sets 2
    sp = set('Python')
    sp.add('i')
    print("Set Python:", sp)
    sm = frozenset('marathon')
    print("Frozenset marathon:", sm)
    print("Union:", sp | sm)  # equiv. sp.union(sm)
    print("Intersection:", sp & sm)  # equiv. sp.intersection(sm


if __name__ == "__main__":
    dictionaries()
    sets()
