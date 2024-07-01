#!/usr/bin/env python3
"""
In this task you will write the first unit test for utils.access_nested_map.

Create a TestAccessNestedMap class that inherits from unittest.TestCase.

Implement the TestAccessNestedMap.test_access_nested_map method to test that
the method returns what it is supposed to.

Decorate the method with @parameterized.expand to test the function for
ollowing inputs:

nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")

"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",)),
            ({"a": 1}, ("a", "b")),
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{path[-1]}'")


class TestGetJson(unittest.TestCase):

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        # Create a mock response object with the desired json method
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the function and check the results
        result = get_json(test_url)
        self.assertEqual(result, test_payload)

        # Verify the mock_get was called once with the test_url
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):

    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
                TestClass, 'a_method', return_value=42) as mock_method:
        test_instance = TestClass()

            # Call the memoized property twice
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            # Assert that the results are correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Assert that a_method was called only once
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
