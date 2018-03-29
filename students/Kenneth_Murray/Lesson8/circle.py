#!/usr/bin/env python3
'''The Circle Class
inputs :
    the_radius
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

    def area(self):
        from math import pi
        from math import pow
        self.area = pi * pow(self.radius, 2)
        return self.area

    def __repr__(self):
        return 'MyCircle({})'.format(self.radius)
