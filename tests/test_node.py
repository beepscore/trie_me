#!/usr/bin/env python3

import unittest
import node


class TestNode(unittest.TestCase):

    def test_is_key_valid_string_0(self):
        self.assertTrue(node.Node.is_key_valid("0"))

    def test_is_key_valid_string_9(self):
        self.assertTrue(node.Node.is_key_valid("9"))

    def test_is_key_valid_none(self):
        self.assertFalse(node.Node.is_key_valid(None))

    def test_is_key_valid_empty_string(self):
        self.assertFalse(node.Node.is_key_valid(""))

    def test_is_key_valid_number(self):
        self.assertFalse(node.Node.is_key_valid(5))

    def test_is_key_valid_letter(self):
        self.assertFalse(node.Node.is_key_valid("a"))

    def test_is_key_valid_string_53(self):
        self.assertFalse(node.Node.is_key_valid("5.3"))

    def test_instantiate(self):
        my_node = node.Node()
        self.assertIsNotNone(my_node)

    def test_name_default_none(self):
        my_node = node.Node()
        self.assertEqual(my_node.name, None)

    def test_children_none(self):
        my_node = node.Node()
        expected = [None, None, None, None, None, None, None, None, None, None]
        self.assertEqual(my_node.children, expected)

    def test_is_leaf_node(self):
        root_node = node.Node()
        self.assertIsNotNone(root_node)
        self.assertTrue(root_node.is_leaf_node())

        child = node.Node()
        root_node.children[2] = child
        self.assertFalse(root_node.is_leaf_node())
        self.assertTrue(child.is_leaf_node())
