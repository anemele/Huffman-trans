import unittest

from faker import Faker

from huffman.huffmancode import HuffmanEncode, HuffmanDecode


class Test(unittest.TestCase):
    def test_trans(self):
        faker = Faker('zh_CN')
        for _ in range(10):
            paragraph = faker.paragraph()
            huffman_encoding = HuffmanEncode(paragraph)
            huffman_decoding = HuffmanDecode(huffman_encoding)
            self.assertEqual(paragraph, str(huffman_decoding))
