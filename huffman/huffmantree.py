"""Classes about generating a Huffman tree."""
from collections import Counter
from itertools import starmap
from typing import Union


class Node:
    """Node in a binary tree."""

    def __init__(self, data: int, code: str = None, left=None, right=None) -> None:
        self.__data = data
        self.__code = code
        self.__left = left
        self.__right = right

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, _):
        raise AttributeError

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, _):
        raise AttributeError

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right


class HuffmanTree:
    """Generate a Huffman tree.
    Expected input:
    1. A string sequence
    2. An object like collections.Counter"""

    def __init__(self, sth: Union[str, Counter]) -> None:
        if isinstance(sth, Counter):
            counter = sth
        elif isinstance(sth, str):
            counter = Counter(sth)
        else:
            raise TypeError

        if len(counter) == 0:
            raise ValueError

        node_list = list(starmap(lambda c, d: Node(d, c), counter.items()))
        for _ in range(len(node_list) - 1):
            node_list = sorted(node_list, key=lambda x: x.data)

            left_node = node_list.pop(0)
            right_node = node_list.pop(0)

            root = Node(left_node.data + right_node.data)
            root.left = left_node
            root.right = right_node

            node_list.append(root)

        self.root = root

    def print_tree(self):
        def recurse(tree):
            if tree is not None:
                print(f'{tree.code} --> {tree.data}')
                recurse(tree.left)
                recurse(tree.right)

        recurse(self.root)
