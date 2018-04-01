#!/usr/bin/env python3
import os
import pathlib
import time


def read_file():
    file_list()
    path = pathlib.Path(input("\nEnter the file to read: "))
    with path.open('r', encoding='utf-8') as handle:
        content = handle.read()

    print(content)


def file_list():
    # Iterate of the files of the current directory
    pth = pathlib.Path.cwd()
    for f in pth.iterdir():
        if f.is_dir():
            continue
        else:
            print(f)


def copy_file():
    """Copy a file from a source to a destination (~1 min for a 3GB file)."""
    file_list()
    source = pathlib.Path(input("\nEnter the file to copy: "))
    """Sending file to users home directory"""
    destination = pathlib.Path.home() / source
    """Found this solution from another student, but added slight modification"""
    with source.open('rb') as source_file, destination.open('wb') as dest_file:
        source_size = os.path.getsize(str(source))
        chunk_size = 1000000
        num_steps = source_size // chunk_size
        print("Copying...")
        """This for loop iterates without using the counter"""
        for _ in range(num_steps):
            dest_file.write(source_file.read(chunk_size))
        dest_file.write(source_file.read())

    print('File copied to {}'.format(destination))


def quit_menu():
    print("Shutting down program, Goodbye", end='\n')
    return "exit menu"


def user_selection(user_prompt, queue_dict):
    """run until user selects exit"""
    while True:
        response = input(user_prompt)
        if queue_dict[response]() == "exit menu":
            break


def main():
    print('\n>>>>>>>>>>Welcome to the Python File Program<<<<<<<<<<')
    print('The current time and date is:', time.asctime())
    user_prompt = ("\nWhat would you like to do?\n"
                   "Type '1- To Display all contents in current directory\n"
                   "Type '2- To Read a file'\n"
                   "Type '3- To Copy a file\n"
                   "Type 'q- To end the program'\n"
                   "Enter value here >> ")

    # Create dictionary with calls to functions
    menu_dict = {"1": file_list, "2": read_file, "3": copy_file, "q": quit_menu}
    # Pass the user_prompt and menu_dict to the user_selection function
    user_selection(user_prompt, menu_dict)


if __name__ == "__main__":
    main()