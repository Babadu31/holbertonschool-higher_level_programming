#!/usr/bin/python3
"""
Module to create class
"""


class Square:
    """
example function class
    """
    def __init__(self, size=0):
        """
Module to create class
"""

        self.__size = size

    def area(self):
        """
example function class
        """
        return (self.__size) ** 2


@proprety
def size(self):
    """
Module to create class
    """


def size(self):
    return self.__size


@size.setter
def size(self, value):
    """
Module to create class
    """
    if type(value) != int:
        raise TypeError("size must be an integer")
    elif value < 0:
        raise ValueError("size must be >= 0")
    else:
        self.__size = value
