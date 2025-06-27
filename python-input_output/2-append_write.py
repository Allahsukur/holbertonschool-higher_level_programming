#!/usr/bin/python3
"""This module contains append_write() function"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and
    returns the number of characters added
    Parameters
    ----------
        filename : str
        text : str
    Return
    ------
        int
            The number of characters appended
    """
    with open(filename, mode="a", encoding="UTF-8") as file:
        number_of_characters = file.write(text)
    return number_of_characters
