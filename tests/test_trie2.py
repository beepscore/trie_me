#!/usr/bin/env python3

import unittest
from trie_me import trie2


class TestTrie2(unittest.TestCase):

    def test_in_trie(self):

        trie = trie2.Trie2.make_trie('hello', 'abc', 'baz', 'bar', 'barz')

        self.assertTrue(trie2.Trie2.in_trie(trie, 'bar'))
        self.assertFalse(trie2.Trie2.in_trie(trie, 'bab'))
        self.assertFalse(trie2.Trie2.in_trie(trie, 'zzz'))

        self.assertFalse(trie2.Trie2.in_trie(trie, 'bax'))
        trie2.Trie2.add(trie, "bax")
        self.assertTrue(trie2.Trie2.in_trie(trie, 'bax'))

    def test_make_trie(self):

        trie = trie2.Trie2.make_trie('hello', 'abc', 'baz', 'bar', 'barz')
        trie2.Trie2.add(trie, "bax")

        self.assertEqual(trie, {'h': {'e': {'l': {'l': {'o': {'_': '_'}}}}}, 'a': {'b': {'c': {'_': '_'}}},
                                'b': {'a': {'z': {'_': '_'}, 'r': {'_': '_', 'z': {'_': '_'}}, 'x': {'_': '_'}}}})

    def test_list_words(self):

        trie = trie2.Trie2.make_trie('hello', 'abc', 'baz', 'bar', 'barz')
        trie2.Trie2.add(trie, "bax")

        self.assertEqual(trie2.Trie2.list_words(trie), ['hello', 'abc', 'baz', 'bar', 'barz', 'bax'])
