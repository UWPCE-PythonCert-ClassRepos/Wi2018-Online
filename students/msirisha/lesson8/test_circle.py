import unittest
from circle import Circle


class CircleClassUnitTests(unittest.TestCase):
    # step 1 circle radius test
    def test_circle_init(self):
        c = Circle(1)
        self.assertEqual(c.radius, 1)
        c = Circle(4)
        self.assertEqual(Circle(4), c)

    # step 2 circle diameter test
    def test_circle_diameter(self):
        c = Circle(2)
        self.assertEqual(c.diameter, 4.0)
        with self.assertRaises(ValueError):
            c = Circle(-10)

    # step 3 test for diameter property
    def test_circle_set_diameter(self):
        c = Circle(4)
        c.diameter = 8
        self.assertEqual(c.radius, 4.0)
        self.assertEqual(c.diameter, 8.0)
        with self.assertRaises(ValueError):
            c.diameter = -10

    # step 4 test for circle area
    def test_circle_area(self):
        c = Circle(2)
        self.assertEqual(c.area, 12.566370614359172)
        with self.assertRaises(AttributeError):
            c.area = 10

    # step 5 test for circle another constructor
    def test_circle_from_diameter(self):
        c = Circle.from_diameter(4)
        self.assertEqual(c.diameter, 4.0)
        self.assertEqual(c.radius, 2.0)
        with self.assertRaises(ValueError):
            c = Circle.from_diameter(-4)

    # step 6 test for str and repr
    def test_circle_str(self):
        c = Circle(4)
        self.assertEqual(c.__str__(), 'Circle with radius: 4.0')
        self.assertEqual(c.__repr__(), 'Circle(4)')

    # step 7 test for circle addition
    def test_circle_add(self):
        c1 = Circle(2)
        c2 = Circle(4)
        self.assertEqual(c1 + c2, Circle(6))

    # test comparison
    def test_circle_cmp(self):
        c1 = Circle(4)
        c2 = Circle(2)

        self.assertTrue(c1 > c2)
        self.assertFalse(c1 < c2)
        self.assertFalse(c1 == c2)

        c1 = Circle(2)
        c2 = Circle(4)
        self.assertTrue(c1 < c2)
        self.assertFalse(c1 > c2)
        self.assertFalse(c1 == c2)

        c1 = Circle(2)
        c2 = Circle(2)
        self.assertTrue(c1 == c2)

    def test_sort_circles(self):
        clist = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0),
                 Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
        clist.sort()
        self.assertEqual(clist,  [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4),
                                  Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)])

    # test for mul and rmul methods
    def test_circle_mul_rmul(self):
        c1 = Circle(2)
        self.assertEqual(c1 * 3, Circle(6))
        self.assertEqual(3 * c1, Circle(6))

    # test subtraction
    def test_circle_sub(self):
        c1 = Circle(4)
        c2 = Circle(2)
        self.assertEqual(c1 - c2, Circle(2))
        self.assertEqual(c2 - c1, Circle(0))

    # test for true division
    def test_circle_truediv(self):
        c = Circle(4)
        self.assertEqual(Circle(2.0), c / 2)
        with self.assertRaises(ZeroDivisionError):
            print(c / 0)
        with self.assertRaises(ValueError):
            print(c / -2)

    # test for floor division
    def test_circle_floordiv(self):
        c = Circle(4)
        self.assertEqual(Circle(2), c // 2)
        with self.assertRaises(ZeroDivisionError):
            print(c / 0)
        with self.assertRaises(ValueError):
            print(c / -2)

    # test for augmented assignments
    def test_for_augmented_operations(self):
        c1 = Circle(4)
        c2 = Circle(2)

        c1 += c2
        self.assertEqual(Circle(6), c1)
        c1 *= 2
        self.assertEqual(Circle(12), c1)
        c1 /= 2
        self.assertEqual(Circle(6), c1)

    def test_for_reflected_numerics(self):
        c = Circle(3)
        self.assertEqual(c * 3, 3 * c)



if __name__ == "__main__":
    unittest.main()
