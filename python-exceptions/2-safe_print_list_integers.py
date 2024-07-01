#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    printed_count = 0
    try:
        while count < x:
            try:
                print("{:d}".format(my_list[count]), end="")
                printed_count += 1
            except (ValueError, TypeError):
                pass
            count += 1
    except IndexError:
        pass
    finally:
        print()  # for the new line after printing the elements
        return printed_count

# Testing the function with your example
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list_integers(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
    nb_print = safe_print_list_integers(my_list, 7)  # Without using len()
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list_integers(my_list, 9)  # Without using len()
    print("nb_print: {:d}".format(nb_print))
