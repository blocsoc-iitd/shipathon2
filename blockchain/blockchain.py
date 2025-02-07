from .blocks import Block, Tx, Input, Output
from .verifiers import TxVerifier, BlockOutOfChain, BlockVerifier, BlockVerificationFailed
import logging

logger = logging.getLogger('Blockchain')

class Blockchain:

    __slots__ = 'max_nonce', 'chain', 'unconfirmed_transactions', 'db', 'wallet', 'on_new_block', 'on_prev_block', 'current_block_transactions', 'fork_blocks'

    def __init__(self, db, wallet, on_new_block=None, on_prev_block=None):
        pass

    def create_first_block(self):
        """
        Creating first block in a chain. Only COINBASE Tx.
        """
        
    def create_coinbase_tx(self, address, amount):
        """
        Create a coinbase transaction.
        """
        
    def is_valid_block(self, block):
        """
        Check if the block is valid.
        """

    def add_block(self, block):
        """
        Add block to the blockchain.
        """

    def add_tx(self, tx):
        """
        Add transaction to the blockchain.
        """

    def force_block(self, check_stop=None):
        """
        Force block to the blockchain.
        """

    def rollover_block(self, block):
        """
        As we use some sort of DB, we need way to update it depends we need add block or remove.
        So we have 2 methods Rollover and Rollback.
        Also i added some sort of callback in case some additional functionality should be added on top.
        For example some Blockchain analytic DB.
        """

    def rollback_block(self, block):
        """
        Rollback block from the blockchain.
        """

    def mine_block(self, check_stop=None):
        """
        Mine a new block with ability to stop in case if check callback return True.
        """

    @property
    def head(self):
        """
        Return the head of the blockchain.
        """
        
    @property
    def blockchain(self):
        """
        Return the blockchain.
        """