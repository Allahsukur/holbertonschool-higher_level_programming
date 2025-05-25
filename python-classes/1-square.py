#!/usr/bin/python3
"""A module that defines a Square class with a private size attribute."""

class Square:
    """A class that defines a square with a private size attribute."""
    
    def __init__(self, size):
        """Initialize a new Square instance with a given size.
        
        Args:
            size: The size of the square (no type or value verification).
        """
        self.__size = size