#!/usr/bin/python3
"""
method trhat calcilates the fewest number
of operation
"""


def minOperations(n):
    """funtion that Returns an integer"""
    len_H = 1
    len_copied_H = 0
    total_operations = 0

    while len_H < n:
        if n % len_H == 0:
            total_operations += 2
            len_copied_H = len_H
            len_H *= 2
        else:
            total_operations += 1
            len_H += len_copied_H
        return total_operations
