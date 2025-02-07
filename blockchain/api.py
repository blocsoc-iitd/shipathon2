from .blocks import Tx, Block

class API:
    '''
        wrapper code for api methods.
    '''

    def __init__(self, blockchain):
        pass

    def get_user_balance(self, address):
        # fetch user balances from db unspent_outputs_amount and return total
        pass
    def get_user_unspent_txs(self, address):
        # fetch user unspent txs from db and return unspent txs data
        pass
    def get_chain(self, from_block:int, limit:int=20):
        # fetch blocks from from_block to from_block+limit
        pass
    def add_block(self, block):
        # add block to the blockchain
        pass
    def mine_block(self, check_stop=None):
        # mine a new block
        pass
    def add_tx(self, tx):
        # add tx to the blockchain
        pass
    def get_head(self):
        # return the head of the blockchain
        pass