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
        :param node_string: string representing a node. Might not be in trie.
        :return: string for parent of this node
        """
        if node_string == "":
            return None

        substring_up_to_last_character = node_string[0: len(node_string) - 1]
        return substring_up_to_last_character

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

    def next_larger_sibling_string(self, string: str):
        """
        :param string: A string representing a node. May or may not be in trie.
        :return: string for next larger sibling, else None
        """
        if string is None or string == "":
            # avoid string index out of range
            return None

        string_last_character = string[-1]
        string_last_character_index = int(string_last_character)

        if string_last_character_index == Node.keys_length - 1:
            # node at string is the largest child
            return None

        start_index = string_last_character_index + 1

        for index in range(start_index, Node.keys_length):

            candidate = Trie.parent_string(string) + str(index)
            if self.get_node(candidate) is not None:
                return candidate

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

    def first_child_greater_than_original(self, original: str, string: str):
        """
        :param original: string to start from. Trie might not have a corresponding node.
        :param string: string currently searching for.
        :return: first child string greater than original and having a node in trie.
        Node might not have a name.
        """
        node = self.get_node(string)

        if node is None:
            return None

        for index in range(0, Node.keys_length):
            child_string = string + Node.keys[index]
            # string may be on a different path than original
            # so compare child_string to original, not just last characters
            if child_string > original and self.get_node(child_string) is not None:
                return child_string

        return None

    def next_node_string(self, original: str, string: str):
        """
        :param original: string to start from. Trie may or may not have a corresponding node.
        Stores original starting point while recursive calls ascend and descend trie.
        :param string: string currently searching for. Typically greater than start string.
        :return: next greater string that has a node in trie. Node might not have a name.
        return None if not found.
        """

        print(original, string)

        if string is None:
            # edge case. Use first key as a starting string
            # To help maintain generality for trie that might contain other letters,
            # use keys[0] instead of literal "0"
            original = Node.keys[0]
            return self.next_node_string(original, original)

        if string > original:
            current_node = self.get_node(string)
            if current_node is not None and self.contains(string):
                # done!
                return string

        # depth first, attempt to go down one trie level
        first_child_greater = self.first_child_greater_than_original(original, string)
        if first_child_greater is not None:
            if self.contains(first_child_greater):
                # trie "contains" node, i.e. it's path is in trie and it has a name
                return first_child_greater
            else:
                return self.next_node_string(original, first_child_greater)

        else:
            # node doesn't have a child_greater than original

            # check current trie level- node's next siblings
            next_sibling = self.next_larger_sibling_string(string)

            if next_sibling is None:
                # node has no larger siblings

                # check parent trie level- parent's next sibling
                parent = self.parent_string(string)
                if parent is None:
                    # attempting to go higher than root level
                    return None

                else:
                    parent_next_sibling = self.next_larger_sibling_string(parent)

                    if parent_next_sibling is None:
                        # keep backing up a level
                        return self.next_node_string(original, parent)
                    else:
                        return self.next_node_string(original, parent_next_sibling)

            else:
                return self.next_node_string(original, next_sibling)

    def items(self) -> list:
        """
        :return: list of all items in trie, sorted alphabetically by string
        each item is a tuple (string, name)
        return empty list if trie contains no items
        """

        string = ""
        item_list = []
        while True:
            string = self.next_node_string(string, string)
            if string is None:
                return item_list
            else:
                node = self.get_node(string)
                item = (string, node.name)
                item_list.append(item)

    def items_in_range(self, greater_than: str, less_than_or_equal_to: str) -> list:
        """
        :param greater_than: returned items will be greater than this
        :param less_than: returned items will be less than or equal to this
        :return: list of items in range in trie, sorted alphabetically by string
        each item is a tuple (string, name)
        return empty list if range contains no items
        """

        string = greater_than
        item_list = []

        # < sic. next_node_string will return <= string
        while string < less_than_or_equal_to:
            string = self.next_node_string(string, string)
            if string is None:
                return item_list
            else:
                node = self.get_node(string)
                item = (string, node.name)
                item_list.append(item)

        return item_list
