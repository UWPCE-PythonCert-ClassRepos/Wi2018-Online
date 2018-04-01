# Write a function that draws a grid

#  + - - - - + - - - - +
#  |         |         |
#  |         |         |
#  |         |         |
#  |         |         |
#  + - - - - + - - - - +
#  |         |         |
#  |         |         |
#  |         |         |
#  |         |         |
#  + - - - - + - - - - +


def grid():
    one = "+" + (4 * "-") + "+" + (4 * "-") + "+"
    two = "|" + (4 * " ") + "|" + (4 * " ") + "|"
    return print(one + '\n' + two + '\n' + two + '\n' + two + '\n' + two + '\n' +
                 one + '\n' + two + '\n' + two + '\n' + two + '\n' + two + '\n' + one)


print("grid1")
grid()


def grid2(n):
    one = "+" + (n * "-") + "+" + (n * "-") + "+"
    two = "|" + (n * " ") + "|" + (n * " ") + "|"
    return print(one + '\n' + ((two + '\n') * n) + one + '\n' + ((two + '\n') * n) + one)


print("grid2")
grid2(7)


# grid3(5,3) - 5 boxes each way, 3 dashes each way
def grid3(b, n):
    one = (("+" + (n * "-")) * b) + "+"
    two = ("|" + (n * " ")) * b + "|"
    new = (((one + '\n') + ((two + '\n') * n)) * b) + one
    return print(new)


print("grid3")
grid3(5, 3)

