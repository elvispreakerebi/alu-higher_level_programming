#!/usr/bin/python3
"""
This script demonstrates the use of the Rectangle class.

The Rectangle class defines a rectangle by its width and height, 
and includes methods for calculating the area and perimeter.

Example usage:
    $ ./2-main.py
"""

Rectangle = __import__('2-rectangle').Rectangle

# Create a rectangle with width 2 and height 4
my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

# Update the rectangle's width to 10 and height to 3
my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
