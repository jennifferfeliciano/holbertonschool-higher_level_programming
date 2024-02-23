#!/usr/bin/python3

import sys
if __name__ =="__main__":
    args = len(sys.argv) - 1

    if args == 0:
        print("0 arguments.")
    elif args == 1:
        print("1 argument:")
    else:
        print(f"{args} arguments:")

        if args >= 1:
            for i, arg in enumerate(sys.argv[1:], start=1):
                print(f"{i}: {arg}")
