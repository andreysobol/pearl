import unittest
import sha3

from genesis import Genesis
from pearl import Pearl

class TestGenesis(unittest.TestCase):

    def test_get_hash(self):

        pearl_owners = [
            (Pearl(0),b'\xF0'*33),
            (Pearl(1),b'\xF1'*33),
        ]
        genesis = Genesis(pearl_owners)
        gh = genesis.get_hash()

        h = sha3.sha3_256(b'\x00'+(b'\xF0'*33)+b'\x01'+(b'\xF1'*33)).digest()
        self.assertEqual(h, gh)