#!/usr/bin/python3
""" This is the script """


def read_file(filename=""):
    """
    Reads a UTF-8 encoded text file and prints its content to stdout.

    Parameters:
    filename (str): The name of the file to read. Defaults to an empty string.

    Returns:
    None
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())

# Example usage:
# read_file("example.txt")
