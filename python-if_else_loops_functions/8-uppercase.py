#!/usr/bin/python3
def uppercase(input_str):
    for char in input_str:
        if 'a' <= char <= 'z':
            print(chr(ord(char) - ord('a') + ord('A')), end='')
        else:
            print(char, end='')
    print()
