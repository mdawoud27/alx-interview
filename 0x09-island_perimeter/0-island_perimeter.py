#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """Function which returns the perimeter of the island described in grid"""
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]:
                perimeter += 4

                if row and grid[row - 1][col]:
                    perimeter -= 2

                if col and grid[row][col - 1]:
                    perimeter -= 2

    return perimeter
