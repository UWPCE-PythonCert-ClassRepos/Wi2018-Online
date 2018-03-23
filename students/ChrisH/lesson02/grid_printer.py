# ------------------------------------
# grid_printer.py
#  draw ascii grids
# ------------------------------------

# Global constants for readability
PLS = '+'
DSH = '-'
VLN = '|'
SPC = ' '


def print_grid(grid_width):
    """ Print a 2x2 grid with size as close to 'n' total columns as possible.
    :rtype: None """

    if grid_width < 3:
        grid_width = 3
    if grid_width > 20:
        grid_width = 20

    box_size = grid_width // 2

    h_line = PLS + DSH * box_size + PLS + DSH * box_size + PLS
    grid_body = (VLN + SPC * box_size + VLN + SPC * box_size + VLN + '\n') * box_size

    print(h_line)           # print top line
    for t in range(2):      # print two grid rows
        print(grid_body, end='')
        print(h_line)


def print_grid2(box_count, box_size):
    """ Print a 'box_count x box_count' grid with each box 'box_size' units wide.
    :rtype: None """

    if box_count <= 0 or box_size < 0:
        return

    h_line = PLS + ((DSH * box_size + PLS) * box_count)
    b_line = VLN + ((SPC * box_size + VLN) * box_count)

    for h_line_count in range(box_count + 1):  # need one more horizontal line than number of cells
        # draw horizontal lines
        print(h_line)

        if h_line_count != box_count:  # don't draw the box body after the last horizontal line
            # draw the box body
            for t in range(box_size):
                print(b_line)


def main():
    """ Test functions for grid printer
    :rtype: None """

    print("grid printer test - print_grid")
    test_data = (8, 3, 20, -5, 30)
    for n in test_data:
        print("grid size: ", n)
        print_grid(n)

    print("grid printer test - print_grid2")
    test_data = [
        (3, 4), (5, 3), (2, 2), (2, 1), (30, 1),
        (2, -5), (0, 0), (1, 1), (1, 0),
        ]
    for grid in test_data:
        print("box count: ", grid[0], ", box size: ", grid[1])
        print_grid2(grid[0], grid[1])


if __name__ == "__main__":
    main()
