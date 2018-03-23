"""Print a 2x2 grid, define two print_grid functions."""
# PART 1 - print a 2x2 grid, each cell 4 dashes large

plus, minus, bar, space = '+', '-', '|', ' '
num_cells = 2
num_dashes = 4

# construct the plus-and-dashes line, + - - - - + - - - - +
plus_line = ''
for _ in range(num_cells):
    plus_line += plus + space + ((minus + space) * num_dashes)
plus_line += plus

# construct the bars-and-spaces line, |         |         |
bar_line = ''
for _ in range(num_cells):
    bar_line += bar + space + (space * 2 * num_dashes)
bar_line += bar

# print the grid
for _ in range(num_cells):
    print(plus_line)
    for __ in range(num_dashes):
        print(bar_line)
print(plus_line)


# PART 2 - convert the above into a function with 1 parameter

def print_grid(cellsize):
    """Print a 2x2 grid.

    cellsize: number of symbols in the top side of one cell,
              i.e. spaces ' ' and dashes '-',
              but excluding plus signs at both ends
    Eg. print_grid(3) or print_grid(4) prints
            + - + - +
            |   |   |
            + - + - +
            |   |   |
            + - + - +
    """
    plus, minus, bar, space = '+', '-', '|', ' '
    num_cells = 2
    # convert number of symbols in the top of each cell into number of dashes
    num_dashes = int((cellsize-1)/2)
    # construct the plus-and-dashes line, eg., + - - - - + - - - - +
    plus_line = ''
    for _ in range(num_cells):
        plus_line += plus + space + ((minus + space) * num_dashes)
    plus_line += plus

    # construct the bars-and-spaces line, eg., |         |         |
    bar_line = ''
    for _ in range(num_cells):
        bar_line += bar + space + (space * 2 * num_dashes)
    bar_line += bar

    # print the grid
    for _ in range(num_cells):
        print(plus_line)
        for __ in range(num_dashes):
            print(bar_line)
    print(plus_line)


# print_grid(0)
# print_grid(3)  # same result as in print_grid(3) in the assignment
# print_grid(4)  # same as print_grid(3) above
# print_grid(9)  # same result as in print_grid(11) in the assignment
# print_grid(15)  # same result as in print_grid(15) in the assignment

# PART 3 - make a 2-parameter function

def print_grid2(num_cells, cellsize):
    """Print a square grid.

    num_cells: number of cells in one side of the grid
    cellsize: number of dashes or bar signs in one side of the cell
    Eg. print_grid2(2, 1) prints
            + - + - +
            |   |   |
            + - + - +
            |   |   |
            + - + - +
    """
    plus, minus, bar, space = '+', '-', '|', ' '
    # construct the plus-and-dashes line, eg., + - - - - + - - - - +
    plus_line = ''
    for _ in range(num_cells):
        plus_line += plus + space + ((minus + space) * cellsize)
    plus_line += plus

    # construct the bars-and-spaces line, eg., |         |         |
    bar_line = ''
    for _ in range(num_cells):
        bar_line += bar + space + (space * 2 * cellsize)
    bar_line += bar

    # print the grid
    for _ in range(num_cells):
        print(plus_line)
        for __ in range(cellsize):
            print(bar_line)
    print(plus_line)


# print_grid2(1, 0)
# print_grid2(1, 1)
# print_grid2(2, 1)
# print_grid2(3, 4)
# print_grid2(5, 3)
