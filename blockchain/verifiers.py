import rsa
import binascii

from .wallet import Address

class TxVerifier:
    def __init__(self, tx):
        self.tx = tx

    def verify(self):
        '''Verify the transaction'''
        pass

class BlockVerifier:
    def __init__(self, db):
        pass

    def verify(self, head, block):
        pass