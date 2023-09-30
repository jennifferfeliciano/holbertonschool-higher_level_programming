#!/usr/bin/python3
def pow(a, b):
    result = 1  # Initialize the result to 1
    for _ in range(b):
        result *= a  # Multiply result by a 'b' times
    return result
