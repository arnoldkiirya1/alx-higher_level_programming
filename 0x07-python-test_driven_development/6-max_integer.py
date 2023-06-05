#!/usr/bin/python3
"""Module to find the max integer in a list"""


def max_integer(list_=[]):
    """Function to find and return the max integer in a list of integers.
    
    Args:
        list_ (list): List of integers.
    
    Returns:
        int: The maximum integer in the list.
            If the list is empty, returns None.
    """
    if len(list_) == 0:
        return None
    
    max_num = list_[0]
    
    for num in list_[1:]:
        if num > max_num:
            max_num = num
    
    return max_num
