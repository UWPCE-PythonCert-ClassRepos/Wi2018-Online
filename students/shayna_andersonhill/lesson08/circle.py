#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import math


class Circle():
    # Do things with circles.

    def __init__(self, radius):
        # Each circle has a diameter and a radius.
        self.radius = radius
        self.diameter = radius * 2

    def area(self):
        # Return circle's area.
        return math.pi * self.radius ** 2.0

# Create a Circle object.
my_circle = Circle(2)
print(my_circle)
#print(my_circle.area())
