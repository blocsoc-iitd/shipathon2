import pickle
from collections import defaultdict

class DB:
    """Database class to store key-value pairs"""
    def __init__(self):
        #  config should contain txs_per_block, mining_reward, difficulty
        self.config = {  
        }
        # initialize the block_index, transaction_by_hash, unspent_txs_by_user_hash, unspent_output_amounts
        # unspent_txs_by_user_hash is a defaultdict with default set to set.
        # unspent_output_amounts is a defaultdict with default set to dict.

    '''
        simple routine to save/restore db data for block number
    '''
    def backup(self):
        with open('block_%s' % self.block_index,'wb') as fp:
            pickle.dump(self.__dict__, fp)

    @classmethod
    def restore(cls, block_index):
        with open('block_%s' % block_index, 'rb') as fp:
            data = pickle.load(fp)

        inst = cls()
        inst.__dict__ = data
        return inst