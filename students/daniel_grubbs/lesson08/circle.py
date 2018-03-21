"""
Create a circle class that represents a simple circle.
"""
import math


class Circle:
    """Create a circle."""

    # Class attribute(s)
    PI = math.pi

    # Instance attribut(s) of Circle class
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        """Calculate the diamter of a circle."""
        return 2 * self.radius

    @diameter.setter
    def diameter(self, value):
        """Set the diameter."""
        self.radius = value // 2
        return self.radius

    @property
    def area(self):
        """Calculate the area of a circle."""
        return self.PI * self.radius ** 2

    def __repr__(self):
        """Show a representation."""
        return "Circle({})".format(self.radius)

    def __str__(self):
        """Display a string representation when printing."""
        return "Circle with radius: {}".format(self.radius)

    @classmethod
    def from_diameter(cls, dia):
        """Lets the user create a Circle directly with the diameter."""
        value = cls(dia // 2)
        return value

    def __add__(self, other):
        """Add two circles together."""
        # the first return statement did not work with testing
        # so need to refactor this and the other dunders
        # return Circle(self.radius + other.radius) - remove Circle
        return (self.radius + other.radius)

    def __mul__(self, other):
        """Add two circles together."""
        return (self.radius * other.radius)

    def __gt__(self, other):
        """Comparing greater than on two circles."""
        return (self.radius > other.radius)

    def __lt__(self, other):
        """Comparing less than on two circles."""
        return (self.radius < other.radius)

    def __eq__(self, other):
        """Comparing equality on two circles."""
        return self.radius == other.radius
