#!/usr/bin/env python3
'''
Test for the Circle class
    test_def_circle_radius
        validates the circle attributes when a radius is used to define the circle
        5 is used as the radius value for the test.
    test_def_circle_diameter
        validates the circle attributes when a diameter is used to define the circle
        10 is used as the radius value for the test.


'''

def test_def_circle_properties(radius = 5):
    '''
    validates the circle attributes when a radius is used to define the circle
    5 is used as the radius value for the test.
    pi = import math pi module
    Diameter should equal 10.
    Area should equal 78.53981633974483
    '''
    from circle import MyCircle
    test_circle = MyCircle(5)
    assert test_circle.radius == 5
    assert test_circle.diameter == 10
    assert test_circle.area == 78.53981633974483
    return True



