#-------------------------------------------------#
# Title: Slicing Lab Exercise
# Dev: Scott Luse
# Date: Feb 4, 2018
#-------------------------------------------------#

# Write some functions that take a sequence as an argument, and return a copy of that sequence:
# with the first and last items exchanged.
# with every other item removed.
# with the first and last 4 items removed, and every other item in between.
# with the elements reversed (just with slicing).
# with the middle third, then last third, then the first third in the new order.

# -- Data --#
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)



# -- Processing --#
def exchange_first_last(seq):
    '''Swap the first and last values of the series and return value'''
    return seq[-1:] + seq[1:-1] + seq[:1]

def test_exchange_first_last():
    '''Tests for exchange first and last'''
    assert exchange_first_last((a_string)) == "ghis is a strint"
    assert exchange_first_last((a_tuple)) == (32, 54, 13, 12, 5, 2)

def remove_every_other(seq):
    '''Remove every other item (step by 2) in the series and return the new series'''
    return seq[0:-1:2]

def first_and_fourth_removed(seq):
    '''Remove first and last 4 items, and every other item in between'''
    # needs work, confirm output
    return seq[1::2]

def elements_reversed(seq):
    '''Reverse the elements and return new series'''
    return seq[::-1]

def middle_third(seq):
    '''with the middle third, then last third, then the first third in the new order.'''
    new_seq = seq[0:3]
    return new_seq[::-1]

# -- Presentation (Input/Output) --#
if __name__ == '__main__':
    test_exchange_first_last()
    print(exchange_first_last(a_string))
    print(exchange_first_last(a_tuple))

    print(remove_every_other(a_string))
    print(remove_every_other(a_tuple))

    print(first_and_fourth_removed(a_string))
    print(first_and_fourth_removed(a_tuple))

    print(elements_reversed(a_string))
    print(elements_reversed(a_tuple))

    print(middle_third(a_string))
    print(middle_third(a_tuple))