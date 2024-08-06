#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """Function returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    result = []
    for row in range(n):
        row_list = []
        for col in range(row + 1):
            if row == col or col == 0:
                row_list.append(1)
            else:
                row_list.append(
                    result[row - 1][col - 1] + result[row - 1][col]
                )
        result.append(row_list)
    return result
