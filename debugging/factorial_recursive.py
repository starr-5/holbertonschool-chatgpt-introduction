#!/usr/bin/python3
"""Compute the factorial of a number using recursion."""
import sys


def factorial(n):
    """
    Calculates the factorial of a number recursively.

    Args:
        n (int): The number to compute the factorial of.

    Returns:
        int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


f = factorial(int(sys.argv[1]))
print(f)