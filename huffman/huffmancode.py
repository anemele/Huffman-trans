"""Huffmane encoding and decoding."""
from itertools import starmap

from .huffmantree import HuffmanTree


class HuffmanEncode:
    def __init__(self, sth: str) -> None:
        huffman_tree = HuffmanTree(sth)
        # huffman_tree.print_tree()
        self._encoding_dict = self._get_encoding_dict(huffman_tree.root)
        self._encoding = tuple(map(lambda x: self._encoding_dict[x], sth))

    def _get_encoding_dict(self, tree):
        encoding_dict = dict()
        stack = []

        def recurse(node):
            if node is None:
                return
            if node.code is not None:
                encoding_dict[node.code] = ''.join(stack)
            stack.append('0')
            recurse(node.left)
            stack.pop()
            stack.append('1')
            recurse(node.right)
            stack.pop()

        recurse(tree)
        return encoding_dict

    @property
    def encoding_dict(self):
        return self._encoding_dict

    @property
    def encoding(self):
        return self._encoding

    def __str__(self) -> str:
        return ''.join(self._encoding)


class HuffmanDecode:
    """No error code required"""

    def __init__(self, huffman: HuffmanEncode) -> None:
        self._decoding_dict = dict(
            starmap(lambda k, v: (v, k), huffman.encoding_dict.items())
        )
        self._decoding = tuple(self._decode(huffman))

    def _decode(self, huffman: HuffmanEncode):
        code_len = tuple(map(len, self._decoding_dict.keys()))
        min_len, max_len = min(code_len), max(code_len)
        index = 0
        span = min_len
        encoding = ''.join(huffman.encoding)
        length = len(encoding)
        while index < length:
            try_code = encoding[index : index + span]
            if try_code in self._decoding_dict:
                yield self._decoding_dict[try_code]
                index += span
                span = min_len
            else:
                span += 1
                if span > max_len:
                    raise ValueError

    @property
    def decoding_dict(self):
        return self._decoding_dict

    @property
    def decoding(self):
        return self._decoding

    def __str__(self) -> str:
        return ''.join(self._decoding)
