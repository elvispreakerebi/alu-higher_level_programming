#!/usr/bin/python3
""" This is the script """


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The path to the text file to be read. Defaults to an empty string.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())
