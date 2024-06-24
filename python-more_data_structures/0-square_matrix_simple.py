#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    new_matrix = []

    # Iterate over each row in the input matrix
    for row in matrix:
        # Create a new row with squared values
        new_row = list(map(lambda x: x**2, row))
        # Append the new row to the new matrix
        new_matrix.append(new_row)

    # Return the new matrix
    return new_matrix

# Example usage:
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)
