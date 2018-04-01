#!/usr/bin/env python3 
def first_series(fruits):
    print()
    print("{:-^80s}".format("First Series"))
    # Call the original list for the user to see
    print("Here is the original list of fruit: {}".format(", ".join(fruits)),end='\n')
    # Insert users input into the list
    fruits.append(input("Enter a new fruit to add to the list:> "))
    print("Here is the new list with the added fruit: {}".format(", ".join(fruits)),end='\n')
    choice = input("Enter a number between 1 and {} to show your item: ".format(len(fruits)))
    if int(choice) <= len(fruits)+1:
        print("Your number was {:d} and the item is: {:s}".format(int(choice), fruits[int(choice)-1]), end='\n')
    else:
        print("Your number> " + choice +" <was not in the listed range...good day Sir!", end='\n')
    print("Adding an additional item to the front of the Fruit List with '+':")
    fruits[:0] += ["Bananas"]
    print(", ".join(fruits),end='\n')
    print("Adding an additional item with the .insert() method.",end='\n')
    fruits.insert(0,"Kiwi")
    print(", ".join(fruits),end='\n')
    print("Displaying all the fruits that begin with 'P':", end='\n')
    for fruit in fruits:
        if 'P' in fruit:
            print(fruit, end=', ')
    print()
    return fruits

def second_series(fruits):
    new_fruit = fruits[:]
    print()
    print("{:-^80s}".format("Second Series"))
    print("The following shows the current fruit list: ", end='\n')
    print(", ".join(new_fruit), end='\n')
    # Pop the last item in the list
    print("Popping the last item in the list, which should be '{}':".format(new_fruit[-1]), end='\n')
    print("Before List: {} ".format(", ".join(new_fruit), end='\n'))
    new_fruit.pop(len(new_fruit) - 1)
    print("After popping list: {} ".format(", ".join(new_fruit), end='\n'))
    # Ask the user for a fruit to delete, find it and remove it.
    choice = input("Please enter a fruit: {} to delete or type 'Q or q' to stop:> ".format(", ".join(new_fruit)))
    # Temp fruit adds a place holder and allows iteration to not be our of sync
    temp_fruit = []
    while True:
        # Create temporary list to original list and deleted fruit
        if choice == 'Q' or choice == 'q':
            break
        for fruit in new_fruit:
            if fruit.lower() != choice.lower():
                temp_fruit.append(fruit)
            else:
                new_fruit.remove(fruit)
        choice = input("Enter another fruit: {} to delete or type 'Q or q' to stop:> ".format(", ".join(new_fruit)))

    print()
    print("Your updated fruit list: {}".format(", ".join(new_fruit)), end='\n')


def third_series(fruits):
    print()
    new_fruit = fruits[:]
    print("{:-^80s}".format("Third Series"))
    print("The original list: {}".format(", ".join(new_fruit)), end='\n')
    # Create temporary list from original fruit list
    # Iterate over the list and prompt user if they like displayed fruit
    for i, fruit in enumerate(new_fruit):
        choice = input("Do you like {}? Type yes/no:> ".format(fruit))
        if choice.lower() == "yes":
            continue
        elif choice.lower() == "no":
            new_fruit[i] = ''
    """
    This in line for loop iterates over the loop and omits the blank elements
    I had to do this because popping the elements above moved n+1 elements to the left
    the for loop would iterate over the item and not present the values in order
    """
    print("The updated fruit list: {}".format(", ".join([fruit for fruit in new_fruit if fruit != ''])), end='\n')

def fourth_series(fruits):
    print()
    print("{:-^80s}".format("Fourth Series"))
    print("The original list: ", end='\n')
    print(", ".join(fruits), end='\n')
    # Using list comprehension to iterate each element in reverse order and assign to new_fruit
    new_fruit = [fruit[::-1] for fruit in fruits]
    # Calling pop without an index automatically deletes the last element
    new_fruit.pop()
    print("The updated list with each element displayed in reverse and the last item removed:")
    print(", ".join(new_fruit),end='\n')

def main():    
    # Create fruit list with global scope
    fruit_list = ["Apples","Pears","Oranges","Peaches"]
    # Call 1st Series
    first_series(fruit_list)
    # Call 2nd Series
    second_series(fruit_list)
    # Call 3rd Series
    third_series(fruit_list)
    # Call 4th Series
    fourth_series(fruit_list)

   
   
if __name__ == "__main__":
    main()