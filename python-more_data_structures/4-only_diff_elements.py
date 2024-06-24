#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    # Find the symmetric difference of the two sets
    diff_set = set_1 ^ set_2
    # Return the set of elements present in only one of the sets
    return diff_set

# Example usage:
if __name__ == "__main__":
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    od_set = only_diff_elements(set_1, set_2)
    print(sorted(list(od_set)))
