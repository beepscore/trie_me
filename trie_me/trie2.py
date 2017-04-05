#!/usr/bin/env python3


def make_trie(*words) -> dict:
    """
    :param words: words to add to trie
    :return: trie containing words
    """
    trie = {}
    add_words(trie, *words)
    return trie


def contains(trie: dict, word: str) -> bool:
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


def add_words(trie: dict, *words) -> dict:
    """
    :param trie: trie to add to
    :param words: words to add to trie
    :return: trie
    """
    for word in words:
        # print("trie {0}".format(trie))
        # print("word {0}".format(word))

        add_word(trie, word)

    return trie


def add_word(trie: dict, word) -> dict:
    if type(word) != str:
        raise TypeError("Trie only works on str!")

    temp_trie = trie

    for letter in word:
        # print("letter {0}".format(letter))

        default_value = {}

        # this statement does a lot!
        # it has side effect on trie
        # if temp_trie[letter] exists, setdefault returns the value
        #
        # if temp_trie[letter] doesn't exist,
        # setdefault adds key-value pair (letter, default_value)
        # to both temp_trie and to trie, and returns default_value
        #
        # In either case, the statement reassigns temp_trie
        # to reference the returned value.
        # trie contains the value referenced by temp_trie.
        # If a subsequent iteration adds to temp_trie, that affects trie.
        # This creates the nested dictionary structure
        # http://xwell.org/2015/04/07/python-tricks-setdefault
        temp_trie = temp_trie.setdefault(letter, default_value)

        # print("trie {0}, temp_trie {1}".format(trie, temp_trie))

    # finished word. if key '_' doesn't exist, add key-value pair ('_', '_')
    temp_trie.setdefault('_', '_')


def list_words(trie: dict) -> list:
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
            for el in list_words(trie[key]):
                my_list.append(key + el)
        else:
            my_list.append('')
    return my_list


