#!/usr/bin/python3
"""
defines a function to check if an object is an instance of a
specified class or a subclass thereof.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a specified class or its subclass.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if 'obj' is an instance of 'a_class' or its subclass,
        False otherwise.
    """
    return isinstance(obj, a_class)
