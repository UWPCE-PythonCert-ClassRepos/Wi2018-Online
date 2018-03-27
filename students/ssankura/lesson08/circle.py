#!/usr/bin/env python3
'''
	Implementation of Circle
'''

import math
import numbers

class Circle(object):
	def __init__(self, radius):
		self.radius = radius

	@property
	def area(self):
		return math.pi * self.radius**2

	@property
	def diameter(self):
		return self.radius * 2.0

	@diameter.setter
	def diameter(self, inpt):
		self.radius = inpt / 2

	@property
	def perimeter(self):
		return 2 * math.pi * self.radius

	def __str__(self):
		return f"Circle [Radius = {self.radius:.4f}, Diameter = {self.diameter:.4f}, Area = {self.area:.4f}, Perimeter = {self.perimeter:.4f}]"

	def __repr__(self):
		return f"Circle({self.radius})"

	def __eq__(self, other):
		if isinstance(other, Circle):
			return self.radius == other.radius
		else: 
			raise TypeError

	def __lt__(self, other):
		if isinstance(other, Circle):
			return self.radius < other.radius
		else:
			return TypeError

	def __gt__(self, other):
		if isinstance(other, Circle):
			return self.radius > other.radius
		else:
			return TypeError

	def sort_key(self):
		return self.radius

	def __add__ (self, other):
		if isinstance(other, Circle):
			return Circle(self.radius + other.radius)
		else:
			raise TypeError

	def __mul__(self, val):
		if isinstance(val, numbers.Number):
			return Circle(self.radius * val)
		else:
			raise TypeError

	def __truediv__(self, val):
		if val <= 0:
			raise ValueError
		if isinstance (val, numbers.Number):
			return Circle(self.radius / val)
		else:
			return TypeError

	@classmethod
	def from_diameter(cls, diameter):
		return cls(diameter/2)

'''
Main method to test all the functionality
'''
if __name__ == "__main__":
	print ("****** STEP1 ******")
	c0 = Circle(4)
	print(f"Circle c0 Radius = {c0.radius}")

	print ("****** STEP2 ******")
	print (f"Circle c0 Diameter = {c0.diameter}")
	#c.area=42

	print ("****** STEP3 ******")

	c0.diameter = 10
	print (f"Circle c0 - Diameter Value after setting new value = {c0.diameter}")
	print (f"Circle c0 - Diameter Value after setting new value = {c0.radius}")

	print ("****** STEP4 ******")
	print (f"Circle c0 area = {c0.area}")
	try:
		c0.area = 42
	except AttributeError:
		print ("Attribute Error (Exception) occured: cannot update area of circle")

	print ("****** STEP5 ******")
	c1 = Circle.from_diameter(20)
	print (f"Created Circle c1 using from_diameter constructor and value 20 : {c1.diameter}")
	print (f"Circle c1 radius : {c1.radius}")

	print ("****** STEP6 ******")
	d = eval(repr(c0))
	print (f"Circle d after eval of repr on c0 = {d}")

	c2 = Circle(2)
	print (f"Circle c1 details using __str__ = {c1}")

	print ("****** STEP7 ******")
	print (f"Circle c1 = {c1}")
	print (f"Circle c2 = {c2}")
	c3 = (c1 + c2)
	print (f"Circle c3 = c1 + c2 : {c3}")

	c4 = Circle.from_diameter(30)
	print (f"Created Circle c4 using from_diameter constructor : {c4}")

	c5 = c2 * 3
	print (f"Circle c2 = {c2}")
	print (f"Circle c5 = c2 * 3 : {c5}")

	c6 = Circle(5)
	print (f"Circle c6 = {c6}")

	print ("****** STEP8 ******")

	print (f"Circle1 greater than Circle2 : {c1 > c2}")

	print (f"Circle1 lesser than Circle2 : {c1 < c2}")

	print (f"Circle0 is equal to Circle6 : {c0 == c6}")

	print (f"Circle0 is equal to Circle1 : {c0 == c1}")

	list_circles = [c4,c1,c5,c3,c2,c6]
	print(f"List of Circles before Sorting: {list_circles}")
	print(f"List of Circles after Sorting:{sorted(list_circles,key=Circle.sort_key)}")

	print ("****** STEP8 - Optional Division ******")
	c7 = c1 / 2
	print (f"Circle1 : {c1}")
	print (f"Circle c7 = c1 / 2 : {c7}")
