import asyncio
import time

from starknet_py.contract import Contract
from starknet_py.net.account.account import Account
from starknet_py.net.full_node_client import FullNodeClient

from starknet_py.net.signer.key_pair import KeyPair
from starknet_py.net.models.chains import StarknetChainId
from starknet_py.net.client_models import Call
from starknet_py.net.client_models import ResourceBounds, ResourceBoundsMapping


FULLNODE_RPC = "http://pathfinder.xxxyyy.space/rpc/v0_9"
client = FullNodeClient(node_url=FULLNODE_RPC)


STRK_CONTRACT = 0x04718f5a0fc34cc1af16a1cdee98ffb20c31f5cd61d6ab07201858f4287c938d
STAKING_CONTRACT = 0x00ca1702e64c81d9a07b86bd2c540188d92a2c73cf5cc0e508d949015e7e84a7

MY_ACCOUNT_KEY = {
    "private_key": 0x035f14e889fd9a4fdaaf864922058771494de73a76843080153d6c4994acd107,

    "address": 0x041c3e6df37144f2287924103d2ced9e2e83a945bb72febf2b4c8a5571a100ac
}


async def transfer_strk(MY_ACCOUNT_KEY, rec, amount):
    account = Account(
        address=MY_ACCOUNT_KEY["address"], client=client, key_pair=KeyPair.from_private_key(MY_ACCOUNT_KEY["private_key"]), chain=StarknetChainId.MAINNET)

    claim_contract = await Contract.from_address(address=STRK_CONTRACT, provider=account)

    claim_invoke = claim_contract.functions["transfer"].prepare_invoke_v3(
        rec,
        amount

    )
    transaction_response = await account.execute_v3(
        calls=[claim_invoke],
        auto_estimate=True
    )

if __name__ == '__main__':
    asyncio.run(transfer_strk(MY_ACCOUNT_KEY, "l", 88))
