#!/usr/bin/env python3
"""Unit test for access_nested_map"""

import unittest
import requests
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch
from typing import Mapping, Sequence, Any


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


class TestGetJson(unittest.TestCase):
    """Mock HTTP calls
       test to get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, moke_requests_get):
        """test_get_json method expected output
           Args:
                url: url to send http request
                plaload: expected json response
        """
        moke_requests_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        moke_requests_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Test the memoization decorator, memoize
    """

    def test_memoize(self):
        """
        Test that utils.memoize decorator works as intended
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock_object:
            test = TestClass()
            test.a_property()
            test.a_property()
            mock_object.assert_called_once()


if __name__ == '__main__':
    unittest.main()
