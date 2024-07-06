#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

# Creating a new Rectangle instance with width 2 and height 4
my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

# Updating the width and height of the Rectangle instance
my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)
