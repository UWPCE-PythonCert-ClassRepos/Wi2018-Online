#-------------------------------------------------#
# Title: Fizz Buzz Exercise, working with modulo
# Dev: Scott Luse
# Date: January 30, 2018
#-------------------------------------------------#

# Write a program that prints the numbers from 1 to 100 inclusive.
# But for multiples of three print “Fizz” instead of the number.
# For the multiples of five print “Buzz” instead of the number.
# For numbers which are multiples of both three and five print “FizzBuzz” instead.

# -- Data --#


# -- Processing --#
def determineValue():
    try:
        x = 0
        for x in range(1, 101):
            strvalue = str(x)

            if(x%3 == 0):
                strvalue = "Fizz"
            if(x%7 == 0):
                strvalue = "Buzz"

            if(x%3 == 0 and x%7 == 0):
                strvalue = "FizzBuzz"

            print(strvalue)
    except Exception as e:
        print("Error: " + str(e))



# -- Presentation (Input/Output) --#

try:
    print("For 1 to 100, this program will print Fizz for multiples of 3 and Buzz for multiples of 7.")
    determineValue()


except Exception as e:
    print("Python reported the following error: " + str(e))