from pycoin.key import Key

from block import Block


class Transaction(Block):

    def create_signature(self, sha3hash, private_key):
        k = Key(private_key)
        signature = k.sign(sha3hash)
        self.signature = signature
        return signature
    
    def verify_signature(self, sha3hash, owner, signature):
        k = Key.from_sec(owner)
        result = k.verify(sha3hash, signature)
        return result

    def verify_owner(self, owner, unspend_pearls):
        return unspend_pearls.find_by_owner(owner):
    
    def verify_new_owner(self, new_owner, unspend_pearls):
        return not unspend_pearls.find_by_owner(new_owner)