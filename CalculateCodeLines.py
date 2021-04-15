# This script fetch all the files with given extension and calculate the code lines
# 
# Ahmed Abdelwadod A. Elkhalifa
# 15/4/2021.


import os
from glob import glob

# Ask the user to enter code directory
search_path = input("Enter directory path to code: ")

file_type = input("Enter code file extension (ex .dart): ")

# Append a directory separator if not already present
if not (search_path.endswith("/") or search_path.endswith("\\") ): 
        search_path = search_path + os.sep
                                                          
# If path does not exist, set search path to current directory
if not os.path.exists(search_path):
        exit(1)

# Get all the code files
file_type = '*' + file_type
files = [y for x in os.walk(search_path) for y in glob(os.path.join(x[0], file_type))]

wholeLines = 0
# Repeat for each file
for fname in files:
    # Open file for reading
    fo = open(fname, encoding='utf-8')

    lines = fo.readlines()
    wholeLines += len(lines)
    fo.close()

print("Number of lines: " + str(wholeLines))