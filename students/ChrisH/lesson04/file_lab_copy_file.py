#!/usr/bin/env python3
# -----------------------------------------------------------
# file_lab_copy_file.py
#  demonstrates basic file copying, using binary mode
#  without using shutil, or the OS copy command
# -----------------------------------------------------------


import os


def check_file(fname, oper):
    """
    Takes a file name and operation in the form 'w' or 'r'. Determines if the file exists
    and prompts the user for confirmation action if needed.
    :param fname: a file name & path
    :param oper: 'w' if the file is to be written to, 'r' if it is to be read from
    :return: False - if file not found(r) or user does not want to overwrite(w). True otherwise.
    """
    if oper == 'r' and not os.path.isfile(fname):
        print('Could not find file: {}'.format(fname))
        return False
    elif oper == 'w' and os.path.isfile(fname):
        while True:
            ans = input('File "{}" already exists, overwrite (Y/n):'.format(fname))
            if ans == '' or ans.lower() == 'y':
                break
            else:
                return False
    return True

def bin_copyfile(file_in, file_out):
    """
    Copies a file from file_in to file_out in 50 byte chunks. Returns bytes written, or False if
    file checks fail.
    :param file_in: file to read
    :param file_out: file to write
    :return: bytes written or False if unable to perform operation
    """
    if not (check_file(file_in, 'r') and check_file(file_out, 'w')):
        return False

    total_bytes = 0
    with open(file_in, 'rb') as file_in:              # method removes need to have a file.close operation
        with open(file_out, 'wb') as file_out:
            while True:
                buffer = file_in.read(50)                   # read file in 50 byte chunks
                total_bytes += file_out.write(buffer)
                if len(buffer) < 50 or buffer == '':        # buffer will be empty at end of file, or have <50 bytes
                    break
    return total_bytes


if __name__ == "__main__":

    # tests for file read/write ability
    assert check_file('shark.jpg','r') == True
    assert check_file('sk.jpg','r') == False
    assert check_file('shark_out.jpg', 'w') == True
    assert check_file('sk.jpg', 'w') == True

    # File copy tests.
    files = [ ('./shark.jpg', './shark_out.jpg'), ('./hobbes_markov.txt', './hobbes_markov_out.txt')]
    for file in files:
        print("Copy file '{}' to '{}'".format(*file))
        print("Bytes written: {:d}".format(bin_copyfile(*file)))
