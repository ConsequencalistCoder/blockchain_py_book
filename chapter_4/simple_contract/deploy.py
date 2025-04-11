from web3 import Web3

w3 = Web3(Web3.IPCProvider('/tmp/geth.ipc'))

with open("bytecode.txt") as f:
    bytecode = f.read().strip()

with open("abi.json") as f:
    abi = f.read().strip()

with open("../my_keystore/UTC--2025-04-11T16-27-48.212634191Z--234db75620bc62d2918ec71198a92194f94b88ac") as keyfile:
    encrypted_key = keyfile.read()
    password = "1234567890"
    deployer_private_key = w3.eth.account.decrypt(encrypted_key, password)

deployer_address = Web3.to_checksum_address("234db75620bc62d2918ec71198a92194f94b88ac")

contract = w3.eth.contract(abi=abi, bytecode=bytecode)

transaction = contract.constructor().build_transaction({
    'from': deployer_address,
    'nonce': w3.eth.get_transaction_count(deployer_address),
    'gas': 200000,
    'gasPrice': Web3.to_wei('50', 'gwei')
})

signed_transaction = w3.eth.account.sign_transaction(transaction, deployer_private_key)

transaction_hash = w3.eth.send_raw_transaction(signed_transaction.raw_transaction)

print(transaction_hash)