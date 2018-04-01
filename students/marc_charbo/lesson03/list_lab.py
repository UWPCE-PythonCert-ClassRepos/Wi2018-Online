#!/usr/bin/env python3

import slicing as slg

def fruit_list(fruits):
    print (fruits[:])
    new_fruit = input('enter a fruit name: ')
    fruits.append(new_fruit)
    print (fruits[:])
    pos_fruit = int(input('enter a number: '))
    print (fruits[pos_fruit-1])
    new_fruit = input('enter another fruit name: ')
    fruits.insert(0,new_fruit)
    print (fruits[:])

    for fruit in fruits:
        if 'P' in fruit:
            print (fruit)
    return fruits

def del_fruit_from_list(fruits):
    print (fruits)
    fruits = fruits[:-1]
    print (fruits)
    del_fruit = input('enter name of fruit you want to delete: ')
    fruits.remove(del_fruit)
    print (fruits)
    return fruits

def query_user(fruits):
    for fruit in fruits:
        answer = input('do you like '+fruit.lower()+'? ')
        prompt = True
        while prompt:
            if answer.lower() == 'no':
                fruits.remove(fruit)
                prompt = False
            elif answer.lower() == 'yes':
                prompt = False
            else:
                answer = input('input only yes or no: ')

def reverse(fruits):
    reverse_fruits = fruits[:]
    for idx, fruit in enumerate(reverse_fruits):
        reverse_fruits[idx] = slg.reversed(fruit)
        print (fruits[idx])
    return reverse_fruits


def main():
    fruits = ['Apples', 'Pears', 'Oranges' ,'Peaches']
    try:
        fruits = fruit_list(fruits)
    except:
        print ('error with series 1')
    try:
        fruits = del_fruit_from_list(fruits)
    except:
        print ('error with series 2')
    try:
        fruits = ['Apples', 'Pears', 'Oranges' ,'Peaches']
        fruits = query_user(fruits)
    except:
        print ('error with series 3')
    try:
        fruits = ['Apples', 'Pears', 'Oranges' ,'Peaches']
        reverse_fruits = reverse(fruits)
        print (fruits)
        print (reverse_fruits)
    except:
        print ('error with series 4')


if __name__ == "__main__":
    main()
