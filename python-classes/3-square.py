#!/usr/bin/python3
"""
Module to create class
"""


class Square:
    """
example function class
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
example function class
        """
        return (self.__size) ** 2
