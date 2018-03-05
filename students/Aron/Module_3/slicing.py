#slicing
a_string = "random fruit and veggies"
a_tuple = (8, 9, 12, 0, 23, 88, 1000)

#with the first and last items exchanged.
def exchange_first_last(seq):
    a_new_sequence = seq[0::2]
    return a_new_sequence

#with every other item removed.
def every_other_item(seq):
    a_new_sequence = seq[0::2]
    return a_new_sequence

#with the first and last 4 items removed, and every other item in between.
def first_last_4_every_other_item(seq):
    a_new_sequence = seq[0::2]
    return a_new_sequence

#with the elements reversed (just with slicing).
def items_reversed(seq):
    a_new_sequence = seq[::1]
    return a_new_sequence

#with the middle third, then last third, then the first third in the new order.
def new_order_bythirds(seq):
    one_third=round(len(seq)/3)
    return seq[one_third:-one_third] + seq[-one_third:] + seq[:one_third]
