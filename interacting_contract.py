import os
from dotenv import load_dotenv
from web3 import Web3
import json

''''
// SPDX-License-Identifier: MIT
pragma solidity >=0.7.0 <0.9.0;

contract GuessNumber {
    uint secretNumber;
    enum State {
        ACTIVE,
        COMPLETE
    }
    State public currentState;
    uint balance;
    
    constructor(uint _secretNumber) payable {
        require(msg.value >= 10 * (10**18), "At least 10 ETH needs to be funded");
        secretNumber = _secretNumber;
        balance = msg.value;
    }
    
    function getBalance() public view returns (uint) {
        return balance;
    }
    
    function guessNumber(address payable _guesser, uint _numberGuess) external payable returns (uint) {
        require(msg.value >= 1 * (10**18), "At least 1 ETH needs to be payed");
        require(currentState == State.ACTIVE, "Guess Number is completed");
        balance = balance + msg.value;
        if (_numberGuess == secretNumber) {
            /* Transferring all Amount of Smart Contract to the right Guesser */
            _guesser.transfer(address(this).balance);
            currentState = State.COMPLETE;
            return balance;
        } else {
            return balance;
        }
    }
}
'''
load_dotenv()
node_provider = os.environ['NODE_PROVIDER_LOCAL']

web3_connection = Web3(Web3.HTTPProvider(node_provider))

# ABI of Smart Contract
contract_abi = json.loads('[{"inputs":[{"internalType":"uint256","name":"_secretNumber","type":"uint256"}],"stateMutability":"payable","type":"constructor"},{"inputs":[],"name":"currentState","outputs":[{"internalType":"enum GuessNumber.State","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address payable","name":"_guesser","type":"address"},{"internalType":"uint256","name":"_numberGuess","type":"uint256"}],"name":"guessNumber","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"payable","type":"function"}]')
contract_bytecode = "0x608060405260405161077b38038061077b83398181016040528101906100259190610099565b678ac7230489e80000341015610070576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610067906100e5565b60405180910390fd5b806000819055503460028190555050610186565b6000815190506100938161016f565b92915050565b6000602082840312156100ab57600080fd5b60006100b984828501610084565b91505092915050565b60006100cf602283610105565b91506100da82610120565b604082019050919050565b600060208201905081810360008301526100fe816100c2565b9050919050565b600082825260208201905092915050565b6000819050919050565b7f4174206c6561737420313020455448206e6565647320746f2062652066756e6460008201527f6564000000000000000000000000000000000000000000000000000000000000602082015250565b61017881610116565b811461018357600080fd5b50565b6105e6806101956000396000f3fe6080604052600436106100345760003560e01c806308f09b34146100395780630c3f6acf1461006957806312065fe014610094575b600080fd5b610053600480360381019061004e91906102e0565b6100bf565b60405161006091906103db565b60405180910390f35b34801561007557600080fd5b5061007e610299565b60405161008b9190610380565b60405180910390f35b3480156100a057600080fd5b506100a96102ac565b6040516100b691906103db565b60405180910390f35b6000670de0b6b3a764000034101561010c576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016101039061039b565b60405180910390fd5b60006001811115610146577f4e487b7100000000000000000000000000000000000000000000000000000000600052602160045260246000fd5b600160009054906101000a900460ff16600181111561018e577f4e487b7100000000000000000000000000000000000000000000000000000000600052602160045260246000fd5b146101ce576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016101c5906103bb565b60405180910390fd5b346002546101dc9190610407565b60028190555060005482141561028d578273ffffffffffffffffffffffffffffffffffffffff166108fc479081150290604051600060405180830381858888f19350505050158015610232573d6000803e3d6000fd5b5060018060006101000a81548160ff0219169083600181111561027e577f4e487b7100000000000000000000000000000000000000000000000000000000600052602160045260246000fd5b02179055506002549050610293565b60025490505b92915050565b600160009054906101000a900460ff1681565b6000600254905090565b6000813590506102c581610582565b92915050565b6000813590506102da81610599565b92915050565b600080604083850312156102f357600080fd5b6000610301858286016102b6565b9250506020610312858286016102cb565b9150509250929050565b610325816104ac565b82525050565b60006103386020836103f6565b91506103438261051c565b602082019050919050565b600061035b6019836103f6565b915061036682610545565b602082019050919050565b61037a816104a2565b82525050565b6000602082019050610395600083018461031c565b92915050565b600060208201905081810360008301526103b48161032b565b9050919050565b600060208201905081810360008301526103d48161034e565b9050919050565b60006020820190506103f06000830184610371565b92915050565b600082825260208201905092915050565b6000610412826104a2565b915061041d836104a2565b9250827fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff03821115610452576104516104be565b5b828201905092915050565b600061046882610482565b9050919050565b600081905061047d8261056e565b919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000819050919050565b60006104b78261046f565b9050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602160045260246000fd5b7f4174206c65617374203120455448206e6565647320746f206265207061796564600082015250565b7f4775657373204e756d62657220697320636f6d706c6574656400000000000000600082015250565b6002811061057f5761057e6104ed565b5b50565b61058b8161045d565b811461059657600080fd5b50565b6105a2816104a2565b81146105ad57600080fd5b5056fea264697066735822122003e03b75244f688ebbe36e8f6e8a154ae32f2eb3b6915a48a9885cf910d3b16564736f6c63430008040033"
# Example Smart Contract Address
contract_address = Web3.toChecksumAddress("0x566b27F3BA138ED19789C5ddf7DF6ef822e0B0e2")

global_gas = 4200000
global_gas_price = web3_connection.toWei(8, "gwei")


def is_connected():
    print("Connected to Ganache: " + str(web3_connection.isConnected()))

# deploy_contract(42, 10, os.environ["ADDRESS_1"], os.environ["PRIVATE_KEY_1"])
def deploy_contract(secret_number, amount, owner, signature):
    guess_number = web3_connection.eth.contract(abi=contract_abi, bytecode=contract_bytecode)
    # Creating Dictionary for Transaction Body
    transaction_body = {
        "nonce": get_nonce(owner),
        "value": web3_connection.toWei(amount, "ether")
    }
    # Building the Deployment with the Constructor of Smart Contract
    deployment = guess_number.constructor(secret_number).buildTransaction(transaction_body)
    signed_transaction = web3_connection.eth.account.sign_transaction(deployment, signature)
    # Deployment of Smart Contract
    result = web3_connection.eth.send_raw_transaction(signed_transaction.rawTransaction)
    return result

def get_balance(contract_address):
    # Creating a Contract Object of Smart Contract
    contract = web3_connection.eth.contract(address=contract_address, abi=contract_abi)
    # getBalance() is a Method from the Smart Contract (ABI)
    # call() is a Python Method to call the Object of Smart Contract
    balance_contract = web3_connection.fromWei(contract.functions.getBalance().call(), "ether")
    return balance_contract

def get_nonce(ethereum_address):
    return web3_connection.eth.get_transaction_count(ethereum_address)

def guessNumber(guesser, number_guess, amount, signature):
    # Creating a Contract Object of Smart Contract
    contract = web3_connection.eth.contract(address=contract_address, abi=contract_abi)
    # Creating Dictionary for Transaction Body
    transaction_body = {
        "nonce": get_nonce(guesser),
        "value": web3_connection.toWei(amount, "ether")
    }
    function_call = contract.functions.guessNumber(guesser, number_guess).buildTransaction(transaction_body)
    signed_transaction = web3_connection.eth.account.sign_transaction(function_call, signature)
    result = web3_connection.eth.send_raw_transaction(signed_transaction.rawTransaction)
    return result
