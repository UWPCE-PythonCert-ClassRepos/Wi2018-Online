#!/usr/bin/env python3
#
# Circle Class
# Chay Casso
# 3/19/2018
# Creates various properties of a circle.


class Circle(object):

    def __init__(self, the_radius=0):
        self._radius = the_radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def diameter(self):
        """Gets the diameter"""
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2