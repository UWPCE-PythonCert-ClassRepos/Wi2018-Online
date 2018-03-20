#!/usr/bin/env python3


def series1(fruits_list):
    """
    Series of tasks as specified in series1. It returns a list that is used by
    series2.
    :return:
    """

    print("Fruits are:{}".format(fruits_list))

    # Ask user to enter a fruit and append to the list
    fruit = input("Enter a fruit")
    fruits_list.append(fruit)
    print("Fruits after adding a new fruit are:{}".format(fruits_list))

    # Ask for a number and display fruit corresponding to that
    idx = input("Enter a number between 1 and " + str(len(fruits_list)))
    print("The number you entered is:{}.The fruit corresponding to"
          " the number is:{}".format(idx, fruits_list[int(idx) - 1]))

    # Add a fruit at beginning of list using "+" operator
    fruits_list = ['Mango'] + fruits_list
    print("Fruits are:{}".format(fruits_list))

    # Add a fruit at beginning of list using insert method
    fruits_list.insert(0, 'Pineapple')
    print("Fruits are:{}".format(fruits_list))

    # Display fruits that begin with 'P'
    print("Following are fruits that begin with P")
    for fruit in fruits_list:
        if fruit[0].lower() == 'p':
            print(fruit)


def series2(fruits_list):
    """
    Remove all occurences of fruit that user entered from the list if it exists
    in list. Otherwise keep prompting till he enters a fruit from the list.
    :param fruits_list:
    :return:
    """
    print("Fruits are:{}".format(fruits_list))

    # Remove last fruit from the list
    fruits_list.pop()
    print("Fruits after deleting last fruit are:{}".format(fruits_list))

    # Ask user for a fruit and delete it
    fruits_list = fruits_list * 2
    del_list = []
    while True:
        fruit_to_del = input("Enter a fruit to be deleted.")
        if fruit_to_del in fruits_list:
            for fruit in fruits_list:
                if fruit == fruit_to_del:
                    fruits_list.remove(fruit)
            break
        else:
            print("Fruit entered does not exist in list. Enter again")
    print("Fruits are:{}".format(fruits_list))


def series3(fruits_list):
    """
    Ask user if he likes the fruit for each fruit in the list. If he responds
    with no, delete it
    :param fruits_list:
    :return: None
    """
    # Create a copy so that original list can be modified while iterating
    copy_list = fruits_list[:]
    for fruit in copy_list:
        while True:
            user_response = input("Do you like {} ?".format(fruit.lower()))
            if user_response.lower() in ('yes', 'no'):
                break
            else:
                print("Please enter a response that is either yes or no")
        if user_response.lower() == 'no':
            fruits_list.remove(fruit)
    print("Fruits are:{}".format(fruits_list))


def series4(fruits_list):
    """
    Make a copy of fruits list and reverse each fruit. Delete last item
    from fruit list.
    :param fruits_list:
    :return: None
    """
    copy_list = fruits_list[:]
    for idx, fruit in enumerate(fruits_list):
        copy_list[idx] = fruit[::-1]
    fruits_list.pop()
    print("Original List is:{}".format(fruits_list))
    print("Copy List is:{}".format(copy_list))


if __name__ == '__main__':
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    #series2(fruits)
    #series3(fruits)
    #series4(fruits)
    pass

