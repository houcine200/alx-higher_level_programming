#!/usr/bin/python3
"""define a Student class """


class Student:
    """ retrieves a dictionary representation of a Student instance """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    result[key] = value

        return result
    
    def reload_from_json(self, json):
        """Replace all attributes of the student.
        Args:
            json (dict): the key/value pairs to replace with
        """
        for k, v in json.items():
            setattr(self, k, v)
