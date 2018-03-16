#!/usr/bin/env python3
# -----------------------------------------------------------
# test_circle_class.py
#  uses unittest module to test Circle class module
# -----------------------------------------------------------


import unittest
from io import StringIO
from contextlib import redirect_stdout
from circle_class import Circle

class CircleClassTest(unittest.TestCase):

    def test_circle_init(self):
        c = Circle()
        self.assertEqual(c.radius, 1)
        c = Circle(4)
        self.assertEqual(c.radius, 4)
        with self.assertRaises(TypeError):
            c = Circle(-100)
        self.assertEqual(Circle(4), c)

    def test_diameter(self):
        c = Circle()
        self.assertEqual(c.diameter, 2)
        c = Circle(4)
        self.assertEqual(c.diameter, 8)

    def test_set_diameter(self):
        c = Circle(4)
        c.diameter = 2
        self.assertEqual(c.diameter, 2)
        self.assertEqual(c.radius, 1)
        with self.assertRaises(ValueError):
            c.diameter = -100

    def test_get_area(self):
        c = Circle(2)
        self.assertAlmostEqual(c.area, 12.5663706, places=7)
        with self.assertRaises(AttributeError):
            c.area = 13

    def test_from_diameter(self):
        c = Circle.from_diameter(8)
        self.assertEqual(c.diameter, 8)
        self.assertEqual(c.radius, 4)
        self.assertEqual(Circle(1.0), Circle.from_diameter())
        with self.assertRaises(ValueError):
            Circle.from_diameter(-100)

    def test_str_method(self):
        c = Circle()
        f = StringIO()
        with redirect_stdout(f):
            print(c)
        self.assertIn("Circle with radius: 1.", f.getvalue())

    def test_repr_method(self):
        c = Circle()
        self.assertEqual("Circle(1.0)", repr(c))
        d = eval(repr(c))
        self.assertEqual(c.radius, d.radius)


    def test_two_circle_add(self):
        c = Circle(2)
        d = Circle(4)
        self.assertEqual(6, (c + d).radius)
        self.assertEqual(12, (c + d).diameter)
        with self.assertRaises(TypeError):
            d = c + 'Square'

    def test_circle_mul(self):
        c = Circle(3)
        self.assertEqual(9, (c * 3).radius)     # Test __mul__
        with self.assertRaises(TypeError):
            d = c * 'monkey'
        self.assertEqual(9, (3 * c).radius)     # Test __rmul__
        self.assertAlmostEqual(9.00, (3.0 * c).radius, places=2)

    def test_lt_oper(self):
        c = Circle(0)
        d = Circle(2)
        self.assertEqual(True, c < d)
        self.assertEqual(True, d > c)
        self.assertEqual(False, c == d)
        c = eval(repr(d))
        self.assertEqual(False, c < d)
        self.assertEqual(False, d > c)
        self.assertEqual(True, c == d)

        with self.assertRaises(TypeError):
            print(c == 'monkey')
        with self.assertRaises(TypeError):
            print(c < 'monkey')


    def test_sort_circles(self):
        cl = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0),
              Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
        cl.sort()
        self.assertEqual(cl,
                         [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4),
                          Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]
                         )

    def test_reflected_numerics(self):
        a = Circle(4)
        self.assertTrue(a * 3 == 3 * a)

    def test_augmented_assignment(self):
        a = Circle(4)
        b = Circle(2)
        a += b
        self.assertEqual(Circle(6), a)

        a *= 2
        self.assertEqual(Circle(12), a)

        a /= 2
        self.assertEqual(Circle(6), a)

    def test_sub_circles(self):
        a = Circle(4)
        b = Circle(2)
        self.assertEqual(Circle(2), a - b)
        self.assertEqual(Circle(0), b - a)

    def test_div_circles(self):
        a = Circle(10)
        self.assertEqual(Circle(5), a / 2)
        with self.assertRaises(ZeroDivisionError):
            print(a / 0)
        with self.assertRaises(ValueError):
            print(a / -2)

    def test_floor_div_circles(self):
        a = Circle(9)
        self.assertEqual(Circle(4), a // 2)
        with self.assertRaises(ZeroDivisionError):
            print(a // 0)
        with self.assertRaises(ValueError):
            print(a // -2)
