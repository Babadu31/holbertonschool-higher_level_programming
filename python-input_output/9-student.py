#!/usr/bin/python3
"""
Write a class Student that defines a student by
"""


class Student():
    """
    A Student class that defines a Student
    Public instance attributes:
    first_name
    last_name
    age
    """
    def __init__(self, first_name, last_name, age):
        """
        INIT (Instantiation)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves a dictionary representation
        of a Student instance (same as 8-class_to_json.py)
        """
        return(self.__dict__)
