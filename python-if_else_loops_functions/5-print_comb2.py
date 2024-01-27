#!/usr/bin/python3

for number in range(0, 100):
    if number <= 98:
        print(f'{number:02d}', end=', ')
    if number == 99:
        print(f'{number}')
