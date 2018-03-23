# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 14:51:16 2018

@author: seelc
"""


for i in range(1,101):
    #prints 'FizzBuzz' if i divisible by 3 and 5
    if i%3 == 0 and i%5 == 0: 
        print('FizzBuzz')
    #prints 'Fizz' if i divisible by just 3
    elif i%3 ==0: 
        print('Fizz')
    #prints 'Buzz' if i divisible by just 5
    elif i%5 ==0: 
        print('Buzz')
    #prints i if none of the previous conditions are true
    else: 
        print(i)