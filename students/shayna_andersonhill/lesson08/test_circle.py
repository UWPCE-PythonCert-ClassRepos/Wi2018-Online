
from circle import Circle
import unittest
import pytest
import sys
import random

#Every function is called by the test

def test_circle_init():
    my_circle = Circle(4)
    assert my_circle.radius == 4
    #Test alternate constructor
    assert my_circle.diameter == 8
    assert my_circle.radius * 2 == my_circle.diameter

def test_negative_radius():
    with pytest.raises(ValueError):
        my_circle = Circle(4)
        my_circle.radius = -10
        Circle(-10)

def test_circle_area():
    my_circle = Circle(4)
    assert my_circle.area == 50.26548245743669
    #Test that area is read-only
    with pytest.raises(AttributeError):
        my_circle.area = 10

def test_repr():
    assert repr(Circle(4)) == "Circle(4)"

def test_str():
    assert str(Circle(4)) == "a circle with a radius of 4"

def test_addition():
    circle1 = Circle(1) 
    circle2 = Circle(2)
    circle3 = Circle(3)
    assert circle3.radius == (circle1.radius + circle2.radius)

def test_multiplication():
    circle8 = Circle(8)
    assert circle8.radius * 2 == 16
    assert 2 * circle8.radius == 16

def test_total_odering():
    c1 = Circle(1) 
    c2 = Circle(2)
    circle2 = Circle(2)
    assert c1 < c2
    assert c2 > c1
    assert c2 == circle2
    circles = [Circle(radius) for radius in range(1,11)]
    random.shuffle(circles)
    if all(circles[i] <= circles[i+1] for i in range(len(circles)-1)) == False:
        pass
    else:
        random.shuffle(circles)
    circles.sort()
    assert all(circles[i] <= circles[i+1] for i in
            range(len(circles)-1)) == True



class MyTest(unittest.TestCase):
    def test_stdout(self):
        my_circle = Circle(4)
        class MyOutput(object):
            def __init__(self):
                self.data = []

            def write(self, s):
                self.data.append(s)

            def __str__(self):
                return "".join(self.data)

        stdout_org = sys.stdout
        my_stdout = MyOutput()
        try:
            sys.stdout = my_stdout
            my_circle.print_circle()
        finally:
            sys.stdout = stdout_org

        self.assertEquals( str(my_stdout), "My favorite circle has a radius of 4 and an area of 50.26548245743669\n") 
