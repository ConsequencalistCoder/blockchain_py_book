from web3 import Web3

KEY_FILE = "/tmp/go-ethereum-keystore4024939732/UTC--2025-04-15T14-10-31.690955436Z--79c9d429febb1ca7233f8ebf1dada01fdc89ae72"
PASSWORD = ""

# initiate the geth channel first
w3 = Web3(Web3.IPCProvider('/tmp/geth.ipc'))

with open(KEY_FILE) as keyfile:
    encrypted_key = keyfile.read()
    password = PASSWORD
    sender_private_key = w3.eth.account.decrypt(encrypted_key, password)

print(sender_private_key.hex())