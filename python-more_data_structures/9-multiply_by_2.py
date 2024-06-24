#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    # Create a new dictionary to store the multiplied values
    new_dict = {}
    # Iterate through the original dictionary
    for key, value in a_dictionary.items():
        # Multiply each value by 2 and store it in the new dictionary
        new_dict[key] = value * 2
    # Return the new dictionary with multiplied values
    return new_dict

# Example usage:
if __name__ == "__main__":
    def print_sorted_dictionary(a_dictionary):
        sorted_keys = sorted(a_dictionary.keys())
        for key in sorted_keys:
            print(f"{key}: {a_dictionary[key]}")

    a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
    new_dict = multiply_by_2(a_dictionary)
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)
