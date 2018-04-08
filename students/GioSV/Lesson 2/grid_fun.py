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
#
def grid(a,b,c):
#a comes to be "+"
#b comes to be "-"
#c comes to be "|"
#I will internally define them like that, just in case the function is called withouth arguments.

#Defining line type 1:
    line_1=a + 5*b    + a + 5*b    + a
    line_2=c + 5*"  " + c + 5*"  " + c

    print (line_1)

    for i in range(5):
        print (line_2)

    print (line_1)

    for i in range(5):
        print (line_2)

    print (line_1)
