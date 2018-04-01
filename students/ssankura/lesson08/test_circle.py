import unittest
import io
import sys 

from circle import Circle

class TestCircle(unittest.TestCase):
    
    def test_step1_circle_init(self):
        c = Circle(4)
        self.assertEqual(c.radius,4)
        
    def test_step2_diameter(self):
        c = Circle(5)
        self.assertEqual(c.radius,5)
        self.assertEqual(c.diameter,10)
        
    def test_step3_set_diameter(self):
        c = Circle(5)
        self.assertEqual(c.radius,5)
        c.diameter = 20
        self.assertEqual(c.diameter,20)
        self.assertEqual(c.radius,10)
        
    def test_step4_area(self):
        c = Circle(10)
        self.assertEqual(c.radius,10)
        self.assertEqual(c.area,314.1592653589793)

    def test_step4_area_attribute_error(self):
        c1 = Circle(10)
        self.assertEqual(c1.area, 314.1592653589793)
        with self.assertRaises(AttributeError):
            c1.area = 42

    def test_step5_ctor_from_diameter(self):
        c = Circle.from_diameter(8)
        self.assertEqual(c.diameter,8)
        self.assertEqual(c.radius,4)

    def test_step6_str_circle(self):
        c1 = Circle(10)
        expected_output = "Circle [Radius = 10.0000, Diameter = 20.0000, Area = 314.1593, Perimeter = 62.8319]"
        #[Radius = 10.0000, Diameter = 20.0000, Area = 314.1592653589793, Perimeter = 62.8319]"
        capturedOutput = io.StringIO()  
        sys.stdout = capturedOutput
        print(c1)
        sys.stdout = sys.__stdout__ 
        self.assertEqual(capturedOutput.getvalue().strip(), expected_output.strip())

    def test_step6_repr_circle(self):
        c1 = Circle(5)
        expected_output = "Circle(5)"
        capturedOutput = io.StringIO()  
        sys.stdout = capturedOutput
        print(repr(c1))
        sys.stdout = sys.__stdout__ 
        self.assertEqual(capturedOutput.getvalue().strip(), expected_output.strip())
        d = eval(repr(c1))
        self.assertEqual(c1.radius,d.radius)
        
    def test_step7_circles_add(self):
        c1 = Circle(2)
        c2 = Circle(4)
        print(c1+c2)
        self.assertEqual((c1+c2).radius, 6)
        self.assertEqual((c1+c2).diameter, 12)

    def test_step7_circle_multiply(self):
        c1 = Circle(5)
        c2 = c1*3
        self.assertEqual(c2.radius,15)
        
    def test_step8_compare_circles(self):
        c1 = Circle(2)
        c2 = Circle(4)
        self.assertEqual(True, c1 < c2)
        self.assertEqual(True, c2 > c1)
        self.assertEqual(False, c1 == c2)

        c3 = Circle(4)
        self.assertEqual(True,c2 == c3)
    
    def test_step8_sort_circles(self):
        circles1 = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
        expected_circles_sorted = [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4),Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]
        circles1.sort()
        print(circles1)
        self.assertEqual(circles1, expected_circles_sorted)

        circles2 = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
        copy_sorted_list = sorted(circles2,key=Circle.sort_key)
        self.assertEqual(True,copy_sorted_list == expected_circles_sorted)

    def test_step8_div_circles(self):
        c1 = Circle(20)
        c2 = c1 / 5
        self.assertEqual(c2.radius, 4)
        self.assertEqual(c2.diameter, 8)
    
        with self.assertRaises(ValueError):
            print(c1 / 0)
        with self.assertRaises(ValueError):
            print(c1 / -2)
        
if __name__ == '__main__':
    unittest.main()