#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """
    Check if an object is an instance of a specified class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if 'obj' is an instance of 'a_class', False otherwise.
    """
    return type(obj) == a_class
