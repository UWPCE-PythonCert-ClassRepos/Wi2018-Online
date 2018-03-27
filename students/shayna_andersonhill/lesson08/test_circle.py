
from circle import Circle
import unittest
import pytest
import sys

#Every function is called by the test

def test_circle_init():
    my_circle = Circle(4)
    assert my_circle.radius == 4
    assert my_circle.diameter == 8


def test_circle_area():
    my_circle = Circle(4)
    assert my_circle.area() == 50.26548245743669


#def test_print_circle():
#    my_circle = Circle(4)
#    assert print(my_circle.print_circle()) == "My favorite circle has a radius of 4 and an area of 50.26548245743669"

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
