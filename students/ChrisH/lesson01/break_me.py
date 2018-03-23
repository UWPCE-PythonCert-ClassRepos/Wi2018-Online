# UW Python 210 - Lesson01
#  write four simple Python functions
#  each function should result in one of the four most common exceptions


def exception_name_error():
    print(this_global_variable_doesnt_exist)
    return


def exception_type_error():
    value1 = "elephant"
    value2 = 5
    return value1 + value2


def exception_attribute_error():
    testobject = []
    return testobject.runaroundaflagpole


def exception_syntax_error(code):
    exec(code)
    return


if __name__ == "__main__":

    for fn, arg in [
            (exception_name_error, None),
            (exception_attribute_error, None),
            (exception_syntax_error, 'if 5 == 5: print("hi")'),  # This executes w/out error
            (exception_syntax_error, 'if 5 = 5: print("hi")'),  # This throws error, can't set 5 to 5
            (exception_type_error, None)]:
        try:
            if arg:
                fn(arg)
            else:
                fn()
        except BaseException as e:
            print(repr(e))
            pass
