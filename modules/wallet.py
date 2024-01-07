from utils import *
from utils.helpers import convert_hex_to_balance, convert_hex_to_total_supply

class Wallet:
    def __init__(self, address, chain_id):
        self.address = address
        self.network = chain_id
        self.assets = []

    def add_asset(self, data):
        self.assets.extend([Asset(**asset) for asset in data])


class Asset:
    def __init__(
        self,
        balance,
        contract_address,
        current_usd_price,
        decimals,
        logos,
        name,
        symbol,
        total_supply,
        urls,
    ):
        self.balance = convert_hex_to_balance(balance)
        self.contract_address = contract_address
        self.current_usd_price = current_usd_price
        self.decimals = decimals
        self.logos = logos
        self.name = name
        self.symbol = symbol
        self.total_supply = convert_hex_to_total_supply(total_supply, decimals)
        self.urls = urls
