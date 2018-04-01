#( 2, 123.4567, 10000, 12345.67)
#and produce:
#'file_002 :   123.46, 1.00e+04, 1.23e+04'
strformat = (2, 123.4567, 10000, 12345.67)
formatter='file_{:0>3d}, {:.2f}, {:.2e}, {:.2e}'
formatter.format(*strformat)

#Using your results from Task One, repeat the exercise, but this time using an
#alternate type of format string (hint: think about alternative ways to use .format()
#(keywords anyone?), and also consider f-strings if you’ve not used them already).

def display_nums(seq):
    ...:     l = len(seq)
    ...:     print (("There are {} your numbers:" + ", ".join(["{}"] * l)).format
    ...: (l, *seq))
