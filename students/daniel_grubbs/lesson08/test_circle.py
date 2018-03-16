"""
Tests for the Circle class
"""
import pytest
from math import pi
from circle import Circle


def test_init():
    """Testing __init__."""
    Circle(4)
    assert True


def test_radius():
    """Test the radius."""
    circle_one = Circle(5)
    circle_two = Circle(8)

    assert circle_one.radius == 5
    assert circle_two.radius == 8


def test_diameter():
    """Test the diameter."""
    circle_one = Circle(5)
    circle_two = Circle(8)

    assert circle_one.diameter == 10
    assert circle_two.diameter == 16


def test_area():
    """Test the area."""
    circle_one = Circle(5)
    circle_two = Circle(8)

    assert circle_one.area == 78.53981633974483
    assert circle_two.area == 201.06192982974676


def test_repr():
    """Test internal representation of Cicle class."""
    circle_one = Circle(5)
    assert "Circle(5)" == repr(circle_one)
    assert circle_one == eval(repr(circle_one))


def test_string():
    """Test external representation of Circle class."""
    circle_one = Circle(5)
    circle_two = Circle(8)

    assert str(circle_one) == "Circle with radius: 5"
    assert str(circle_two) == "Circle with radius: 8"


def test_from_diameter():
    circle_one = Circle.from_diameter(5)
    circle_two = Circle.from_diameter(8)

    assert  type(circle_one) == Circle
    assert circle_one.radius == 2

    assert type(circle_two) == Circle
    # Uncomment line below, testing for failure
    # assert circle_two.radius == 6
    assert circle_two.radius == 4



def test_add_circles():
    """Test adding circles."""
    circle_one = Circle(5)
    circle_two = Circle(8)
    circle_three = circle_one + circle_two

    assert circle_three == 13


def test_multiply_circles():
    """Test multiplying circles."""
    circle_one = Circle(5)
    circle_two = Circle(8)
    circle_three = circle_one * circle_two

    assert circle_three == 40


def test_greater_than():
    """Testing greater than."""
    circle_one = Circle(5)
    circle_two = Circle(8)

    assert (circle_two > circle_one) == True
    assert (circle_one > circle_two) == False


def test_less_than():
    """Testing less than."""
    circle_one = Circle(5)
    circle_two = Circle(8)

    assert (circle_one < circle_two) == True
    assert (circle_two < circle_one) == False

def test_equal_to_each_other():
    """Testing Circle equality."""
    circle_one = Circle(5)
    circle_two = Circle(8)
    circle_three = Circle(5)

    assert (circle_one == circle_two) == False
    assert (circle_one == circle_three) == True


