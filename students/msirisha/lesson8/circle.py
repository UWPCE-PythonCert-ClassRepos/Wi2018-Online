import math


class Circle(object):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius should be greater than 0")
        self.radius = radius

    @property
    def diameter(self):
        return 2.0 * self.radius

    @diameter.setter
    def diameter(self, diameter):
        if diameter < 0:
            raise ValueError("radius can not be less than zero")
        self.radius = diameter / 2.0

    @property
    def area(self):
        return math.pi * self.radius * self.radius

    @classmethod
    def from_diameter(cls, diameter):
        if diameter <= 0:
            raise ValueError("diameter can not be less than zero")
        radius = diameter / 2.0
        return cls(radius)

    def __str__(self):
        return f"Circle with radius: {float(self.radius)}"

    def __repr__(self):
        #return f"{self.__class__.__name__}({self.radius})"
        return f"Circle({self.radius})"

    def __add__(self, other):
        if isinstance(other, Circle):
            #return eval(f"Circle({self.radius + other.radius})")
            return Circle(self.radius + other.radius)
        else:
            raise TypeError

    def __mul__(self, value):
        if isinstance(value, int):
            return Circle(self.radius * value)
        else:
            raise TypeError

    def __rmul__(self, value):
        return self.__mul__(value)

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        else:
            raise TypeError("Expected circle type object")

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Circle):
            if self.radius - other.radius < 0:
                return Circle(0)
            else:
                return Circle(self.radius - other.radius)

    def __truediv__(self, value):
        if value == 0:
            raise ZeroDivisionError
        elif value < 0:
            raise ValueError
        if type(value) is int:
            return Circle(self.radius / value)
        else:
            TypeError("Provide integer for circle true div")

    def __floordiv__(self, value):
        if value == 0:
            raise ZeroDivisionError
        elif value < 0:
            raise ValueError
        if type(value) is int:
            return Circle(self.radius // value)
        else:
            TypeError("Provide integer for circle floor division")








