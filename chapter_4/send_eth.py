from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

sender_private_key = "0x8b92f58b3cdbbf136a51cb960715423a7962370f6dbcaeaf8794dbefe6f9fbe1"

sender_address = "0x1F279d982Cb7919C4Cb88ebdfe923A630C8D5e38"

recipient_address = "0xf355eC388b03E71AaC5c1551EcCC1C8Ced8421Ac"

amount = Web3.to_wei(5, 'ether')

transaction = {
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