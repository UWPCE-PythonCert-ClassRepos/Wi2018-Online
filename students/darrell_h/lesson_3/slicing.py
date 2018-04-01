#!/usr/local/bin/python3

str = 'abcdefghijklmnopqrstuvwxyz'
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]


print("\nexhange first and last item...")
print(exchange_first_last(str))
print(exchange_first_last(list))


def every_other_item_removed(seq):
    return seq[0:-1:2]


print("\nprint every other item...")
print(every_other_item_removed(str))
print(every_other_item_removed(list))


def first_and_last_4_items_removed_and_every_other_item_in_between(seq):
    return seq[4:-4:2]


print("\nprint every other item...")
print(first_and_last_4_items_removed_and_every_other_item_in_between(str))
print(first_and_last_4_items_removed_and_every_other_item_in_between(list))


def reversed_items(seq):
    # step through backwards
    return seq[::-1]


print("\nreversed items...")
print(reversed_items(str))
print(reversed_items(list))


def middle_third_last_third_first_third(seq):
    one_third = round(len(seq)/3)
    return seq[one_third:-one_third] + seq[-one_third:] + seq[:one_third]


print("\nprint middle, end and first third...")
print(middle_third_last_third_first_third(str))
print(middle_third_last_third_first_third(list))
