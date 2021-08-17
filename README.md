## Creating a virtual Environment that has Python3 as default Interpreter
* A virtual Environment allows each Project to have its own Dependencies
* ```python3 -m venv venv```

### Activate (initialize) the virtual Environment
* ```.\venv\Scripts\activate```

### Deactivate the virtual Environment
* ```deactivate```

### Dependencies
* ```pip install web3```

### Importing and calling everything from Module "web3_connection"
* ```python```
* ```from web3_connection import *```
* ```is_connected()```

## Web3 Ecosystem
![python web3 ecosystem](https://user-images.githubusercontent.com/29623199/129577745-27d90342-65b7-4dd3-9d9d-fff95c5deccf.JPG)
* A dApp interact with a Web3 Library that uses a JSON RPC Protocol to interact with a Provider Node which runs the Blockchain

## Ethereum Transaction
![python transaction](https://user-images.githubusercontent.com/29623199/129596566-874e2ad6-a6d2-4788-923d-81da7afc8bac.JPG)
* A Block contains several Transactions
* A Transaction contains of some Elements like Nonce which is a Method to avoid Double Spending, a Signature which is a private Key and so on

## JSON RPC
* JSON RPC is a Protocol that allows dApps to communicate with a Node in the Network
