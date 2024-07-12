#!/usr/bin/python3
""" This is the script """
def is_same_class(obj, a_class):
    """
    Function to check if an object is exactly an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
