#!/usr/bin/env python3

# Practice string slicing

def exchange_first_last(seq):
    """First and last items swapped."""
    return seq[-1:] + seq[1:-1] + seq[:1]


def every_other_removed(seq):
    """Remove every other item."""
    return (seq[::2])


def remove_first_last_four(seq):
    """Remove the first four and last four."""
    return seq[4:-4:2]


def elements_reversed(seq):
    """Reversing the elements of a sequence."""
    return seq[::-1]


def changing_thirds(seq):
    """Middle third, then last third, then the first third in the new order"""
    return seq[len(seq) // 3:len(seq) // 3] + seq[:len(seq) // 3] + seq[len(seq) // 3:]


def test_elements_reversed():
    """Testing the function for reversing elements in a sequence"""
    try:
        assert elements_reversed(my_elements) == ['what', ' do', 'you', 'think']
        print("The assertion test passed and all elements of the sequence reversed.")
    except AssertionError:
        print("Your assertion test failed. Look at your function to see what is causing it to fail.")


if __name__ == '__main__':
    # Define the sequences
    my_elements = ['think', 'you', ' do', 'what', 'pretty', 'cool', 'right', 'need', 'more', 'words', 'for', 'testing']
    my_string = "UW Python Certification - Winter 2018"
    my_tuple = ('dog', 'cat', 'lion', 'panda', 'elephant')

    # Test with assert
    assert exchange_first_last(my_string) == "8W Python Certification - Winter 201U"
    assert exchange_first_last(my_tuple) == ('elephant', 'cat', 'lion', 'panda', 'dog')

    assert every_other_removed(my_string) == "U yhnCriiain-Wne 08"
    assert every_other_removed(my_tuple) == ('dog', 'lion', 'elephant')

    assert remove_first_last_four(my_string) == "yhnCriiain-Wne "
    assert remove_first_last_four(my_tuple) == ()
    assert remove_first_last_four(my_elements) == ['pretty', 'right']

    assert elements_reversed(my_string) == "8102 retniW - noitacifitreC nohtyP WU"
    assert elements_reversed(my_tuple) == ('elephant', 'panda', 'lion', 'cat', 'dog')

    assert changing_thirds(my_string) == "UW Python Certification - Winter 2018"
    assert changing_thirds(my_tuple) == ('dog', 'cat', 'lion', 'panda', 'elephant')

    print('All assert tests passed. Commit your work for submission to GitHub')
