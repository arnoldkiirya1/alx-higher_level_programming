#!/usr/bin/python3
def uppercase(s):
    result = ""
    for c in s:
        if ord('a') <= ord(c) <= ord('z'):
            result += "{}".format(chr(ord(c) - 32))
        else:
            result += "{}".format(c)
    print(result)
