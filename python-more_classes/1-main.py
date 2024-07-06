#!/usr/bin/python3
"""
This script demonstrates the usage of the Rectangle class.

It creates a Rectangle instance, prints its initial state, updates its width 
and height, and then prints its updated state.
"""

Rectangle = __import__('1-rectangle').Rectangle

# Creating a new Rectangle instance with width 2 and height 4
my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)  # Expected output: {'_Rectangle__width': 2, '_Rectangle__height': 4}

# Updating the width and height of the Rectangle instance
my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)  # Expected output: {'_Rectangle__width': 10, '_Rectangle__height': 3}
