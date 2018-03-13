#!/usr/bin/env python

import math
from functools import total_ordering

@total_ordering
class Circle():
    def __init__(self, radius):
        try:
            self.radius = float(radius)
        except ValueError:
            print("The radius must be numeric. ")
            
    @property
    def diameter(self):
        return self.radius*2
        
    @diameter.setter
    def diameter(self, value):
        try:
            self.radius = float(value)/2
        except ValueError:
            print("The new diameter must be numeric. ")
            
    @property
    def area(self):
        return math.pi*self.radius**2
            
    @classmethod
    def from_diameter(cls, diameter):
        try:
            return cls(float(diameter)/2)
        except ValueError:
            print("The diameter must be numeric. ")
    
    def __str__(self):
        return "Circle with radius: {}".format(self.radius)
    
    def __repr__(self):
        return "Circle({})".format(self.radius)
        
    def __add__(self, other):
        try:
            total_radius = self.radius + other.radius
            return Circle(total_radius)
        except TypeError:
            print("Both objects must be of class Circle. ")
    
    def __mul__(self, scaling_factor):
        try:
            scaled_radius = self.radius*float(scaling_factor)
            return Circle(scaled_radius)
        except ValueError:
            print("The radius scaling factor must be numeric. ")
            
    def __eq__(self, other_circle):
        return self.radius == other_circle.radius
    
    def __lt__(self, other_circle):
        return self.radius < other_circle.radius
    

    

    
    
    
        

