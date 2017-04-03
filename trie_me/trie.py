#!/usr/bin/env python3
from trie_me.node import Node


class Trie:
    """
    Trie holds a trie data structure
    """

    # For both binary tree and trie, root node level is called level 0.
    # Unlike a binary tree, a trie root node doesn't hold a single value.
    # A trie needs (n+1) levels 0-n to hold a string of length n.
    # social security numbers have length of 9 digits.
    # if each item is a social security number, the trie needs 10 levels 0-9
    item_length = 9

    def __init__(self, root_node):
        """
        Initializes the class.

        :param root_node: root node of trie. value is empty string "".
        :return: None
        """
        self.root_node = root_node

    @classmethod
    def parent_string(cls, node_string):
        """
        :param node_string: string representing a node
        :return: node_string for parent of this node, node_string characters up to last character
        """
        if node_string == "":
            return ""

        trimmed = node_string[0: len(node_string) - 1]
        return trimmed

    def contains(self, item: str) -> bool:
        """
        :param item: item to find. A string of decimal digits, typically length 9.
        :return: True if trie contains number. False otherwise.
        """
        if self.get_node(item) is not None:
            return True
        else:
            return False

    def get_node(self, item: str) -> Node:
        """
        :param item: item to find. A string of decimal digits, typically length 9.
        :return: node at position described by item. 
        If node doesn't exist, return None
        """
        current_node = self.root_node

        for character in item:
            index = int(character)
            if current_node.children[index] is None:
                # didn't find a match
                return None
            else:
                current_node = current_node.children[index]

        # loop got all the way to the last digit in number
        return current_node

    def add_item(self, item: str) -> Node:
        """
        :param item: item to add to trie. A string of decimal digits, typically length 9.
        :return: terminal node at position described by item. 
        If trie contains item, this method overwrites it.
        """
        current_node = self.root_node

        for character in item:
            index = int(character)
            if current_node.children[index] is None:
                # nothing at this position yet, add a new node
                current_node.children[index] = Node(character)

            # traverse to next level down
            current_node = current_node.children[index]

        # loop got all the way to the last digit in number
        return current_node

    def add_items(self, filename: str):
        with open(filename, 'r', encoding='utf-8') as items:

            for line in items:
                item = line.strip('\n')
                self.add_item(item)

