#!/usr/bin/python3

# Print numbers 00 to 09
print(", ".join("{:02}".format(i) for i in range(10)), end=", ")

# Print numbers 10 to 99
print(", ".join("{:02}".format(i) for i in range(10, 100)))
