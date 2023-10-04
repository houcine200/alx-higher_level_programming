#!/usr/bin/python3
"""
Module: say_my_name
prints the first and last name if both are strings.
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name prints out the input strings prepended with "My name is".
    Raises value error if both first_name and last_name are not strings
    Can accept one or two arguments
    """
    if first_name is None or isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if last_name is None or isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
