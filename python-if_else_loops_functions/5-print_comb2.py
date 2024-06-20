#!/usr/bin/python3

# Loop through numbers from 0 to 99
for i in range(100):
    # Format each number to have two digits
    formatted_number = "{:02}".format(i)
    
    # Print the formatted number followed by ", " except for the last number
    if i < 99:
        print(formatted_number + ", ", end="")
    else:
        print(formatted_number)  # Print the last number with a newline
