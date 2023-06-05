#!/usr/bin/python3
# 5-text_indentation.py
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    indentation = ""
    for char in text:
        if char == '.' or char == '?' or char == ':':
            print(char + "\n\n" + indentation, end="")
            indentation = ""
        else:
            print(char, end="")
            if char == '\n':
                indentation = ""
            elif char != ' ':
                indentation += char
