#!/usr/bin/env python3

import unittest
from trie_me import node


class TestNode(unittest.TestCase):

    def test_is_value_valid_string_0(self):
        self.assertTrue(node.Node.is_value_valid("0"))

    def test_is_value_valid_string_9(self):
        self.assertTrue(node.Node.is_value_valid("9"))

    def test_is_value_valid_none(self):
        self.assertFalse(node.Node.is_value_valid(None))

    def test_is_value_valid_number(self):
        self.assertFalse(node.Node.is_value_valid(5))

    def test_is_value_valid_empty_string(self):
        self.assertFalse(node.Node.is_value_valid(""))

    def test_is_value_valid_letter(self):
        self.assertFalse(node.Node.is_value_valid("a"))

    def test_is_value_valid_string_53(self):
        self.assertFalse(node.Node.is_value_valid("5.3"))

    def test_instantiate(self):
        my_node = node.Node("0", None)
        self.assertIsNotNone(my_node)

    def test_children(self):
        my_node = node.Node("2", None)
        self.assertIsNone(my_node.children)

    def test_value(self):
        my_node = node.Node("2", None)
        self.assertEqual(my_node.value, "2")

    def test_visited(self):
        my_node = node.Node("0", None)
        self.assertFalse(my_node.visited)
