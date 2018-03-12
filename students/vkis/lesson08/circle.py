class Circle():
    PI = 3.14

    # enables Circle(input) definition
    def __init__(self, the_radius):
        self.radius = the_radius

    # defines self.diameter then relates back to radius
    @property
    def diameter(self):
        return self.radius * 2

    # enables user definition of self.diameter, relates back to radius
    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    # alternate definition of Circle, that reruns the class as Circle(d/2)
    @classmethod
    def from_diameter(cls, diameter):
        return Circle(diameter / 2)

    # defines self.area then relates it back to self.radius
    @property
    def area(self):
        return self.PI * self.radius ** 2

    # enables user definition of self.area = # then raises an exception
    @area.setter
    def area(self, val):
        raise AttributeError("Area is calculated not set")

    # enables print() functionality
    def __str__(self):
        return f"Circle with radius: {self.radius:.6f}"

    # enables Circle() return
    def __repr__(self):
        return f"Circle({self.radius:d})"
        # __repr__ can also return things other than str:
        # return repr(self.radius)

    # __add__ takes the first class and adds the second to it
    # a + b is same as a.__add__(b)
    def __add__(self, b):
        if type(b) is type(self):
            return Circle(self.radius + b.radius)
        elif type(b) is int:
            return Circle(self.radius + b)
        else:
            raise TypeError("Addition must be done with int or Circle class")

    # after left to right fails, right to left exceutes with __radd__
    def __radd__(self, a):
        if type(a) is int:
            return Circle(self.radius + a)
        else:
            raise TypeError("Addition must be done with int or Circle class")

    # similar to __add__ but for multiply
    def __mul__(self, b):
        if type(b) is type(self):
            return Circle(self.radius * b.radius)
        elif type(b) is int:
            return Circle(self.radius * b)
        else:
            raise TypeError("Multiplication must be done with int or Circle class")

    # reverse mult, for when int * class
    def __rmul__(self, a):
        if type(a) is int:
            return Circle(self.radius * a)
        else:
            raise TypeError("Multiplication must be done with int or Circle class")

    # comparrison
    def __lt__(self, b):
        if self.radius < b.radius: return True
        else: return False

    def __gt__(self, b):
        if self.radius > b.radius: return True
        else: return False

    def __eq__(self, b):
        if self.radius == b.radius: return True
        else: return False
