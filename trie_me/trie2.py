#!/usr/bin/env python3


def make_trie(*words) -> dict:
    """
    :param words: words to add to trie
    :return: trie containing words
    """
    trie = {}
    add_words(trie, *words)
    return trie


def make_trie_from_file(filename: str):
    """
    :param filename: name of file containing words to add to trie. One word per line.
    :return: trie containing words
    """
    with open(filename, 'r', encoding='utf-8') as lines:

        trie = {}

        for line in lines:
            word = line.strip('\n')
            add_word(trie, word)

    return trie


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

    # start at root level
    subtrie = trie

    for letter in word:
        # print("letter {0}".format(letter))

        default_value = {}

        # this statement does a lot!
        # it has side effect on trie
        # if subtrie[letter] exists, setdefault returns the value
        #
        # if subtrie[letter] doesn't exist,
        # setdefault adds key-value pair (letter, default_value)
        # to both subtrie and to trie, and returns default_value
        #
        # In either case, the statement reassigns subtrie
        # to reference the returned value, the subtrie at the next level down.
        #
        # trie contains the value referenced by subtrie.
        # So if a subsequent iteration adds to subtrie, that affects trie.
        # This creates the trie nested dictionary structure.
        # http://xwell.org/2015/04/07/python-tricks-setdefault
        subtrie = subtrie.setdefault(letter, default_value)

        # print("trie {0}".format(trie))
        # print("subtrie {0}".format(subtrie))

    # finished word. if key '_' doesn't exist, add key-value pair ('_', '_')
    subtrie.setdefault('_', '_')


def contains(trie: dict, word: str) -> bool:
    """
    :param trie: trie to search
    :param word: word to search for
    :return: True if trie contains word. False otherwise.
    """
    if type(word) != str:
        raise TypeError("Trie only works on str!")

    # start at root level
    subtrie = trie

    for letter in word:
        if letter not in subtrie:
            return False

        # set subtrie to next level down
        subtrie = subtrie[letter]

    # every letter in word was in corresponding subtrie
    return True


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
    # For ascii lowercase alpha there are <=26, and for decimal digits there are <=10.
    # (plus key '_')
    keys_sorted = sorted(trie.keys())

    # prefix is a single character
    for prefix in keys_sorted:
        if prefix != '_':

            # set subtrie to next level down
            subtrie = trie[prefix]

            # recurse into subtrie
            suffixes = list_words(subtrie)
            
            for suffix in suffixes:
                my_list.append(prefix + suffix)
        else:
            my_list.append('')
    return my_list


def successor_key(trie: dict, key: str) -> str:
    """
    :param trie: trie to search
    :param key: typically a one letter string containing a decimal digit e.g. "2" 
    :return: first key in trie with int value greater than key int value, else None
    return None if key equals "_"
    """
    if key == '_':
        return None

    keys_sorted = sorted(trie.keys())
    for candidate_key in keys_sorted:
        if int(candidate_key) > int(key):
            return candidate_key

    return None


