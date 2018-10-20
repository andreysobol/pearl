# Structure:

# parrent_transaction_hash 32b
# block_type 1b 00
# out_transaction_hash 32b
# new_owner 33b
# signature

# parrent_transaction 32b
# block_type 1b 01
# out_transaction 32b
# signature

import sha3

TRANSACTION_TYPE = b'\x00'
WITNESS_TYPE = b'\x01'

class Block:

    def unpack_block_type(self, raw_data):
        self.block_type = raw_data[32:33]
        return self.block_type

    def unpack(self, raw_data):
        self.parrent_transaction_hash = raw_data[:32]
        buffer = raw_data[32:]
        self.block_type = buffer[:1]
        buffer = buffer[1:]
        self.out_transaction_hash = buffer[:32]
        buffer = buffer[32:]
        if self.block_type == TRANSACTION_TYPE:
            self.new_owner = buffer[:33]
        buffer = buffer[33:]
        self.signature = buffer

    def get_hash(self):
        buffer = self.parrent_transaction_hash \
            + self.block_type \
            + self.out_transaction_hash \
            + (self.new_owner if self.block_type == TRANSACTION_TYPE else b'')
        return sha3.sha3_256(buffer).digest()