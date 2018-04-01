#!/usr/bin/env python
"""
This module has various functions that slice sequences
"""


def exchange_first_last(seq):
    """
    This function returns the a new sequence with the first and last values
    exchanged and all the other values in original sequence intact.
    :param seq:
    :return: A copy of the seq with the first and last elements swapped
    """
    if len(seq) > 1:
        return seq[-1:] + seq[1:-1] + seq[:1]
    else:
        return seq


def alternate_items_removed(seq):
    """
    Returns a copy of the sequence with the alternate elements
    :param seq: An input sequence
    :return: Copy of sequence with alternate elements
    """
    return seq[::2]


def first_last4_removed(seq):
    """
    Returns a copy of the sequence with first and last elements removed and
    every other element in between
    :param seq: A sequence
    :return: A new sequence with elements as described
    """
    return seq[4:-4:2]


def reversed_seq(seq):
    """
    This method returns a copy of an input sequence with elements from the
    original sequence in reversed order
    :param seq: A sequence
    :return: Reversed sequence
    """
    return seq[::-1]


def thirds_sequence(seq):
    """
    This method returns a copy of an input sequence with the middle third,
    last third, then the first third elements in that order
    :param seq: A sequence
    :return: Copy sequence
    """
    one_third_len = int(len(seq) / 3)
    return seq[one_third_len: (2 * one_third_len)] + seq[(2 * one_third_len):]\
        + seq[:one_third_len]

if __name__ == '__main__':
    # Tests to verify exchange_first_last method on strings
    assert exchange_first_last('') == ''
    assert exchange_first_last('a') == 'a'
    assert exchange_first_last('ab') == 'ba'
    assert exchange_first_last('abc') == 'cba'

    # Tests to verify exchange_first_last method on lists
    assert exchange_first_last([]) == []
    assert exchange_first_last([1]) == [1]
    assert exchange_first_last([1,2]) == [2,1]
    assert exchange_first_last([4, 3, 2]) == [2, 3, 4]

    assert alternate_items_removed([]) == []
    assert alternate_items_removed([1]) == [1]
    assert alternate_items_removed([1,2]) == [1]
    assert alternate_items_removed([2,3,4]) == [2, 4]

    assert first_last4_removed('') == ''
    assert first_last4_removed([1]) == []
    assert first_last4_removed([1, 2]) == []
    assert first_last4_removed([2, 3, 4]) == []
    assert first_last4_removed([2, 3, 4, 5]) == []
    assert first_last4_removed([2, 3, 4, 5, 6]) == []
    assert first_last4_removed([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [5, 7]
    assert first_last4_removed("Great Fun!") == 't'

    assert reversed_seq('noon') == 'noon'
    assert reversed_seq([]) == []
    assert reversed_seq((1, 2, 3)) == (3, 2, 1)

    assert thirds_sequence([1, 2, 3, 4, 5, 6]) == [3, 4, 5, 6, 1, 2]
    assert thirds_sequence([1, 2, 3]) == [2, 3, 1]
    assert thirds_sequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [4, 5, 6, 7, 8,
                                                        9, 10, 1, 2, 3]





