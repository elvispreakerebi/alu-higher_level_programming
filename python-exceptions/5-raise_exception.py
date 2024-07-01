#!/usr/bin/python3


def raise_exception():
    raise TypeError

# Testing the function with your example
if __name__ == "__main__":
    try:
        raise_exception()
    except TypeError as te:
        print("Exception raised")
