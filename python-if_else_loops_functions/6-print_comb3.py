#!/usr/bin/python3

for first_digit in range(100):
    for second_digit in range(first_digit + 1, 10):
        if second_digit != first_digit:
            if first_digit == 8 and second_digit == 9:
                print(f'{first_digit:1d}{second_digit:1d}')
            else:
                print(f'{first_digit:1d}{second_digit:1d}', end=', ')

