#!/usr/bin/env python3


class Trie2:
    """
        # http://stackoverflow.com/questions/36977439/python-trie-how-to-traverse-it-to-build-list-of-all-words#36977856
    """

    @classmethod
    def make_trie(cls, *words) -> dict:
        """
        :param words: words to add to trie
        :return: trie containing words
        """
        trie = {}
        Trie2.add(trie, *words)
        return trie

    @classmethod
    def contains(cls, trie: dict, word: str) -> bool:
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

    @classmethod
    def add(cls, trie: dict, *words) -> dict:
        """
        :param trie: trie to add to
        :param words: words to add to trie
        :return: trie
        """
        for word in words:
            if type(word) != str:
                raise TypeError("Trie only works on str!")
            temp_trie = trie
            for letter in word:
                # if temp_trie[letter] exists, setdefault returns the value
                # if temp_trie[letter] doesn't exist, setdefault adds key-value pair temp_trie[letter] = default_value
                # http://xwell.org/2015/04/07/python-tricks-setdefault
                default_value = {}
                temp_trie = temp_trie.setdefault(letter, default_value)
            temp_trie.setdefault('_', '_')
        return trie

    @classmethod
    def list_words(cls, trie: dict):
        """
        reference stack overflow answer
        http://stackoverflow.com/questions/36977439/python-trie-how-to-traverse-it-to-build-list-of-all-words#36977856
        :param trie: trie to list
        :return: list of words in trie, sorted alphabetically.
        """
        my_list = []
        # trie is composed of nested dictionaries, which aren't sorted.
        # To list words in order, need to sort keys.
        keys_sorted = sorted(trie.keys())

        for key in keys_sorted:
            if key != '_':
                # recursive call
                for el in Trie2.list_words(trie[key]):
                    my_list.append(key + el)
            else:
                my_list.append('')
        return my_list

