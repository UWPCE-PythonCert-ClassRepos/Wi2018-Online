import math
from unittest import TestCase
from circle import Circle


class TstCircle(TestCase):

    # Test Radius
    def test_radius(self):
        val = Circle(5)
        self.assertEqual(val.radius, 5)

    # Test Diameter
    def test_diameter(self):
        val = Circle(5)
        self.assertEqual(val.diameter, 10)

    # Test changing radius with evaluating diameter value
    def test_change_radius(self):
        c = Circle(5)
        c.radius = 2
        self.assertEqual(c.diameter, 4)

    # Test changing diameter with evaluating radius value
    def test_change_diameter(self):
        c = Circle(5)
        c.diameter = 12
        self.assertEqual(c.radius, 6)

    # Test class circle area method, value should be rounded
    def test_area(self):
        c = Circle(5)
        self.assertEqual(c.area, 79)

    def test_add(self):
        c1 = Circle(3)
        c2 = Circle(4)
        self.assertEqual(c1.radius + c2.radius, 7)

    def test_mul(self):
        c1 = Circle(3)
        c2 = Circle(4)
        self.assertEqual(c1.radius * c2.radius, 12)


if __name__ == 'main':
    TestCase()