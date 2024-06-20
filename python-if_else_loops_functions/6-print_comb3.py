#!/usr/bin/python3

# Print all possible combinations of two digits in ascending order
for tens in range(9):  # tens place digit ranges from 0 to 8
    for units in range(tens + 1, 10):  # units place digit ranges from (tens + 1) to 9
        print("{:d}{:d}, ".format(tens, units), end="")

# Print the last combination without the trailing comma and space
print("{:d}{:d}".format(8, 9))
