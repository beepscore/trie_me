#!/usr/bin/env python3

import unittest
from trie_me import trie2


class TestTrie(unittest.TestCase):

    def test_trie2(self):

        trie = trie2.Trie2.make_trie('hello', 'abc', 'baz', 'bar', 'barz')
        # print(trie)
        # get_file()
        words = []
        # list(trie, "", words)
        print(trie2.Trie2.in_trie(trie, 'bar'))
        print(trie2.Trie2.in_trie(trie, 'bab'))
        print(trie2.Trie2.in_trie(trie, 'zzz'))
        trie2.Trie2.add(trie, "bax")
        print(trie2.Trie2.in_trie(trie, 'bax'))
        print(trie2.Trie2.in_trie(trie, 'baz'))
        print(trie)
        trie2.Trie2.list(trie, "", 'hello')
