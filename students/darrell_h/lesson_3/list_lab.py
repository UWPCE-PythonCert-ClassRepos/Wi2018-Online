#!/usr/local/bin/python3

fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']


def display_list():
    print(fruit)


def series_1():
    display_list()
    fruit.append(input("enter a new fruit >"))
    display_list()
    while True:
        # will keep prompting until valid number in range is entered
        number = input("Enter a number between 1 and {:d} ".format(len(fruit)))
        if int(number) in range(1, len(fruit) + 1):
            print('Fruit number {:d} is a {:s}'.format(
                int(number), fruit[int(number) - 1]))
            break
    fruit[0] = 'strawberry'
    fruit.insert(0, 'fig')
    display_list()

    for item in fruit:
        if item[0] == 'P':
            print(item)


def series_2():
    display_list()
    fruit.pop(-1)  # remove last element
    fruit.extend(fruit)  # multiple by 2
    display_list()

    while True:
        # will keep prompting until valid fruit is entered
        fruit_to_remove = input('enter a fruit to delete ')
        if fruit_to_remove in fruit:
            while fruit_to_remove in fruit:
                fruit.remove(fruit_to_remove)
            display_list()
            break


def series_3():
    print(fruit)
    # go backwards otherwise removing messes up indexes
    for i in range(len(fruit) - 1, -1, -1):
        while True:
            # will loop on same item unless y or n is entered
            answer = input('Do you like {:s}(y/n)? '.format(fruit[i]))
            if answer == 'y':
                print('ok')
                break
            elif answer == 'n':
                print("deleting {:s}".format(fruit[i]))
                fruit.remove(fruit[i])
                break

    print("Remaining Friut\n", fruit)


def series_3_alternate():
    print(fruit)
    temp_fruit = fruit[:]
    # make a copy and delete from that.
    for item in fruit:
        while True:
            # will loop on same item unless y or n is entered
            answer = input('Do you like {:s}(y/n)? '.format(item))
            if answer == 'y':
                print('ok')
                break
            elif answer == 'n':
                print("deleting {:s}".format(item))
                temp_fruit.remove(item)
                break
    print("Remaining Friut\n", temp_fruit)


def series_4():
    print('Before::: ', fruit)
    temp_fruit = fruit[:]
    for index, item in enumerate(fruit):
        temp_fruit[index] = item[::-1]
    print('After::: ', temp_fruit)


# series_1()
# series_2()
series_3()
# series_3_alternate()
series_4()
