#!/usr/bin/python3

# Print all possible combinations of two digits in ascending order
for tens in range(9):  # tens place digit ranges from 0 to 8
    for units in range(tens + 1, 10):  # units place digit ranges from (tens + 1) to 9
        if tens == 8 and units == 9:
            print("{:d}{:d}".format(tens, units))  # Print the last combination without ", "
        else:
            print("{:d}{:d}, ".format(tens, units), end="")
