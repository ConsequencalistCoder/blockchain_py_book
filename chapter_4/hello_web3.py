from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

print(f"Python script is connected? {w3.is_connected()}")

account_balance = w3.eth.get_balance('0x1F279d982Cb7919C4Cb88ebdfe923A630C8D5e38')

print(f"The balance of the 3rd account is {account_balance}")