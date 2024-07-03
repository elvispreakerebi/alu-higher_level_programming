#!/usr/bin/python3
class Square:
    """Represents a square with a private instance attribute size."""
    
    def __init__(self, size=0):
        """Initializes the square with a given size.
        
        Args:
            size (int): The size of the square, default is 0.
        """
        self.size = size

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square, with type and value validation.
        
        Args:
            value (int): The size to set for the square.
        
        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square.
        
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
