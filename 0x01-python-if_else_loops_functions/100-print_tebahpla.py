#!/usr/bin/python3
i = 0
for c in range(ord('z'), ord('A') - 1, -1):
    print("{}".format(chr(c + i)), end="")
    i = 32 - i if i == 0 else 0
print()
