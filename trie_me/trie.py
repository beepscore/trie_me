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

    def contains(self, string: str) -> bool:
        """
        :param string: string to search. A string of zero or more decimal digits.
        :return: True if node is not None and node.name is not None. False otherwise.
        """
        node = self.get_node(string)
        if node is not None and node.name is not None:
            return True
        else:
            return False

    def get_node(self, string: str):
        """
        :param string: string to find. A string of zero or more decimal digits.
        :return: node at position described by string. 
        If node doesn't exist, return None
        """
        current_node = self.root_node

        for character in string:
            index = int(character)
            if current_node.children[index] is None:
                # didn't find a match
                return None
            else:
                current_node = current_node.children[index]

        # loop got all the way to the last character in string
        return current_node

    def next_larger_sibling_string(self, node_string: str):
        """
        :param node_string: A string representing a node. May or may not be in trie.
        :return: string for next larger sibling, else None
        """
        node_string_last_character = node_string[-1]
        node_string_last_character_index = int(node_string_last_character)

        if node_string_last_character_index == Node.keys_length - 1:
            # node at node_string is the largest child
            return None

        start_index = node_string_last_character_index + 1

        for index in range(start_index, Node.keys_length):

            candidate = Trie.parent_string(node_string) + str(index)
            if self.contains(candidate):
                return candidate

        return None

    def next_larger_child_string(self, string: str):
        """
        :param string: A string representing a parent node. May or may not be in trie.
        :return: string for next larger child node. else None
        return None if all larger children are None
        """
        node = self.get_node(string)

        if node is None:
            return None

        if node.is_leaf_node():
            # leaf node never has children
            return None

        for index in range(0, Node.keys_length):
            if node.children[index] is not None:
                candidate_child_string = string + str(index)
                return candidate_child_string

        return None

    def add_item(self, string: str, name: str) -> Node:
        """
        :param string: string to add to trie.
        :param name: name associated with this string, stored in the last node.
        :return: node at position described by string. 
        If trie contains string, this method overwrites name.
        """
        current_node = self.root_node

        for character in string:
            index = int(character)
            if current_node.children[index] is None:
                # nothing at this position yet, add a new node
                # TODO: Consider call current_node.add_child or delete method add_child
                current_node.children[index] = Node()

            # traverse to next level down
            current_node = current_node.children[index]

        # loop got all the way to the last character in string
        current_node.name = name
        return current_node

    def add_items(self, filename: str):
        """
        :param filename: name of file to read from.
        file is comma separated value, each line is of the form <string>, <name>
        e.g. each line is like 123456789, "Joe Smith"
        """
        with open(filename, 'r', encoding='utf-8') as items:

            for item in items:
                item_list = item.strip('\n').split(',')
                string = item_list[0]
                name = item_list[1]
                self.add_item(string, name)

