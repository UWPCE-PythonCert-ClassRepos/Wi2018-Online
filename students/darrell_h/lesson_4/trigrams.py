#!/usr/local/bin/python3


import string


def strip_characters(str):
    return ''.join(char for char in str if char not in (string.punctuation + string.whitespace + string.digits))


def create_list_from_file(filename):
    result = []
    i = 0
    with open(filename, "r") as myfile:
        for line in myfile:
            for word in line.split():
                result.append(strip_characters(word))
    return result


def create_tigram(filename):
    l = create_list_from_file(filename)
    #  some code here that iterates through this list...


if __name__ == "__main__":
    pass
