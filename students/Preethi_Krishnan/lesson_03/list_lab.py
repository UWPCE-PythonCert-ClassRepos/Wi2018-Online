#!/usr/bin/env python3
import copy

def series_1_list(a):
    """This function takes user input as a list
     displays the list
     add a fruit from user input to end of the list
     display new list
     ask user input for number and display fruit in the corresponding to that number in list
     add fruit using + to the beginning of list
     add fruit using insert to the beginning of list
     display all fruits beginning with P or p"""
    new_list = a
    print ("Current fruit list is: {}".format(new_list))
    new_item = raw_input("Please enter a fruit name that needs to be added to current list")
    print new_item
    new_list.append(new_item)
    print ("New list after user input {}".format(new_list))
    len_list = len(new_list)
    index_value = int(input("Enter a number between 1 to {}".format(len_list)))
    if((index_value >= 1) and (index_value <= len_list)):
        print("This is the fruit {} corresponding to requested {} number in list".format(new_list[index_value - 1], index_value))
    else:
        print("You did not enter the number in the range.. Please enter..")
        if ((index_value >= 1) and (index_value <= len_list)):
            print("This is the fruit {} corresponding to requested {} number in list".format(new_list[index_value - 1], index_value))
    new_list = ["Pears"] + new_list
    new_list.insert(0, "Pomes")
    print("This is the new list: {}".format(new_list))
    p_list = []
    for i in new_list:
        if((i[0] == "p") or (i[0] == "P")):
            p_list.append(i)
    print ("Element/Elements containing letter P or p first in the list are: {}".format(p_list))
    return new_list

def series_2_list(a):
    "Get the list from series 1, remove last fruit and display. Ask user to delete fruit"
    if not a:
        new_list_2 = series_1_list(["Apple", "Orange", "Mango", "Peaches"])
    else:
        new_list_2 = a
    print("This is the list for series 2: {}".format(new_list_2))
    new_list_2.pop()
    print("This is the list after popping last element:{}".format(new_list_2))
    response = raw_input("Do you want to delete a fruit from the list above?Y/N")
    while(("Y" in response) and (len(new_list_2) > 0)):
        fruit_delete = raw_input("Please input a fruit name to delete to delete from {}".format(new_list_2))
        if fruit_delete in new_list_2:
            #new_list_2.remove(fruit_delete)
            new_list_2[:] = (value for value in new_list_2 if value != fruit_delete)
        else:
            fruit_delete = raw_input("Please input a fruit name to delete to delete from {}".format(new_list_2))
            if fruit_delete in new_list_2:
                #new_list_2.remove(fruit_delete)
                new_list_2[:] = (value for value in new_list_2 if value != fruit_delete)
        if (len(new_list_2) >= 1):
            response = raw_input("Do you want to continue deleting?Y/N")
        else:
            print("All items removed...")
            response = "N"
    else:
        print("The input is unrecognized or you answered No for deletion.. Exiting..")

    print("The list items after all removals: {}".format(new_list_2))
    return new_list_2

def series_3_list(a):
    new_list_3 = []
    for fruit in a:
        response = raw_input("Do you like {}".format(fruit))
        if(response in "Y"):
            new_list_3.append(fruit)
        if(response not in "Y" and response not in "N"):
            response = raw_input("Please enter Y or N.. Do you like {}".format(fruit))
            if(response in "Y"):
                new_list_3.append(fruit)
    print("This is the list of fruits you like: {}".format(new_list_3))
    return(new_list_3)

def series_4_list(a):
    new_list_4 = copy.deepcopy(a)
    for fruit in new_list_4:
        i = new_list_4.index(fruit)
        fruit1 = fruit[::-1]
        new_list_4[i] = fruit1
    print new_list_4
    print a

s = series_1_list(["Apple", "Orange", "Mango", "Peaches"])
series_2_list(s)
series_3_list(s)
series_4_list(s)


