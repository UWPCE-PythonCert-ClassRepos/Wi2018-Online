#!/usr/local/bin/python3


def dictionaries_1():
    d = {'name': 'chris', 'city': 'Seattle', 'cake': 'chocolate'}
    print(d)
    del(d['cake'])  # remove k/v
    print(d)
    d['fruit'] = 'mango'  # add new k/v
    print(d)
    print('cake is in dictionary? ', 'cake' in d)
    print('fruit is in dictionary? ', 'fruit' in d)
    print('Fruit is in dictionary? ', 'Fruit' in d)   # case sensitive
    'mango' in d.keys()
    'mango' in d.values()
    'mango' in d.items()  # returns False even when is a key or value
    for k, v in d.items():
        print('key & value', k, v)
    for v in d.values():
        print('value', v)
    for v in d.keys():
        print('key', v)


def sets():  # https://www.python-course.eu/sets_frozensets.php
    s2 = set()
    s3 = set()
    s4 = set()

    for i in range(20):
        if i % 2 == 0:
            s2.add(i)
        if i % 3 == 0:
            s3.add(i)
        if i % 4 == 0:
            s4.add(i)

    print(s2, "\n", s3, "\n", s4, "\n")
    print('s3 is subset of s2: ', s3.issubset(s2))
    print('s4 is subset of s2: ', s4.issubset(s2))



if __name__ == "__main__":
    # dictionaries_1()
    sets()
