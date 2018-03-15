#!/usr/bin/env python3

"""
a simple script to run circle geometry class
"""

import circle_geometry as cg

print('#--- Set Radius to 4 ---#')
c = cg.Circle(4)
print("radius-1: " + str(c.radius))
print("diameter-1: " + str(c.diameter))
area = c.area
print("area-1: " + str(area))


print('#--- Set Diameter to 4 ---#')
c.diameter = 4
print("diameter-2: " + str(c.diameter))
print("radius-2: " + str(c.radius))
area = c.area
print("area-2: " + str(area))

print('#--- Create Circle from Diameter ---#')
c2 = cg.Circle.from_diameter(30)
print("diameter-3: " + str(c2.diameter))
print("radius-3: " + str(c2.radius))

print('#--- Printing ---#')
print(c2)
print(repr(c2))

print(c + c2)
print(c * c2)
print(c < c2)
print(c == c2)

c1 = cg.Circle.from_diameter(40)
c3 = cg.Circle.from_diameter(8)
c4 = cg.Circle.from_diameter(18)

new = [c, c1, c2, c3, c4]
print(new)
new.sort()
print(new)

print("Fun all done!")
