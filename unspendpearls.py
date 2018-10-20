class UnspendPearls:

    def __init__(self, transactions):
        self.transactions = transactions

    def find_by_owner(self, owner):
        for tx in self.transactions:
            if tx.owner == owner:
                return tx
        return False