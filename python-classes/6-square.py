#!/usr/bin/python3
"""
This module defines a class Square that defines a square by
private instance attributes for size and position,
property getters and setters for size and position,
public instance methods for calculating area and printing the square.
"""


class Square:
    """A class that defines a square by its size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with optional size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square, with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square, with type and value checks."""
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #, considering the position."""
        if self.__size == 0:
            print("")
            return

        [print("") for _ in range(self.__position[1])]
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
