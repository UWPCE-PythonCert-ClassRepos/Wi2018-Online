#!/usr/local/bin/python3

import parrot


#  No need to do == True.
def test_1():
    assert parrot.parrot_trouble(True, 6)


#  use not to test for false rather than == False.
def test_2():
    assert not parrot.parrot_trouble(True, 7)


def test_3():
    assert not parrot.parrot_trouble(False, 6)


def test_4():
    assert parrot.parrot_trouble(True, 21)


def test_5():
    assert not parrot.parrot_trouble(True, 20)
