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

    @property
    def size(self):
        """Property to retrieve the square size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter to set the age."""
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(0, self.size):
                for j in range(0, self.size):
                    print("#", end="")
                print()
