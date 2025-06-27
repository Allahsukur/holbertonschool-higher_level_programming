#!/usr/bin/python3
"""This module contains read_file() function"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout

    Parameters
    ----------
        filename : str
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
