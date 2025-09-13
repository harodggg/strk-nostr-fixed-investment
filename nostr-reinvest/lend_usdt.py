import asyncio
import time

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
    l1_gas=ResourceBounds(max_amount=int(1e5), max_price_per_unit=int(5e13)),
    l2_gas=ResourceBounds(max_amount=int(1e10), max_price_per_unit=int(5e17)),
    l1_data_gas=ResourceBounds(
        max_amount=int(1e5), max_price_per_unit=int(5e13)
    ),
)

the_lastlow_price = 100000  # 1str = 0.1usdt

# nostr swap contract
SWAP_CONTRACT = 0x040784ffdde08057a5957e64ed360c0ae4e04117b6d8e351c6bb912c09c5cbf5


STARK_CONTRACT = 0x04718f5a0fc34cc1af16a1cdee98ffb20c31f5cd61d6ab07201858f4287c938d
USDT_CONTRACT = 0x068F5c6a61780768455de69077E07e89787839bf8166dEcfBf92B645209c0fB8

MY_ACCOUNT_KEY = {
    "private_key": 0x035f14e889fd9a4fdaaf864922058771494de73a76843080153d6c4994acd107,

    "address": 0x041c3e6df37144f2287924103d2ced9e2e83a945bb72febf2b4c8a5571a100ac
}


async def lend_to_usdt(amount) -> Union[str, bool]:
    if amount <= 0:
        print("error：please input valid number and  > 0")
        return False

    account = Account(
        address=MY_ACCOUNT_KEY["address"], client=client, key_pair=KeyPair.from_private_key(MY_ACCOUNT_KEY["private_key"]), chain=StarknetChainId.MAINNET)
   # Create contract from contract's address - Contract will download contract's ABI to know its interface.
    strk_contract = await Contract.from_address(address=STARK_CONTRACT, provider=account)

    nostra_swap_contract = await Contract.from_address(address=SWAP_CONTRACT, provider=account)

    invocation_approve = strk_contract.functions["approve"].prepare_invoke_v3(
        SWAP_CONTRACT, int(amount * pow(10, 18)))

    invocation_swap = nostra_swap_contract.functions["swap_exact_tokens_for_tokens"].prepare_invoke_v3(
        int(amount * pow(10, 18)),
        int(the_lastlow_price * amount),
        0x4718f5a0fc34cc1af16a1cdee98ffb20c31f5cd61d6ab07201858f4287c938d,
        [
            0x7ae43abf704f4981094a4f3457d1abe6b176844f6cdfbb39c0544a635ef56b0,
            0xc318445d5a5096e2ad086452d5c97f65a9d28cafe343345e0fa70da0841295
        ],
        0x41c3e6df37144f2287924103d2ced9e2e83a945bb72febf2b4c8a5571a100ac,
        int(time.time()) + 60)

    transaction_response = await account.execute_v3(
        calls=[invocation_approve, invocation_swap],
        auto_estimate=True
    )
    print(transaction_response)

if __name__ == '__main__':
    asyncio.run(lend_to_usdt(0.1))
