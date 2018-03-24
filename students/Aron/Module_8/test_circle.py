from circle import Circle
import pytest

def test_equal():
    c1=Circle(5)
    assert c1.cir_radius == 5

def test_diameter():
    c1 = Circle(5)
    assert c1.cir_diameter == 10

def test_set_diameter():
    c1 = Circle(5)
    c1.cir_diameter = 20
    assert c1.cir_radius == 10

def test_cir_area():
    c1 = Circle(2)
    assert round(c1.cir_area,6) == 12.566371

def test_alt_constructor():
    c = Circle.fromDiam(10)
    assert c.cir_radius == 5

def test_add_instances():
    c1 = Circle(5)
    c2 = Circle(5)
    c3 = Circle(10)
    assert c1 + c2 == c3

def test_mulit_instances():
    c1 = Circle(5)
    assert c1 * 3 == Circle(15)

def test_lt_comparison():
    c1 = Circle(5)
    c2 = Circle(10)
    assert c1 < c2
