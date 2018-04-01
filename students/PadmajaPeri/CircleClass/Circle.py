from math import pi


class Circle(object):
    """
    Class that specifies the circle object and methods that support
    operations on circles
    """

    def __init__(self, radius):
        """ Initialize a circle given the radius """
        self.radius = radius

    @property
    def diameter(self):
        """ Diameter is computed based on radius """
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        """ If diameter is set, update the radius """
        self.radius = value / 2

    @property
    def area(self):
        """ Area = pi * radius * radius """
        return pi * pow(self.radius, 2)

    @classmethod
    def from_diameter(cls, value):
        """
        An alternate way of creating a circle is based on its diameter. Since
        the constructor for the Circle class takes the radius as parameter, we
        pass 1/2 of diameter as a parameter to create the Circle
        :param value:
        :return:
        """
        circle_obj = Circle(value / 2)
        return circle_obj

    def __str__(self):
        """ Magic method invoked when a Circle object is passed as parameter
        to print method
        """
        return "Circle with radius: " + str(self.radius)

    def __repr__(self):
        """
        Can be used to return a string representation of circle object. When
        the return value is passed to eval an object of cirlce is created
        :return:
        """
        return "Circle(" + str(self.radius) + ")"

    def __add__(self, other):
        """
        Invoked implicitly when 2 circle objects are added with + operator
        """
        return Circle(self.radius + other.radius)

    def __lt__(self, other):
        """
        Invoked implicitly when 2 circle objects are compared with < or >
        """
        return self.radius < other.radius

    def __eq__(self, other):
        """
        Invoked implicitly when 2 circle objects are compared with ==
        """
        return self.radius == other.radius

    def __mul__(self, other):
        """
        Invoked implicitly when 2 circle objects are multiplied with *
        """
        return Circle(self.radius * other)

    def __rmul__(self, other):
        """
        Invoked implicitly when a number is multiplied with Circle object.
        Ex: a_circle = Circle(3)
        3 * a_cicle
        """
        return Circle(self.radius * other)

    def __iadd__(self, other):
        """
        Invoked implicitly when an integer is added with Circle object using
        += . It adds the integer to the Circle object and assigns the new
        Circle object to the existing refernce
        Ex: a_circle = Circle(3)
        a_circle += 3
        """
        return Circle(self.radius + other.radius)


if __name__ == '__main__':
    c1 = Circle(4)
    c2 = Circle(4)
    print(c1 == c2)

    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0),
               Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]

    circles.sort()
    print(circles)


