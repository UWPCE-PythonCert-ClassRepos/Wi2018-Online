import math

class Circle:
    
    def __init__(self, val):
        self.radius = val
        
    @property
    def diameter(self):
        return 2*self.radius
    
    @diameter.setter
    def diameter(self,val):
        self.radius = val/2
        
    @property
    def area(self):
        return self.radius**2*math.pi
    
    @area.setter
    def area(self,val):
        raise AttributeError
    
    @classmethod
    def from_diameter(cls,val):
        return cls(val/2)
    
    def __str__(self):
        return f'Circle with radius: {self.radius}'
    
    def __repr__(self):
        return f'Circle({self.radius})'
    
    def __add__(self, other):
        return Circle(self.radius + other.radius)
    
    def __mul__(self, val):
        return Circle(self.radius * val)
    
    def __rmul__(self, val):
        return self.__mul__(val)
    
    def __lt__(self, other):
        return self.radius < other.radius
    
    def __eq__(self, other):
        return self.radius == other.radius
    
    def __ne__(self, other):
        return self.radius != other.radius
        
    def __le__(self, other):
        return self.radius <= other.radius
        
    def __gt__(self, other):
        return self.radius > other.radius
        
    def __ge__(self, other):
        return self.radius >= other.radius
    