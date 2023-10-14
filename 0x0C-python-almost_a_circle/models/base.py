#!/usr/bin/python3
"""Defines a base model class."""
from json import dumps, loads


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
    
    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ loads instance from dictionary """
        if cls.__name__ == "Rectangle":
            new_ins = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        new_ins.update(**dictionary)
        return new_ins

    @classmethod
    def load_from_file(cls):
        """  returns a list of instances """
        try:
            instance_list = []
            with open(cls.__name__ + ".json", mode='r') as a_file:
                j_file = cls.from_json_string(a_file.read())
                for dic in j_file:
                    instance_list.append(cls.create(**dic))
                return instance_list
        except:
            return []
