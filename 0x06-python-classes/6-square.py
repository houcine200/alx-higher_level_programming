#!/usr/bin/python3
""" define class square """


class Square:
    """ the class square """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) is False or \
                len(value) != 2 or \
                all(isinstance(num, int) for num in value) is False or \
                all(num >= 0 for num in value) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for _ in range(self.position[1]):
            print()
        for _ in range(self.__size):
            print('{}'.format(' ' * self.position[0] + '#' * self.__size))
