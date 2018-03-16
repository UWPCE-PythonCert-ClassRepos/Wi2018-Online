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
c2 = cg.from_diameter(3)
print("diameter-3: " + str(c2.diameter))
print("radius-3: " + str(c2.radius))