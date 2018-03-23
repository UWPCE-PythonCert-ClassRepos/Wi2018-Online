#!/usr/bin/env python3

from unittest import TestCase
from circle import Circle

class CircleTest(TestCase):
    def test_radius(self):
        cr = Circle(4)
        self.assertEqual(cr.radius, 4)

    def test_diameter(self):
        cr = Circle(4)
        self.assertEqual(cr.diameter, 8)

    def test_set_diameter(self):
        cr = Circle(4)
        cr.diameter=4
        self.assertEqual(cr.radius, 2)

    def test_area(self):
        cr = Circle(2)
        self.assertAlmostEqual(cr.area, 12.566370,places=4)

    def test_print_obj(self):
        cr = Circle(2)
        print(cr)
        # self.assertEqual(print(cr), 'test')

    def test_print_obj(self):
        cr = Circle(2)
        print(repr(cr))

    def test_add(self):
        cr = Circle(2)
        cr2 = Circle(4)
        cr3 = Circle(6)
        self.assertEqual(cr.radius+cr2.radius,6)

    def test_multiply(self):
        cr = Circle(2)
        self.assertEqual(cr.radius*3,6)

    def test_lt(self):
        cr = Circle(2)
        cr2 = Circle(4)
        #self.assertLess(cr,cr2) # could also use this test
        self.assertTrue(cr < cr2)

    def test_lt(self):
        cr = Circle(2)
        cr2 = Circle(4)
        #self.assertLess(cr,cr2) # could also use this test
        self.assertTrue(cr < cr2)

    def test_gt(self):
        cr = Circle(10)
        cr2 = Circle(9)
        self.assertTrue(cr > cr2)

    def test_eq(self):
        cr = Circle(11)
        cr2 = Circle(11)
        self.assertTrue(cr == cr2)

    def test_ne(self):
        cr = Circle(10)
        cr2 = Circle(1)
        self.assertTrue(cr != cr2)