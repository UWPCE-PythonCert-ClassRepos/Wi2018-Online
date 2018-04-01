#!/usr/bin/env python3


def print_column(size_of_grid, cell_size):
    for cell in range(cell_size):
        for num in range(size_of_grid):
            print('|', '  ' * cell_size, end='')
        print('|')


def print_row(size_of_grid, cell_size):
    for num in range(size_of_grid):
        print('+', '- ' * cell_size, end='')
    print('+')


def print_grid2(size_of_grid, cell_size):
    for i in range(size_of_grid):
        print_row(size_of_grid, cell_size)
        print_column(size_of_grid, cell_size)
    print_row(size_of_grid, cell_size)


print_grid2(5, 3)




