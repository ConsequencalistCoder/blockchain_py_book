from ape import accounts, project

def main():
    password = '1234567890'
    wealthy_dev = accounts.load("wealthy_working_dev")
    wealthy_dev.set_autosign(True, passphrase=password)
    contract = project.SimpleStorage.deploy(sender=wealthy_dev)
    num_value = contract.retrieve.call()
    print(f"The num value is {num_value}")

