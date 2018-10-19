import sha3

from pearlbase import PearlBase

class Genesis:

    def __init__(self, pearl_bases):
        self.pearl_bases = pearl_bases

    def get_hash(self):
        buffer = bytes()
        for item in self.pearl_bases:
            buffer = buffer + item.get_bytes()
        return sha3.sha3_256(buffer).digest()