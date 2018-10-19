from pycoin.key import Key

from block import Block


class Transaction(Block):

    def create_signature(self, sha3hash, private_key):
        k = Key(private_key)
        signature = k.sign(sha3hash)
        self.signature = signature
        return signature