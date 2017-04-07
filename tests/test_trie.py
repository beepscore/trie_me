#!/usr/bin/env python3

import unittest
from trie_me import trie
from trie_me import node


class TestTrie(unittest.TestCase):

    def test_instantiate(self):
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
        self.assertEqual(numbers_trie.get_node("6"), child)

    def test_get_node_not_in_trie(self):
        root_node = node.Node("")
        numbers_trie = trie.Trie(root_node)
        child = node.Node("6")
        root_node.add_child(child)
        self.assertEqual(numbers_trie.get_node("2"), None)

    def test_contains_empty_string(self):
        root_node = node.Node("")
        numbers_trie = trie.Trie(root_node)
        self.assertTrue(numbers_trie.contains(""))

    def test_contains_in_trie(self):
        root_node = node.Node("")
        numbers_trie = trie.Trie(root_node)
        child = node.Node("6")
        root_node.add_child(child)
        self.assertTrue(numbers_trie.contains("6"))

    def test_contains_node_not_in_trie(self):
        root_node = node.Node("")
        numbers_trie = trie.Trie(root_node)
        child = node.Node("6")
        root_node.add_child(child)
        self.assertFalse(numbers_trie.contains("2"))

    def test_next_larger_sibling_string(self):
        root_node = node.Node("")
        numbers_trie = trie.Trie(root_node)
        numbers_trie.add_items("./data/input/numbers_names_test.txt")
        self.assertEqual(numbers_trie.next_larger_sibling_string("588327984"), "588327987")
        self.assertEqual(numbers_trie.next_larger_sibling_string("588327987"), "588327988")
        self.assertIsNone(numbers_trie.next_larger_sibling_string("588327988"))

    def test_next_larger_child_string(self):
        root_node = node.Node("")
        numbers_trie = trie.Trie(root_node)
        numbers_trie.add_items("./data/input/numbers_names_test.txt")
        self.assertEqual(numbers_trie.next_larger_child_string(""), "0")
        self.assertEqual(numbers_trie.next_larger_child_string("58832798"), "588327984")
        self.assertIsNone(numbers_trie.next_larger_child_string("588327988"))

    def test_add_item_contains_true(self):
        root_node = node.Node("")
        numbers_trie = trie.Trie(root_node)
        item = "123456789"
        name = "jorge"
        self.assertFalse(numbers_trie.contains(item))
        numbers_trie.add_item(item, name)
        self.assertTrue(numbers_trie.contains(item))

    def test_add_item_contains_false(self):
        root_node = node.Node("")
        numbers_trie = trie.Trie(root_node)
        item = "123456789"
        name = "jorge"
        self.assertFalse(numbers_trie.contains(item))
        numbers_trie.add_item(item, name)
        self.assertFalse(numbers_trie.contains("987654321"))

    def test_add_items_contains_true(self):
        root_node = node.Node("")
        numbers_trie = trie.Trie(root_node)
        numbers_trie.add_items("./data/input/numbers_names_test.txt")
        self.assertTrue(numbers_trie.contains("123456789"))
        self.assertTrue(numbers_trie.contains("588327984"))
        self.assertTrue(numbers_trie.contains("555555555"))

    def test_add_items_contains_leading0(self):
        root_node = node.Node("")
        numbers_trie = trie.Trie(root_node)
        numbers_trie.add_items("./data/input/numbers_names_test.txt")
        self.assertTrue(numbers_trie.contains("012345678"))

    def test_add_items_contains_false(self):
        root_node = node.Node("")
        numbers_trie = trie.Trie(root_node)
        numbers_trie.add_items("./data/input/numbers_names_test.txt")
        self.assertFalse(numbers_trie.contains("222222222"))
        self.assertFalse(numbers_trie.contains("986422389"))

    def test_parent_string(self):
        self.assertEqual(trie.Trie.parent_string("123456789"), "12345678")
        self.assertEqual(trie.Trie.parent_string("803517"), "80351")

    def test_parent_string_empty_string(self):
        root_node = node.Node("")
        numbers_trie = trie.Trie(root_node)
        numbers_trie.add_items("./data/input/numbers_names_test.txt")
        self.assertEqual(trie.Trie.parent_string(""), "")
