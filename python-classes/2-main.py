#!/usr/bin/python3
"""
This script demonstrates the usage of the Square class.
"""

Square = __import__('2-square').Square

# Creating a Square instance with size 3
my_square_1 = Square(3)
print(type(my_square_1))  # Expected output: <class '2-square.Square'>
print(my_square_1.__dict__)  # Expected output: {'_Square__size': 3}

# Creating a Square instance with default size (0)
my_square_2 = Square()
print(type(my_square_2))  # Expected output: <class '2-square.Square'>
print(my_square_2.__dict__)  # Expected output: {'_Square__size': 0}

# Trying to access the private attribute size directly
try:
    print(my_square_1.size)
except Exception as e:
    print(e)  # Expected output: 'Square' object has no attribute 'size'

# Trying to access the private attribute __size directly
try:
    print(my_square_1.__size)
except Exception as e:
    print(e)  # Expected output: 'Square' object has no attribute '__size'

# Attempting to create a Square instance with a non-integer size
try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)  # Expected output: size must be an integer

# Attempting to create a Square instance with a negative size
try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)  # Expected output: size must be >= 0
