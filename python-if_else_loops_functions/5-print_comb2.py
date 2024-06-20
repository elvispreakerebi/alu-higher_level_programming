#!/usr/bin/python3

# Print numbers 00 to 99 in the specified format
for i in range(100):
    if i < 99:
        print("{:02}, ".format(i), end="")
    else:
        print("{:02}".format(i))
