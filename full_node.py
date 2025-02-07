from fastapi import FastAPI, BackgroundTasks, Request
from fastapi.encoders import jsonable_encoder
import uvicorn
import requests
import asyncio
import logging
import sys

from models import *
from blockchain.db import DB
from blockchain.blockchain import Blockchain
from blockchain.wallet import Wallet
from blockchain.api import API
from blockchain.blocks import Input, Output, Tx
from contextlib import asynccontextmanager

class ColorFormatter(logging.Formatter):

    def __init__(self, fmt="%(asctime)s - Blockchain - %(message)s"):
        super(ColorFormatter,self).__init__(fmt)
        red = '\033[0;31m'
        nc = '\033[0m'
        cyan = '\033[0;96m'

        err_fmt  = f"{red}%(asctime)s - Blockchain{nc} - %(message)s"
        info_fmt = f"{cyan}%(asctime)s - Blockchain{nc} - %(message)s"
        self.err = logging.Formatter(err_fmt)
        self.log = logging.Formatter(info_fmt)

    def format(self, record):
        if record.levelno == logging.ERROR:
            return self.err.format(record)
        else:
            return self.log.format(record)


logger = logging.getLogger("Blockchain")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    app.config['sync_running'] = True
    loop = asyncio.get_running_loop()

    # Sync data before running the node
    await loop.run_in_executor(None, sync_data)

    # Add our node address to connected nodes for network broadcasting
    loop.run_in_executor(
        None, 
        broadcast, 
        '/server/add_nodes', 
        {'nodes': [f"{app.config['host']}:{app.config['port']}"]}, 
        False
    )

    if app.config['mine']:
        app.jobs['mining'] = asyncio.Event()
        loop.run_in_executor(None, mine, app.jobs['mining'])

    yield  # Application runs here

    # Shutdown logic
    if app.jobs.get('mining'):
        app.jobs['mining'].set()

'''
TODO:
* sync data while split brain exist 
'''

app = FastAPI(lifespan=lifespan)
app.config = {}
app.jobs = {}

### TASKS
def sync_data():
    logger.info('================== Sync started =================')
    bc = app.config['api']
    # implement block sync

def broadcast(path, data, params=False, fiter_host=None):
    # broadcast data to all connected nodes
    pass

def mine(event):
    logger.info('>>>>>>>>>> Starting mining loop')
    # mine a new block

### SERVER OPERATIONS
@app.post("/chain/stop-mining")
async def stop_mining():
    pass

@app.post("/chain/start-mining")
async def start_minig():
    if not app.jobs.get('mining'):
        loop = asyncio.get_running_loop()
        app.jobs['mining'] = asyncio.Event()
        loop.run_in_executor(None, mine, app.jobs['mining'])

@app.get("/server/nodes")
async def get_nodes():
    return app.config['nodes']

@app.post("/server/add_nodes")
async def add_nodes(nodes:NodesModel, request: Request):
    # add a new node and return true on success
    pass

### DEMO OPERATIONS

@app.get("/demo/send_amount")
async def send_amount(address_to:str, amount:int, background_tasks: BackgroundTasks):
    # Sending amount of coins from server wallet to some other wallet
    pass


### ON CHAIN OPERATIONS

@app.get("/chain/get_amount")
async def get_wallet(address):
    # return the wallet address and balance 
    pass

@app.get("/chain/get_unspent_tx")
async def get_unspent_tx(address):
    # return the unspent txs for the wallet
    pass

@app.get("/chain/status")
async def status():
    # return the status 
    # pass empty_node = True, for not head and 
    # block data for head 
    pass

@app.get("/chain/sync")
async def sync(from_block:int, limit:int=20):
    # sync block 
    pass

@app.post("/chain/add_block")
async def add_block(block:BlockModel, background_tasks: BackgroundTasks, request: Request):
    # add block to the blockchain
    pass

@app.post("/chain/tx_create")
async def add_tx(tx: TxModel, background_tasks: BackgroundTasks, request: Request):
    # add tx to the blockchain
    pass

#### Utils ###########################
def restart_miner():
    pass

if __name__ == "__main__":
    
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(ColorFormatter())
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)

    import argparse
    parser = argparse.ArgumentParser(description='Blockchain full node.')
    parser.add_argument('--node', type=str, help='Address of node to connect. If not will init fist node.')
    parser.add_argument('--port', required=True, type=int, help='Port on which run the node.')
    parser.add_argument('--mine', required=False, type=bool, help='Port on which run the node.')
    parser.add_argument('--diff', required=False, type=int, help='Difficulty')

    args = parser.parse_args()
    _DB = DB()
    _DB.config['difficulty']
    _W = Wallet.create()
    _BC = Blockchain(_DB, _W)
    _API = API(_BC)
    logger.info(' ####### Server address: %s ########' %_W.address)

    app.config['db'] = _DB
    app.config['wallet'] = _W
    app.config['bc'] = _BC
    app.config['api'] = _API
    app.config['port'] = args.port  
    app.config['host'] = '127.0.0.1'
    app.config['nodes'] = set([args.node]) if args.node else set(['127.0.0.1:%s' % args.port])
    app.config['sync_running'] = False
    app.config['mine'] = args.mine

    if not args.node:
        _BC.create_first_block()

    uvicorn.run(app, host="127.0.0.1", port=args.port, access_log=True)