#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2.

    Args:
        a_dictionary (dict): The dictionary to multiply the values.

    Returns:
        dict: A new dictionary with all values multiplied by 2.
    """
    multiplied_dict = {}

    for key, value in a_dictionary.items():
        multiplied_dict[key] = value * 2

    return multiplied_dict
