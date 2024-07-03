#!/usr/bin/python3
"""
This script demonstrates the use of the Square class defined in 3-square.py.
It creates instances of the Square class and prints their area.
"""

Square = __import__('3-square').Square

def main():
    """
    Main function to create square instances and print their area.
    """
    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))

if __name__ == "__main__":
    main()
