import sha3


class Genesis:

    def __init__(self, pearl_owners):
        self.pearl_owners = pearl_owners

    def get_hash(self):
        buffer = bytes()
        for item in self.pearl_owners:
            buffer = buffer + item[0].get_color_bytes() + item[1]
        return sha3.sha3_256(buffer).digest()