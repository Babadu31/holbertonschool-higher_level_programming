#!/usr/bin/python3
"""
tests for class
"""

import unittest
import sys
from models.base import Base
import json

class TestBaseClass(unittest.TestCase):
    """Class testing the Base class
    """

    def test_no_id(self):
        """Tests id as None"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_no_id_after_set(self):
        """Tests id as None after not None"""
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id_set(self):
        """Tests id as not None"""
        b98 = Base(98)
        self.assertEqual(b98.id, 98)

    def test_None_to_json_String(self):
        json_s = Base.to_json_string(None)
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_empty_to_json_string(self):
        """Test for passing empty list/ None"""
        json_s = Base.to_json_string([])
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_from_json_string(self):
        """Tests regular from_json_string"""
        json_str = '[{"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}, \
{"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}]'
        json_l = Base.from_json_string(json_str)
        self.assertTrue(type(json_l) is list)
        self.assertEqual(len(json_l), 2)
        self.assertTrue(type(json_l[0]) is dict)
        self.assertTrue(type(json_l[1]) is dict)
        self.assertEqual(json_l[0],
                         {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8})
        self.assertEqual(json_l[1],
                         {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0})
