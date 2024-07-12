#!/usr/bin/python3
"""
This script demonstrates the usage of the lookup function from the 0-lookup module.
The lookup function returns a list of available attributes and methods of an object.
"""

# Importing the lookup function from the 0-lookup module
lookup = __import__('0-lookup').lookup

# Example class definitions
class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

if __name__ == "__main__":
    # Printing the list of attributes and methods of MyClass1
    print(lookup(MyClass1))
    # Printing the list of attributes and methods of MyClass2
    print(lookup(MyClass2))
    # Printing the list of attributes and methods of the built-in int type
    print(lookup(int))
