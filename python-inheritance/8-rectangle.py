#!/usr/bin/python3
"""
Rectangle module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class BaseGeometry
    """
    def __init__(self, width, height):
        """
            Initialize rectangle BaseGeometry
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
