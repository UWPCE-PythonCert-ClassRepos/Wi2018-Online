#!/usr/bin/env python3
from decimal import Decimal


def string_format1(format_string):
    format_newstr1 = "file_" + '%03d' % format_string[0]
    format_newstr2 = str(round(float(format_string[1]), 2))
    format_newstr3 = '%.2E' % Decimal(format_string[2])
    format_newstr4 = '%.2E' % Decimal(format_string[3])
    print(format_newstr1 + ": " + format_newstr2 + ", " + format_newstr3 + ", " + format_newstr4)

def string_format2(format_string):
    format_newstr1 = "file_" + '%03d' % format_string[0]
    format_newstr2 = str(round(float(format_string[1]), 2))
    format_newstr3 = '%.2E' % Decimal(format_string[2])
    format_newstr4 = '%.2E' % Decimal(format_string[3])
    print("{} :   {}, {}, {}".format(format_newstr1, format_newstr2, format_newstr3, format_newstr4))

def string_format3(tuple_number):
    tuple_length = len(tuple_number)
    format_string = "{:d}, " * tuple_length
    actual_format = format_string.format(*tuple_number)
    print("The {} number are {}".format(tuple_length, actual_format))

def fstring_format4(input_tup):
    #Output should be '02 27 2017 04 30'
    print('{3} {4} {2} {0} {1}'.format('%.02d'%input_tup[0], input_tup[1], input_tup[2], '%.02d'%input_tup[3], input_tup[4]))

def format_string5(input_lis):
    #Output should be The weight of an orange is 1.3 and the weight of a lemon is 1.1
    print('The weight of an {0} is {1} and the weight of a {2} is {3}'.format(input_lis[0].upper(), '%.02d'%input_lis[1], input_lis[2].upper(), '%.02d'%input_lis[3]))

def format_string6(input_lists):
    for every_list in input_lists:
        print('{:10}{:15}{:15}'.format(every_list[0], every_list[1], every_list[2]))

if __name__ == "__main__":
    string_format1((2, 123.4567, 10000, 12345.67))
    string_format2((2, 123.4567, 10000, 12345.67))
    string_format3((2, 3, 4, 5))
    string_format3((1, 2, 3, 4, 5, 6, 7))
    fstring_format4((4, 30, 2017, 2, 27))
    format_string5(['orange', 1.3, 'lemon', 1.1])
    format_string6([['Cow1', '2years', '2lb'], ['Cow2', '4years', '5lb'], ['Cow3', '1year', '1lb']])
