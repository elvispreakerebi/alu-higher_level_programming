#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    finally:
        print()  # for the new line after printing the elements
        return count

# Testing the function with your example
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list(my_list, 5)  # Without using len()
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list(my_list, 7)  # Without using len()
    print("nb_print: {:d}".format(nb_print))
