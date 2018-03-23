# Functions that takes sequence as an argument and returns a copy of seuqence
def exchange_first_last(seq):
    """
    with the first and last items exchanged.
    :param seq: Takes sequence as an argument
    :return: Returns a modified sequence.
    """
    if len(seq) < 2:
        return seq

    return seq[-1:] + seq[1:-1] + seq[:1]

def remove_every_other_item(seq):
    """
    Remove every other item in a given sequence
    :param seq: Takes sequence as an argument
    :return: Returns a modified sequence.
    """
    if len(seq) < 2:
        return seq

    return seq[::2]

def remove_first4_last4_and_every_other_item(seq):
    """
    Remove first four and last four items with every other item removed
    :param seq: Takes sequence as an argument
    :return: Returns a modified sequence
    """
    return remove_every_other_item(seq[4:-4])

def sequence_elements_reversed(seq):
    """
    Reverse the given sequence
    :param seq: Takes sequence as an argument
    :return: Returns the modified sequence
    """
    return seq[::-1]

def sequence_with_thirds_231(seq):
    """
    Returns a sequence with the middle third, then last third, then the first third in the new order.
    If the sequence is not divided up evenly into three parts, then the extra elements in last third i.e will show in the
    middle
    :param seq:  Any type of sequence
    :return: Returns a modified sequence
    """
    third = len(seq) // 3
    return seq[third:] + seq[:third]

if __name__ == "__main__":
    test_set = ['hi sirisha.',[1,2,3,4,5], (1,2,3,4,5), 'something_different']
    exchange_set = ['.i sirishah',[5,2,3,4,1],(5,2,3,4,1),'tomething_differens']
    remove_set = ['h iih.', [1, 3, 5], (1, 3, 5), 'smtigdfeet']
    remove4_set = ['ii', [], (), 'tigdfe']
    reverse_set = ['.ahsiris ih',[5, 4, 3, 2, 1],(5, 4, 3, 2, 1), 'tnereffid_gnihtemos']
    thirds_set = ['sirisha.hi ', [2, 3, 4, 5, 1], (2, 3, 4, 5, 1), 'ing_differentsometh']

    test_functions_result_set = [(exchange_first_last, exchange_set),
                                 (remove_every_other_item, remove_set),
                                 (remove_first4_last4_and_every_other_item, remove4_set),
                                 (sequence_elements_reversed, reverse_set),
                                 (sequence_with_thirds_231, thirds_set)]

    for func, result_set in test_functions_result_set:
        print("Testing function {:s}".format(func.__name__))
        for index, sequence in enumerate(test_set):
            print(func(sequence))
            assert func(sequence) == result_set[index]

