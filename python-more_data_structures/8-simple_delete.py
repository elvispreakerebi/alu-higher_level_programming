#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    # Check if the key exists in the dictionary
    if key in a_dictionary:
        # Delete the key from the dictionary
        del a_dictionary[key]
    # Return the dictionary
    return a_dictionary

# Example usage:
if __name__ == "__main__":
    def print_sorted_dictionary(a_dictionary):
        sorted_keys = sorted(a_dictionary.keys())
        for key in sorted_keys:
            print(f"{key}: {a_dictionary[key]}")

    a_dictionary = {'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3]}

    new_dict = simple_delete(a_dictionary, 'track')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)

    print("--")
    print("--")

    new_dict = simple_delete(a_dictionary, 'c_is_fun')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)
