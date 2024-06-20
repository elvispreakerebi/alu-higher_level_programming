#!/usr/bin/python3

def print_last_digit(number):
    last_digit = abs(number) % 10  # Get the last digit using modulus operator
    print(last_digit, end='')  # Print the last digit without a newline
    return last_digit  # Return the last digit

# Test cases (for standalone testing)
if __name__ == "__main__":
    print_last_digit(98)
    print_last_digit(0)
    r = print_last_digit(-1024)
    print(r)
