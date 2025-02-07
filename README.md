# 🚀 Proof-of-Work Blockchain — Shipathon Project

Welcome to the Shipathon! 🎉 This project is a simplified proof-of-work blockchain built in Python. Your task is to complete the missing components and get the blockchain up and running!

## 📁 Project Structure

```
.
├── requirements.txt        # Dependencies for the project
├── models.py               # Data models for the blockchain
├── full_node.py            # Full node implementation
├── blockchain/
│   ├── api.py              # FastAPI methods (already implemented)
│   ├── blockchain.py       # Core blockchain logic
│   ├── blocks.py           # Block structure (to be completed)
│   ├── verifiers.py        # Block validation logic
│   ├── db.py               # Database layer (to be completed)
│   ├── wallet.py           # Wallet implementation (to be completed)
```

## 🏁 Getting Started

### 1️⃣ Install Dependencies

You can use a virtual environment or an Anaconda environment for better dependency management.

#### Using a Virtual Environment
Ensure you have Python 3.8+ installed. Then, install required packages:
```sh
pip install -r requirements.txt
```

#### Using Anaconda (Optional)
Create and activate a new Anaconda environment:
```sh
conda create --name blockchain-env python=3.8
conda activate blockchain-env
pip install -r requirements.txt
```
Ensure you have Python 3.8+ installed. Then, install required packages:
```sh
pip install -r requirements.txt
```

### 2️⃣ Implement Core Components
Complete the following files in order:

1. `wallet.py` - Implement wallet creation and digital signatures.
2. `db.py` - Implement persistent storage for the blockchain.
3. `blocks.py` - Define the structure of a block.
4. `blockchain.py` - Implement the blockchain class with proof-of-work logic.
5. `blockchain/api.py` - Connect blockchain logic with API endpoints.
6. `full_node.py` - Set up a full node to run the blockchain network.
7. `verifiers.py` - Implement block validation logic.

### 4️⃣ Usage Instructions
Open 3 terminals. In the first terminal, run:
```sh
python3 full_node.py --port=8000 -mine=1
```
After you see that the server is up and the sync process has finished, run the following commands in two additional terminals:
```sh
python3 full_node.py --port=8001 --node=127.0.0.1:8000 --mine=1
```
```sh
python3 full_node.py --port=8002 --node=127.0.0.1:8000 --mine=1
```

### 3️⃣ Run the API Server

Access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## 🎯 Goal
By the end of this Shipathon, you'll have a working blockchain with:
✅ Blocks mined using Proof-of-Work (PoW)
✅ Secure digital wallets with public-private key encryption
✅ A REST API to interact with the blockchain

Good luck, and happy coding! 🚀

