import unittest
from io import StringIO

from CircleClass import Circle

class TestCircle(unittest.TestCase):
    
    def test_step1(self):
        c = Circle(4)
        self.assertEqual(c.radius,4)
        
    def test_step2(self):
        c = Circle(4)
        self.assertEqual(c.diameter,8)
        
    def test_step3(self):
        c = Circle(4)
        c.diameter = 2
        self.assertEqual(c.diameter,2)
        self.assertEqual(c.radius,1)
        
    def test_step4(self):
        c = Circle(2)
        print(c.area)
        
    def test_step5(self):
        c = Circle.from_diameter(8)
        self.assertEqual(c.diameter,8)
        self.assertEqual(c.radius,4)
        
    def test_step6(self):
        c = Circle(4)
        print(c)
        print(repr(c))
        eval(repr(c))
        
    def test_step7(self):
        c1 = Circle(2)
        c2 = Circle(4)
        print(c1+c2)
        self.assertEqual(c1+c2, Circle(6))
        c3 = c2*3
        self.assertEqual(c3.radius,12)
        
    def test_test8(self):
        c1 = Circle(2)
        c2 = Circle(4)
        self.assertFalse(c1 > c2)
        self.assertTrue(c2 > c1)
        self.assertTrue(c1 < c2)
        self.assertFalse(c1 == c2)
        c3 = Circle(4)
        self.assertTrue(c2 == c3)
        
        circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), \
                   Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
        circles_sorted = [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4),\
                          Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]
        circles.sort()
        print(circles)
        self.assertTrue(circles == circles_sorted)
        
    def test_test9(self):
        a = Circle(4)
        self.assertTrue(a*3 == 3*a)
        another = Circle(3)
        a += another
        self.assertTrue(a.radius == 7)
        another *= 2
        self.assertTrue(another.radius == 6)
        
if __name__ == '__main__':
    unittest.main()
    