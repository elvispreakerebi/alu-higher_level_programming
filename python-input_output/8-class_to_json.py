#!/usr/bin/python3
""" This is the script """


def class_to_json(obj):
    """
    Converts an instance of a class into a dictionary suitable for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary representation of the class instance.
    """
    # Get all attributes of the object
    attributes = vars(obj)

    # Dictionary to hold JSON serializable attributes
    json_dict = {}

    # Iterate through each attribute
    for key, value in attributes.items():
        # Check if the value is serializable
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value

    return json_dict
