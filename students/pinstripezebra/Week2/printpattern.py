# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 14:51:39 2018

@author: seelc
"""

#Part 1
def printPattern1():
    horizontalSpacing = 4
    rows = 9
    fullRow = '+ - - - - + - - - - +'
    sparseRow = '|         |         |'
    for i in range(0,rows):
        if i%horizontalSpacing == 0:
            print(fullRow)
        else:
            print(sparseRow)

#Part 2
def printPattern2(size):
    size = size +2;
    #iterates through all the rows
    for i in range(0,size): 
        line = ''
        #iterates through all columns to print a complete row
        for j in range(0,size): 
            #Checks if the current row is a border
            if i %size ==0 or i == (size - 1)/2 or i == size - 1:
                # if its the left column
                if j == 0: 
                    line = line + '+ '
                #if its the middle column
                elif j == (size - 1)/2: 
                    line = line +'+ '
                 #if its the right column
                elif j ==size-1:     
                    line = line + '+'
                #any other
                else:               
                    line = line + '- '
            #if its a non border row
            else: 
                if j ==0 or j == (size - 1)/2:
                    line = line +'| '
                elif j == size - 1:
                    line = line + '|'
                #if its a non border
                else:
                    line = line +'  ' 
        print(line)

#part 3
def printPattern3(repeats, size):
    repeats = repeats +2
    #Row
    for i in range (repeats*size-repeats+1): 
        line = ''
        #Columns
        for j in range(repeats*size-repeats+1):
            #if it is a 'border' row
            if i%repeats ==0:
                #intersection point of two lines
                if j%repeats == 0 and j!=0: 
                    line = line+ ' +'
                elif j%repeats == 0 and j==0:
                    line = line + '+'
                else:
                    line = line + ' -'
            #Not a border row
            else: 
                if j%repeats == 0:
                    line = line + '| '
                else: 
                    line = line + '  '
        print(line)
    

                 