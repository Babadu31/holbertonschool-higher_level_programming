#!/usr/bin/python3
"""
class rectangle inherits from Base
"""
from .base import Base


class Rectangle(Base):
    """
    A representation of a rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):  # class constructor
        """
        Init Class
        Private instance attributes, each with its own public getter and setter
        __width -> width
        __height -> height
        __x -> x
        __y -> y
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
        """
        super class with id -
        this super call with use the logic of the __init__ of the Base class
        """
