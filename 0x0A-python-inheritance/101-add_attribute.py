#!/usr/bin/python3
"""Defines a function that adds attributes to objects"""


def add_attribute(object, attribute, value):
    """Adds an attribute to an object if possible.

    Args:
        object: The target object.
        attribute: The name of the attribute to add.
        value: The value to assign to the new attribute.

    Raises:
        TypeError: If the object doesn't have a '__dict__' attribute,
                   indicating that attributes cannot be added.
    """
    if hasattr(object, "__dict__") is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(object, attribute, value)
