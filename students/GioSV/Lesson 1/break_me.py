#In the break_me.py file write four simple Python functions:
#Each function, when called, should cause an exception to happen
#Each function should result in one of the install package four most common exceptions you’ll find.
#For review: NameError, TypeError, SyntaxError, AttributeError
#Hint – the interpreter will quit when it hits a Exception – so you can comment out all but the one you are testing at the moment.
#Use the Python standard library reference on Built In ExceptionsLinks to an external site. as a reference
#https://docs.python.org/3/library/exceptions.html

# Attribute references
# An attribute reference is a primary followed by a period and a name:
# attributeref ::=  primary "." identifier

# The primary must evaluate to an object of a type that supports attribute references, which most objects do. 
# This object is then asked to produce the attribute whose name is the identifier. This production can be customized by overriding the __getattr__() method. If this attribute is not available, the exception AttributeError is raised. Otherwise, the type and value of the object produced is determined by the object. Multiple evaluations of the same attribute reference may yield different objects.
            # CODE BEGINS
            # Atrribute Error example (evaluate)
            # string1= "whatever"
            # string1.capitalze
            # CODE ENDS
# This should come back with an attribute error, as I was suppose to type the attribute 'capitalize' and ended up misstyping it instead.
# Update: it worked! 


# exception NameError
# Raised when a local or global name is not found. This applies only to unqualified names. The associated value is an error message that includes the name that could not be found.
            # CODE BEGINS
            # Name Error example (evaluate)
            # x= 5
            # z= x+y
            # z
            # CODE ENDS
# I would understand this should come back with a name error, as y is not define and the operation is not possible.


# exception SyntaxError
# Raised when the parser encounters a syntax error. This may occur in an import statement, in a call to the built-in functions exec() or eval(), or when reading the initial script or standard input (also interactively).
# Instances of this class have attributes filename, lineno, offset and text for easier access to the details. str() of the exception instance returns only the message.
            # Syntax Error example (evaluate)
            # x="hello_there"
            # a= 3
            # z=5x
            # w= 5 x
            # v= x a
# z, w and v provoke a syntax error, as you putting an integer next to a string does not comeup with a known solution.


# exception TypeError
#     Raised when an operation or function is applied to an object of inappropriate type. The associated value is a string giving details about the type mismatch.
#     This exception may be raised by user code to indicate that an attempted operation on an object is not supported, and is not meant to be. If an object is meant to support a given operation but has not yet provided an implementation, NotImplementedError is the proper exception to raise.
#     Passing arguments of the wrong type (e.g. passing a list when an int is expected) should result in a TypeError, but passing arguments with the wrong value (e.g. a number outside expected boundaries) should result in a ValueError.
            # Type Error example (evaluate)
            # x="hello_there"
            # a= 3
            # z=x + a
# Technically, this is a case of Type Error, as you cannot add an integer and a string.
