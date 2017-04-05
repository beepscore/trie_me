#!/usr/bin/env python3

# http://stackoverflow.com/questions/36977439/python-trie-how-to-traverse-it-to-build-list-of-all-words#36977856
# Make My trie


class Trie2:


    @classmethod
    def make_trie(cls, *args):
        """
        Make a trie by given words.
        """
        trie = {}
        for word in args:
            if type(word) != str:
                raise TypeError("Trie only works on str!")
            temp_trie = trie
            for letter in word:
                temp_trie = temp_trie.setdefault(letter, {})
            temp_trie = temp_trie.setdefault('_', '_')
        return trie


    # Is a word in the trie
    @classmethod
    def in_trie(cls, trie, word):
        """
        Detect if word in trie.
        :param word:
        :param trie:
        """
        if type(word) != str:
            raise TypeError("Trie only works on str!")
        temp_trie = trie
        for letter in word:
            if letter not in temp_trie:
                return False
            temp_trie = temp_trie[letter]
        return True


    # add to the trie
    @classmethod
    def add(cls, trie, *args):
        for word in args:
            if type(word) != str:
                raise TypeError("Trie only works on str!")
            temp_trie = trie
            for letter in word:
                temp_trie = temp_trie.setdefault(letter, {})
            temp_trie = temp_trie.setdefault('_', '_')
        return trie


    # My Attempt to list out words
    @classmethod
    def list(cls, obj, text, words):
       str = ""
       temp_trie = obj
       for index, word in enumerate(temp_trie):
           print(temp_trie[word])


