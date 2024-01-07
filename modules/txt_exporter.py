from utils.helpers import convert_hex_to_balance, get_network


class TxtExporter:
    
    @staticmethod
    def export_txt(address, chain_id, hex_value):
        balance = convert_hex_to_balance(hex_value)
        result = f"{address} - {get_network(chain_id)} - {balance}"
        with open("balances.txt", "a") as file:
            file.write(result + "\n")
