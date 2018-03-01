"""
*args and **kwargs in python explained
https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/
"""


def test_var_args(f_arg, *argv):
    print "first normal arg:", f_arg
    for arg in argv:
        print "another arg through *argv :", arg


test_var_args('yasoob', 'python', 'eggs', 'test')


def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.iteritems():
            print "%s == %s" % (key, value)


greet_me(name="yasoob",age=10)

#  So here we will see how to call a function using *args and **kwargs.
#  Just consider that you have this little function:
def test_args_kwargs(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3


# first with *args
args = ("two", 3, 5)
test_args_kwargs(*args)
#  arg1: two
#  arg2: 3
#  arg3: 5

# now with **kwargs:
kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)
#  arg1: 5
#  arg2: two
#  arg3: 3
