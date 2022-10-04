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
        super().__init__(id)  # call of super class with id
        """
        super class with id -
        this super call with use the logic of the __init__ of the Base class
        """
    @property  # validation of all setter methods and instantiation
    def width(self):
        """
        Width Getter
        """
        return self.__width

    @property  # validation of all setter methods and instantiation
    def height(self):
        """
        height Getter
        """
        return self.__height

    @property  # validation of all setter methods and instantiation
    def x(self):
        """
        x Getter
        """
        return self.__x

    @property  # validation of all setter methods and instantiation
    def y(self):
        """
        y Getter
        """
        return self.__y

    @width.setter  # validation of all setter methods and instantiation
    def width(self, value):
        """
        Width Setter
        Attribute:
        Value(int): value to assign
        Raises:
        TypeError: Value must be int
        ValueError: Value must be > 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter  # validation of all setter methods and instantiation
    def height(self, value):
        """
        height Setter
        Attribute:
        Value(int): value to assign
        Raises:
        TypeError: Value must be int
        ValueError: Value must be > 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter  # validation of all setter methods and instantiation
    def x(self, value):
        """
        x Setter
        Attribute:
        Value(int): value to assign
        Raises:
        TypeError: Value must be int
        ValueError: Value must be >= 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter  # validation of all setter methods and instantiation
    def y(self, value):
        """
        Width Setter
        Attribute:
        Value(int): value to assign
        Raises:
        TypeError: Value must be int
        ValueError: Value must be >= 0
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):  # public method
        """
        Define The Area of Rectangle
        returns the area value of the Rectangle instance.
        """
        return self.__width * self.__height

    def display(self):  # public method
        """
        Display The Rectangle Using  '#'
        prints in stdout the Rectangle instance with the character #
        """
        for y in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):  # overriding the __str__ method
        """Returns a string representation of a Rectangle instance.
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        s = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return s

    def update(self, *args, **kwargs):   # public method (prototype)
        """
        assigns an argument to each attribute
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        Updates the rectangle by args or kwargs
        **kwargs can be thought of as a double pointer to
        a dictionary: key/value
        **kwargs must be skipped if *args exists and is not empty
        """
        if args is not None and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
        else:
            if kwargs is not None and len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    elif key == "width":
                        self.width = value
                    elif key == "height":
                        self.height = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value

    def to_dictionary(self):
        """
            returns the dictionary
            representation of a Rectangle
        """
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}
