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

def test_def_circle_properties():
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


def test_def_circle_change_diameter():
    '''
    Validate that the radius or diameter can be changed after the circle has been defined and will affect a change on each other.
    This will test the properties.
    '''
    from circle import MyCircle
    test_circle_diameter = MyCircle(5)
    assert test_circle_diameter.radius == 5
    assert test_circle_diameter.diameter == 10
    assert test_circle_diameter.area == 78.53981633974483
    test_circle_diameter.diameter = 14
    assert test_circle_diameter.radius == 7
    assert test_circle_diameter.diameter == 14


def test_from_diameter():
    from circle import MyCircle
    test_circle_diameter = MyCircle.from_diameter(10)
    assert test_circle_diameter.radius == 5
    assert test_circle_diameter.diameter == 10
    assert test_circle_diameter.area == 78.53981633974483
    test_circle_diameter.diameter = 14
    assert test_circle_diameter.radius == 7
    assert test_circle_diameter.diameter == 14


def test_compare():
    from circle import MyCircle
    circ1 = MyCircle(5)
    circ2 = MyCircle(10)
    circ3 = MyCircle(15)
    circ4 = MyCircle(50)
    assert circ1 < circ2
    assert circ2 > circ1
    assert circ1 + circ2 == circ3
    assert circ1 * circ2 == circ4




