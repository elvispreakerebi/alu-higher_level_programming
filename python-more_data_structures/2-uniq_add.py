#!/usr/bin/python3


def uniq_add(my_list=[]):
    # Use a set to store unique integers
    unique_integers = set(my_list)
    # Sum all the unique integers
    total_sum = sum(unique_integers)
    # Return the total sum
    return total_sum

# Example usage:
if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))
