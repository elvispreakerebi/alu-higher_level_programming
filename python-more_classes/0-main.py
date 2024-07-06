#!/usr/bin/python3
"""
This script tests the Rectangle class from the module 0-rectangle.
"""

Rectangle = __import__('0-rectangle').Rectangle

if __name__ == "__main__":
    my_rectangle = Rectangle()
    print(type(my_rectangle))
    print(my_rectangle.__dict__)
