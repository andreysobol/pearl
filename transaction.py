from pycoin.key import Key

from block import Block


class Transaction(Block):

    def get_new_owner(self):
        return self.new_owner

    def create_signature(self, sha3hash, private_key):
        k = Key(private_key)
        signature = k.sign(sha3hash)
        self.signature = signature
        return signature
    
    def verify_signature(self, sha3hash, owner, signature):
        k = Key.from_sec(owner)
        result = k.verify(sha3hash, signature)
        return result

    def verify_owner(self, parrent_transaction_hash, unspend_pearls):
        return unspend_pearls.find_by_hash(parrent_transaction_hash)
    
    def verify_new_owner(self, new_owner, unspend_pearls):
        return not unspend_pearls.find_by_owner(new_owner)
    
    def verify(self, current_unspend_pearls):
        if not self.verify_new_owner(self.new_owner, current_unspend_pearls):
            return False
        if not self.verify_owner(self.parrent_transaction_hash, current_unspend_pearls):
            return False
        parrent_tx = current_unspend_pearls.find_by_hash(self.parrent_transaction_hash)
        return self.verify_signature(self.get_hash(), parrent_tx.get_new_owner(), self.signature)
    
    def set_unspend_pearls(self, unspend_pearls):
        self.unspend_pearls = unspend_pearls