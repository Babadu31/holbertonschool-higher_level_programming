#!/usr/bin/python3
"""
the class square that inherits from Rectangle
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """
        Class Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
            Size Getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            Size Setter
        """
        self.height = value
        self.width = value
