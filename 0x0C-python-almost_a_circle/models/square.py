#!/usr/bin/python3
""" Square class, inherits from rectangle. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines a Square """
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for the Square class."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of the square."""
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for the size attribute, which is synonymous with width."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute, updating both width and height."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update with args and kwargs """
        attrs = ["id", "size", "x", "y"]

        if args is not None and len(args) != 0:
            for i in range(min(len(args), len(attrs))):
                setattr(self, attrs[i], args[i])

        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation """
        attrs = ["id", "size", "x", "y"]
        values = [self.id, self.width, self.x, self.y]
        return dict(zip(attrs, values))
