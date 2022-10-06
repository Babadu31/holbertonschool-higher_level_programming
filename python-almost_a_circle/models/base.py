#!/usr/bin/python3
"""
base module
"""
import json
from os.path import exists


class Base:
    """
    Base class
    """
    __nb_objects = 0   # private class attribute

    def __init__(self, id=None):  # class constructor
        """
        Init
        Attributes:
            id (): id
        """
        if id is not None:
            self.id = id
            """
            if id is not None, assign the public instance
            attribute id with this argument value
            """
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        """"
        otherwise, increment __nb_objects and assign the new value
        to the public instance attribute id
        """

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return A JSON STRING a representation list_dict..
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save Dict To Json
        """
        d = []
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            if list_objs:
                for obj in list_objs:
                    d.append(obj.to_dictionary())
            f.write(cls.to_json_string(d))

    @staticmethod
    def from_json_string(json_string):
        """
            Write Json Representation of String
        """
        if not json_string:
            return []
        return json.loads(json_string)
