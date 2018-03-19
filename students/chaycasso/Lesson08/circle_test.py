#!/usr/bin/env python3
#
# Circle Class Test
# Chay Casso
# 3/19/2018
# Tests the circle class.

import circle_class as cir
import unittest


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

if __name__ == '__main__':
    unittest.main()