#!/usr/bin/python3
""" This is the script """

def inherits_from(obj, a_class):
    """
    Function to check if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a class that inherited from a_class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
