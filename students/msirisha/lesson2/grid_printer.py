# ===================== #
# grid printer #
# ===================== #

plus = "+"
minus = "-"
bar = "|"
space = " "

# part1 print 2 * 2 grid
def first_grid():
    """
    print 2 x 2 grid like below
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
    """
    num_dashes = 4
    num_cells = 2

    hline =  ((plus + space + (minus + space) * num_dashes) * num_cells) + plus
    vline = ((bar + space + (num_dashes * 2 * space)) * num_cells) + bar
    grid_body = (vline + '\n') * num_dashes

    print(hline)
    for i in range(2):
        print(grid_body, end="")
        print(hline)

# part2 convert first print grid function as a generic function to print based on a given grid width size
def print_grid(n):
    """ print grid based on given grid width size"""

    # Put some lower and higher limits on grid width size
    if n < 3:
        n = 3
    elif n > 25:
        n = 25

    cell_size = n // 2
    num_cells = 2

    hline = ((plus + space + (minus + space) * cell_size) * num_cells) + plus
    vline = ((bar + space + (cell_size * 2 * space)) * num_cells) + bar
    grid_body = (vline + '\n') * cell_size

    print(hline)
    for i in range(2):
        print(grid_body, end="")
        print(hline)

# part3 print grid based on given no of rows and columns. The function should take no of rows and columns as arguments.
def print_grid2(num_cells, cell_size):
    """ print grid based on given grid no of cells and cell size"""

    hline = plus + (((space + minus) * cell_size) + space + plus) * num_cells
    vline = ((bar + space + (cell_size * 2 * space)) * num_cells) + bar

    for hline_count in range(num_cells + 1 ):
        print(hline)

        if hline_count != num_cells:
            for vline_count in range(cell_size +1):
                print(vline)

if __name__ == "__main__":
    data = [3, 4, 5, -1, 25]
    print("print_grid - Print grid test")
    for width in data:
        print_grid(width)

    data = [(3,4), (1,1), (4,3), (25, 1), (0,0)









