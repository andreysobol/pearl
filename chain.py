from block import Block, TRANSACTION_TYPE

class Chain:
    
    def __init__(self, genesis):
        self.genesis = genesis
        self.blocks = [genesis]
        self.current_unspend_pearls = genesis.unspend_pearls

    def add_transaction(self, raw):
        transaction = Transaction()
        transaction.unpack(raw)
        if transaction.verify(current_unspend_pearls):
            tx_list = current_unspend_pearls.without_hash(transaction.out_transaction_hash)
            tx_list.append(transaction)
            up = UnspendPearls(tx_list)
            transaction.set_unspend_pearls(up)
            self.current_unspend_pearls = up

    def add_block(self, raw):
        block = Block()
        block.unpack_block_type(raw)
        if block.block_type == TRANSACTION_TYPE:
            self.add_transaction(self, raw)