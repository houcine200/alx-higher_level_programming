#!/usr/bin/python3

"""Returns a list of available attributes and methods of an object."""


def lookup(obj):

    """Return a list of an object's available attributes."""
    return dir(obj)
