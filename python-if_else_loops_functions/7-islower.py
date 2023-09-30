#!/usr/bin/python3
def islower(c):
    if len(c) == 0:
        # Handle the case of an empty string
        return False
    elif ord('a') <= ord(c) <= ord('z'):
        return True
    else:
        return False
