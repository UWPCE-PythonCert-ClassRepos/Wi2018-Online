"""
Lesson 03
Slicing Lab Exercise
"""

def exchange_first_last(seq):
    """
    Take a sequence as an argument, and return a copy of that sequence
    with the first and last items exchanged
    :param seq: input sequence
    :return: copy of the sequence
    """
    a_new_sequence = seq[-1:] + seq[1:-1] + seq[:1]
    return a_new_sequence


def remove_every_other_item(seq):
    """
    Take a sequence as an argument, and return a copy of that sequence
    with every other item remove
    :param seq: input sequence
    :return: copy of the sequence
    """
    a_new_sequence = seq[::2]
    return a_new_sequence


def remove_items(seq):
    """
    Take a sequence as an argument, and return a copy of that sequence
    with the first and last 4 items removed, and every other item in between.
    :param seq: input sequence
    :return: copy of the sequence
    """
    a_new_sequence = seq[4:-4:2]
    return a_new_sequence


def change_item_order(seq):
    """
    Take a sequence as an argument, and return a copy of that sequence
    with the middle third, then last third, then the first third in the new order.
    :param seq: input sequence
    :return: copy of the sequence
    """
    third_len = len(seq)//3
    print(third_len)
    first_third  = seq[:third_len]
    middle_third = seq[third_len:-third_len]
    last_third   = seq[-third_len:]
    a_new_sequence = middle_third + last_third + first_third
    return a_new_sequence


if __name__ == "__main__":

    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    # test  exchange_first_last()
    print(exchange_first_last(a_tuple))
    print(exchange_first_last(a_string))
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert exchange_first_last(a_string) == "ghis is a strint"

    # test remove_every_other_item()
    print(remove_every_other_item(a_tuple))
    print(remove_every_other_item(a_string))
    assert remove_every_other_item(a_tuple) == (2, 13, 5)
    assert remove_every_other_item(a_string) == "ti sasrn"

    another_tuple = (2, 54, 13, 12, 5, 32, 21, 45, 56, 75, 30, 49, 95, 82, 18)

    # test remove_items()
    print(remove_items(another_tuple))
    assert remove_items(another_tuple) == (5, 21, 56, 30)

    # test change_item_order()
    print(change_item_order(another_tuple))
    assert  change_item_order(another_tuple) == (32, 21, 45, 56, 75, 30, 49, 95, 82, 18, 2, 54, 13, 12, 5)


