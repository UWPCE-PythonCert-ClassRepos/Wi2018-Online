import unittest
import circle as MOc

class MyTest(unittest.TestCase):
    # Step 1
    def test_init(self):
        c = MOc.Circle(4)
        self.assertEqual(c.radius, 4)

    # Step 2
    def test_dia(self):
        c = MOc.Circle(4)
        self.assertEqual(c.diameter, 8)

    # Step 3
    def test_diaIN(self):
        c = MOc.Circle(4)
        c.diameter = 2
        self.assertEqual(c.diameter, 2)
        self.assertEqual(c.radius, 1)

    # Step 4
    def test_area(self):
        c = MOc.Circle(2)
        self.assertEqual(c.area, c.PI * c.radius ** 2)
        with self.assertRaises(AttributeError):
            c.area = 5

    # Step 5
    def test_from_dia(self):
        c = MOc.Circle.from_diameter(8)
        self.assertEqual(c.radius, 8 / 2)

    # Step 6
    def test_StrRepr(self):
        c = MOc.Circle(4)
        self.assertEqual(c.__str__(), "Circle with radius: 4.000000")
        self.assertEqual(c.__repr__(), "Circle(4)")

    def test_math(self):
        c1 = MOc.Circle(2)
        c2 = MOc.Circle(4)

        # add 2 classes
        self.assertEqual((c1 + c2).radius, MOc.Circle(6).radius)
        # add class + int
        self.assertEqual((c1 + 4).radius, MOc.Circle(6).radius)
        # add int + class
        self.assertEqual((2 + c2).radius, MOc.Circle(6).radius)

        # mult 2 classes
        self.assertEqual((c1 * c2).radius, MOc.Circle(8).radius)
        # mult class + int
        self.assertEqual((c1 * 4).radius, MOc.Circle(8).radius)
        # mult int + class
        self.assertEqual((2 * c2).radius, MOc.Circle(8).radius)

        # doing math with anything other than int should error out
        with self.assertRaises(TypeError):
            c1 + "try me"

    def test_comparing(self):
        c1 = MOc.Circle(2)
        c2 = MOc.Circle(4)

        self.assertTrue(c1 < c2)
        self.assertFalse(c1 > c2)
        self.assertFalse(c1 == c2)



if __name__ == "__main__":
    unittest.main()
