#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to delete the key from.
        key (str): The key to delete. Defaults to an empty string.

    Returns:
        None
    """
    if key in a_dictionary:
        del a_dictionary[key]

