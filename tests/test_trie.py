#!/usr/bin/env python3

import unittest
from trie_me import trie
from trie_me import node


class TestTrie(unittest.TestCase):

    def test_instantiate(self):
        # numbers_filename = "data/input/numbers_test.txt"
        root_node = None
        numbers_trie = trie.Trie(root_node)
        self.assertIsNotNone(numbers_trie)

    def test_root_node(self):
        root_node = node.Node("")
        self.assertIsNotNone(root_node)
        numbers_trie = trie.Trie(root_node)
        self.assertEqual(numbers_trie.root_node, root_node)

    def test_get_node_in_trie(self):
        root_node = node.Node("")
        numbers_trie = trie.Trie(root_node)
        child = node.Node("6")
        root_node.add_child(child)
        self.assertEqual(numbers_trie.get_node(6), child)

    def test_get_node_not_in_trie(self):
        root_node = node.Node("")
        numbers_trie = trie.Trie(root_node)
        child = node.Node("6")
        root_node.add_child(child)
        self.assertEqual(numbers_trie.get_node(2), None)
