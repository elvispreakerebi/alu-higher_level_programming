#!/usr/bin/python3
""" This is the script """


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to be serialized to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    import json
    return json.dumps(my_obj)
