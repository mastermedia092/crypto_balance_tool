CHAINBASE_API_KEY = "2aSFuxwp11zf6KPXBkEEuoKtQBi"

ADDRESSES = []
with open("wallets.txt", "r") as file:
    ADDRESSES = file.readlines()

URLS = {
    "erc20": "https://api.chainbase.online/v1/account/tokens",
    "native": "https://api.chainbase.online/v1/account/balance",
}
