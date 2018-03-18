# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 19:20:59 2018

@author: seelc
"""
import math

class Circle(object):
    radius = 0
    diameter = 0
    def __init__(self, radius):
        self.radius = radius
        
    
    #allows the creation of a circle from diameter      
    @classmethod
    def from_diameter(cls,val):
        cls(val/2)
        return cls(val/2)

    #Allows user to call area without being able to directly set it
    @property    
    def area(self):
        return self.radius**2*math.pi
    
    #Creates diameter, establishs diameter = 2*radius
    @property    
    def diameter(self):
        return 2 *self.radius
    
    #Declaring setter method to allow user to set diameter and update radius
    @diameter.setter
    def diameter(self, val):
        self.radius = val/2
        
    def get_Circle(self):
        return self.radius
    
    #Prints the radius of a circle when called
    def __str__(self):
        return str(self.radius)
    
    def __repr__(self):
        return str(self.radius)
    
    #Allows the addition of multiple circles, results in a new circle with
    #a radius the sum of the two added circles
    def __add__(self, second_circle):
        return Circle(self.radius + second_circle.radius)
    
    #Returns the multiplied radius's of the two circles
    def __mul__(self, second_circle):
        return Circle(self.radius * second_circle.radius)
    
    def __le__(self, second_circle):
        return not second_circle.radius < self.radius
    
    def __gt__(self, second_circle):
        return second_circle.radius < self.radius
    
    def __eq__(self, second_circle):
        return second_circle.radius == self.radius
    
    #Allows calling of modules for use in testing class
    def __call__(self):
        return self
    

'''Below code tests the 8 functions described in the assignment description'''       
#Testing ability to create a circle and produce the readius
myCircle = Circle(4)
assert myCircle.radius == 4

#Testing ability to alter the radius by setting the diameter
myCircle.diameter = 2
assert myCircle.radius == 1

#Testing ability to calculate area of a circle from radius
assert myCircle.area == myCircle.radius ** 2 * math.pi

#Testing ability to create a circle from the diameter
my_second_circle = Circle.from_diameter(4)
assert my_second_circle.diameter == 4
assert my_second_circle.radius == 2
assert my_second_circle.area == my_second_circle.radius ** 2 * math.pi

c = Circle(4)
#Testing ability to set circle area
try:
    c.area = 10
    print("Should not have been able to set area by calling it")
except AttributeError:
    print("Behaved correctly, shouldnt be able to alter area directly")

#newCircle = myCircle + Circle(2)
print(myCircle.__repr__)

#Testing ability to add circle  objects
addition_circle = Circle(4) + Circle(3)
assert Circle(6) == Circle(6)


small_circle = Circle(2)
large_circle = Circle(50)
second_small_circle = Circle(2)

#Testing ability to compare circle objects
assert large_circle > small_circle
assert small_circle < large_circle
assert second_small_circle == small_circle


circle_list = [Circle(1), Circle(3), Circle(2)]
circle_list.sort()
assert circle_list[0] == Circle(1) and circle_list[1] == Circle(2) and circle_list[2] == Circle(3)


