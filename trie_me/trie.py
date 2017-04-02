#!/usr/bin/env python3
from trie_me.node import Node


class Trie:
    """
    Trie holds a trie data structure
    """

    def __init__(self, root_node):
        """
        Initializes the class.

        :param root_node: root node of trie. Does not have a number value.
        :return: None
        """
        self.root_node = root_node

    def contains(self, number: int) -> bool:
        """
        :param number: number to find. Typically 9 decimal digits.
        :return: True if trie contains number. False otherwise.
        """
        if self.get_node(number) is not None:
            return True
        else:
            return False

    def get_node(self, number: int) -> Node:
        """
        :param number: number to find. Typically 9 decimal digits.
        :return: node at position described by number. 
        If node doesn't exist, return None
        """
        string = str(number)

        current_node = self.root_node

        for character in string:
            index = int(character)
            if current_node.children[index] == None:
                # didn't find a match
                return None
            else:
                current_node = current_node.children[index]

        # loop got all the way to the last digit in number
        return current_node

