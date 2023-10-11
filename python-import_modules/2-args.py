#!/usr/bin/python3

import sys

number_of_elements = len(sys.argv) - 1
if number_of_elements == 0:
    print("0 arguments.")
else:
    if number_of_elements == 1:
        print("1 argument:")
    else:
        print(f"{number_of_elements} arguments:")

    for i in range(1, len(sys.argv)):
        print(f"{i}: {sys.argv[i]}")
