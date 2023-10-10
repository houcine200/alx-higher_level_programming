#!/usr/bin/python3
""" Module that returns a list of lists of integers representing Pascal's"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal's"""
    if n <= 0:
        return []
    
    triangle = []
    row = [1]

    for _ in range(n):
        triangle.append(row)
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]

    return triangle