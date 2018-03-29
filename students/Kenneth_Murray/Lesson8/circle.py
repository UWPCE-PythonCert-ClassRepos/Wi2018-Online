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
        from math import pi
        from math import pow
        self.radius = the_radius
        self.diameter = the_radius * 2
        self.area = pi * pow(the_radius,2)

