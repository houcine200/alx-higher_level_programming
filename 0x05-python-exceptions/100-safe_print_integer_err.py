#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        if isinstance(value, int) == False:
            raise TypeError("Exception: Unknown format code 'd' for object of type 'str'")
        print(value)
        return True
    except TypeError as err:
        print(err)
        return False
