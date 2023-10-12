#!/usr/bin/python3
"""
method trhat calcilates the fewest number
of operation
"""


def minOperations(n):
    """Calculates the fewest number of operations (copy, paste) needed
    to result in exactly n H characters.
    """

    if n == 1:
        return 0

    operations = [0] * (n + 1)

    for i in range(2, n + 1):
        operations[i] = float('inf')

        for j in range(1, i // 2 + 1):
            if i % j == 0:
                operations[i] = min(operations[i], operations[j] + 2 + i // j)

    return operations[n] if operations[n] != float('inf') else 0
