#!/usr/bin/python3


class CountedIterator:
    """
    A custom iterator that tracks the number of items iterated over.
    """

    def __init__(self, iterable):
        """
        Initialize the iterator and counter.

        Args:
            iterable: An iterable object to create the iterator from.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Return the next item from the iterator and increment the counter.

        Raises:
            StopIteration: If there are no more items to iterate.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """
        Return the number of items that have been iterated over.

        Returns:
            int: The current count of iterated items.
        """
        return self.count
