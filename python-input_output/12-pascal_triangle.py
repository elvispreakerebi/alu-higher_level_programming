#!/usr/bin/python3
""" This is sthe script """


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        list of lists of int: A list containing lists representing each row of Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)  # Initialize each row with 1s
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)

    return triangle
