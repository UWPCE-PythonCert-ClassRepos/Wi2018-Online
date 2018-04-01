"""
Lesson 08 Assignment Simple Circle - unit test
"""

import unittest
from math import pi
from circle import Circle


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def test_radius_init(self):
        """ test initialize radius """
        c = Circle(4)
        self.assertEqual(c.radius, 4)

    def test_diameter_get_property(self):
        """ test get diameter property """
        c = Circle(4)
        self.assertEqual(c.diameter, 8)

    def test_diameter_set_property(self):
        """ test set diameter property """
        c = Circle(4)
        c.diameter = 2
        self.assertEqual(c.diameter, 2)
        self.assertEqual(c.radius, 1)

    def test_area_get_property(self):
        """ test get area property """
        c = Circle(2)
        self.assertEqual(c.area, pi * pow(2, 2))

    def test_set_area_AttributeError(self):
        """ test user should not be able to set the area"""
        c = Circle(2)
        with self.assertRaises(AttributeError) as e:
            c.area = 32
        self.assertIn(str(e.exception), "can't set attribute")

    def test_circle_from_diameter(self):
        """ test create a Circle directly with the diameter"""
        c = Circle.from_diameter(8)
        self.assertEqual(c.diameter, 8)
        self.assertEqual(c.radius, 4)

    def test__str__method(self):
        c = Circle(4)
        self.assertEqual(str(c), "Circle with radius: 4")

    def test__repr__method(self):
        c = Circle(4)
        self.assertEqual(repr(c), "Circle(4)")

    def test_adding_circles(self):
        c1 = Circle(2)
        c2 = Circle(4)
        c = c1 + c2
        self.assertEqual(repr(c), "Circle(6)")

    def test_multiply_circle(self):
        c1 = Circle(4)
        c = c1 * 2
        self.assertEqual(repr(c), "Circle(8)")

    def test_augmented_multiply(self):
        c1 = Circle(3)
        c1 *= 5
        self.assertEqual(repr(c1), "Circle(15)")

    def test_reverse_multiply(self):
        c1 = Circle(3)
        c2 = 3 * c1
        self.assertEqual(repr(c2), "Circle(9)")

    def test_equal(self):
        c1 = Circle(1)
        c2 = Circle(1)
        self.assertEqual(c1, c2)

    def test_not_equal(self):
        c1 = Circle(2)
        c2 = Circle(1)
        self.assertNotEqual(c1, c2)

    def test_greater_than(self):
        c1 = Circle(2)
        c2 = Circle(1)
        self.assertGreater(c1, c2)

    def test_less_than(self):
        c1 = Circle(2)
        c2 = Circle(1)
        self.assertLess(c2, c1)


if __name__ == '__main__':
    unittest.main()
