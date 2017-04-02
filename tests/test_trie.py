#!/usr/bin/env python3

import unittest
from trie_me import trie


class TestTrie(unittest.TestCase):

    def test_instantiate(self):
        # numbers_filename = "data/input/numbers_test.txt"
        root_node = None
        numbers_trie = trie.Trie(root_node)
        self.assertIsNotNone(numbers_trie)
