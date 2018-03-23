
"""
Lesson 03
List Lab Exercise
"""


def series_1(fruit_list):
    print('----- Series 1 ----- ')
    # Ask the user for another fruit and add it to the end of the list
    item = input("Enter another fruit?: ")
    fruit_list.append(item)
    print(fruit_list)

    # Ask the user for a number and display the number back to the user and the fruit corresponding to that number
    item_number = int(input("what fruit number to display?: "))
    print('Fruit number ', item_number, ' : ', end='')
    print(fruit_list[item_number-1])  # todo check for out of range index

    # Add another fruit to the beginning of the list using “+” and display the list.
    print('Add Banana to the beginning of the list')
    another_fruit1 = ['Banana']
    fruit_list = another_fruit1 + fruit_list
    print(fruit_list)

    # Add another fruit to the beginning of the list using insert() and display the list.
    print('Add Avocado to the beginning of the list')
    another_fruit2 = 'Avocado'
    fruit_list.insert(0,another_fruit2)
    print(fruit_list)


def series_2(fruit_list):
    print('----- Series 2 ----- ')
    print(fruit_list)

    # Remove the last fruit from the list.
    item = fruit_list.pop()

    print('Remove last item', item)
    print(fruit_list)

    # Ask the user for a fruit to delete, find it and delete it
    item = input("Enter fruit to remove?: ")
    fruit_list.remove(item)
    print(fruit_list)


def series_3(fruit_list):
    """
    Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list.
    For each "no", delete that fruit from the list.
    For any answer that is not 'yes" or 'no', prompt the user to answer with one of those two values (a while loop is good here)
    Display the list.
    :param fruit_list:
    """
    print('----- Series 3 ----- ')
    print(fruit_list)
    for fruit in fruit_list:
        response = input("Do you like: %s (please answer 'yes' or 'no')?: " % fruit)
        if response == 'no':
            while fruit in fruit_list:
                fruit_list.remove(fruit)
        elif response == 'yes':
            pass
    print("Remaining fruit list ", fruit_list)


def series_4(fruit_list):
    print('----- Series 4 ----- ')
    print(fruit_list)

    reverse_fruit_list = []
    print('Reverse the letters in each fruit in the copy')
    for item in fruit_list:
        reverse_fruit_list.append(item[::-1])
    print(reverse_fruit_list)

    print("Delete the last item of the original list. Display the original list and the copy")
    fruit_list.pop()
    print(fruit_list)
    print(reverse_fruit_list)


if __name__ == "__main__":
    fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
    print(fruit_list)

    series_1(fruit_list)
    series_2(fruit_list)
    series_3(fruit_list)

    fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
    series_4(fruit_list)
