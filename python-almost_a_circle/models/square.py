#!/usr/bin/python3
"""
the class square that inherits from Rectangle
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square
    """
    def __init__(self, size, x=0, y=0, id=None):  # class constructor
        """
        """
        super().__init__(size, size, x, y, id)  # super class
        self.size = size

    @property  # public getter and setter size
    def size(self):
        """
        Size Getter
        """
        return self.width

    @size.setter  # public getter and setter size
    def size(self, value):
        """
        Size Setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.height = value
        self.width = value

    def __str__(self):
        """informal string representation of the square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)

    def update(self, *args, **kwargs):  # public method
        """
        update class Square
        assigns attributes
        *args is the list of arguments - no-keyworded arguments
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        **kwargs can be thought of as a double pointer to
        a dictionary: key/value (keyworded arguments)
        **kwargs must be skipped if *args exists and is not empty
        Each key in this dictionary represents an attribute to the instance
        """
        i = 0
        if args:
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
                i += 1
        else:
            for arg in kwargs:
                setattr(self, arg, kwargs.get(arg))

    def to_dictionary(self):  # public method
        """
        returns the dictionary
        representation of a square
        This dictionary must contain:
        id
        size
        x
        y
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
