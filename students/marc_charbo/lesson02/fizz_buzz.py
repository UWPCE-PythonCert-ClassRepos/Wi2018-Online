#!/usr/bin/env python3

import sys

def fizz_buzz(x=100):
    for i in range(1,x):
        if(i%3==0) and (i%5==0):
            print ("fizz buzz")
        elif(i%3==0):
            print ("fizz")
        elif (i%5==0):
            print ("buzz")
        else:
            print (i)

def main():
    try:
        print("Run Fizz Buzz")
        print(" ")
        fizz_buzz()
        print(" ")
        print("Finish Fizz Buzz")

    except:
        print ("Error running Fizz Buzz")

if __name__ == "__main__":
    main()