#!/usr/bin/python3
#Shayna Anderson-Hill
#Goal: Get the basics of sequence slicing down.
#02-10-2018


def exchange_first_last(seq):
    '''Returns a sequence with the first and last items exchanged.'''
    first = seq[0:1]
    last = seq[-1:]
    middle = seq[1:-1]
    a_new_sequence = last + middle + first
    return a_new_sequence

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

def remove_every_other(seq):
    '''Returns a sequence with every other item removed.'''
    a_new_sequence = seq[0:len(seq):2]
    return a_new_sequence

string1 = "hi my name is shayna"
tuple1 = (1, 2, 3, 4, 5, 6, 7)

assert remove_every_other(string1) == "h ynm ssan"
assert remove_every_other(tuple1) == (1, 3, 5, 7)

def remove_every_other_special(seq):
    '''Returns a sequence with the first and last 4 items removed, and
    every other item in between.'''
    a_new_sequence = seq[4:-4:2]
    return a_new_sequence

long_string = "abcdefghijklmnopqrstuvwxyz"
tuple2 = tuple1 + tuple1 + tuple1

assert remove_every_other_special(long_string) == "egikmoqsu"
assert remove_every_other_special(tuple2) == (5, 7, 2, 4, 6, 1, 3)

def reverse(seq):
    '''Returns a sequence with the elements reversed '''
    a_new_sequence = seq[::-1]
    return a_new_sequence

assert reverse(long_string) == "zyxwvutsrqponmlkjihgfedcba"
assert reverse(tuple1) == (7, 6, 5, 4, 3, 2, 1)

def thirds(seq):
    '''Returns a sequence with the middle third, then last third, then
    the first third in the new order.'''
    cut = int(len(seq)/3)
    first_third = seq[0:cut]
    rest = seq[cut:] #last two-thirds
    a_new_sequence =  rest[:] + first_third[:]
    return a_new_sequence

assert thirds(a_string) == "is a stringthis "
assert thirds(a_tuple) == (13, 12, 5, 32, 2, 54)

