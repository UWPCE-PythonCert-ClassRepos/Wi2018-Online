#!/usr/bin/env python3

"""Lesson03 - Assignment 2 - Operations on lists."""

# Series 1

fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]


def series_1(a_list):
    """Perform a series of actions on a_list."""
    my_list = a_list[:]

    # Display the list.
    print(my_list)

    # Ask the user for another fruit and add it to the end of the list.
    response = input("Type the name of a fruit > ")
    my_list.append(response)

    # Display the list.
    print(my_list)

    # Ask the user for a number...
    prompt_num = "Type a number from 1 to {} > ".format(len(my_list))
    response_num = int(input(prompt_num))
    # ... and display the number and the corresponding fruit.
    print(response_num, my_list[response_num - 1])

    # Add another fruit to the beginning of the list using “+” ...
    my_list = ["Melons"] + my_list
    # ... and display the list.
    print("\nAdded another fruit to the beginning of the list using '+'")
    print(my_list)

    # Add another fruit to the beginning of the list using insert() ...
    my_list.insert(0, 'Lemons')
    # ... and display the list.
    print("\nAdded another fruit to the beginning of the list using insert()")
    print(my_list)

    # Display all the fruits that begin with “P”, using a for loop.
    print("\nDisplay all the fruits that begin with 'P', using a for loop")
    for name in my_list:
        if name.lower().startswith('p'):
            print(name, end=' ')
    print("\n\n")


# Series 2

def find_del_fruit(seq, msg):
    """Ask the user for a fruit to delete, find it and delete it."""
    # Display the list.
    print(msg)
    print(seq)
    print()

    # Remove the last fruit from the list.
    my_list = seq[:-1]

    # Display the list.
    print("Removed the last fruit from the list")
    print(my_list)
    print()

    # Ask the user for a fruit to delete, find it and delete it.
    chosen_fruit_to_del = input("Type the name of a fruit to delete > ")
    while not chosen_fruit_to_del in my_list:
        print('Not found. Try again.')
        chosen_fruit_to_del = input("Type the name of a fruit to delete > ")
    new_fruit = []
    for item in my_list[:]:
        if item != chosen_fruit_to_del:
            new_fruit.append(item)
    print("The current list")
    print(new_fruit)
    print()


# Series 3

def do_you_like(seq):
    """Delete fruit the user don't like."""
    new_seq = []
    for item in seq:
        prompt = "Do you like {}? yes/no > ".format(item.lower())
        response = input(prompt)
        while not (response == "yes" or response == "no"):
            print("Not a valid answer. Try again.")
            response = input(prompt)
        if response == "yes":
            new_seq.append(item)
    print("The current list")
    print(new_seq)
    print()


# Series 4

def reverse_each_fruit(seq):
    """Reverse the letters in each item in a copy of seq."""
    # Make a copy of the list...
    reversed_seq = seq[:]
    # ... and reverse the letters in each fruit in the copy.
    for index, fruit in enumerate(seq):
        reversed_fruit = fruit[::-1]
        reversed_seq[index] = reversed_fruit

    # Delete the last item of the original list.
    seq = seq[:-1]

    # Display the original list and the copy.
    print("Original list with last item deleted: ", seq)
    print("Reversed copy, last item not deleted: ", reversed_seq)
    print()


if __name__ == "__main__":
    series_1(fruit_list)
    find_del_fruit(fruit_list, "Display the initial list")
    find_del_fruit(fruit_list * 2, "Display the doubled initial list ")
    do_you_like(fruit_list)
    reverse_each_fruit(fruit_list)
