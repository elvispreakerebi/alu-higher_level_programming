#!/usr/bin/python3
"""Script to test the Square class."""

Square = __import__('4-square').Square

def main():
    """Main function to demonstrate the usage of the Square class."""
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
