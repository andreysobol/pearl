class Chain:
    
    def __init__(self, genesis):
        self.genesis = genesis
        self.blocks = [genesis]
        self.current_unspend_pearls = genesis.unspend_pearls

    def add_transaction(self):
        pass