#!/usr/bin/python3
"""function that write in a file"""


def write_file(filename="", text=""):
    """ write a string in a file """
    with open(filename, "w") as file:
        file.write(text)
        return len(text)
