import sha3

class Pearl:

    def __init__(self, color):
        self.color = color
    
    def get_color_bytes(self):
        return bytes([self.color])

    def get_hash(self):
        sha3.sha3_256(self.get_color_bytes()).digest()