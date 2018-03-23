"""
Lesson 08 Assignment
Create a class that represents a simple circle
"""

from math import pi

class Circle(object):
    def __init__(self, radius):
        """
        Required parameter radius
        :param radius: circle's radius
        """
        self.radius = radius

    @property
    def diameter(self):
        """ get diameter property """
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        """set diameter property"""
        self.radius = diameter / 2

    @property
    def area(self):
        """ area property """
        return pi * pow(self.radius, 2)

    @classmethod
    def from_diameter(cls, diameter):
        """ alternate constructor that lets create a Circle directly with the diameter"""
        return Circle(diameter / 2)

    def __str__(self):
        return "Circle with radius: {}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, multiplier):
        return Circle(self.radius * multiplier)

    def __rmul__(self, multiplier):
        return Circle(self.radius * multiplier)

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius


if __name__ == '__main__':
    c = Circle(4)
    print(c.radius)
    print(c.diameter)
    print(c.area)
    # c.area = 2

    c = Circle.from_diameter(8)
    print(c.diameter)
    print(c.radius)

    print(c)  # Circle with radius: 4.0
    repr(c)
    d = eval(repr(c))
    print(d)  # Circle with radius: 4.0

    c1 = Circle(2)
    c2 = Circle(4)
    print(c1 + c2)
    print(c2 * 3)

    c1 = Circle(3)
    c2 = c1 * 3
    print(str(c2))

    c1 = Circle(3)
    c2 = 3 * c1
    print(str(c2))

    c1 = Circle(1)
    c2 = Circle(1)
    print(c1 == c2)

    c1 = Circle(1)
    c2 = Circle(2)
    print(c1 != c2)

    c1 = Circle(2)
    c2 = Circle(1)
    print(c1 > c2)

    c1 = Circle(2)
    c2 = Circle(1)
    print(c1 < c2)
