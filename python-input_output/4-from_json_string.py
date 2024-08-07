#!/usr/bin/python3
""" This is the script """


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to be deserialized.

    Returns:
        object: The Python object represented by the JSON string.
    """
    import json
    return json.loads(my_str)
