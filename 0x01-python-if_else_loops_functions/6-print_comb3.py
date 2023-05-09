#!/usr/bin/python3
for i in range(10):
    for j in range(i+1, 10):
        if i == 0:
            print("{:02d}".format(j), end=", ")
        else:
            print("{:02d}".format(j+i*10), end=", ")
print("\b\b ")

