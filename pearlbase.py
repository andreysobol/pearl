class PearlBase:

    def __init__(self, pearl, owner):
        self.pearl = pearl
        self.owner = owner
    
    def get_bytes(self):
        return self.pearl.get_color_bytes() + self.owner