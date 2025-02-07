import time
from hashlib import sha256
from pymerkle import InmemoryTree as MerkleTree
import base64
from .wallet import Address


class Input:
    __slots__ = 'prev_tx_hash', 'output_index', 'signature', '_hash', 'address', 'index', 'amount'

    def __init__(self, prev_tx_hash, output_index, signature, address, amount, index):
        pass

    def sign(self, wallet):
        pass
    
    @property
    def hash(self):
        pass

    @property
    def as_dict(self):
        return {
            "prev_tx_hash":self.prev_tx_hash,
            "output_index":self.output_index,
            "address":str(self.address),
            "index":self.index,
            "hash":self.hash,
            "signature":self.signature
        }

    @classmethod
    def from_dict(cls, data):
        inst = cls(
            data['prev_tx_hash'],
            data['output_index'],
            Address(data['address']),
            data['index'],
        )
        inst.signature = data['signature']
        inst._hash = None
        return inst

class Output:

    __slots__ = '_hash', 'address', 'index', 'amount', 'input_hash'
    def __init__(self, address, amount, index):
        pass

    @property
    def hash(self):
        pass

    @property
    def as_dict(self):
        return {
            "amount":int(self.amount),
            "address":str(self.address),
            "index":self.index,
            "input_hash": self.input_hash,
            "hash":self.hash
        }
        
    @classmethod
    def from_dict(cls, data):
        inst = cls(
            Address(data['address']),
            data['amount'],
            data['index'],
        )
        inst.input_hash = data['input_hash']
        inst._hash = None
        return inst

class Tx:
    __slots__ = 'inputs', 'outputs', 'timestamp', '_hash'

    def __init__(self, inputs, outputs, timestamp=None):
        pass

    @property
    def hash(self):
        pass

    @property
    def as_dict(self):
        inp_hash = sha256((str([el.as_dict for el in self.inputs]) + str(self.timestamp)).encode()).hexdigest()
        for el in self.outputs:
            el.input_hash = inp_hash
        return {
            "inputs":[el.as_dict for el in self.inputs],
            "outputs":[el.as_dict for el in self.outputs],
            "timestamp":self.timestamp,
            "hash":self.hash
        }

    @classmethod
    def from_dict(cls, data):
        inps = [Input.from_dict(el) for el in data['inputs']]
        outs = [Output.from_dict(el) for el in data['outputs']]
        inp_hash = sha256((str([el.as_dict for el in inps]) + str(data['timestamp'])).encode()).hexdigest()
        for el in outs:
            el.input_hash = inp_hash
            
        inst = cls(
            inps,
            outs,
            data['timestamp'],
        )
        inst._hash = None
        return inst

class Block:
    __slots__ = 'nonce', 'prev_hash', 'index', 'txs', 'timestamp', 'merkel_root'

    def __init__(self, txs, index, prev_hash, timestamp=None, nonce=0):
        pass

    def build_merkle_tree(self):
        pass

    def hash(self, nonce=None):
        pass
    @property
    def as_dict(self):
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "prev_hash": self.prev_hash,
            "hash": self.hash(),
            "txs": [el.as_dict for el in self.txs],
            "nonce": self.nonce,
            "merkel_root":self.merkel_root
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            [Tx.from_dict(el) for el in data['txs']],
            data['index'],
            data['prev_hash'],
            data['timestamp'],
            data['nonce']
        )