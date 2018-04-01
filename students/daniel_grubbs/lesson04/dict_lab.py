#!/usr/bin/env python3

# Lesson 04
# filename: dict_lab.py


def main():
    """Main function of the program."""
    print_header()
    tasks = "Tasks from lesson04 dictionary assignment.\n"
    print(tasks)
    dict_tasks()
    set_tasks()


def print_header():
    """Print the header of the program."""
    print('------------------------------------')
    print('             Lesson04')
    print('      Dictionary Assignment')
    print('------------------------------------\n')


def dict_tasks():
    """Perform the dictionary tasks outlined in the lesson.
    - Dictionaries 1
    """
    dict_task1 = {
        'name': 'Chris',
        'city': 'Seattle',
        'cake': 'Chocolate'
    }
    print(dict_task1)
    del dict_task1['cake']
    print("Removed 'cake' key from the dictionary, let's take a look at our dictionary now: \n")
    for k, v in dict_task1.items():
        print('{}: {}'.format(k, v))

    dict_task1['fruit'] = 'Mango'
    print(dict_task1.keys())
    print(dict_task1.values())

    if 'cake' not in dict_task1.keys():
        print("'cake' is not in the dictionary. This item of task completed, move on.")
    else:
        print("'cake' is in the dictionary.")

    if 'Mango' in dict_task1.values():
        print("'Mango' is in the dictionary. This item of task completed, move on.")
    else:
        print("'Mango' is not in the dictionary.")


def set_tasks():
    """Performing the tasks for 'set'"""
    s2 = set()
    s3 = set()
    s4 = set()

    for i in range(21):
        if i % 2:
            s2.add(i)
        elif i % 3:
            s3.add(i)
        elif i % 4:
            s4.add(i)
    print(s2)
    print(s3)
    print(s4)

    if not s3.issubset(s2):
        print('s3 is not a subset of s2, so False')
    if s4.issubset(s2):
        print('s4 is a subset of s2, so True')

    s1 = set('Python')
    s1.add('i')
    print(s1)

    s5 = ('m', 'a', 'r', 'a', 't', 'h', 'o', 'n')

    frozen = frozenset(s5)

    print(s1.union(frozen))
    print(s1.intersection(frozen))


if __name__ == '__main__':
    main()
