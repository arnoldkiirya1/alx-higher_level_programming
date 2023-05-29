#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Safely prints the first 'x' integers from 'my_list'.

    Args:
        my_list (list): List of elements.
        x (int): Number of elements to print.

    Returns:
        int: Number of integers printed.
    """
    printed = 0
    try:
        for element in my_list[:x]:
            if isinstance(element, int):
                print("{:d}".format(element), end="")
                printed += 1
    except:
        pass
    finally:
        print()
        return printed
