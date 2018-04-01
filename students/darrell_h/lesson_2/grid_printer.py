#!/usr/local/bin/python3

def print_grid(width,columns,rows):
    result = ""

    result += corner_row(width,columns)
    for i in range(rows):
        if i < rows:
            # add internal_row and a corner_row
            result += internal_row(width,columns)
            result += corner_row(width,columns)
        else:
            # just finish with a corner row.
            result += corner_row(width,columns)
    print(result)

def corner_row(width,columns):
    result = ""
    plus = '+'
    minus = '-'

    result += plus + ' '
    for i in range(columns):
        result += (minus + ' ') * width
        result += plus + ' '
    result += "\n"
    return result

def internal_row(width,columns):
    result = ""
    pipe = '|'

    result += pipe + ' '
    for i in range(columns):
        result += ('  ') * width
        result += pipe + ' '
    result += "\n"
    return result * width



print_grid(width=5,columns=3,rows=3)
