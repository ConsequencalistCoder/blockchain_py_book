from web3 import Web3

with open("abi.json") as f:
    abi = f.read().strip()

w3 = Web3(Web3.IPCProvider('/tmp/geth.ipc'))

account_address =  Web3.to_checksum_address("234db75620bc62d2918ec71198a92194f94b88ac")

with  open("../my_keystore/UTC--2025-04-11T16-27-48.212634191Z--234db75620bc62d2918ec71198a92194f94b88ac") as keyfile:
    encrypted_key = keyfile.read()
    password = "1234567890"
    account_private_key = w3.eth.account.decrypt(encrypted_key, password)

address = Web3.to_checksum_address("0xEC44C431D4430F8750B89C60804a85e1c9032980")
contract = w3.eth.contract(address=address, abi=abi)

transaction = contract.functions.donate().build_transaction({
    'from': account_address,
    'value': Web3.to_wei('1', 'ether'),
    'nonce': w3.eth.get_transaction_count(account_address),
    'gas': 200000,
    'gasPrice': Web3.to_wei('50', 'gwei')
})

signed_transaction = w3.eth.account.sign_transaction(transaction, account_private_key)

transaction_hash = w3.eth.send_raw_transaction(signed_transaction.raw_transaction)

print(transaction_hash)