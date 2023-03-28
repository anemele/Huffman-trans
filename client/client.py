"""A simple client to simulate a chat program."""
from datetime import datetime
from huffman.huffmancode import HuffmanEncode, HuffmanDecode


class Client:
    send_label = '发送'
    recv_label = '接收'

    def __init__(self, name: str) -> None:
        self.__name = name

    @property
    def name(self):
        return self.__name

    def send(self, who, msg: str):
        huffman = HuffmanEncode(msg)
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f'[{date_time}] {self.name} {self.send_label}\n{msg}')
        who.receive(huffman)

    def receive(self, msg: HuffmanEncode):
        huffman = HuffmanDecode(msg)
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f'[{date_time}] {self.name} {self.recv_label}\n{str(huffman)}\n')

    def __repr__(self) -> str:
        return f'<{__class__.__name__} {self.__name}>'
