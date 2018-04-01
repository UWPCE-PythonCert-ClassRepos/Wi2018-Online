#!/usr/bin/env python3

# Filename: file_lab.py
# Daniel Grubbs
import os


def main():
    """Main function of the program."""
    print_header()
    overview = "Tasks from lesson04 file assignment.\n"
    print(overview)
    file_operations()
    copy_source_to_destination()


def print_header():
    """Print the header of the program."""
    print('------------------------------------')
    print('             Lesson04')
    print('          File Assignment')
    print('------------------------------------\n')


def file_operations():
    """Function to perform file/directory operations."""
    current_dir = os.getcwd()
    files_in_directory = os.listdir(current_dir)

    for i, f in enumerate(files_in_directory, 1):
        print(i, f)


def copy_source_to_destination():
    """Copy a file contents from a source, to a destination" without using shutil or the OS copy command."""
    with open('some_file.txt', 'rb') as fout:
        with open('output.txt', 'wb') as fin:
            for line in fout:
                fin.write(line)


if __name__ == '__main__':
    main()
