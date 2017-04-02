#!/usr/bin/env python3


class Node:
    """
    Node in trie.
    """

    @classmethod
    def is_value_valid(cls, value: str) -> bool:
        digit_strings = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
        if value in digit_strings:
            return True
        else:
            return False

    def __init__(self, value: str, children):
        """
        Initializes the class.
        Sets property visited to False.

        :param value: a string representing a decimal digit from 0-9
        :param children: collection of child nodes. May be empty. Maximum length is 10.
        :return: None
        """
        self.value = value
        self.children = children

        # visited: Used when traversing the trie.
        # true if this node and all of its children have been visited
        self.visited = False

