import json
from web3 import Web3

//localhost rpc call
url = 'http://127.0.0.1:7545';
web3 = Web3(Web3.HTTPProvider(url));

abi2 = json.loads('[ {"inputs": [{"internalType": "uint256","name": "_value","type": "uint256"}],"stateMutability": "nonpayable","type": "constructor"},{"inputs": [],"name": "getBalance","outputs": [{"internalType": "uint256","name": "","type": "uint256"}],"stateMutability": "view","type": "function"},{"inputs": [],"name": "getOwner","outputs": [{"internalType": "address","name": "","type": "address"}],"stateMutability": "view","type": "function"},{"inputs": [{"internalType": "uint256","name": "_amount","type": "uint256"}],"name": "transfer","outputs": [{"internalType": "bool","name": "","type": "bool"}],"stateMutability": "nonpayable","type": "function"}]')

#smart address
address = "";
contract = web3.eth.contract(address=address,abi=abi2)

#need to put .call() at the end to call the smart contract
Owner = contract.functions.getOwner().call()

#result
print('Contract Owner: ',Owner)
print('Get Balance msg.sender: ',contract.functions.getBalance().call())

#nonce prints number of tx
nonce = web3.eth.getTransactionCount(address);

print('nonce: ',nonce)
