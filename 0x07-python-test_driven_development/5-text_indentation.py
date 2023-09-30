#!/usr/bin/python3
"""Module for text_indentation method."""


def text_indentation(text):
    """Method for adding 2 new lines after '.?:' chars.

    Args:
        text: The string text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for sep in ".?:":
        
        text = (sep + "\n\n").join(
            [line.strip(" ") for line in text.split(sep)])

    print(text, end="")
