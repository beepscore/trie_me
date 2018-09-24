#!/usr/bin/env python3

from node import Node

# This module creates a trie of nested dictionaries.
# It uses code similar to
# http://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python#11016430
# http://stackoverflow.com/questions/36977439/python-trie-how-to-traverse-it-to-build-list-of-all-words#36977856
# list_words works, but successor isn't working yet

# sentinel character, terminal key or value at end of a path
end_char = '_'


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

    # finished word. if key end_char doesn't exist, add key-value pair (end_char, end_char)
    subtrie.setdefault(end_char, end_char)


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
    # (plus key end_char)
    keys_sorted = sorted(trie.keys())

    # key is a single character
    for key in keys_sorted:
        if key != end_char:

            # set subtrie to next level down
            subtrie = trie[key]

            # recurse into subtrie
            suffixes = list_words(subtrie)
            
            for suffix in suffixes:
                my_list.append(key + suffix)
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
    if key == end_char:
        return None

    keys_sorted = sorted(trie.keys())
    for candidate_key in keys_sorted:
        if int(candidate_key) > int(key):
            return candidate_key

    return None


# TODO: FIXME
def successor(trie: dict, node_string: str, trie_level: int) -> str:
    """
    for trie of fixed length items such as 9 digit numbers,
    number of levels including end_char is item length + root + end_char = 11
    We can avoid checking end_char level
    This method checks to number_of_trie_levels = 10
    
    :param trie: trie to search
    :param node_string: A string representing a node. May or may not be in trie.
    :param trie_level: level in the trie. trie_level 0 contains root node
            first call with trie_level = 1
    :return: next greater word in trie, else None
    return None if len(node_string) > 9.
    """

    number_of_trie_levels = 10

    if len(node_string) > number_of_trie_levels - 1:
        # invalid argument value
        return None

    # start at root level
    subtrie = trie

    # might need to walk down, up, down the trie many times to find successor!
    # navigation stack is the letters of the node_string
    # push/pop a letter onto string to handle navigation

    # TODO: handle key or value are end_char

    # walk down trie along node_string as far as possible

    prefix = node_string[:trie_level + 1]

    if contains(trie, prefix):

        subtrie = subtrie[node_string[trie_level]]

        if trie_level == len(node_string) - 1:
            # at last letter of node_string

            if trie_level == number_of_trie_levels:
                # at bottom level of tree
                # current_key is prefix last letter
                current_key = prefix[-1]
                sk = successor_key(subtrie, current_key)
                if sk is not None:
                    # found next larger sibling
                    return prefix[: -1] + sk

                else:
                    # no larger sibling, ascend trie one level
                    # FIXME: check successor key on previous level??
                    return successor(trie, prefix[: -1], trie_level - 1)

            else:
                # not at bottom of trie, keep walking down
                # FIXME:
                pass
        else:
            # advance to node_string next letter
            return successor(trie, node_string, trie_level + 1)

    else:
        # trie doesn't contain prefix
        # FIXME:
        pass

    # default for now
    # FIXME: By definition this is wrong!
    return node_string

