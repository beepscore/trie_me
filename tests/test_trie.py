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
        root_node = node.Node()
        self.assertIsNotNone(root_node)
        numbers_trie = trie.Trie(root_node)
        self.assertEqual(numbers_trie.root_node, root_node)

    def test_get_node_in_trie(self):
        root_node = node.Node()
        numbers_trie = trie.Trie(root_node)
        child = node.Node()
        root_node.children[6] = child
        self.assertEqual(numbers_trie.get_node("6"), child)

    def test_get_node_not_in_trie(self):
        root_node = node.Node()
        numbers_trie = trie.Trie(root_node)
        child = node.Node()
        root_node.children[6] = child
        self.assertEqual(numbers_trie.get_node("2"), None)

    def test_contains_empty_string(self):
        root_node = node.Node()
        numbers_trie = trie.Trie(root_node)
        self.assertFalse(numbers_trie.contains(""))

    def test_contains_in_trie(self):
        root_node = node.Node()
        numbers_trie = trie.Trie(root_node)
        child = node.Node()
        root_node.children[6] = child
        # child is in trie, but it doesn't have a name
        self.assertIsNone(child.name)
        self.assertFalse(numbers_trie.contains("6"))

        child.name = "Ron"
        self.assertEqual(child.name, "Ron")
        self.assertTrue(numbers_trie.contains("6"))

    def test_contains_node_not_in_trie(self):
        root_node = node.Node()
        numbers_trie = trie.Trie(root_node)
        child = node.Node()
        root_node.children[6] = child
        self.assertFalse(numbers_trie.contains("2"))

    def test_next_larger_sibling_string(self):
        root_node = node.Node()
        numbers_trie = trie.Trie(root_node)
        numbers_trie.add_items("./data/input/numbers_names_test.txt")
        self.assertEqual(numbers_trie.next_larger_sibling_string("588327984"), "588327987")
        self.assertEqual(numbers_trie.next_larger_sibling_string("588327987"), "588327988")
        self.assertIsNone(numbers_trie.next_larger_sibling_string("588327988"))

    def test_add_item_contains_true(self):
        root_node = node.Node()
        numbers_trie = trie.Trie(root_node)
        string = "123456789"
        name = "Jorge Ruiz"
        self.assertFalse(numbers_trie.contains(string))
        numbers_trie.add_item(string, name)
        self.assertTrue(numbers_trie.contains(string))
        added_node = numbers_trie.get_node(string)
        self.assertEqual(added_node.name, name)

    def test_add_item_contains_false(self):
        root_node = node.Node()
        numbers_trie = trie.Trie(root_node)
        string = "123456789"
        name = "Jorge Ruiz"
        self.assertFalse(numbers_trie.contains(string))
        numbers_trie.add_item(string, name)
        self.assertFalse(numbers_trie.contains("987654321"))

    def test_add_items_contains_true(self):
        root_node = node.Node()
        numbers_trie = trie.Trie(root_node)
        numbers_trie.add_items("./data/input/numbers_names_test.txt")
        self.assertTrue(numbers_trie.contains("123456789"))
        self.assertTrue(numbers_trie.contains("588327984"))
        self.assertTrue(numbers_trie.contains("555555555"))

    def test_add_items_contains_leading0(self):
        root_node = node.Node()
        numbers_trie = trie.Trie(root_node)
        numbers_trie.add_items("./data/input/numbers_names_test.txt")
        self.assertTrue(numbers_trie.contains("012345678"))

    def test_add_items_contains_false(self):
        root_node = node.Node()
        numbers_trie = trie.Trie(root_node)
        numbers_trie.add_items("./data/input/numbers_names_test.txt")
        self.assertFalse(numbers_trie.contains("222222222"))
        self.assertFalse(numbers_trie.contains("986422389"))

    def test_parent_string(self):
        self.assertEqual(trie.Trie.parent_string("123456789"), "12345678")
        self.assertEqual(trie.Trie.parent_string("803517"), "80351")

    def test_parent_string_empty_string(self):
        root_node = node.Node()
        numbers_trie = trie.Trie(root_node)
        numbers_trie.add_items("./data/input/numbers_names_test.txt")
        self.assertEqual(trie.Trie.parent_string(""), None)

    def test_first_child_greater_than_original(self):
        root_node = node.Node()
        numbers_trie = trie.Trie(root_node)
        numbers_trie.add_items("./data/input/numbers_names_test.txt")
        self.assertEqual(numbers_trie.first_child_greater_than_original("256", "25"), None)
        self.assertEqual(numbers_trie.first_child_greater_than_original("1234", "12"), None)
        self.assertEqual(numbers_trie.first_child_greater_than_original("58", "5"), None)
        self.assertEqual(numbers_trie.first_child_greater_than_original("57", "5"), "58")
        self.assertEqual(numbers_trie.first_child_greater_than_original("58832797", "5883279"), "58832798")
        self.assertEqual(numbers_trie.first_child_greater_than_original("588327982", "58832798"), "588327984")
        self.assertEqual(numbers_trie.first_child_greater_than_original("588327984", "58832798"), "588327987")
        self.assertEqual(numbers_trie.first_child_greater_than_original("588327987", "58832798"), "588327988")

    def test_next_item_none(self):
        root_node = node.Node()
        numbers_trie = trie.Trie(root_node)
        numbers_trie.add_items("./data/input/numbers_names_test.txt")
        self.assertEqual(numbers_trie.next_item(None, None), "012345678")

    def test_next_item_empty(self):
        root_node = node.Node()
        numbers_trie = trie.Trie(root_node)
        numbers_trie.add_items("./data/input/numbers_names_test.txt")
        self.assertEqual(numbers_trie.next_item("", ""), "012345678")

    def test_next_item_return_none(self):
        root_node = node.Node()
        numbers_trie = trie.Trie(root_node)
        numbers_trie.add_items("./data/input/numbers_names_test.txt")
        # the trie doesn't contain a next node string
        self.assertEqual(numbers_trie.next_item("888259025", "888259025"), None)

    def test_next_item_is_prefix(self):
        root_node = node.Node()
        numbers_trie = trie.Trie(root_node)
        numbers_trie.add_items("./data/input/numbers_names_test.txt")
        # the string argument is a node in the trie, a prefix of an item in the trie
        self.assertEqual(numbers_trie.next_item("0123456", "0123456"), "012345678")

    def test_next_item_not_in_trie(self):
        root_node = node.Node()
        numbers_trie = trie.Trie(root_node)
        numbers_trie.add_items("./data/input/numbers_names_test.txt")
        # the string argument is not a node in the trie
        self.assertEqual(numbers_trie.next_item("256", "256"), "555555555")

    def test_next_item_trie_contains_string(self):
        root_node = node.Node()
        numbers_trie = trie.Trie(root_node)
        numbers_trie.add_items("./data/input/numbers_names_test.txt")
        # the string argument is an item in the trie
        self.assertEqual(numbers_trie.next_item("012345678", "012345678"), "123456789")
        self.assertEqual(numbers_trie.next_item("588327984", "588327984"), "588327987")

    def test_next_item_has_earlier_sibling(self):
        root_node = node.Node()
        numbers_trie = trie.Trie(root_node)
        numbers_trie.add_items("./data/input/numbers_names_test.txt")
        # the string argument has an earlier sibling in the trie
        self.assertEqual(numbers_trie.next_item("555555557", "555555557"), "588327984")
        # earlier sibling is 588327984
        self.assertEqual(numbers_trie.next_item("588327987", "588327987"), "588327988")

    def test_items(self):
        root_node = node.Node()
        numbers_trie = trie.Trie(root_node)
        numbers_trie.add_items("./data/input/numbers_names_test.txt")

        expected = [
            ('012345678', 'jill collins'),
            ('123456789', 'joe smith'),
            ('555555555', 'rianna yup'),
            ('588327984', 'mary quant'),
            ('588327987', 'fu bar'),
            ('588327988', 'joe blow'),
            ('625358960', 'joe smith')
        ]

        self.assertEqual(numbers_trie.items(), expected)

    def test_items_in_range(self):
        root_node = node.Node()
        numbers_trie = trie.Trie(root_node)
        numbers_trie.add_items("./data/input/numbers_names_test.txt")

        actual = numbers_trie.items_in_range("012345678", "588327988")
        expected = [
            ('123456789', 'joe smith'),
            ('555555555', 'rianna yup'),
            ('588327984', 'mary quant'),
            ('588327987', 'fu bar'),
            ('588327988', 'joe blow')
        ]
        self.assertEqual(actual, expected)

    def test_items_in_range_prefix(self):
        root_node = node.Node()
        numbers_trie = trie.Trie(root_node)
        numbers_trie.add_items("./data/input/numbers_names_test.txt")

        actual = numbers_trie.items_in_range("0", "2")
        expected = [
            ('012345678', 'jill collins'),
            ('123456789', 'joe smith')
        ]
        self.assertEqual(actual, expected)

    def test_items_in_range_prefix2(self):
        root_node = node.Node()
        numbers_trie = trie.Trie(root_node)
        numbers_trie.add_items("./data/input/numbers_names_test.txt")

        actual = numbers_trie.items_in_range("0", "199999999")
        expected = [
            ('012345678', 'jill collins'),
            ('123456789', 'joe smith')
        ]
        self.assertEqual(actual, expected)

    def test_items_with_name(self):
        root_node = node.Node()
        numbers_trie = trie.Trie(root_node)
        numbers_trie.add_items("./data/input/numbers_names_test.txt")

        actual = numbers_trie.items_with_name("joe smith")
        expected = [
            ('123456789', 'joe smith'),
            ('625358960', 'joe smith')
        ]
        self.assertEqual(actual, expected)
