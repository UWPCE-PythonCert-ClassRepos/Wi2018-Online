import math


class Circle(object):

    # Step 1: Create a Circle class and initialize class attributes
    def __init__(self, radius):
        self.radius = radius

    # Step 2: Create a diameter property
    @property
    def diameter(self):
        return self.radius * 2

    # Step 3: Enable user to set diameter
    @diameter.setter
    def diameter(self, val):
        self.radius = round(val / 2)

    # Step 4: Create an area property
    @property
    def area(self):
        return round(math.pi * self.radius ** 2)

    # Step 5: Enable the user to create a Circle directly with diameter
    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter/2
        return cls(radius)

    # Step 6: Create __str__ and __repr__ methods
    def __str__(self):
        return "Circle with radius: {}".format(self.radius)

    # Step 6: (cont)
    def __repr__(self):
        return "Circle({})".format(self.radius)

    # Step 7: Create more special methods
    def __add__(self, other):
        return self.radius + other.radius

    # Step 7: (cont)
    def __sub__(self, other):
        return self.radius - other.radius

    # Step 7: (cont)
    def __mul__(self, other):
        return self.radius * other.radius

    # Step 8: Create even more special methods
    def __gt__(self, other):
        return self.radius > other.radius

    # Step 8: (cont)
    def __lt__(self, other):
        return self.radius < other.radius

    # Step 8: (cont)
    def __eq__(self, other):
        return self.radius == other.radius


if __name__ == "__main__":

    # Step 1: Create a Circle class
    c1 = Circle(2)

    # Step 2: Get the diameter
    print(c1.diameter)
    print("")

    # Step 3: Set a new diameter
    c1.diameter = 6
    print(c1.diameter)
    print(c1.radius)
    print("")

    # Step 4: Get the area
    print(c1.area)
    print("")

    # Step 5: Create a Circle directly with diameter
    c2 = Circle.from_diameter(4)
    print(c2.diameter)
    print("")

    # Step 6: __str and __repr__ methods in the Circle class
    print(str(c1))
    print(repr(c1))
    print("")

    # Step 7: Use special methods (add, subtract, multiple) in the Circle class
    print(c1 + c2)
    print(c1 - c2)
    print(c1 * c2)
    print("")

    # Step 8: Use special methods (greater than, less than, equal to) in the Circle class
    print(c1 > c2)
    print(c1 < c2)
    print(c1 == c2)
    print("")

    # Sort a list of circles
    c1 = Circle(6)
    c2 = Circle(2)
    c3 = Circle(4)
    c4 = Circle(3)
    c5 = Circle(7)

    circles = [c1, c2, c3, c4, c5]

    print(circles)
    circles.sort()
    print(circles)














