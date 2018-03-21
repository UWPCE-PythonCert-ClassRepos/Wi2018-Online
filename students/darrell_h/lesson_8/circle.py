#!/usr/local/bin/python3

from math import pi


class Circle():
    """
    circle class with the following attributes / properties
    ARGS:
        radius : set on initialization, can be overwritten.
    PROPERTIES:
        diameter : not set on initialization, calculated, SETTABLE.
    """

    x = 100

    def __init__(self, initial_radius_parameter):
        self.radius = initial_radius_parameter

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return pi * self.radius ** 2

    @classmethod
    def from_diameter(cls, intial_diameter_parameter):
        """ alternate constructor """
        return cls(intial_diameter_parameter /2)

    def __repr__(self):
        return 'Circle({0})'.format(str(self.radius))

    def __str__(self):
        return 'Circle with a radius {:.6f}'.format(self.radius)

    def f(self):
        raise SystemExit(1)

    def __eq__(self, other):
        return self.radius == other.radius

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __gt__(self, other):
        return self.radius > other.radius

    def __rmul__(self, other):
        return Circle(other * self.radius)


