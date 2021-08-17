import os
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()
node_provider = os.environ['NODE_PROVIDER']

web3_connection = Web3(Web3.HTTPProvider(node_provider))


def is_connected():
    print("Connected to Infura: " + str(web3_connection.isConnected()))


def latest_block():
    print(web3_connection.eth.block_number)


def balance_of(ethereum_address):
    balance = web3_connection.eth.get_balance(ethereum_address)
    balance_ether = web3_connection.fromWei(balance, "ether")
    print(balance)
    print(balance_ether)
