#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        # Print each row
        for i, val in enumerate(row):
            if i < len(row) - 1:
                print("{:d}".format(val), end=" ")
            else:
                print("{:d}".format(val), end="")
        print("")  # Newline after each row

# Example usage
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()
