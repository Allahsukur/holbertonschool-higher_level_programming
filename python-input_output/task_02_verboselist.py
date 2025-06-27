#!/usr/bin/python3
"""This module contains VerboseList class"""

class VerboseList(list):
    """
    A subclass of list that logs actions when modifying the list.
    """

    def append(self, element):
        """
        Append an element to the list, printing a message before adding.
        """
        print(f"Added [{element}] to the list.")
        super().append(element)

    def extend(self, element):
        """
        Extend the list with elements, printing a message before adding.
        """
        print(f"Extended the list with [{len(element)}] items.")
        super().extend(element)

    def remove(self, element):
        """
        Remove the first occurrence of an element, printing a message.
        """
        print(f"Removed [{element}] from the list.")
        super().remove(element)

    def pop(self, index=None):
        """
        Pop an element at the specified index, printing a message.
        If no index is provided, pop the last element.
        """
        if index is None:
            index = len(self) - 1
        print(f"Popped [{self[index]}] from the list.")
        
        popped = super().pop(index)
        return popped
