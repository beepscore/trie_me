#!/usr/bin/env python3


class Node:
    """Node in trie."""

    values_length = 10
    """int: number of possible values.
    For decimal digits this is 10.
    For lowercase ascii alphabet letters could be 26."""

    name = ""
    """str: e.g. In a trie of social security numbers, leaf node name could be the person's name."""

    @classmethod
    def is_key_valid(cls, key: str) -> bool:
        digit_keys = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
        if key == "":
            # root node will have key empty string ""
            return True
        elif key in digit_keys:
            return True
        else:
            return False

    def __init__(self, value: str):
        """
        Initializes the class.
        Sets property visited to False.
        
        children is a list of child nodes fixed length 10
        initially all children are None
        this simplifies implementation
        https://www.toptal.com/java/the-trie-a-neglected-data-structure
        TODO: Consider if this is memory inefficient and if it is worth optimizing

        :param value: a string representing a decimal digit from "0" - "9"
        Note this constructor does not enforce that value is valid!
        :return: None
        """
        self.value = value

        # http://stackoverflow.com/questions/10712002/create-an-empty-list-in-python-with-certain-size#10712044
        self.children = [None, None, None, None, None, None, None, None, None, None]

        # visited: Used when traversing the trie.
        # True if this node and all of its children have been visited
        self.visited = False

        # typically None or 0 to (values_length - 1) inclusive
        self.index_largest_child_visited = None

    def add_child(self, child):
        """
        :param child: node to be added to children. 
        If child is None or child.value is not valid, doesn't add child
        If self already has a child with this value, overwrites previous child
        :return: None
        """

        if child is None:
            return

        if Node.is_key_valid(child.value) and child.value != "":
            index = int(child.value)
            self.children[index] = child

    def is_leaf_node(self) -> bool:
        """
        :return: True if all children are None, False otherwise
        """
        for child in self.children:
            if child is not None:
                return False

        return True

