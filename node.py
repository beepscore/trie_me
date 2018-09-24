#!/usr/bin/env python3


class Node:
    """Node in trie."""

    # keys is a class variable
    # https://stackoverflow.com/questions/2714573/instance-variables-vs-class-variables-in-python#2714590
    # keys could be digits or or lowercase ascii alphabet letters
    # ignore root node
    keys = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

    name = None
    """str: e.g. In a trie of social security numbers, leaf node name could be the person's name."""

    # @staticmethod is independent of instance state
    # https://www.youtube.com/watch?v=HTLu2DFOdTg
    @staticmethod
    def is_key_valid(key: str) -> bool:
        if key in Node.keys:
            return True
        else:
            return False

    def __init__(self):
        self.none_ = """
        Initializes the class.
        
        children is a list of child nodes fixed length of len(keys)
        initially all children are None
        this simplifies implementation
        https://www.toptal.com/java/the-trie-a-neglected-data-structure
        TODO: Consider if this is memory inefficient and if it is worth optimizing

        :return: None
        """
        # http://stackoverflow.com/questions/10712002/create-an-empty-list-in-python-with-certain-size#10712044
        self.children = [None, None, None, None, None, None, None, None, None, None]

    def is_leaf_node(self) -> bool:
        """
        :return: True if all children are None, False otherwise
        """
        for child in self.children:
            if child is not None:
                return False

        return True

