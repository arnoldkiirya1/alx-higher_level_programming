#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(number, "is positive")
elif number == 0:
    print(number, "is zero")
else:
    last_digit = abs(number) % 10
    if number < 0:
        last_digit = -last_digit
    print(last_digit, "is negative")
