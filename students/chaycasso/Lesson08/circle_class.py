#!/usr/bin/env python3
#
# Circle Class
# Chay Casso
# 3/19/2018
# Creates various properties of a circle.

from math import pi


class Circle(object):

    def __init__(self, the_radius = 0):
        self._radius = the_radius

    @classmethod
    def from_diameter(cls, value):
        self = cls()
        self._radius = value / 2
        return self

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def diameter(self):
        """Gets the diameter"""
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self._radius = value / 2

    @property
    def area(self):
        return self._radius * 2 * pi

    def __str__(self):
        return "Circle with radius: " + str(self.radius)

    def __repr__(self):
        return "Circle(%r)" % (self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        if type(self) == str:
            return Circle(self * other.radius)
        else: return Circle(self.radius * other)