# -----------------------------------------------------------
# slicing_lab.py
#  functions that take sequences and return modified copies
# -----------------------------------------------------------


def exchange_first_last(seq):
    """
    Take a sequence and return a copy with the first and last items exchanged.
    :param seq: a sequence of items
    :return: seq with first/last items exchanged
    """

    if len(seq) < 2:
        return seq

    return seq[-1:] + seq[1:-1] + seq[:1]


def remove_every_other_item(seq):
    """
    Remove every other item in the seq.
    :param seq: a sequence of items
    :return: seq with every other item removed
    """
    if len(seq) < 2:
        return seq

    return seq[::2]


def remove_first4_last4_every_other(seq):
    """
    Remove first 4 items & last 4 items, and every other item in between
    :param seq: a sequence of items
    :return: seq with first 4, last 4 removed and every other item remaining removed
    """
    return remove_every_other_item(seq[4:-4])


def reorder_by_thirds_231(seq):
    """
    Reorder with middle third, last third, then first third. If the sequence does not
    divide evenly, the remaining items are placed with the 'last third' section - i.e. they
    will show up in the middle of the returned sequence.
    :param seq: a sequence of items
    :return: seq in the order of middle third, last third (plus remainders), first third
    """
    third = len(seq) // 3
    return seq[third:] + seq[:third]


def reverse(seq):
    """
    Reverse the given sequence.
    :param seq: a sequence of items
    :return: seq with elements in reverse order
    """
    return seq[::-1]


if __name__ == "__main__":
    test_set = ['The quick brown fox jumped over the lazy dog.',
                [0, 1, 2, 3, 4, 5],
                (0, 1, 2, 3, 4, 5),
                'alphabet_soup',
                ]

    exch_set = ['.he quick brown fox jumped over the lazy dogT',
                [5, 1, 2, 3, 4, 0],
                (5, 1, 2, 3, 4, 0),
                'plphabet_soua',
                ]

    remove_set = ['Teqikbonfxjme vrtelz o.',
                  [0, 2, 4],
                  (0, 2, 4),
                  'apae_op',
                  ]

    remove4_set = ['qikbonfxjme vrtelz ',
                   [],
                   (),
                   'ae_',
                   ]

    reverse_set = ['.god yzal eht revo depmuj xof nworb kciuq ehT',
                   [5, 4, 3, 2, 1, 0],
                   (5, 4, 3, 2, 1, 0),
                   'puos_tebahpla',
                   ]

    bythirds_set = [' fox jumped over the lazy dog.The quick brown',
                    [2, 3, 4, 5, 0, 1],
                    (2, 3, 4, 5, 0, 1),
                    'abet_soupalph'
                    ]

    test_functions = [(exchange_first_last, exch_set),
                      (remove_every_other_item, remove_set),
                      (remove_first4_last4_every_other, remove4_set),
                      (reverse, reverse_set),
                      (reorder_by_thirds_231, bythirds_set)
                      ]

    for func, result_set in test_functions:
        print("Testing {:s}".format(func.__name__))
        for index, test in enumerate(test_set):
            print(func(test))
            assert func(test) == result_set[index]
