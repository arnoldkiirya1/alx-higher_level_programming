#!/usr/bin/python3

def safe_print_integer(value):
    """
    Safely prints an integer value.

    Args:
        value (int): Integer value to print.

    Returns:
        bool: True if value is successfully printed, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except:
        return False
