#-------------------------------------------------#
# Title: Grid Printer Exercise, working with Functions
# Dev: Scott Luse
# Date: January 30, 2018
#-------------------------------------------------#

# Write a function that draws a grid like the following:
'''
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
'''


# -- Data --#
intValue = 0

# -- Processing --#
def createOneHorizontal(n):
    try:
        for x in range(1, n+1):
            print("+----" * n + "+")
            print("|    " * (n+1))
        print("+----" * n + "+")
    except Exception as e:
        print("Error: " + str(e))



# -- Presentation (Input/Output) --#

try:
    print("This program draws a X by Y grid.")
    # Loop until user exit
    while (True):
        # Ask user for grid size
        strParam = input("Enter size of grid (2, 3, or 4) or type exit: ")

        # check for user 'exit' or continue
        if (strParam.lower() == "exit"):
            break

        # check for empty size
        elif (len(strParam) < 1):
            print("Please enter grid size.")

        else:
            intValue = int(strParam)
            createOneHorizontal(intValue)



except Exception as e:
    print("Python reported the following error: " + str(e))