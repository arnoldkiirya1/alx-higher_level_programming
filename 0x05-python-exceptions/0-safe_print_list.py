#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    printed = 0
    try:
        for element in my_list[:x]:
            print(element, end="")
            printed += 1
    except:
        pass
    finally:
        print()
        return printed
