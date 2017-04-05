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
                # temp_trie type may be either str or dict
                temp_trie = temp_trie.setdefault(letter, {})
            temp_trie.setdefault('_', '_')
        return trie

    @classmethod
    def in_trie(cls, trie, word: str) -> bool:
        """
        :param trie: trie to search
        :param word: word to search for
        :return: True if trie contains word. False otherwise.
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

    # stack overflow answer
    @classmethod
    def list_words(cls, trie):
        my_list = []
        for k, v in trie.items():
            if k != '_':
                # recursive call
                for el in Trie2.list_words(v):
                    my_list.append(k+el)
            else:
                my_list.append('')
        return my_list

