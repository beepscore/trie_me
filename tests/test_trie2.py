#!/usr/bin/env python3

import unittest
from trie_me import trie2


class TestTrie2(unittest.TestCase):

    def test_trie2(self):

        trie = trie2.Trie2.make_trie('hello', 'abc', 'baz', 'bar', 'barz')

        self.assertTrue(trie2.Trie2.in_trie(trie, 'bar'))
        self.assertFalse(trie2.Trie2.in_trie(trie, 'bab'))
        self.assertFalse(trie2.Trie2.in_trie(trie, 'zzz'))

        trie2.Trie2.add(trie, "bax")
        self.assertTrue(trie2.Trie2.in_trie(trie, 'bax'))
        
        self.assertTrue(trie2.Trie2.in_trie(trie, 'baz'))

        self.assertEqual(trie, {'h': {'e': {'l': {'l': {'o': {'_': '_'}}}}}, 'a': {'b': {'c': {'_': '_'}}},
         'b': {'a': {'z': {'_': '_'}, 'r': {'_': '_', 'z': {'_': '_'}}, 'x': {'_': '_'}}}})

        self.assertEqual(trie2.Trie2.list_words(trie), ['hello', 'abc', 'baz', 'bar', 'barz', 'bax'])