# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 20:59:47 2018

@author: seelc
"""

#generalized function: Takes n = 'sequence index', first, second = 'first two values'
def sum_Series(n, first = 0, second = 1):
    storage = [first, second]
    newSum = 0
    for i in range(0, n-2):
        first = storage[1]
        newSum = storage[0] + storage[1]
        storage[0] = first
        storage[1] = newSum
    return newSum

#Calls generalized sum_Series with default arguments of (0,1) as first two values
def fibonnaci(n):
    newSum = sum_Series(n)
    #newSum is the nth value of Fibonnaci series
    return newSum 

#Calls generalized sum_Series with addisional arguments of (2,1) as first two values
def lucas(n):
    newSum = sum_Series(n, 2,1)
    #newSum is the nth value of the Lucas series
    return newSum 

fibonnaci_Test = [0,1,1,2,3,5,8]
lucas_Test = [2,1,3,4,7,11,18]

#assertions: Testing 
assert (lucas(6) == 11), '6th lucas value incorrect'
assert (fibonnaci(6) == 5), '6th fibonnaci value incorrect'
