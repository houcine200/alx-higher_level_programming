#!/usr/bin/python3
"""Defines a base model class."""
from json import dumps, loads
import csv

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
        '''Loads instance from dictionary.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

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
        
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes to Csv """
        flag = 0
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', encoding='utf-8') as file:
            if cls.__name__ == "Rectangle":
                value_dict = {"width": "width", "height": "height",
                              "x": "x", "y": "y", "id": "id"}
                names_list = ["width", "height", "x", "y", "id"]
            else:
                value_dict = {"size": "size", "x": "x", "y": "y", "id": "id"}
                names_list = ["size", "x", "y", "id"]

            written_f = csv.DictWriter(file, fieldnames=names_list)
            for instance in list_objs:
                if flag == 0:
                    written_f.writerow(value_dict)
                    flag += 1
                written_f.writerow(instance.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ deserializes csv """
        filename = cls.__name__ + ".csv"
        with open(filename, mode='r', encoding='utf-8') as a_file:
            instance_dict = {}
            instance_array = []

            csv_file = csv.DictReader(a_file)
            for instance in csv_file:
                for key, value in instance.items():
                    instance_dict[key] = int(value)
                inst = cls.create(**instance_dict)
                instance_array.append(inst)
            return instance_array
        
    