#!/usr/bin/python3
"""Module: 2-inherits_from.py
"""


def inherits_from(obj, a_class):
    """Check if an object inherits from a given class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if 'obj' is an instance of 'a_class' or a subclass,
        otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
