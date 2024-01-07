import sys
import questionary
from questionary import Choice
from chainbase import Chainbase


async def chainbase_get_balance(session, address, network, type):
    chainbase = Chainbase(session)
    await chainbase.get_token_balance(address, network, type)


def get_module():
    result = questionary.select(
        "Select a method to get started",
        choices=[
            # Choice("1) Get native token balances (Chainbase)", "native"),
            Choice("1) Get ERC20 token balances (Chainbase)", "erc20"),
        ],
        qmark="🛠 ",
        pointer="✅ ",
    ).ask()
    if result == "exit":
        sys.exit()
    return result
