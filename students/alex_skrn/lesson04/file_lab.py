"""Lesson04 - Activity 2: Files."""

import os
# import time
import tkinter as tk
from tkinter import filedialog


def print_curr_dir_files():
    """Print the full path for all files in the current dir, 1 per line."""
    for file in os.listdir():
        print(os.path.abspath(file))


def copy_any_binary(source, destination):
    """Copy a file from a source to a destination (~1 min for a 3GB file)."""
    with open(source, 'rb') as fromF, open(destination, 'wb') as toF:
        source_size = os.path.getsize(source)
        chunk_size = 1000000
        num_steps = source_size // chunk_size
        print("Copying...")
        # start_time = time.time()
        for _ in range(num_steps):
            toF.write(fromF.read(chunk_size))
        toF.write(fromF.read())
        # mytime = time.time() - start_time
        # print("Elapsed time = {:.0f} minutes".format(mytime/60))


def copy_file_user_interaction():
    """Interact with the user on file copying operations."""
    root = tk.Tk()
    root.withdraw()

    # Get the name of the source file from the user.
    print("Choose a file to be copied in the open dialog")
    source_path = filedialog.askopenfilename()
    print("You chose {}\n".format(source_path))

    # Get the target directory for the source copy from the user.
    print("Select a directory to save a copy of the file")
    target_dir = filedialog.askdirectory()
    print("You selected {}\n".format(target_dir))

    # Construct the full path name for the copy of the source file.
    source_name = os.path.split(source_path)[1]
    target_path = "{}/copy_of_{}".format(target_dir, source_name)

    # Copy the source to the target destination.
    copy_any_binary(source_path, target_path)
    print("Copied {} to {}".format(source_path, target_path))


if __name__ == "__main__":
    # print_curr_dir_files()
    copy_file_user_interaction()
