#!/usr/bin/python3
def pow(a, b):
    if b >= 0:
        result = 1
        for i in range(b):
            result *= a
    else:
        result = 1
        for i in range(-b):
            result /= a
    return result
