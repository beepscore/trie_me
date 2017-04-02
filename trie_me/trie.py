#!/usr/bin/env python3


class Trie:
    """
    Controller composed of several objects.
    Reads input commands.
    Requests a list of web pages and writes each one to a file.
    Path includes directory name and file name.
    Creates directory if it doesn't exist.
    """

    def __init__(self, root_node):
        """
        Initialize the class.

        :param root_node: root node of trie. Does not have a number value.
        :return: None
        """
        self.root_node = root_node
