"""Class Module thta define a cipher class called Message"""

from typing_extensions import Self


class Message():
    def __init__(self, original_message, offset):
        self.original = original_message
        self.off = offset 
        self.encrypted_message = self.__encode()