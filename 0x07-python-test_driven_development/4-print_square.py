#!/usr/bin/python3
"""Module for print_square method."""


def print_square(size):
    """
    Print a square made of '#' symbols with the specified size.

    Parameters:
        size (int): The size of the square. Must be a non-negative integer.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is a negative integer.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()
