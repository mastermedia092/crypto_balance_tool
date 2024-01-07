import asyncio
import aiohttp
from loguru import logger

from config import ADDRESSES
from modules import *
from modules.network import Network

from settings import chainbase_get_balance, get_module
from utils.helpers import get_network
from utils.sleeping import async_sleep


async def run_module(session, address, network, module):
    await chainbase_get_balance(session, address, network, module)


async def main(module):
    async with aiohttp.ClientSession() as session:
        for address in ADDRESSES:
            for network in Network.networks:
                await run_module(session, address, network, module)
                logger.info(f"Balance for {address} in chain {get_network(network)} has been calculated")
                await async_sleep(5, 10)
    
    logger.info("File with balances has been created")


if __name__ == "__main__":
    module = get_module()
    asyncio.run(main(module))
