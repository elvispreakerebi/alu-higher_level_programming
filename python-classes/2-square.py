#!/usr/bin/python3
"""
This module defines a class Square.
"""

class Square:
    """
    This class represents a square with a private instance attribute size.
    """
    def __init__(self, size=0):
        """
        Initializes the square with an optional size (default is 0).
        size must be an integer and greater than or equal to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
