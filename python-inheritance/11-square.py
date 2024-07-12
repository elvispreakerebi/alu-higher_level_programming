#!/usr/bin/python3
""" This is the script """

class BaseGeometry:
    """
    BaseGeometry class with methods to calculate the area and validate integers.
    """
    def area(self):
        """
        Raises an Exception to indicate that the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value of the parameter to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height.

        Args:
            width (int): Width of the rectangle (positive integer).
            height (int): Height of the rectangle (positive integer).
        """
        super().__init__()  # Call the initializer of the BaseGeometry class
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes the area of the rectangle.

        Returns:
            int: Area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the Rectangle.

        Returns:
            str: String representation of the rectangle in the format '[Rectangle] <width>/<height>'.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """
    def __init__(self, size):
        """
        Initializes a Square instance with a size.

        Args:
            size (int): Size of the square (positive integer).
        """
        super().__init__(size, size)  # Initialize Rectangle with size for both width and height
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
            str: String representation of the square in the format '[Square] <size>/<size>'.
        """
        return f"[Square] {self.__size}/{self.__size}"
