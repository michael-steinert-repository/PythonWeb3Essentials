import os
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()
node_provider = os.environ['NODE_PROVIDER_LOCAL']

web3_connection = Web3(Web3.HTTPProvider(node_provider))

global_gas = 4200000
global_gas_price = web3_connection.toWei(8, "gwei")


def is_connected():
    print("Connected to Ganache: " + str(web3_connection.isConnected()))


def get_nonce(ethereum_address):
    return web3_connection.eth.get_transaction_count(ethereum_address)


# Calling the Function: transfer_ether(os.environ["ADDRESS_1"],os.environ["ADDRESS_2"],os.environ["PRIVATE_KEY_1"], 42)
def transfer_ether(sender, receiver, signature, amount):
    # Creating a Dictionary for a Transaction
    transaction_body = {
        "nonce": get_nonce(sender),
        "to": receiver,
        "value": web3_connection.toWei(amount, "ether"),
        "gas": global_gas,
        "gasPrice": global_gas_price
    }
    signed_transaction = web3_connection.eth.account.sign_transaction(transaction_body, signature)
    # sending the raw Transaction to Blockchain
    result = web3_connection.eth.send_raw_transaction(signed_transaction.rawTransaction)
    return result
