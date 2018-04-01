#!/usr/bin/env python3

import sys

def exchange_first_last(seq):
    a_new_sequence = seq[:]
    a_new_sequence = a_new_sequence[-1:] + a_new_sequence[1:-1] + a_new_sequence[:1]
    return a_new_sequence

def every_other_item_removed(seq):
    a_new_sequence = seq[:]
    a_new_sequence = a_new_sequence[::2]
    return a_new_sequence

def first_last_four_items_removed(seq):
    a_new_sequence = seq[:]
    a_new_sequence = a_new_sequence[1:-4]
    a_new_sequence = every_other_item_removed(a_new_sequence) 
    return a_new_sequence

def reversed(seq):
    a_new_sequence = seq[::-1]
    return a_new_sequence

def thirds(seq):
    a_new_sequence = seq[:]
    one_third = int((len(a_new_sequence) / 3))
    two_third = int(2*one_third)
    a_new_sequence = a_new_sequence[one_third:two_third] + a_new_sequence[two_third:] + a_new_sequence[:one_third]
    return a_new_sequence

def main():
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32,99,1,6,65,34,7,0)
    try:
        print("first and last items exchanged")
        print (exchange_first_last(a_string))
        print("done \n")

    except:
        print ("error first and last items exchanged")

    try:
        print("every other item removed")
        print (every_other_item_removed(a_string))
        print("done \n")
    except:
        print ("error every other item removed")

    try:
        print("first and last 4 items removed, and every other item in between")
        print (first_last_four_items_removed(a_string))
        print("done \n")
    except:
        print ("first and last 4 items removed, and every other item in between")

    try:
        print("elements reversed ")
        print (reversed(a_string))
        print("done \n")
    except:
        print ("error elements reversed")

    try:
        print("middle third, then last third, then the first third in the new order")
        print (thirds(a_string))
        print("done \n")
    except:
        print ("error middle third, then last third, then the first third in the new order")

if __name__ == "__main__":
    main()