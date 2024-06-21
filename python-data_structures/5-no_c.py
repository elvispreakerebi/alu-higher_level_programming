#!/usr/bin/python3


def no_c(my_string):
    # Initialize an empty list to hold the characters
    result = []

    # Iterate over each character in the string
    for char in my_string:
        # If the character is not 'c' or 'C', add it to the result list
        if char != 'c' and char != 'C':
            result.append(char)

    # Join the list into a string and return it
    return ''.join(result)

# Example usage
if __name__ == "__main__":
    print(no_c("Best School"))  # Should print: Best Shool
    print(no_c("Chicago"))      # Should print: hiago
    print(no_c("C is fun!"))    # Should print:  is fun!
