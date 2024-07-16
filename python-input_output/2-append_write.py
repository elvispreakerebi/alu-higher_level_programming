#!/usr/bin/python3
""" This is the script """


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns the number of characters added.

    Args:
        filename (str): The path to the text file to be written. Defaults to an empty string.
        text (str): The text to be appended to the file. Defaults to an empty string.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
