#!/usr/bin/python3
"""
method trhat calcilates the fewest number
of operation
"""


def minOperations(n):
    """Calculates the fewest number of operations (copy, paste) needed
    to result in exactly n H characters.
    """
    len_h = 1
    len_copied_h = 0
    total_operations = 0

    while len_h < n:
        if n % len_h == 0:
            total_operations += 2
            len_copied_h = len_h
            len_h *= 2
        else:
            total_operations += 1
            len_h += len_copied_h
        return total_operations
