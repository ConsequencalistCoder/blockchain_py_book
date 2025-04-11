from web3 import Web3

with open("abi.json") as f:
    abi = f.read().strip()

w3 = Web3(Web3.IPCProvider('/tmp/geth.ipc'))

address = "0xEC44C431D4430F8750B89C60804a85e1c9032980"
contract = w3.eth.contract(address=address, abi=abi)

logs = contract.events.Donation().get_logs()

for log in logs:
    print(f"The donatur address is {log.args.donatur}")
    print(f"The donation amount is {log.args.amount}")