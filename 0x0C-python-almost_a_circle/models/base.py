#!/usr/bin/python3
"""Defines a base model class."""
from json import dumps


class Base:
    """class representing a base object with an optional unique ID."""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file """

        file_name = cls.__name__ + ".json"
        lista = []
        with open(file_name, mode='w') as file:
            if list_objs is None:
                file.write(cls.to_json_string([]))
            else:
                for obj in list_objs:
                    lista.append(obj.to_dictionary())
                file.write(cls.to_json_string(lista))

