#!/usr/bin/env python3
"""Unit test for access_nested_map"""

import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
    ])
    def test_access_nested_map(self, nested_map, path, output):
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, output)

    """Test access_nested_map KeyError"""
    @parameterized.expand([
        ({}, ["a"], KeyError('a')),
        ({"a": 1}, ["a", "b"], KeyError('b')),
    ])
    def test_access_nested_map_exception(self, nested_map, path, ee):
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        exception = cm.exception
        self.assertEqual(str(exception), str(ee))


if __name__ == '__main__':
    unittest.main()
