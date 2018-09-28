#!/usr/bin/env python3

import unittest
import trie2


class TestTrie2(unittest.TestCase):

    def test_in_trie(self):

        # alternative ways to call
        # tuple is probably safer than a list as it is immutable
        # words_tuple = ('hello', 'abc', 'baz', 'bar', 'barz')
        # * expands the collection
        # trie = trie2.make_trie(*words_tuple)

        # words_list = ['hello', 'abc', 'baz', 'bar', 'barz']
        # * expands the collection
        # trie = trie2.make_trie(*words_list)

        trie = trie2.make_trie('hello', 'abc', 'baz', 'bar', 'barz')

        self.assertTrue(trie2.contains(trie, 'bar'))
        self.assertFalse(trie2.contains(trie, 'bab'))
        self.assertFalse(trie2.contains(trie, 'zzz'))

        self.assertFalse(trie2.contains(trie, 'bax'))
        trie2.add_words(trie, "bax")
        self.assertTrue(trie2.contains(trie, 'bax'))

    def test_make_trie(self):

        trie = trie2.make_trie('hello', 'abc', 'baz', 'bar', 'barz')
        trie2.add_words(trie, "bax")

        self.assertEqual(trie, {
            'h': {'e': {'l': {'l': {'o': {'_': '_'}}}}},
            'a': {'b': {'c': {'_': '_'}}},
            'b': {'a': {'z': {'_': '_'},
                        'r': {'_': '_', 'z': {'_': '_'}},
                        'x': {'_': '_'}}}})

    def test_make_trie_from_file(self):

        trie = trie2.make_trie_from_file("./data/input/numbers_test.txt")

        self.assertEqual(trie, {
            '1': {'2': {'3': {'4': {'5': {'6': {'7': {'8': {'9': {'_': '_'}}}}}}}}},
            '0': {'1': {'2': {'3': {'4': {'5': {'6': {'7': {'8': {'_': '_'}}}}}}}}},
            '5': {'8': {'8': {'3': {'2': {'7': {'9': {'8': {'4': {'_': '_'},
                                                            '7': {'_': '_'},
                                                            '8': {'_': '_'}}}}}}}},
                  '5': {'5': {'5': {'5': {'5': {'5': {'5': {'5': {'_': '_'}}}}}}}}}
        }
                         )

    def test_list_words(self):

        trie = trie2.make_trie('hello', 'abc', 'baz', 'bar', 'barz')
        trie2.add_words(trie, "bax")

        self.assertEqual(trie2.list_words(trie), ['abc', 'bar', 'barz', 'bax', 'baz', 'hello'])

    def test_list_words_from_file(self):

        trie = trie2.make_trie_from_file("./data/input/numbers_test.txt")

        self.assertEqual(trie2.list_words(trie),
                         ['012345678', '123456789', '555555555', '588327984', '588327987', '588327988'])

    def test_contains_true(self):

        trie = trie2.make_trie_from_file("./data/input/numbers_test.txt")

        self.assertTrue(trie2.contains(trie, '012345678'))
        self.assertTrue(trie2.contains(trie, '123456789'))
        self.assertTrue(trie2.contains(trie, '588327984'))
        self.assertTrue(trie2.contains(trie, '555555555'))
        self.assertTrue(trie2.contains(trie, '012'))

    def test_contains_false(self):

        trie = trie2.make_trie_from_file("./data/input/numbers_test.txt")

        self.assertFalse(trie2.contains(trie, '222222222'))
        self.assertFalse(trie2.contains(trie, '986422389'))

    def test_successor_key(self):
        trie = trie2.make_trie_from_file("./data/input/numbers_test.txt")
        self.assertEqual(trie2.successor_key(trie, "0"), "1")
        self.assertEqual(trie2.successor_key(trie, "1"), "5")

    def test_successor_key_digit_not_in_trie(self):
        trie = trie2.make_trie_from_file("./data/input/numbers_test.txt")
        self.assertEqual(trie2.successor_key(trie, "2"), "5")

    def test_successor_key_none(self):
        trie = trie2.make_trie_from_file("./data/input/numbers_test.txt")
        self.assertEqual(trie2.successor_key(trie, "_"), None)

    def test_successor_trie_1(self):
        # trie = trie2.make_trie_from_file("./data/input/numbers_test.txt")
        trie = trie2.make_trie('111111111', '111111112')
        # TODO: Fix RecursionError: maximum recursion depth exceeded in comparison
        self.assertEqual(trie2.successor(trie, '111111111', 1),  '111111111')

