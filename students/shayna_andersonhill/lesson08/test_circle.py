
from circle import Circle
import unittest
import pytest

#Every function is called by the test

def test_circle_init():
    my_circle = Circle(4)
    assert my_circle.radius == 4
    assert my_circle.diameter == 8


