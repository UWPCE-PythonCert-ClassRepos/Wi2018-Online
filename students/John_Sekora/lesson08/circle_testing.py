from unittest import TestCase
from circle import Circle


class TestCircle(TestCase):

    def test_radius(self):
        c = Circle(2)
        self.assertEqual(c.radius, 2)

    def test_diameter(self):
        c = Circle(2)
        self.assertEqual(c.diameter, 4)

    def test_area(self):
        c = Circle(2)
        self.assertEqual(c.area, 13)

    def test_create_diameter(self):
        c = Circle(2)
        c.diameter = 10
        self.assertEqual(c.radius, 5)
        self.assertEqual(c.diameter, 10)
        self.assertEqual(c.area, 79)

    def test_add(self):
        c1 = Circle(2)
        c2 = Circle(3)
        self.assertEqual(c1.radius + c2.radius, 5)
        self.assertEqual(c1.diameter + c2.diameter, 10)
        self.assertEqual(c1.area + c2.area, 41)

    def test_sub(self):
        c1 = Circle(7)
        c2 = Circle(4)
        self.assertEqual(c1.radius - c2.radius, 3)
        self.assertEqual(c1.diameter - c2.diameter, 6)
        self.assertEqual(c1.area - c2.area, 104)

    def test_mul(self):
        c1 = Circle(7)
        c2 = Circle(4)
        self.assertEqual(c1.radius * c2.radius, 28)
        self.assertEqual(c1.diameter * c2.diameter, 112)
        self.assertEqual(c1.area * c2.area, 7700)

    def test_gt_lt_eq(self):
        c1 = Circle(7)
        c2 = Circle(4)
        self.assertEqual(c1 > c2, True)
        self.assertEqual(c1 < c2, False)
        self.assertEqual(c1 == c2, False)

    def test_sort_circles(self):
        cl = [Circle(5), Circle(9), Circle(8), Circle(7), Circle(1),
              Circle(6), Circle(2), Circle(3), Circle(4), Circle(0)]
        cl.sort()
        self.assertEqual(cl,
                         [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4),
                          Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]
                         )


if __name__ == 'main':

    TestCase()


