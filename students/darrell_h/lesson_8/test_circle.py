#!/usr/local/bin/python3

from circle import Circle
import pytest

def test_instance_creation():
    c1 = Circle(5)
    assert c1.radius == 5

def test_get_diameter():
    c1 = Circle(5)
    assert c1.diameter == 10

def test_set_diameter():
    c1 = Circle(5)
    c1.diameter = 100
    assert c1.radius == 50

def test_set_radius():
    "test that a change in radius updates the diameter"
    c1 = Circle(5)
    c1.radius = 100
    assert c1.diameter == 200

def test_get_area():
    c1 = Circle(2)
    assert round(c1.area,6) == 12.566371

def test_alternative_constructor():
    c = Circle.from_diameter(8)
    assert c.radius == 4

def test__str__():
    c = Circle(4)
    assert str(c) == 'Circle with a radius 4.000000'

def test_exception():
    c = Circle(4)
    with pytest.raises(SystemExit):
        c.f()

def test_adding_instances():
    c1 = Circle(3)
    c2 = Circle(5)
    c3 = Circle(8)
    assert c1 + c2 == c3

def test_mulitplying_instances():
    c1 = Circle(3)
    assert c1 * 3 == Circle(9)

def test_mulitplying_instances_alternate():
    c1 = Circle(3)
    assert 3 * c1 == Circle(9)

def test_greater_than_comparison():
    c1 = Circle(3)
    c2 = Circle(10)
    assert c2 > c1

def test_less_than_comparison():
    c1 = Circle(5)
    c2 = Circle(10)
    assert c1 < c2

def test__repr__():
    c = Circle(4)
    d = eval(repr(c))
    assert  d == c


