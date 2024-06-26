#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    # Get the keys in the dictionary and sort them
    sorted_keys = sorted(a_dictionary.keys())
    # Iterate through the sorted keys and print each key-value pair
    for key in sorted_keys:
        print(f"{key}: {a_dictionary[key]}")

# Example usage:
if __name__ == "__main__":
    a_dictionary = {'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3]}
    print_sorted_dictionary(a_dictionary)
