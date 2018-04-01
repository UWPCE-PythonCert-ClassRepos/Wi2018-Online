#!/usr/bin/env python3
# -----------------------------------------------------------
# file_lab_list_files.py
#  demonstrates basic file operations
# -----------------------------------------------------------

import os


# Activity 2 - File Lab
cwd = os.getcwd()
dir_items = os.listdir(cwd)

print("Current working directory is:\n", cwd)
print("List of files in current working directory:")

for item in dir_items:
    full_path = os.path.join(cwd, item)
    if os.path.isfile(full_path):
        print('', full_path)




