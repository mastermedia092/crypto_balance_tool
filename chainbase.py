import asyncio
from loguru import logger
from web3 import Web3

from config import CHAINBASE_API_KEY, URLS
from converters import convertHexToBalance
from excel_exporter import ExcelExporter
from network import Network
from wallet import Wallet
import os


class Chainbase:
    def __init__(self, session):
        self.chain_id = None
        self.session = session
        self.urls = URLS
        self.headers = {
            "accept": "application/json",
            "x-api-key": CHAINBASE_API_KEY,
        }

    async def get_token_balance(self, address, chain_id, type):
        params = {"chain_id": chain_id, "address": address, "limit": 20, "page": 1}
        try:
            sleep = 3

            async with self.session.get(
                URLS[type], headers=self.headers, params=params, timeout=10
            ) as resp:
                if resp.status == 200:
                    resp_json = await resp.json(content_type=None)
                    if resp_json["data"] is None:
                        logger.warning(f"no data for {address} on {Network.networks.get(chain_id)}")
                        return

                    if isinstance(resp_json["data"], str):
                        balance = convertHexToBalance(resp_json["data"])
                        
                        # Save result to txt file
                        result = f"{address} - {chain_id} - {balance}"
                        with open("balances.txt", "a") as file:
                            file.write(result + "\n")
                            return

                    wallet = Wallet(address, chain_id)
                    wallet.add_asset(resp_json["data"])
                    excel_exporter = ExcelExporter("balances.xlsx")
                    excel_exporter.export_data(wallet, address, chain_id)
                else:
                    await asyncio.sleep(sleep)

        except Exception as error:
            logger.info(f"error: {error}")
            logger.info(f"{address} : {error}, try again in {sleep} sec.")
            await asyncio.sleep(3)
