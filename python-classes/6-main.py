#!/usr/bin/python3
"""
This script demonstrates the use of the Square class
from the 6-square module.

The script creates instances of the Square class with different sizes
and positions, and uses the my_print() method to print them.
"""

Square = __import__('6-square').Square

# Create a square with size 3 and default position (0, 0)
my_square_1 = Square(3)
# Print the square
my_square_1.my_print()

print("--")

# Create a square with size 3 and position (1, 1)
my_square_2 = Square(3, (1, 1))
# Print the square
my_square_2.my_print()

print("--")

# Create a square with size 3 and position (3, 0)
my_square_3 = Square(3, (3, 0))
# Print the square
my_square_3.my_print()

print("--")
