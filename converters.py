from web3 import Web3


@staticmethod
def convertHexToBalance(hex_value):
    return Web3.from_wei(int(hex_value, 16), "ether")

@staticmethod
def convertHexToTotalSupply(hex_value, decimals):
    decimal = 10 ** decimals 
    return int(hex_value, 16) / decimal
