def formatter(*flex_tuple):
    """
    Takes an arbitrary number of values multiplies it
    with formatters, form_string takes the formatting values
    """
    tuple_len = len(flex_tuple)
    form_string = "The {} numbers are: " + ", ".join(["{:d}"] * tuple_len)
    return form_string.format(tuple_len, *flex_tuple)


def main():
    tuple_items = (2, 123.4567, 10000, 12345.67)
    print("{:-^70s}".format("Task One"), end='\n')
    print("Using each tuple element value for string formatter reference: ", end='\n')
    print('file_{:0>3d} : {:.2f}, {:.2e}, {:.3e}'.format(tuple_items[0], tuple_items[1], tuple_items[2], \
                                                         tuple_items[3]))

    print("{:-^70s}".format("Task Two"), end='\n')
    print("Results with string format *value and using 'f-string':", end='\n')
    print('file_{:0>3d} : {:.2f}, {:.2e}, {:.3e}'.format(*tuple_items))
    print(f"file_{tuple_items[0]:03d} :{tuple_items[1]:7.2f}, {tuple_items[2]:.2e}, {tuple_items[3]:.3e}")

    print("{:-^70s}".format("Task Three"), end='\n')
    print(formatter(1, 2, 3))
    print(formatter(1, 2, 3, 4, 5))

    print("{:-^70s}".format("Task Four"), end='\n')
    items = (4, 30, 2017, 2, 27)
    # Output will be: '02 27 2017 04 30'    
    print("{3:02d} {4:02d} {2:d} {0:02d} {1:02d}".format(*items))

    print("{:-^70s}".format("Task Five"), end='\n')
    list_items = ['oranges', 1.3, 'lemons', 1.1]
    orange, o_weight, lemon, l_weight = list_items
    print(f"The weight of an {orange[:-1]} is {o_weight} lsbs & {lemon[:-1]} is {l_weight} lbs")
    print("Printing the string above with .upper() method & changing the weight value.")
    print(
        f"The weight of an {orange[:-1].upper()} is {o_weight+(1*.20)} lbs & {lemon[:-1].upper()} is {l_weight+(1*.20)} lbs")

    print("{:-^70s}".format("Task Six"), end='\n')

    names = [('Win Butler', 30, 10400000), ('Régine Chassagne', 35, 10500000), ('William Butler', 28, 10200000),
             ('Richard Reed Parry', 34, 10100000)]
    print("{:^14} {:^13} {:^11}".format('Name', 'Age', 'Cost'))
    for name in names:
        print("{:<20}{:<8d}${:^11,.2f}".format(*name))

    numbers = "0123456789"
    print(f"{'     '.join(numbers)}")


if __name__ == "__main__":
    main()