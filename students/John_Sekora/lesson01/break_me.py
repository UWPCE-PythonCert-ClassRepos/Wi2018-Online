# NameError: (undefined variable)
def fun_name(f):
    try:
        cat = f + dog
    except NameError as e:
        print('Handling run-time error:', e)

fun_name(1)

# TypeError: (different class variables)
def fun_type(m):
    try:
        3 + '7' + m
    except TypeError as e:
        print('Handling run-time error:', e)

fun_type(1)

# SyntaxError: (improper syntax)
def fun_syntax(name):
    try:
        while True
            print("Nice to meet you: " + name)
            break
    except SyntaxError as e:
        print('Handling run-time error:', e)

fun_syntax("Steve")

# AttributeError: (I don't know what this is)
def fun_attribute(d):
    try:

    except AttributeError as e:
        print('Handling run-time error:', e)

fun_attribute(1)


