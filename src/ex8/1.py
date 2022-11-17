# Write a program that creates a new nested directory (files\ex1) in the current directory. Make sure
# you can re-run your program without an error and create the nested directory using a single
# function call. Next, print a directory listing of the current directory to verify that the new directory
# has been created. Finally, change to the files directory for the remaining exercises (using Python
# code!).

import os

os.makedirs(r"files\ex1", exist_ok=True)
