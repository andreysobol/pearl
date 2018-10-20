class UnspendPearls:

    def __init__(self, transactions):
        self.transactions = transactions

    def find_by_owner(self, owner):
        for tx in self.transactions:
            if tx.owner == owner:
                return tx
        return False

    def find_by_hash(self, sha3hash):
        for tx in self.transactions:
            if tx.get_hash() == sha3hash:
                return tx
        return False
    
    def without_hash(self, sha3hash):
        res = []
        for tx in self.transactions:
            if tx.get_hash() != sha3hash:
                res += tx
        return False