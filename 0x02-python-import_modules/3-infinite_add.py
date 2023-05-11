#!/usr/bin/python3

import sys

if __name__ == "__main__":
   """Print the addition of all arguments."""
    total = sum(int(arg) for arg in sys.argv[1:])
    print("{}".format(total))
