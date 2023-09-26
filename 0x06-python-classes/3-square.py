#!/usr/bin/python3
""" define class square """


class Square:
    """ the class square """
    def __init__(self, size=0):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Compute and return the area of the square."""
        return self.__size ** 2
