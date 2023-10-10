#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = []
    row = [1]

    for _ in range(n):
        triangle.append(row)
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]

    return triangle