import unittest

from genesis import Genesis
from pearl import Pearl
from pearlbase import PearlBase
from unspendpearls import UnspendPearls

class TestUnspendPearls(unittest.TestCase):

    def test_get_hash(self):

        o1 = b'\xF0'*33
        o2 = b'\xF1'*33
        o3 = b'\xF2'*33

        pearl_owners = [
            PearlBase(Pearl(0), o1),
            PearlBase(Pearl(1), o2),
        ]
        up = UnspendPearls(pearl_owners)

        tx = up.find_by_owner(o1)
        self.assertTrue(tx)
        self.assertEqual(tx.pearl.color, 0)

        tx = up.find_by_owner(o3)
        self.assertFalse(tx)