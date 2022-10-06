#!/usr/bin/python3
"""
tests for class
"""

import unittest
import sys
from models.base import Base

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


