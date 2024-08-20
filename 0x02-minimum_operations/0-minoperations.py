#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute
only two operations in this file: `Copy All` and `Paste`. Given a number `n`,
write a method that calculates the fewest number of operations needed to
result in exactly n H characters in the file.
"""


def minOperations(n: int) -> int:
    """
    Function that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.

    Args:
        n (int): given number

    Return:
        An integer
        If n is impossible to achieve, return 0

    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
