#!/usr/bin/python3
"""Define class square"""


class Square:
    """square"""
    def __init__(self, size=0):
        """init square
        attribute : dssd
            Returns: none
        """

        self.size = size

    def area(self):
        """example function class
                attribute : dssd
            Returns: area of square
        """
        return (self.__size) ** 2


@proprety
def size(self):
    """size of square
        attribute : dssd
        Returns: size of square
    """
    return self.__size


@size.setter
def size(self, value):
    """set the size of square
        attribute : dssd
        Returns: none
        """
    if type(value) != int:
        raise TypeError("size must be an integer")
    elif value < 0:
        raise ValueError("size must be >= 0")
    else:
        self.__size = value
