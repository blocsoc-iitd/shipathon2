import rsa
import binascii

class Address:
    def __init__(self, addr):
        # check if rsa.PublicKey object and initiate the address.
        pass
    def __str__(self):
        # return the address in string format
        pass

    @property
    def key(self):
        # return the public key
        pass

class Wallet:
    '''For real case wallet use ECDSA cryptography'''

    __slots__ = '_pub', '_priv'
    
    def __init__(self, pub=None, priv=None):
        if pub:
            pass
            # initiate the pub key and priv key
    
    @classmethod
    def create(cls):
        pass
        # create a new wallet
        # generate a new key pair
        # return a new wallet object

    @classmethod
    def verify(cls, data, signature, address):
        signature = binascii.unhexlify(signature.encode())
        # verify the signature
        # return signature validity
    
    @property
    def address(self):
        return str(self._pub)

    @property
    def priv(self):
        return self._priv.save_pkcs1()
    
    def sign(self, hash):
        return binascii.hexlify(rsa.sign(hash, self._priv, 'SHA-256')).decode()