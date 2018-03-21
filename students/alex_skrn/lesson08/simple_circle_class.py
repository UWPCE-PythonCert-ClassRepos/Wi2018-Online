#!/usr/bin/python
"""A Simple Circle Class - Week 8 assignment."""

import math
import functools


@functools.total_ordering
class Circle(object):
    """Class to create circles."""

    def __init__(self, radius):
        """Instantiate a circle object with a non-negative radius."""
        if radius < 0:
            raise ValueError("radius must be non-negative")
        self._radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        """Provide an alternative constructor -- a circle from a diameter."""
        return cls(diameter / 2.0)

    @property
    def radius(self):
        """Provide a getter method for the radius property."""
        return self._radius

    @radius.setter
    def radius(self, val):
        """Provide a setter method for the radius property."""
        if val < 0:
            raise ValueError("radius must be non-negative")
        self._radius = val

    @property
    def diameter(self):
        """Provide a getter method for the diameter property."""
        return 2 * self._radius

    @diameter.setter
    def diameter(self, val):
        """Provide a setter method for the diameter property."""
        self._radius = val / 2.0

    @property
    def area(self):
        """Provide a getter method for the area property."""
        return math.pi * self._radius ** 2.0

    # Define a set of special methods
    def __str__(self):
        return "Circle with radius: {:.6f}".format(float(self._radius))

    def __repr__(self):
        return "Circle({})".format(self._radius)

    def __eq__(self, other):
        """Return self==other."""
        return self._radius == other.radius

    def __lt__(self, other):
        """Return self<other."""
        return self._radius < other.radius

    def __add__(self, other):
        """Return self+other."""
        return Circle(self._radius + other.radius)

    def __mul__(self, val):
        """Return self*value."""
        return Circle(self._radius * val)

    def __rmul__(self, val):
        """Return value*self."""
        return Circle(val * self._radius)

    def __sub__(self, other):
        """Return self-other."""
        return Circle(self._radius - other.radius)


class Sphere(Circle):
    """Class to create spheres. A subclass of the Circle class."""
    @property
    def volume(self):
        """Provide a getter method for the volume property."""
        return (4/3) * math.pi * (self._radius ** 3)

    def __str__(self):
        return "Sphere with radius: {:.6f}".format(float(self._radius))

    def __repr__(self):
        return "Sphere({})".format(self._radius)
