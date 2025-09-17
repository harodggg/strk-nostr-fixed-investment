import os
import asyncio
from stake import claim_stark
from loguru import logger


PRIVATE_KEY = os.getenv(
    'PRIVATE_KEY', 'you need to set a enviroment variable for private_key')
logger.info(f"PRIVATE_KEY: {PRIVATE_KEY}")
ADDRESS = os.getenv(
    "ADDRESS", "you need to set a enviroment variable for address")
logger.info(f"ADDRESS: {ADDRESS}")


if __name__ == "__main__":
    logger.info("Over above is ok, now staring...")
    asyncio.run(claim_stark(
        {"private_key": PRIVATE_KEY, "address": ADDRESS}))
