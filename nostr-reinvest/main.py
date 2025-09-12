import asyncio
from starknet_py.net.full_node_client import FullNodeClient
from starknet_py.contract import Contract

FULLNODE_RPC = "http://pathfinder.xxxyyy.space/rpc/v0_9"
client = FullNodeClient(node_url=FULLNODE_RPC)

CONTRACT_ADDRESS = 0x049d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7
ABI = [
    {
        "name": "balanceOf",
        "type": "function",
        "inputs": [{"name": "account", "type": "felt"}],
        "outputs": [{"name": "balance", "type": "felt"}],
        "stateMutability": "view"
    }
]


USDC_CONTRACT_ADDRESS = 0x053c91253bc9682c04929ca02ed00b3e423f14cd4076060cfa724545620a2d

USDT_CONTRACT_ADDRESS = 0x068f5c6a1e8e50337c72477161ac2408b68a3563914945d7a64c483984102607

STARK_CONTRACT_ADDRESS = 0x04718f5a0fc34cc1af16a1cdee98ffb20c31f5cd61d6ab07201858f4287c938d


async def query_balance(address, coin_contract):


async def main():
    address = 0x0729373f0e1e4e9ba6f8923d0e089a63625258ec8d0649ad4456b1c6f4b417b9
    await query_balance(address, STARK_CONTRACT_ADDRESS)
    print("hell")


# async def claim_reward_from_nostr():


if __name__ == '__main__':
    asyncio.run(main())
    print("hello")
