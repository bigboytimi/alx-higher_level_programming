#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    
    def test_ordered_list(self):
        num_list1 = [2, 5, 6, 9, 90]
        self.assertEqual(max_integer(num_list1), 90)

    def test_unordered_list(self):
        num_list2 = [25, 11, 78, 5, 4, 2]
        self.assertEqual(max_integer(num_list2), 78)
    
    def test_floats(self):
        num_list3 = [2.5, 7.0, 9.21, 86.5, 90.34, 2]
        self.assertEqual(max_integer(num_list3), 90.34)

    def test_empty_list(self):
        num_list4 = []
        self.assertEqual(max_integer(num_list4), None)

    def test_mixed_list(self):
        num_list5 = [34, -5, 0.7, 11.7, 87, 901.4]
        self.assertEqual(max_integer(num_list5), 901.4)

if __name__ == '__main__':
    unittest.main()
