import random
import asyncio

from tqdm import tqdm


async def async_sleep(sleep_from: int, sleep_to: int):
    delay = random.randint(sleep_from, sleep_to)
    with tqdm(
        total=delay,
        desc="💤 Sleep",
        bar_format="{desc}: |{bar:20}| {percentage:.0f}% | {n_fmt}/{total_fmt}",
        colour="green",
    ) as pbar:
        for _ in range(delay):
            await asyncio.sleep(1)
            pbar.update(1)
