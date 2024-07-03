#!/usr/bin/python3
"""
This script demonstrates the use of the Square class.

The Square class allows for the creation of square objects with a private
size attribute, which can be accessed and modified through getter and setter
methods. The class also includes a method to calculate the area of the square.
"""

Square = __import__('4-square').Square

# Create a Square instance with size 89
my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

# Change the size of the square to 3
my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

# Attempt to set the size to a non-integer value to demonstrate error handling
try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)
