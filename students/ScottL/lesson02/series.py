#-------------------------------------------------#
# Title: Series Exercise, working with Fibonacci and Lucas Series
# Dev: Scott Luse
# Date: January 30, 2018
#-------------------------------------------------#

# Create a new module series.py in the lesson02 folder in your student folder.
# In it, add a function called fibonacci.
# The function should have one parameter, n.
# The function should return the nth value in the fibonacci series.
# Ensure that your function has a well-formed docstring

# -- Data --#
intValue = 0

# -- Processing --#
def determineSeriesValue(n):
    try:
            nthvalue = round(.4472 * (1.618**n+1), 1)
            strvalue = str(int(nthvalue))
            print(strvalue)

    except Exception as e:
        print("Error: " + str(e))



# -- Presentation (Input/Output) --#

try:
    print("Please enter the Nth paramter in the Fibonacci series or type 'exit' to end program.")
    # Loop until user exit
    while (True):
        # Ask user for parameter
        strParam = input("Nth parameter: ")
        # check for user 'exit' or continue
        if (strParam.lower() == "exit"):
            break
        # check for empty name
        elif (len(strParam) < 1):
            print("Please enter Nth parameter.")
        else:
            intValue = int(strParam)
            determineSeriesValue(intValue)


except Exception as e:
    print("Python reported the following error: " + str(e))