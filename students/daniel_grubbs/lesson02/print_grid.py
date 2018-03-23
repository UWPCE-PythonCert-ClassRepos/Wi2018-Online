#!/usr/bin/env python3

# Variables section
plus = "+ "
minus = "- "
pipe = "| "
space = "  "


def main():
    """Main execution of the program."""
    print_header()
    row = int(input('Enter the number of rows for the grid: '))
    column = int(input('Enter the number of columns for the grid: '))
    width = int(input('Enter the width for the grid: '))
    print_grid(row, column, width)


def print_header():
    """Print out a header for the program."""
    print('-----------------------------')
    print('    Print Grid Assignment')
    print('-----------------------------\n')


def print_grid(row, column, width):
    """Build the structure of the grid."""
    box_top = plus + minus * width
    box_side = pipe + space * width

    # Iterate through and build the box based on inputs
    for i in range(row):
        print(box_top * column + plus)
        for j in range(width):
            print(box_side * column + pipe)
    print(box_top * column + plus)


if __name__ == '__main__':
    main()
