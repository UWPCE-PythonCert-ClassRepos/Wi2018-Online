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

class from_diameter(Circle):
    def __init__(self, diameter):
        radius = diameter / 2
        Circle.__init__(self, radius)
