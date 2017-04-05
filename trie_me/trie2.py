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
    def in_trie(cls, trie: dict, word: str) -> bool:
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
                # http://stackoverflow.com/questions/7423428/python-dict-get-vs-setdefault#7423648
                temp_trie = temp_trie.setdefault(letter, {})
            temp_trie.setdefault('_', '_')
        return trie

    @classmethod
    def list_words(cls, trie: dict):
        """
        stack overflow answer
        http://stackoverflow.com/questions/36977439/python-trie-how-to-traverse-it-to-build-list-of-all-words#36977856
        :param trie: trie to list
        :return: list of words in trie, in order added to trie. Not sorted alphabetically.
        """
        my_list = []
        for k, v in trie.items():
            if k != '_':
                # recursive call
                for el in Trie2.list_words(v):
                    my_list.append(k+el)
            else:
                my_list.append('')
        return my_list

