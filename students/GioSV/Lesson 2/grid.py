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
#def grind()
#Defining line type 1:
line_1="+ " + 5*"- " + "+ " + 5*"- " + "+"
line_2="| " + 5*"  " + "| " + 5*"  " + "|"

altitude=5

print (line_1)

for i in range(altitude):
    print (line_2)

print (line_1)

for i in range(altitude):
    print (line_2)

print (line_1)
