import sha3


class Genesis:

    def __init__(self, pearl_owners):
        self.pearl_owners = pearl_owners

    def get_hash(self):
        buffer = []
        for item in pearl_owners:
            buffer = buffer + item[0] + item[1]
        return sha3.sha3_256(buffer).digest()