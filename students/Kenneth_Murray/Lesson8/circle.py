#!/usr/bin/env python3
'''The Circle Class
inputs :
    the_radius

methods:
    .from diameter

properties :
    diameter
    radius
    area
'''


class MyCircle():

    def __init__(self, the_radius):
        self.radius = the_radius


    @property
    def diameter(self):
        return self.radius * 2


    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2


    @property
    def area(self):
        from math import pi
        from math import pow
        my_area = pi * pow(self.radius, 2)
        return my_area


    @classmethod
    def from_diameter(cls,val):
        radius = val / 2
        return cls(radius)


    def __add__(self, another_circle):
        return MyCircle( self.radius + another_circle.radius)


    def __lt__(self, another_circle):
        return MyCircle( self.radius < another_circle.radius)


    def __gt__(self, another_circle):
        return MyCircle( self.radius > another_circle.radius)


    def __eq__(self, another_circle):
        return MyCircle( self.radius == another_circle.radius)


    def __mul__(self, another_circle):
        return MyCircle( self.radius * another_circle.radius)


    def __str__(self):
        return 'MyCircle has a radius of ({})'.format(self.radius)

    def __repr__(self):
        return 'MyCircle({})'.format(self.radius)
