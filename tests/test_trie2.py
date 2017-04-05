#!/usr/bin/env python3

import unittest
from trie_me import trie2


class TestTrie2(unittest.TestCase):

    def test_in_trie(self):

        trie = trie2.make_trie('hello', 'abc', 'baz', 'bar', 'barz')

        self.assertTrue(trie2.contains(trie, 'bar'))
        self.assertFalse(trie2.contains(trie, 'bab'))
        self.assertFalse(trie2.contains(trie, 'zzz'))

        self.assertFalse(trie2.contains(trie, 'bax'))
        trie2.add(trie, "bax")
        self.assertTrue(trie2.contains(trie, 'bax'))

    def test_make_trie(self):

        trie = trie2.make_trie('hello', 'abc', 'baz', 'bar', 'barz')
        trie2.add(trie, "bax")

        self.assertEqual(trie, {'h': {'e': {'l': {'l': {'o': {'_': '_'}}}}}, 'a': {'b': {'c': {'_': '_'}}},
                                'b': {'a': {'z': {'_': '_'}, 'r': {'_': '_', 'z': {'_': '_'}}, 'x': {'_': '_'}}}})

    def test_list_words(self):

        trie = trie2.make_trie('hello', 'abc', 'baz', 'bar', 'barz')
        trie2.add(trie, "bax")

        self.assertEqual(trie2.list_words(trie), ['abc', 'bar', 'barz', 'bax', 'baz', 'hello'])

