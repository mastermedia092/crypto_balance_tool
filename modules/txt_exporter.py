from utils.helpers import *


class TxtExporter:
    @staticmethod
    def export_txt(address, chain_id, hex_value):
        balance = convert_hex_to_balance(hex_value)
        usdt_balance = convert_eth_to_usdt(balance)
        result = f"{address} - {get_network(chain_id)} - {balance} - {usdt_balance}"
        with open("balances.txt", "a") as file:
            file.write(result + "\n")
