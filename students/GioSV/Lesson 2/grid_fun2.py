# Write a function that draws a grid like the following:
#
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
#
#We gotta define two types of lines:
#   1. The lines from the beginning, middle and end of the grind.
#   2. The lines in between.
#
#I don't like the idea of printing everything in order and just have the exercise done in a manual way. That's why I'll try and do it in a different way.
#
#
#IN ORDER TO CALL THE FUNCTION, ONE MUST TYPE:
#       grid("+ ","- ","| ")
#OR:
#       
#
#
print("In order to call the function grid, please type 'grid(a,b,c)', where a, b and c are the symbols you want to input to make your grid.\n")
def grid(a,b,c):
#a comes to be "+"
#b comes to be "-"
#c comes to be "|"
#I will internally define them like that, just in case the function is called withouth arguments.

#Defining line type 1:
    line_1=a +" "+ 5*(b+" ")    + a +" " + 5*(b+" ")    + a
    line_2=c +" "  + 5*"  " + c + 5*"  " +" " + c

    print (line_1)

    for i in range(5):
        print (line_2)

    print (line_1)

    for i in range(5):
        print (line_2)

    print (line_1)


#While this function does what it must, now I gotta generalize this particular function in order for the user not to input three different values -related to the symbols in the grid- but only one.
#By studying the example grid as it is, it's easy to know that 11 is the number of symbols in a row, as it is the number of symbols in the colums that close the grid and in the center.the
#In this sense, the whole configuration should change to permit grids of different sizes.

print("If you're looking to call the function print_grid, you should type print_grid(n), where 'n' is the size of the grid you want to built. \n Note that the minimum size of the grid is 5 and, if you enter a number below 5, a grid(5) will be the output.\n Note that the numbers should be odds that equals 5 or above.")
def print_grid(n):
    #The minimum configuration in a row to have an ordered grid is the following:
    #   +-+-+
    #Hence, the minimum size should be 5.
    #I will clarify this point by making a print statement.
    size_a=0
    size_b=0
    size_c=0
    if (n%2==0):
        return("Please, enter an odd number")
    
    a="+"
    b="-"
    c="|"
    size=n
    size_a= size - 2 #spaces of the grid that are left once the spaces for a have been taken.
    size_c= size_a - 1 #spaces of the grid that are left once the spaces for c have been taken.
    size_b= size_c -2 #spaces of the grid that are left once the minimum spaces for b have been taken. 
    line_1=a +" "+ (size_b+1)*(b+" ")    + a +" " + (size_b+1)*(b+" ")    + a
    line_2=c +" "  + (size_b+1)*"  " + c + (size_b+1)*"  " +" " + c
    if n<5:
        n=5

    print (line_1)
    for i in range(size_c//2):
        print (line_2)
    print (line_1)
    for i in range(size_c//2):
        print (line_2)
    print (line_1)


