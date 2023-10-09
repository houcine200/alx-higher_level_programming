#!/usr/bin/python3
"""Implementing a Geometry class"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle classe"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return: Area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return  rectangle description: [Rectangle] <width>/<height>"""
        stri = "[" + str(self.__class__.__name__) + "] "
        stri += str(self.__width) + "/" + str(self.__height)
        return stri
