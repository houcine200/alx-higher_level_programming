#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """the class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.width * self.height
    
    def display(self):
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print()
    
    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__, self.id, self.x, self.y, self.width, self.height)
    
    def update(self, *args, **kwargs):
        """ Updates the values of the attributes """
        attrs = ["id", "width", "height", "x", "y"]

        if args is not None and len(args) != 0:
            for i in range(min(len(args), len(attrs))):
                setattr(self, attrs[i], args[i])
        
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation """
        attrs = ["id", "width", "height", "x", "y"]
        values = [self.id, self.width, self.height, self.x, self.y]
        return dict(zip(attrs, values))