#!/usr/bin/python3
"""
tests for class
"""

import unittest
import json
from models import base
Base = base.Base


def _too_many_args(self):
    """testing too many args to init"""
    with self.assertRaises(TypeError):
        b = Base(1, 1)
