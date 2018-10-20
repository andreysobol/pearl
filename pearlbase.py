import sha3


class PearlBase:

    def __init__(self, pearl, owner):
        self.pearl = pearl
        self.owner = owner
    
    def get_bytes(self):
        return self.pearl.get_color_bytes() + self.owner

    def get_hash(self):
        return sha3.sha3_256(self.pearl.get_color_bytes() + self.owner).digest()
    
    def get_new_owner(self):
        return self.owner