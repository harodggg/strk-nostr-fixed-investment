import asyncio


from starknet_py.contract import Contract
from typing import Union
from starknet_py.net.account.account import Account
from starknet_py.net.full_node_client import FullNodeClient

from starknet_py.net.signer.key_pair import KeyPair
from starknet_py.net.models.chains import StarknetChainId
from starknet_py.net.client_models import Call
from starknet_py.net.client_models import ResourceBounds, ResourceBoundsMapping


FULLNODE_RPC = "http://pathfinder.xxxyyy.space/rpc/v0_9"
client = FullNodeClient(node_url=FULLNODE_RPC)

resource_bounds = ResourceBoundsMapping(
    l1_gas=ResourceBounds(max_amount=int(1e5), max_price_per_unit=int(1e13)),
    l2_gas=ResourceBounds(max_amount=int(1e10), max_price_per_unit=int(1e17)),
    l1_data_gas=ResourceBounds(
        max_amount=int(1e5), max_price_per_unit=int(1e13)
    ),
)

SWAP_CONTRACT =
STARK_CONTRACT = 0x04718f5a0fc34cc1af16a1cdee98ffb20c31f5cd61d6ab07201858f4287c938d
USDT_CONTRACT = 0x068F5c6a61780768455de69077E07e89787839bf8166dEcfBf92B645209c0fB8


async def swap_strk_to_usdt(amount: int) -> Union[str, bool]:
    if not isinstance(amount, int) or amount <= 0:
        print("error：please input valid number and  > 0")
        return False

    pass

if __name__ == '__main__':
    asyncio.run(get_usdt_balance(
        0x0729373f0e1e4e9ba6f8923d0e089a63625258ec8d0649ad4456b1c6f4b417b9
    ))
