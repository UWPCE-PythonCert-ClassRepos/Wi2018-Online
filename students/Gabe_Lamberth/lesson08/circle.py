#!/usr/bin/env python3
import math


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f'a circle object with radius: {self.radius}'

    def __repr__(self):
        return f'Circle({self.radius})'

    def __add__(self, other):
        return self.radius + other.radius

    def __mul__(self, other):
        return self.radius * other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def sort_key(self):
        return self.radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, val):
        self.radius = round(val / 2)

    @property
    def area(self):
        return round(self.radius ** 2 * math.pi)


if __name__ == "__main__":

    c1 = Circle(4)
    c2 = Circle(2)
    c3 = Circle(3)
    c4 = Circle(1)
    c5 = Circle(5)

    a_list = [c3, c2, c4, c1]

    # Calling the __str__ method
    print(f'c1 radius value has {c1}\n')
    print(f'c1 object is {repr(c1)}\n')
    print(f'Circle of radius: {c5.radius} has a diameter of: {c5.diameter}\n')
    print(f'Changing value of c5 radius: {c5.radius} to 9\n')
    c5.radius = 9
    print(f'New Circle value with radius: {c5.radius} has a diameter of: {c5.diameter}\n')
    print(f'Changing value of c5 diameter: {c5.diameter} to 20\n')
    c5.diameter = 20
    print(f'New Circle radius: {c5.radius} value with new diameter {c5.diameter}\n')
    print(f'Value of objects c1 + c2 = {c1 + c2}\n')
    print(f'Value of objects c1 * c2 = {c1 * c2}\n')
    print(f'Showing boolean of {c4} > of {c3} is {c4 > c3}\n')
    print(f'Showing boolean of {c4} < of {c3} is {c4 < c3}\n')
    print(f'List before sorting: {a_list}\n')
    print(f'List after sorting: {sorted(a_list,key=Circle.sort_key)}\n')
    print(f'Showing area of {repr(c1)} is {c1.area}')











