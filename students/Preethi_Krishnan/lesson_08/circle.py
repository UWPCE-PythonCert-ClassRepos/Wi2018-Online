from math import pi


class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        diameter = self.radius * 2
        return diameter

    @diameter.setter
    def diameter(self, dia):
        self.radius = dia / 2

    def area(self):
        area_circle = pi * (self.radius ** 2)
        return area_circle

    @classmethod
    def from_diameter(cls, dia):
        circle_rad = Circle(dia / 2)
        return circle_rad

    def __str__(self):
        return "Circle with radius: " + str(self.radius)

    def __abs__(self, n):
        return abs(n)

    def __repr__(self):
        return "Circle({})".format(str(self.radius))

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __lt__(self, other):
        return self.radius < other.radius

    def __sub__(self, other):
        return abs(self.radius - other.radius)

    def __eq__(self, other):
        return self.radius == other.radius

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    def __ne__(self,other):
        return self.radius != other.radius

    def __gt__(self,other):
        return self.radius > other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ge__(self, other):
        return self.radius >= other.radius




if __name__ == '__main__':

    circle_1 = Circle(10)
    print("This is the circle radius: {}".format(circle_1.radius))
    print("This is the circle diameter: {}".format(circle_1.diameter))
    print("This is the circle area: {}".format(circle_1.area()))

    circle_2 = Circle(10)
    circle_3 = Circle(10)
    print("C1 is equal to C2?? {}".format(circle_2 == circle_3))

    c3 = Circle(10)
    c4 = Circle(10)
    print("C1 is equal to C2?? {}".format(c3 >= c4))

    c5 = Circle(10)
    c6 = Circle(1)
    print("C1 is equal to C2?? {}".format(c5 >= c6))

    c7 = Circle(-10)
    print("The absolute radius of circle is: {}".format(abs(-10)))

    c8 = Circle.from_diameter(20)
    print("This is the radius, diameter and area of the circle: {}, {}, {} ".format(c8.radius, c8.diameter, c8.area()))





