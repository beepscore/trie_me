#!/usr/bin/env python3


class Node:
    """
    Node in trie.
    """

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

