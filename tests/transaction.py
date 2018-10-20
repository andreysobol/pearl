import unittest
import sha3
from pycoin.key import Key

from transaction import Transaction
from unspendpearls import UnspendPearls
from block import TRANSACTION_TYPE
from pearlbase import PearlBase
from pearl import Pearl

class TestTransaction(unittest.TestCase):

    def test_create_signature(self):

        private_key = 112173377222920129593162218520911143413373757558304408147751653234671616107365
        sha3hash = b'\xf9\xe2\xea\xaaB\xd9\xfe\x9eU\x8a\x9b\x8e\xf1\xbf6o\x19\n\xac\xaa\x83\xba\xd2d\x1e\xe1\x06\xe9\x04\x10\x96\xe4'
        signature = b'0E\x02!\x00\xa6\x84\x81\xe7\xfaU\xe1\x8c\x9a\x100\xe4\xcfi\x98\xee\xb2\xcf\xe4\\\x80\nC%\xd5X\x01\x86\xae\xf0T3\x02 D\x0bR^\xaeJ&\xfc"\xa2\xf6\xb6\xa5\xe2\xbe]\x91\x0b\xb7q{\xa4D1\x80]\x88\xf5Hv\x8f\xb1'

        transaction = Transaction()
        transaction.create_signature(sha3hash, private_key)
        self.assertEqual(signature, transaction.signature)

    def test_verify_signature(self):

        owner = b'\x02\xd3\xdcYh{t%\xe3\x99\x91\x1c\x1b\x12\xbeO\xf6\x95\x83\xd0\xac\xe77\xc4\x1e\xe9\x12\xb4\x00\xd5\xeb\xd2\x14'
        sha3hash = b'\xf9\xe2\xea\xaaB\xd9\xfe\x9eU\x8a\x9b\x8e\xf1\xbf6o\x19\n\xac\xaa\x83\xba\xd2d\x1e\xe1\x06\xe9\x04\x10\x96\xe4'
        signature = b'0E\x02!\x00\xa6\x84\x81\xe7\xfaU\xe1\x8c\x9a\x100\xe4\xcfi\x98\xee\xb2\xcf\xe4\\\x80\nC%\xd5X\x01\x86\xae\xf0T3\x02 D\x0bR^\xaeJ&\xfc"\xa2\xf6\xb6\xa5\xe2\xbe]\x91\x0b\xb7q{\xa4D1\x80]\x88\xf5Hv\x8f\xb1'

        transaction = Transaction()
        self.assertTrue(transaction.verify_signature(sha3hash, owner, signature))
        self.assertFalse(transaction.verify_signature(sha3hash[:31]+b'\x00', owner, signature))

    def test_verify(self):

        k = Key(112173377222920129593162218520911143413373757558304408147751653234671616107365)
        owner = b'\x02\xd3\xdcYh{t%\xe3\x99\x91\x1c\x1b\x12\xbeO\xf6\x95\x83\xd0\xac\xe77\xc4\x1e\xe9\x12\xb4\x00\xd5\xeb\xd2\x14'
        #signature = b'0E\x02!\x00\xa6\x84\x81\xe7\xfaU\xe1\x8c\x9a\x100\xe4\xcfi\x98\xee\xb2\xcf\xe4\\\x80\nC%\xd5X\x01\x86\xae\xf0T3\x02 D\x0bR^\xaeJ&\xfc"\xa2\xf6\xb6\xa5\xe2\xbe]\x91\x0b\xb7q{\xa4D1\x80]\x88\xf5Hv\x8f\xb1'

        pb = PearlBase(Pearl(0), owner)
        up = UnspendPearls([pb])

        raw = pb.get_hash()+TRANSACTION_TYPE+pb.get_hash()+b'\x00'*33
        sha3hash = sha3.sha3_256(raw).digest()
        signature = k.sign(sha3hash)
        raw += signature

        transaction = Transaction()
        transaction.unpack(raw)
        self.assertTrue(transaction.verify(up))