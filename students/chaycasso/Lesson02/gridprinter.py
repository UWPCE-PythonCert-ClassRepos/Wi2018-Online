#Grid Printer Exercise
#Chay Casso, 1/29/18

PLUS = "+"
MINUS = "-"
BLANK = " "
PIPE = "|"
BLANK_MINUS = BLANK + MINUS


def grid1():
    """Draw a simple 2x2 grid composed of 5x5 squares."""

    print(PLUS + BLANK_MINUS * 4 + BLANK + PLUS + BLANK_MINUS * 4 + BLANK + PLUS)
    for i in range(1, 5):
        print(PIPE + BLANK * 9 + PIPE + BLANK * 9 + PIPE)
    print(PLUS + BLANK_MINUS * 4 + BLANK + PLUS + BLANK_MINUS * 4 + BLANK + PLUS)
    for i in range(1, 5):
        print(PIPE + BLANK * 9 + PIPE + BLANK * 9 + PIPE)
    print(PLUS + BLANK_MINUS * 4 + BLANK + PLUS + BLANK_MINUS * 4 + BLANK + PLUS)


def grid_line2(grid_size=3):
    """Draw a line with dashes and PLUS signs for a 2x2 grid of total length grid_size."""
    print(PLUS + BLANK_MINUS * int((grid_size - 1) / 2) + BLANK + PLUS + BLANK_MINUS * int((grid_size - 1) / 2) + BLANK + PLUS)


def grid_space2(grid_size=3):
    """Draw the inner space of the 2x2 grid with total length grid_size."""
    print(PIPE + BLANK * grid_size + PIPE + BLANK * grid_size + PIPE)


def grid2(grid_size=3):
    """Draw a 2x2 grid of squares with total length grid_size."""
    grid_line2(grid_size)
    for i in range(1, int((grid_size + 1) / 2)):
        grid_space2(grid_size)
    grid_line2(grid_size)
    for i in range(1, int((grid_size + 1) / 2)):
        grid_space2(grid_size)
    grid_line2(grid_size)


# The use of grid_size is different between Part 2 and Part 3 because it changes in the given examples for Part 2 and
# Part 3.

def grid_line3(columns=2, grid_size=3):
    """Draw a line for a grid of columns x columns size, each square a grid_size length."""
    print((PLUS + BLANK_MINUS * grid_size + BLANK) * columns + PLUS)


def grid_space3(columns=2, grid_size=3):
    """Draw the inner spaces for a grid of columns x columns size, each square a grid_size length."""
    print((PIPE + BLANK * (grid_size * 2 + 1)) * columns + PIPE)


def grid3(columns=2, grid_size=3):
    """Draw a grid of columns x columns size, each square a grid_size length."""
    for j in range(1, columns + 1):
        grid_line3(columns, grid_size)
        for i in range(1, grid_size + 1):
            grid_space3(columns, grid_size)
    grid_line3(columns, grid_size)


grid3(5,3)