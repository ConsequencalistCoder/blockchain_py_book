import web3
from web3 import Web3

w3 = Web3(Web3.IPCProvider('/tmp/geth.ipc'))

with open("my_keystore/UTC--2025-04-11T16-27-48.212634191Z--234db75620bc62d2918ec71198a92194f94b88ac") as keyfile:
    encrypted_key = keyfile.read()
    password = "1234567890"
    sender_private_key = w3.eth.account.decrypt(encrypted_key, password)

sender_address =  Web3.to_checksum_address("234db75620bc62d2918ec71198a92194f94b88ac")

recipient_address = Web3.to_checksum_address("0xd30561464ee30ff007e8e1c49aa950448db485bd")

amount = Web3.to_wei(2, 'ether')

transaction = {
    'chainId': 1337,
    'from': sender_address,
    'to': recipient_address,
    'value': amount,
    'gas': 21000,
    'gasPrice': Web3.to_wei('50', 'gwei'),
    'nonce': w3.eth.get_transaction_count(sender_address),
}

signed_transaction = w3.eth.account.sign_transaction(transaction, sender_private_key)

transaction_hash = w3.eth.send_raw_transaction(signed_transaction.raw_transaction)

print(transaction_hash)