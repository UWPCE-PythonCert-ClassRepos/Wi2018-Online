#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 19:40:00 2018

@author: du060e
"""

import lesson08 as l8
import unittest
import math
import io
import sys

class lesson08_TestCase(unittest.TestCase):
    # step 1 tests

    # test 1
    def test_radius_attribute(self):
        circ = l8.Circle(4)
        self.assertEqual(circ.radius, 4)
    # test 2    
    def test_valid_string_radius(self):
        circ = l8.Circle("3.14")
        self.assertEqual(circ.radius, 3.14)
            
    # step 2 tests
            
    # test 3       
    def test_diameter_attribute(self):
        circ = l8.Circle(4)
        self.assertEqual(circ.diameter, 8)
    # test 4
    def test_string_diameter_attribute(self):
        circ = l8.Circle("5.5")
        self.assertEqual(circ.diameter, 11)
        
    # step 3 tests
    
    # test 5        
    def test_set_diameter(self):
        circ = l8.Circle(4)
        circ.diameter = 20
        self.assertEqual(circ.diameter, 20)
    # test 6                
    def test_set_diameter_radius_changes(self):
        circ = l8.Circle(4)
        circ.diameter = 10
        self.assertEqual(circ.radius, 5)
    
    # step 4 tests
    
    # test 7
    def test_area(self):
        circ = l8.Circle(5)
        self.assertEqual(circ.area, math.pi*circ.radius**2)
    
    # step 5 tests
    
    # test 8
    def test_alternate_constructor_numeric(self):
        circ = l8.Circle.from_diameter(8)
        self.assertEqual(circ.diameter, 8)
    # test 9
    def test_alternate_constructor_string(self):
        circ = l8.Circle.from_diameter("6.28")
        self.assertEqual(circ.radius, 3.14)
        
    # step 6 tests
    
    # test 10
    def test_str_method(self):
        # capture printed statements
        captured_output = io.StringIO()
        sys.stdout = captured_output
        # create circle and call __str__ method               
        circ = l8.Circle(25)
        print(circ)
        # reset redirect
        sys.stdout = sys.__stdout__
        self.assertEqual('Circle with radius: 25.0', captured_output.getvalue().rstrip())
    # test 11
    def test_repr_method(self):
        circ = l8.Circle(30)
        self.assertEqual('Circle(30.0)', repr(circ))
        
    # step 7 tests
    
    # test 12
    def test_circle_addition(self):
        circ1 = l8.Circle(2)
        circ2 = l8.Circle(4)
        circ_add = circ1 + circ2
        self.assertEqual('Circle(6.0)', repr(circ_add))
    
    # test 13
    def test_circle_multiplication(self):
        circ1 = l8.Circle(40)
        circ_multiply = circ1 * 4
        self.assertEqual('Circle(160.0)', repr(circ_multiply))
        
    # step 8 tests
        
    # test 14
    def test_greater_than(self):
        circ1 = l8.Circle(2)
        circ2 = l8.Circle(3)
        self.assertTrue(circ2 > circ1)
    # test 15
    def test_less_than(self):
        circ1 = l8.Circle(2)
        circ2 = l8.Circle(3)
        self.assertTrue(circ1 < circ2)
    # test 16
    def test_equal(self):
        circ1 = l8.Circle(5)
        circ2 = l8.Circle("5")
        self.assertTrue(circ1 == circ2)
    # test 17
    def test_not_equal(self):
        circ1 = l8.Circle(10)
        circ2 = l8.Circle(10.1)
        self.assertEqual(circ1 == circ2, False)
    # test 18
    def test_circle_sort(self):
        circles = [l8.Circle(1), l8.Circle("10"), l8.Circle(0.1), l8.Circle("0.01")]
        circles.sort()
        print(circles)
        # reset redirect
        sys.stdout = sys.__stdout__
        self.assertEqual('[Circle(0.01), Circle(0.1), Circle(1.0), Circle(10.0)]',
                         repr(circles))
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()    