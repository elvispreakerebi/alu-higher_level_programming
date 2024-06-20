#!/usr/bin/python3

def islower(c):
    # Check if c is between 'a' and 'z' in ASCII values
    return 'a' <= c <= 'z'

# Test cases (for standalone testing)
if __name__ == "__main__":
    print("a is {}".format("lower" if islower("a") else "upper"))
    print("H is {}".format("lower" if islower("H") else "upper"))
    print("A is {}".format("lower" if islower("A") else "upper"))
    print("3 is {}".format("lower" if islower("3") else "upper"))
    print("g is {}".format("lower" if islower("g") else "upper"))
