#!/usr/bin/python3
""" This is the script """

def is_kind_of_class(obj, a_class):
    """
    Function to check if an object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a_class or an instance of a class that inherited from a_class, False otherwise.
    """
    return isinstance(obj, a_class)
