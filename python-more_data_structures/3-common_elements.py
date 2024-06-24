#!/usr/bin/python3


def common_elements(set_1, set_2):
    # Find the intersection of the two sets
    common_set = set_1 & set_2
    # Return the set of common elements
    return common_set

# Example usage:
if __name__ == "__main__":
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    c_set = common_elements(set_1, set_2)
    print(sorted(list(c_set)))
