#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import math


class Circle():
    # Do things with circles.

    def __init__(self, radius):
        # Each circle has a diameter and a radius.
        self.radius = radius
        self.diameter = radius * 2

    @property
    _diameter = None
    def diameter(self):
        return self._diameter

    def area(self):
        # Return circle's area.
        return math.pi * self.radius ** 2.0

    def print_circle(self):
        print(f"My favorite circle has a radius of {self.radius} and an area of {self.area()}")

    def add_circles(self, other_circle):
        total_area = self.area() + other_circle.area()
        return total_area

# Create a Circle object.
my_circle = Circle(4)
new_circle = Circle(2)
#print(my_circle)
print(my_circle.area())
my_circle.print_circle()
print(my_circle.add_circles(new_circle))
