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

    def test_add(self):
        cr = Circle(2)
        self.assertEqual(cr.radius*3,6)
