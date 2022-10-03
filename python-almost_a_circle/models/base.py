#!/usr/bin/python3
"""
base module
"""
import json


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
