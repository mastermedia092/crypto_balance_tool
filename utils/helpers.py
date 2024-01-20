from web3 import Web3
from modules.network import Network


@staticmethod
def convert_hex_to_balance(hex_value):
    return Web3.from_wei(int(hex_value, 16), "ether")


@staticmethod
def convert_hex_to_total_supply(hex_value, decimals):
    decimal = 10**decimals
    return int(hex_value, 16) / decimal


@staticmethod
def get_network(chain_id):
    return Network.networks.get(chain_id)

@staticmethod
def convert_eth_to_usdt(eth_amount):
    eth_to_usdt_rate = 2470,43
    return eth_amount * eth_to_usdt_rate

