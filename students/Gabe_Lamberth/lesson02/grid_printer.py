
# Global vairables
plus = '+ '
dash = '- '
bar = '| '


def printGrid(size):
    # Print arbitrary grid size like image in assignment part 2
    # using variable space to make arbitrary gridsize with value size
    # using round to round up
    space = round(size / 2)

    # I messed around with the formatting so much, that once I found
    # something that worked, I left good enough alone
    print('{}{}'.format(
        (plus + dash * space),
        (plus + dash * space),
    ), end='+')
    print()

    for l in range(space):
        print('{}'.format(bar + '  ' * space) * 3)

    print('{}{}'.format((plus + dash * space), (plus + dash * space),), end='+')
    print()

    for l in range(space):
        print('{}'.format(bar + '  ' * space) * 3)

    print('{}{}'.format(
        (plus + dash * space),
        (plus + dash * space),
    ), end='+')


def printGridRowCol(size, row=0, col=0):
    # Instead of throwing all function calls in the for loop,
    # I instead tested and assigned it to a variable for
    # readablility
    x = (plus + dash * size) * col + plus
    y = (bar * col) + bar
    for i in range(row):
        print(x)
        for i in range(size):
            print('\t'.join(y).expandtabs(size + 1))
    print(x)


def main():
    # Part two with single value given
    tstNum1 = 3
    tstNum2 = 10
    print('Printing grid with value of 3:')
    printGrid(tstNum1)
    print()
    print('Printing grid with value of 10:')
    printGrid(tstNum2)
    print()
    print()

    # Part three with multiple values givien
    gridSize, rows, columns = 4, 3, 5

    print("Printing grid with multiple Values given 4, 3, 5", end='\n')
    printGridRowCol(gridSize, rows, columns)
    print()
    gridSize, rows, columns = 5, 3, 7
    print("Printing grid with multiple Values given 5, 3, 7", end='\n')
    printGridRowCol(gridSize, rows, columns)


if __name__ == "__main__":
    main()
