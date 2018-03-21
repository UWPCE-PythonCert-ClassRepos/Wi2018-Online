"""Provide a set of unit tests for the Simple Circle class."""
import pytest
import random
from simple_circle_class import Circle
from simple_circle_class import Sphere


########
# Step 1
########
def test_init(capsys):
    """Test instantiation and radius property."""
    c = Circle(4)
    assert c.radius == 4
    print(c.radius)
    out, _ = capsys.readouterr()
    assert out.strip() == "4"


########
# Step 2
########
def test_diam_prop(capsys):
    """Test the diameter property."""
    c = Circle(4)
    assert c.diameter == 8
    print(c.diameter)
    out, _ = capsys.readouterr()
    assert out.strip() == "8"


########
# Step 3
########
def test_diam_setter():
    """Test the diameter property setter."""
    c = Circle(4)
    c.diameter = 2
    assert c.radius == 1
    assert c.diameter == 2


########
# Step 4
########
def test_area():
    """Test the area property."""
    c = Circle(2)
    assert c.area == pytest.approx(12.566370)

def test_area_attr_error():
    """Test that the user can't set the area."""
    c = Circle(2)
    with pytest.raises(AttributeError):
        c.area = 42


########
# Step 5
########
def test_alt_constr_diam():
    """Test an alternative constructor to create a Circle from diameter."""
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4


########
# Step 6
########
def test_str(capsys):
    """Test the __str__ method."""
    c = Circle(4)
    print(c)
    out, _ = capsys.readouterr()
    assert out.strip() == "Circle with radius: 4.000000"

def test_repr():
    """Test the __repr__ method."""
    c = Circle(4)
    assert repr(c) == "Circle(4)"
    d = eval(repr(c))
    assert d == Circle(4)  # Circle.__eq__ must be implemented to compare!

def test_eq():
    """Test the __eq__ method."""
    c1 = Circle(4)
    c2 = Circle(4)
    assert c1 == c2
    assert Circle(3) != Circle(1)

########
# Step 7 - some numerics
########
def test_add():
    """Test the addition of two circles with the + sign."""
    c1 = Circle(2)
    c2 = Circle(4)
    assert c1 + c2 == Circle(6)

def test_mul():
    """Test the scalar multiplication."""
    assert Circle(4) * 3 == Circle(12)

def test_rmul():
    """Test the __rmul__ for the right scalar multiplication."""
    assert 3 * Circle(4) == Circle(12)


########
# Step 8 - comparison
########
# The code was written before these tests, at Step 6, when testing __repr__
def test_comparison():
    """Test if @functools.total_ordering really works."""
    c1 = Circle(2)
    c2 = Circle(4)
    assert (c1 > c2) is False
    assert (c1 < c2) is True
    assert (c1 == c2) is False
    c3 = Circle(4)
    assert (c2 == c3) is True

def test_sort():
    """Test if I can sort a list of circles by radius."""
    circles = []
    for i in range(0, 11):
        circles.append(Circle(i))
    random.shuffle(circles)
    circles.sort()
    assert circles == [Circle(0), Circle(1), Circle(2), Circle(3),
                       Circle(4), Circle(5), Circle(6), Circle(7),
                       Circle(8), Circle(9), Circle(10)]


########
# Step 8 - Optional Features
########
def test_reflected_numerics():
    """Test __eq__ fpr additional cases."""
    a_circle = Circle(2)
    assert (a_circle * 3) == (3 * a_circle)


def test_non_negative_radius():
    """Test that the radius cannot be made negative."""
    with pytest.raises(ValueError):
        c = Circle(-1)
    with pytest.raises(ValueError):
        d = Circle.from_diameter(-4)
    with pytest.raises(ValueError):
        Circle(4) - Circle(5)
    with pytest.raises(ValueError):
        c = Circle(1)
        c.radius -= 2

def test_sub_circle():
    """Test subtraction of one circle from another."""
    a_circle = Circle(4)
    c3 = a_circle - Circle(1)
    assert c3 == Circle(3)


def test_augmented_assignments():
    """Test if +=, -=, and *= operators work."""
    a_circle = Circle(2)
    a_circle += Circle(3)
    assert a_circle == Circle(5)
    a_circle = Circle(2)
    a_circle *= 4
    assert a_circle == Circle(8)
    a_circle = Circle(3)
    a_circle -= Circle(2)
    assert a_circle == Circle(1)


########
# Step 9 - Subclassing. Sphere sub-class
########
def test_init_sphere():
    """Test istantiation and the volume property."""
    s = Sphere(3)
    assert round(s.volume, 3) == pytest.approx(113.097)


def test_str_sphere(capsys):
    """Test the __str__ method."""
    s = Sphere(4)
    print(s)
    out, _ = capsys.readouterr()
    assert out.strip() == "Sphere with radius: 4.000000"


def test_repr_shere():
    """Test the __repr__ method."""
    s = Sphere(4)
    assert repr(s) == "Sphere(4)"
    d = eval(repr(s))
    assert d == Sphere(4)


def test_alt_constr_diam_sphere():
    """Test that the Circle alternative constructor also works here."""
    s = Sphere.from_diameter(8)
    assert s.diameter == 8
    assert s.radius == 4


def test_some_other_things():
    """Test Sphere addition, multiplication, equality."""
    s1 = Sphere(4)
    s2 = Sphere(6)
    assert (s1 + s2) == Sphere(10)
    assert (s1 * 3) == Sphere(12)
    assert s1 != s2
