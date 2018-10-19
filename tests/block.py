import unittest

from block import Block

class TestBlock(unittest.TestCase):

    def test_unpack(self):

        parrent_transaction_hash = b'\x01'*32
        block_type = b'\x00'
        out_transaction_hash = b'\x02'*32
        new_owner = b'\x03'*33
        signature = b'\x03'*71

        raw = parrent_transaction_hash + block_type + out_transaction_hash + new_owner + signature
        block = Block()
        block.unpack(raw)

        self.assertEqual(block.parrent_transaction_hash, parrent_transaction_hash)
        self.assertEqual(block.block_type, block_type)
        self.assertEqual(block.out_transaction_hash, out_transaction_hash)
        self.assertEqual(block.new_owner, new_owner)
        self.assertEqual(block.signature, signature)

    def test_unpack_block_type(self):

        parrent_transaction_hash = b'\x01'*32
        block_type = b'\x00'
        out_transaction_hash = b'\x02'*32
        new_owner = b'\x03'*33
        signature = b'\x03'*71

        raw = parrent_transaction_hash + block_type + out_transaction_hash + new_owner + signature
        block = Block()
        block.unpack_block_type(raw)

        self.assertEqual(block.block_type, block_type)