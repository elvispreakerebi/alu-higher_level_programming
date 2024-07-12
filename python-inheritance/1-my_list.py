#!/usr/bin/python3
""" This is the script """

class MyList(list):
    """
    MyList is a subclass of the built-in list class with an additional method
    to print the elements of the list in sorted order.
    """
    def print_sorted(self):
        """
        Prints the elements of the list in ascending sorted order.
        Assumes all elements of the list are integers.
        """
        print(sorted(self))
