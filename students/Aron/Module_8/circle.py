import math

class Circle:
    def __init__(self, radius):
        self.cir_radius = radius

    @property
    def cir_diameter(self):
        return 2 * self.cir_radius
    @cir_diameter.setter
    def cir_diameter(self, val):
        self.cir_radius = val / 2

#Add area property to get area of circle, area has to be calculated
    @property
    def cir_area(self):
        return math.pi * 2 * self.cir_radius

    @classmethod
    def fromDiam(cls, value=None):
        self = cls(value/2)
        return self

    def __str__(self):
        return "Circle with a radius:" + str(self.cir_radius)

    def __repr__(self):
        return "Circle({})".format(self.cir_radius)

    def __add__(self, object):
        return Circle(self.cir_radius + object.cir_radius)

    def __mul__(self, object):
        return Circle(self.cir_radius * object)

    def __lt__(self, other):
        return self.cir_radius < other.cir_radius

    def __eq__ (self, other):
        return self.cir_radius == other.cir_radius

#    def from_diameter(self, d):
#       self.cir_radius = d / 2


#create circle from diameter


#Add __str__ and __repr__ methods to your Circle class


#    @cir_area.setter
#    def cir_area(x = c.cir_radius):
#        self.cir_area = math.pi*2*x
#        #return math.pi*2*x



