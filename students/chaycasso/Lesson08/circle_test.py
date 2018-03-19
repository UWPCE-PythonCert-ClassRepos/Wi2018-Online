#!/usr/bin/env python3
#
# Circle Class Test
# Chay Casso
# 3/19/2018
# Tests the circle class.

import circle_class as cir
import unittest
from math import pi


class CircleTest(unittest.TestCase):

    def test_radius(self):
        c = cir.Circle(4)
        assert c.radius == 4

    def test_diameter(self):
        c = cir.Circle(4)
        assert c.diameter == 8

    def test_set_diameter(self):
        c = cir.Circle(4)
        c.diameter = 2
        assert c.radius == 1

    def test_area(self):
        c = cir.Circle(2)
        assert c.area == 2 * 2 * pi

    def test_from_diameter(self):
        c = cir.Circle.from_diameter(8)
        assert c.radius == 4.0

    def test_str(self):
        c = cir.Circle(4)
        print(c)

    def test_repr(self):
        c = cir.Circle(4)
        assert repr(c) == "Circle(4)"

    def test_add(self):
        c1 = cir.Circle(2)
        c2 = cir.Circle(4)
        c3 = cir.Circle(6)
        assert c1.radius + c2.radius == c3.radius

    def test_multi(self):
        c2 = cir.Circle(4)
        c4 = cir.Circle(12)
        assert c2.radius * 3 == c4.radius
        assert 3 * c2.radius == c4.radius

    def test_gt(self):
        c1 = cir.Circle(2)
        c2 = cir.Circle(4)
        a = c1 > c2
        b = c2 > c1
        assert a == False
        assert b == True

    def test_lt(self):
        c1 = cir.Circle(2)
        c2 = cir.Circle(4)
        a = c1 < c2
        b = c2 < c1
        assert a == True
        assert b == False

    def test_eq(self):
        c1 = cir.Circle(2)
        c2 = cir.Circle(4)
        a = (c1 == c2)
        assert a == False
        c3 = cir.Circle(4)
        b = (c2 == c3)
        assert b == True

    def test_sort(self):
        a = [cir.Circle(6), cir.Circle(7), cir.Circle(8), cir.Circle(4), cir.Circle(0), cir.Circle(2), cir.Circle(3), cir.Circle(5), cir.Circle(9), cir.Circle(1)]
        a.sort()
        assert a == [cir.Circle(0), cir.Circle(1), cir.Circle(2), cir.Circle(3), cir.Circle(4), cir.Circle(5), cir.Circle(6), cir.Circle(7), cir.Circle(8), cir.Circle(9)]


if __name__ == '__main__':
    unittest.main()