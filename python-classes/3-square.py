#!/usr/bin/python3
"""
This module defines a class Square
"""

class Square:
    """
    This class defines a square by its size
    """
    def __init__(self, size=0):
        """
        Initializes the square with a size

        Args:
            size (int): size of a side of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Computes the area of the square

        Returns:
            int: the area of the square
        """
        return self.__size ** 2
