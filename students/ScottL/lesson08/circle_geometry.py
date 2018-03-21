# ------------circle_geometry.py Module ---------------#
# Desc:  Class for Circle Geometry
# Dev:   Scott Luse
# Date:  03/10/2018
# ---------------------------------------------#
if __name__ == "__main__":
    raise Exception("This file is not meant to run by itself")

import math

class Circle(object):
    # --Constructor--
    def __init__(self, radius):
        # Attributes
        self.radius = radius

    # --Properties--
    # Radius
    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    # Area
    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    # Circumference
    @property
    def circumference(self):
        return 2 * math.pi * self.radius

    # Diameter
    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, value):
        self.__radius = value / 2

    def __str__(self):
        return f'Circle with radius({self.radius})'

    def __repr__(self):
        return 'Circle(%r)' % self.radius

    def __add__(self, other):
        return f'Adding two circles with radius {self.radius} and {other.radius} = ' + str(self.__radius + other.radius)

    def __mul__(self, other):
        return f'Multiply two circles with radius {self.radius} and {other.radius} = ' + str(self.__radius * other.radius)

    def __lt__(self, other):
        return self.__radius < other.radius

    def __eq__(self, other):
        return self.__radius== other.radius


    # --Methods--
    @classmethod
    def from_diameter(cls, value):
        radius = value / 2
        return cls(radius)

