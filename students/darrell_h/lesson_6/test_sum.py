#!/usr/local/bin/python3

from sum import sum_double


def test_1():
    assert sum_double(1, 2) == 3


def test_2():
    assert sum_double(5, 4) == 9


def test_3():
    assert sum_double(2, 2) == 8


def test_4():
    assert sum_double(100, 100) == 400
