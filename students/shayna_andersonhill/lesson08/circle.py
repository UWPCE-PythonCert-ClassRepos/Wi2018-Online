#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import math
import functools

@functools.total_ordering
class Circle():
    # Do things with circles.

    def __init__(self, radius):
        # Each circle has a diameter and a radius.
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, val):
        if val < 0:
            raise ValueError("radius cannot be less than zero")
        self._radius = val

    @property
    def diameter(self):
        #diameter should always be twice the radius
        return 2 * self.radius
    @diameter.setter
    def diameter(self, val):
        #Allow ability to set the diameter
        self.radius = val / 2
    
    @property
    def area(self):
        # Return circle's area. Read-Only property.
        return math.pi * self.radius ** 2.0

    def print_circle(self):
        print(f"My favorite circle has a radius of {self.radius} and an area of {self.area}")

    def __str__(self):
        return "a circle with a radius of {self.radius}".format(self=self)

    def __repr__(self):
        return "{self.__class__.__name__}({self.radius})".format(self=self)

    def __add__(self, other):
        return self.radius + other.radius

    def __mul__(self, val):
        return self.radius * val

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius 
        
