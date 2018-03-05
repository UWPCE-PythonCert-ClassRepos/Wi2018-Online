# here is a mostly-straightforward solution to the
# two-by-two version of the grid.

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print ('+ - - - -',end=' '),

def print_post():
    print ('|        ', end=' '),

def print_beams():
    do_twice(print_beam)
    print ('+')

def print_posts():
    do_twice(print_post)
    print ('|')

def print_row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_twice(print_row)
    print_beams()

print_grid()

if __name__=="__main__":
    print('This is run as module')


# here is a less-straightforward solution to the
# four-by-four grid
