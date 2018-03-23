### Explore Errors ###
### These functions demonstrate the different types of errrors ###

def name_error():
    """ This method causes the NameError exception to happen,
        by printing not available string """
    print("I am printing not available string to generate NameError exception")
    print(non_exist_variable)

def type_error():
    """ This method causes the TypeError exception to happen,
        by string to integer
    """
    print("\nAdding string to integer to generate TypeError exception")
    print("string" + 1)


def syntax_error():
    """ This method causes the SyntaxError exception to happen,
        by having syntax error in print statement
    """
    code="print(\"hey printing with syntax error\"))"
    print("\nPrinting statement with out parenthesis to generate syntax error")
    exec(code)

def attribute_error():
    """ This method causes the AttributeError exception to happen,
        by accessing un available attributes of module
    """
    print("\ntrying to access non available attribute of empty list")
    list = []
    print(list.nonexistattribute)

if __name__ == "__main__":
    for function in [name_error, type_error, syntax_error, attribute_error]:
        try:
            function()
        except Exception as e:
            print(repr(e))







