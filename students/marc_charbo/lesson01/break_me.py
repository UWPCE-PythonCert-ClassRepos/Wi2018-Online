#!/usr/bin/env python3

print ('break me and more things')
print('develop stuff')
print ('break me.this is totally different')

def division (x,y):
    try:
        print (x/y)
    except ZeroDivisionError:
        print('division by zero error!')

def add(x):
    try:
        x+something
    except NameError:
        print ('variable something in function is not defined, NameError')

def count_char(word):
    var_type = type(word)
    try:
        print (len(word))
    except TypeError:
        print ('object type is %s has no len() property, TypeError' %(var_type))

def eval_something(x,y):
    try:
        print (eval('x=y'))
    except SyntaxError:
        print ('illegal eval operation, SyntaxError')

def attribute(x):
    try:
        x.something()
    except AttributeError:
        print ('%s has no attribute something(), AttributeError' %(x))
