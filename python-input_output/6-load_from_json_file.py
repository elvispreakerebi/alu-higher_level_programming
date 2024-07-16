#!/usr/bin/python3
""" This is the script """


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        object: The Python object represented by the JSON file.
    """
    import json
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
