#!/usr/bin/env python3

import unittest
from trie_me import node


class TestNode(unittest.TestCase):

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
