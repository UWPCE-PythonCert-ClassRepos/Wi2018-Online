"""Lesson03 - Assignment 1 - Sequence slicing."""


def exchange_first_last(seq):
    """Return a copy of seq with the 1st and last items exchanged."""
    return seq[-1:] + seq[1:-1] + seq[0:1]


def remove_every_other(seq):
    """Return a copy of seq with every other item removed."""
    return seq[::2]


def remove_first_last_4_and_every_other(seq):
    """Return a copy of seq with the first and last 4 items removed.

    Also removes  every other item in between.
    """
    return seq[4:-4:2]


def reverse_elements(seq):
    """Return a copy of seq with the elements reversed (just with slicing)."""
    return seq[::-1]


def reorder_middle_last_first(seq):
    """Return a copy of seq with the first third moved to the back."""
    cut_point = len(seq) // 3
    return seq[cut_point:] + seq[:cut_point]


# TESTING SECTION

def test_exchange_first_last():
    """Test the exchange_first_last function."""
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)


def test_remove_every_other():
    """Test the remove_every_other function."""
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13, 5)


def test_remove_first_last_4_and_every_other():
    """Test the remove_first_last_4_and_every_other function."""
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32, 17, 55, 31, 1, 57, 21, 8)

    assert remove_first_last_4_and_every_other(a_string) == " sas"
    assert remove_first_last_4_and_every_other(a_tuple) == (5, 17, 31)


def test_reverse_elements():
    """Test the reverse_elements function."""
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    assert reverse_elements(a_string) == 'gnirts a si siht'
    assert reverse_elements(a_tuple) == (32, 5, 12, 13, 54, 2)


def test_reorder_middle_last_first():
    """Test the reorder_middle_last_first function."""
    a_string = "this is a string"
    a_tuple = (1, 2, 3)
    a_tuple_2 = (1, 2, 3, 4)
    a_tuple_3 = (1, 2, 3, 4, 5)
    a_tuple_4 = (1, 2, 3, 4, 5, 6)
    assert reorder_middle_last_first(a_string) == "is a stringthis "
    assert reorder_middle_last_first(a_tuple) == (2, 3, 1)
    assert reorder_middle_last_first(a_tuple_2) == (2, 3, 4, 1)
    assert reorder_middle_last_first(a_tuple_3) == (2, 3, 4, 5, 1)
    assert reorder_middle_last_first(a_tuple_4) == (3, 4, 5, 6, 1, 2)


def run_tests():
    """Run all tests."""
    test_exchange_first_last()
    test_remove_every_other()
    test_remove_first_last_4_and_every_other()
    test_reverse_elements()
    test_reorder_middle_last_first()


if __name__ == '__main__':
    run_tests()
