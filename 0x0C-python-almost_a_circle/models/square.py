#!/usr/bin/python3
""" Square class, inherits from rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines a Square """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
