#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
if n:
    last_dig = abs(n) % 10
    if last_dig > 5:
        print(f"Last digit of {n} is {last_dig} and is greater than 5")
    if last_dig == 0:
        print(f"Last digit of {n} is {last_dig} and is 0")
    elif last_dig < 6 and last_dig != 0:
        print(f"Last digit of {n} is {last_dig} and is less than 6 and not 0")
